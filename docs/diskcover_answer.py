#!/usr/bin/env python3
"""Canonical answer fingerprint for a self-reported disk-cover benchmark."""

import argparse
import hashlib
import json
import math
import re
import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP, localcontext
from pathlib import Path

PROTOCOL = "diskcover-minpoly-v1"


def fingerprint(n, coefficients, radius_text):
    if type(n) is not int or n < 1:
        raise ValueError("n must be an exact positive integer")
    if not isinstance(radius_text, str):
        raise ValueError("radius must be supplied as a decimal string")
    if not isinstance(coefficients, list) or not coefficients:
        raise ValueError("coefficients must be a nonempty JSON integer array")
    if any(type(c) is not int for c in coefficients):
        raise ValueError("each coefficient must be an exact JSON integer")
    coefficients = coefficients.copy()
    while len(coefficients) > 1 and coefficients[-1] == 0:
        coefficients.pop()
    if len(coefficients) < 2:
        raise ValueError("the polynomial must be nonconstant")
    content = math.gcd(*coefficients)
    divisor = content if coefficients[-1] > 0 else -content
    coefficients = [c // divisor for c in coefficients]

    radius = Decimal(radius_text)
    if not radius.is_finite() or not 0 <= radius <= 1:
        raise ValueError("radius must be a finite decimal between zero and one")
    with localcontext() as context:
        context.prec = max(40, len(radius.as_tuple().digits) + 2)
        rounded = radius.quantize(Decimal("0.00000000000000000001"),
                                  rounding=ROUND_HALF_UP)
    if rounded.is_zero():
        rounded = abs(rounded)
    payload = {
        "protocol": PROTOCOL,
        "n": n,
        "coefficients": coefficients,
        "radius": format(rounded, ".20f"),
    }
    canonical = json.dumps(payload, ensure_ascii=True, sort_keys=True,
                           separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return payload, canonical, digest


def main():
    # Python 3.11+ otherwise limits conversion of sufficiently large integers.
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--coefficients", type=Path, required=True,
                        help="UTF-8 JSON integer array, constant term first")
    parser.add_argument("--radius", required=True,
                        help="high-precision decimal text; no float conversion")
    parser.add_argument("--expected-sha256", help="published reference digest")
    args = parser.parse_args()
    try:
        expected = args.expected_sha256
        if expected is not None:
            expected = expected.strip().lower()
            if not re.fullmatch(r"[0-9a-f]{64}", expected):
                raise ValueError("expected SHA-256 must contain 64 hex digits")
        coefficients = json.loads(args.coefficients.read_text(encoding="utf-8-sig"))
        payload, canonical, digest = fingerprint(args.n, coefficients, args.radius)
        result = {"answer": payload, "canonical_json": canonical,
                  "sha256": digest}
        if expected is not None:
            result["matches_reference"] = digest == expected
        print(json.dumps(result, ensure_ascii=True, indent=2))
        return 1 if expected is not None and digest != expected else 0
    except (ValueError, OSError, InvalidOperation) as error:
        parser.error(str(error))


if __name__ == "__main__":
    sys.exit(main())
