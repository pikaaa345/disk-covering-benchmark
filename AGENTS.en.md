# Agent instructions

[中文](AGENTS.md) · **English**

This repository is the public interface to a disk-covering benchmark, not a solver. Read README.en.md and benchmark.json first. Select the English task entry in the language map; do not summarize or replace the full prompt.

1. Read the selected task's English prompt in benchmark.json in full. Preserve the current Git commit, prompt and protocol version.
2. Record the model/reasoning setting, starting materials, tools, network rules, hardware, time and cost budgets before the test. Do not claim a formal ranking when the contract is not frozen.
3. Perform the mathematical task. A candidate image, floating-point optimization, finite sampling or matching hash is not a rigorous proof. Report unknowns honestly; do not invent polynomials, isolating intervals or certificates.
4. Keep the exact integer coefficient JSON and high-precision radius locally. Read docs/answer-protocol.en.txt and run tools/diskcover_answer.py. Never convert large integers through floating point.
5. A null reference_sha256 permits only generating your own fingerprint. When a reference exists, use --expected-sha256. Exit code 0 means successful fingerprint generation or a match, 1 means a mismatch, and 2 means invalid input. The checker does not prove irreducibility or optimality.
6. Keep the rational isolating interval and full proof separately: neither is included in the v1 hash. Generate a factual report using prompts/research-work-report.en.txt.
7. Calculate scores with tools/score.py under the agreed criteria. Historical records are not automatically passes under the current prompt. Public submissions are closed: do not automatically open an issue/PR, upload answers or publish research materials. For n≤30 the deadline is 43200 seconds; only valid completion by the deadline can score above 0, and later completion remains 0. Pass --n N.

## Environment and maintenance

Discover Python and its version first; require 3.9+ and only the standard library. On Windows, use python or py -3; on Linux/macOS, python3 may be appropriate. Do not install or change global environments automatically. Run python tools/check_tools.py; exit code 0 is a synthetic tool-check pass, not a solved mathematical task.

The public repository contains downloadable tools and test materials. Website source is maintained privately. Do not publish answers or modify website deployment automatically. Missing hashes, reports and configurations remain null.
