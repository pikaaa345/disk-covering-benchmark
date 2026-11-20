#!/usr/bin/env python3
"""Calculate an integer logarithmic score; completion is declared, not certified."""
import argparse
import json
import math
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP, localcontext

SCORING_VERSION = 'diskcover-log-score-v1'
SCORE_FORMULA = 'round_half_up(200 + 100 * log2(reference_time_seconds / elapsed_seconds))'
SCORE_ROUNDING = 'decimal_ROUND_HALF_UP_integer'

def positive(text):
    value = Decimal(text)
    if not value.is_finite() or value <= 0:
        raise ValueError('time must be finite and positive')
    return value

def calculate_score(reference, elapsed):
    """Estimate with decimals, then certify rounding using exact rational powers."""
    if not all(value.is_finite() and value > 0 for value in (reference, elapsed)):
        raise ValueError('time must be finite and positive')
    if any(abs(value.adjusted()) > 1000 for value in (reference, elapsed)):
        raise ValueError('time magnitude exceeds supported range (decimal exponent -1000 to 1000)')
    with localcontext() as context:
        context.prec = 80
        value = Decimal(200) + Decimal(100) * (
            reference.ln() - elapsed.ln()
        ) / Decimal(2).ln()
        candidate = int(value.to_integral_value(rounding=ROUND_HALF_UP))
    rn, rd = reference.as_integer_ratio()
    tn, td = elapsed.as_integer_ratio()
    numerator, denominator = rn * td, rd * tn
    divisor = math.gcd(numerator, denominator)
    numerator, denominator = (numerator // divisor) ** 200, (denominator // divisor) ** 200
    def compare_half_boundary(integer):
        # Score = integer+1/2 iff (reference/elapsed)^200 = 2^(2*integer-399).
        exponent = 2 * integer - 399
        left, right = (numerator, denominator << exponent) if exponent >= 0 else (numerator << -exponent, denominator)
        return (left > right) - (left < right)
    # An exact rational ratio cannot hit these half boundaries: the power of
    # two on the right has an odd exponent, while a rational 200th power has
    # a 2-adic valuation divisible by 200. Thus ties cannot occur.
    while compare_half_boundary(candidate - 1) < 0:
        candidate -= 1
    while compare_half_boundary(candidate) > 0:
        candidate += 1
    return str(candidate)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--n', type=int, help='problem size; omit to use the 12-hour default')
    parser.add_argument('--reference-seconds', required=True)
    parser.add_argument('--elapsed-seconds')
    parser.add_argument('--budget-seconds')
    parser.add_argument('--status', choices=['completed', 'not_completed', 'not_tested'], required=True)
    args = parser.parse_args()
    try:
        reference = positive(args.reference_seconds)
        elapsed = positive(args.elapsed_seconds) if args.elapsed_seconds is not None else None
        budget = positive(args.budget_seconds) if args.budget_seconds is not None else None
        if args.n is not None and args.n < 1:
            raise ValueError('n must be positive')
        fixed_limit = args.n is None or args.n <= 30
        if fixed_limit:
            budget = min(budget, Decimal('43200')) if budget is not None else Decimal('43200')
        status = args.status
        if status == 'completed' and elapsed is None:
            raise ValueError('completed requires elapsed time')
        if status == 'completed' and budget is not None and elapsed > budget:
            status = 'over_budget'
        if status == 'not_tested':
            score = None
        elif status != 'completed':
            score = '0'
        else:
            score = calculate_score(reference, elapsed)
        print(json.dumps({'status': status, 'score': score, 'reference_seconds': str(reference),
                          'elapsed_seconds': str(elapsed) if elapsed is not None else None,
                          'budget_seconds': str(budget) if budget is not None else None,
                          'budget_specified': args.budget_seconds is not None,
                          'n': args.n, 'fixed_12_hour_limit_applies': fixed_limit,
                          'scoring_version': SCORING_VERSION, 'score_formula': SCORE_FORMULA,
                          'score_rounding': SCORE_ROUNDING,
                          'deadline_inclusive': True, 'completion_independently_verified': False}))
        return 0
    except (ValueError, InvalidOperation):
        parser.error('invalid time or status parameters; use finite positive decimal seconds')

if __name__ == '__main__':
    raise SystemExit(main())
