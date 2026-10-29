# n=12 algorithm run report

This records a locally executed algorithm developed and optimized through human–AI research. Development time is outside the measured program interval. It is not a foundation model solving the prompt independently.

## Best recorded run

| Item | Record |
|---|---|
| Run ID | `joint-v15-overlap-gmp-24-n12` |
| Date (UTC) | 2026-10-01 |
| Proof engine | DGC v62-G |
| Minimal-polynomial engine | MinPoly v15 |
| Complete elapsed time | 37.498 seconds |
| Score | 1117 |
| Logical-core limit | 24 |
| Observations of this configuration | 1 |
| Website SHA-256 comparison | Match |

“Best” means the minimum complete measured time among the three archives checked for this publication: 40 accepted pipeline observations. This is not an exhaustive ranking of all project history. Single observations with different versions and core limits do not establish a stable speedup.

## Local hardware and environment

- CPU: AMD Ryzen 9 8945HX with Radeon Graphics; 32 host logical processors.
- Memory: DDR5, 32 GiB on the host. Execution was in local Ubuntu under WSL2. The pre-run snapshot for the latest batch recorded MemTotal=15968388 KiB, approximately 15.23 GiB.
- SageMath 10.7: exact algebra and original-equation/root-box consumers. Python 3.12.3: proof program and controller. The public fingerprint script uses the Python standard library.
- No tools were installed during this batch. Earlier selected observations use the shared machine record; a separate hardware snapshot at each earlier run's start was not preserved.

## Algorithm versions

The proof engine derives from DGC v62. `DGC v62-F` identifies frozen internal code `radius-code-feedback-v1`, which adds fresh-source geometry feedback. `DGC v62-G` identifies `radius-code-gmp-v1`, which adds a GMP exact-rational backend for local certificate verification. The minimal-polynomial engine has an independent version sequence: this selected run uses MinPoly v15 (`minpoly-code-v15`). Original run-file SHA-256 identities are recorded in the machine-readable data.

Starting from n, the program discovers a new configuration and root system, generates and checks radius certificates, then extracts an irreducible radius polynomial from that new system and checks the original rational equations and root box. The controller requires both consumers to bind to the same final source. Overlap versions may start algebra after the provisional root system passes; provisional output cannot be accepted before final certificate and source binding.

The run uses existing research algorithms and conditional lemmas. Algorithm development is outside this interval. No public reference coefficients or saved configuration were passed to the solver. Solver source remains unpublished.

## Timing and principal stages

T+00:00:00 is the per-case controller start. The final bound result was saved at T+37.498 seconds. Radius stage: 15.348 seconds; algebra stage: 34.724 seconds; overlap: 12.585 seconds. The controller independently measures complete time, including process startup, certificate consumers, final same-root binding and saved result. Overlapping stages must not be added.

Fingerprint calculation and post-solve reference checks are outside the elapsed time used for scoring. “Cold start” means fresh processes starting from n, not an operating-system reboot or empty system caches. Research-development time, cost and task-system cumulative time were not recorded.

The score uses the same formula as the model tests: `ROUND_HALF_UP(200 + 100 × log₂(21600 / t))`, where t is complete program time in seconds. Higher is better: six hours scores 200, and each halving of time adds 100 points. Both kinds of record use the same score scale to compare completion efficiency; their starting conditions, algorithm versions and hardware are documented in the reports.

## Latest 32-core rerun

The latest observation is `single32-n12`: DGC v62-G · MinPoly v15, 39.430 seconds, score 1110, at most 32 logical cores. Radius: 18.070 seconds; algebra: 36.652 seconds; overlap: 15.304 seconds. The latest run and historical minimum are retained separately.

## Verification and publication scope

The runs executed the radius and algebra consumers and checked final source identity. Subsequent checks for this case compared all coefficients, irreducibility and the same root, established rounding to 20 places after the decimal point from exact intervals, and checked both the unchanged website script and an independent canonical-JSON reconstruction.

During publication preparation, the solver was not rerun. The selected historical result for this case was checked against its latest result for identical coefficients and intersecting certified root intervals; their fingerprints were recalculated with the shared website script and matched the registered values. Existing source-admission and finite-classification trust remains inherited; no new independent mathematical review or proof-assistant formalization was performed.

This report and [machine-readable n=12 run records](record-n12-algorithm-run-20261001.json) are public. Solver code, radii, polynomial coefficients, root intervals and proof trees remain in the research assets. The checks performed and materials published have different scopes.
