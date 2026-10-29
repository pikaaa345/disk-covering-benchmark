#!/usr/bin/env python3
"""Offline synthetic protocol checks. Contains no disk-covering answers."""
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from diskcover_answer import fingerprint

HERE = Path(__file__).resolve().parent

def run(script, *args):
    return subprocess.run([sys.executable, '-B', str(HERE / script), *args], capture_output=True, text=True, encoding='utf-8')

def main():
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    checks = 0
    def check(condition, message):
        nonlocal checks
        if not condition:
            raise AssertionError(message)
        checks += 1
    payload, canonical, digest = fingerprint(1, [4, 0, -8, 0], '0.500000000000000000005')
    expected = '{"coefficients":[-1,0,2],"n":1,"protocol":"diskcover-minpoly-v1","radius":"0.50000000000000000001"}'
    check(canonical == expected, 'canonical integer encoding and half-up rounding')
    check(digest == hashlib.sha256(expected.encode('utf-8')).hexdigest(), 'SHA256 of exact bytes')
    check(fingerprint(1, [-1, 0, 2], '0.500000000000000000005')[2] == digest, 'primitive sign normalization')
    check(fingerprint(1, [-1, 1], '-0')[0]['radius'] == '0.00000000000000000000', 'signed zero')
    big = 10 ** 5000 + 1
    check(fingerprint(1, [big, -1], '0.1')[0]['coefficients'][0] == -big, 'exact huge integer')
    for coefficients, radius in [([1], '0.1'), ([True, 1], '0.1'), ([1.0, 1], '0.1'), ([0, 0], '0.1'), ([1, 1], 'NaN'), ([1, 1], '1.1')]:
        try:
            fingerprint(1, coefficients, radius)
        except ValueError:
            checks += 1
        else:
            raise AssertionError('invalid data accepted')
    for invalid_n in (True, 1.0, "1", None, 0, -1):
        try:
            fingerprint(invalid_n, [-1, 1], "0.5")
        except ValueError:
            checks += 1
        else:
            raise AssertionError("invalid n type or value accepted")
    for invalid_radius in (0.5, 1, True, None):
        try:
            fingerprint(1, [-1, 1], invalid_radius)
        except ValueError:
            checks += 1
        else:
            raise AssertionError("non-string radius accepted")
    with tempfile.TemporaryDirectory(prefix='diskcover synthetic ') as folder:
        coefficients = Path(folder) / '系数.json'
        coefficients.write_text('[4,0,-8,0]', encoding='utf-8')
        args = ['--n', '1', '--coefficients', str(coefficients), '--radius', '0.500000000000000000005']
        result = run('diskcover_answer.py', *args, '--expected-sha256', digest.upper())
        check(result.returncode == 0 and json.loads(result.stdout)['matches_reference'] is True, 'CLI match and normalized digest')
        result = run('diskcover_answer.py', *args, '--expected-sha256', '0' * 64)
        check(result.returncode == 1 and json.loads(result.stdout)['matches_reference'] is False, 'CLI mismatch exit code')
        result = run('diskcover_answer.py', *args, '--expected-sha256', 'bad')
        check(result.returncode == 2, 'CLI input error exit code')
    for elapsed, expected_score in [('180', '891'), ('20895.189', '205'), ('22648', '193'), ('21600', '200'), ('10800', '300')]:
        result = run('score.py', '--reference-seconds', '21600', '--elapsed-seconds', elapsed, '--status', 'completed')
        check(result.returncode == 0 and json.loads(result.stdout)['score'] == expected_score, 'integer logarithmic scoring')
    # Synthetic elapsed time just below the 202.5-point rounding boundary.
    elapsed = '21228.924928577422907748960725463694382977501192600668010138661694803146543972313453028724336664818274061629360185207929445043749635684680122157100738855287905675193957249680916118952818489323373295480704217658075037293544482611012664856055443947355908512136603544230197680782225911803074184619080161588350964590803851156151420797850946528839230133849719546567289130315203310543413145870086435211734307791801660758211094082062885529619463026322843727857529'
    result = run('score.py', '--reference-seconds', '21600', '--elapsed-seconds', elapsed, '--status', 'completed')
    check(result.returncode == 0 and json.loads(result.stdout)['score'] == '202', 'exact rounding near a half-point boundary')
    result = run('score.py', '--reference-seconds', '21600', '--elapsed-seconds', '361', '--budget-seconds', '360', '--status', 'completed')
    check(result.returncode == 0 and json.loads(result.stdout)['score'] == '0' and json.loads(result.stdout)['status'] == 'over_budget', 'over budget')
    for problem_n in ('11', '30'):
        result = run('score.py', '--n', problem_n, '--reference-seconds', '21600', '--elapsed-seconds', '43200', '--status', 'completed')
        check(result.returncode == 0 and json.loads(result.stdout)['score'] == '100', 'completion at the 12-hour deadline')
        result = run('score.py', '--n', problem_n, '--reference-seconds', '21600', '--elapsed-seconds', '43200.001', '--status', 'completed')
        check(result.returncode == 0 and json.loads(result.stdout)['score'] == '0' and json.loads(result.stdout)['status'] == 'over_budget', 'late completion remains zero')
    result = run('score.py', '--n', '30', '--reference-seconds', '21600', '--elapsed-seconds', '43201', '--budget-seconds', '86400', '--status', 'completed')
    check(result.returncode == 0 and json.loads(result.stdout)['budget_seconds'] == '43200' and json.loads(result.stdout)['score'] == '0', 'cannot extend the n<=30 deadline')
    result = run('score.py', '--n', '31', '--reference-seconds', '21600', '--elapsed-seconds', '43201', '--status', 'completed')
    check(result.returncode == 0 and json.loads(result.stdout)['budget_seconds'] is None and json.loads(result.stdout)['status'] == 'completed', 'n>30 is outside the fixed-limit policy')
    result = run('score.py', '--reference-seconds', '21600', '--status', 'not_tested')
    check(result.returncode == 0 and json.loads(result.stdout)['score'] is None, 'not tested is not zero')
    result = run('score.py', '--reference-seconds', '21600', '--elapsed-seconds', '0', '--status', 'completed')
    check(result.returncode == 2, 'zero time rejected')
    print(json.dumps({'synthetic_checks_passed': checks, 'mathematical_solver_executed': False}))

if __name__ == '__main__':
    main()
