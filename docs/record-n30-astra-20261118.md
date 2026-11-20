# n=30 · gpt 6.2 astra/max test report

[Back to n=30](n30.html?lang=en) · [Test record notes](records.html)

**Score: 0 (Incomplete).** In one 12-hour test, the model obtained an exact candidate covering, verified coverage of the entire closed unit disk, and matched the published answer fingerprint. It established an unconditional lower bound of 0.215 for arbitrary placements of 30 centers. The global optimality proof remained incomplete at the deadline.

## Task and acceptance criteria

The task was to find the smallest radius of thirty congruent closed disks covering the closed unit disk. A valid result required the primitive integer minimal polynomial and an irreducibility proof, rational endpoints isolating the radius, thirty exact ordered centers, continuous coverage, and a matching lower bound for every configuration. The test forbade local skills and local research materials or data outside the working directory. Public sources were allowed. [Full problem statement and scoring rule](n30.html?lang=en)

## Test information and timing

| Item | Record |
| --- | --- |
| Test ID | T_20261118T004433Z_01a1ec1c |
| Display model | gpt 6.2 astra/max |
| Runtime model and reasoning effort | gpt-6.2-astra, max |
| Test date (UTC) | 2026-11-18 |
| Independent runs | 1 |
| Limit | 12 hours of accumulated Goal time (43,200 seconds) |
| Natural elapsed time at final test report | Approximately 13 h 12 min 39 s |
| Recorded Goal usage at pause after the report | 12 h 00 min 45 s and 4,562,631 tokens |
| Successful completion time | Unavailable because the submission was incomplete |
| Actual cost | Unavailable |

The Goal timer determined the deadline. The natural timeline includes recorded pauses. The model initially stopped at 12 hours of wall time, then resumed after the user clarified the timing convention and the Goal counter showed time remaining. Archiving and publication were separate activities.

The last thread-wide usage event before the final test report recorded 220,073,577 input tokens, including 216,445,952 cached input tokens, and 997,557 output tokens, for 221,071,134 total tokens. These cumulative thread counters and the Goal token counter have distinct scopes.

## Computing conditions

The run recorded local Windows 11 AMD64, Python 3.13.13, GNU C++ for geometric enumeration, NumPy 2.3.5, SciPy 1.17.0, mpmath 1.3.0, python-flint 0.9.0 with FLINT 3.6.0, and Clarabel 0.11.1. Number-theoretic and interval checks used integer polynomials, rational arithmetic and Arb enclosures. The selected test record does not establish a complete test-start inventory or a verified CPU model and memory type and capacity. Test-start installation status for individual tools is unavailable.

## Research timeline

Times are natural elapsed time from the test start, rounded from the archived progress messages.

| Time | Checkpoint |
| --- | --- |
| T+00:17 | An exact candidate placement and its continuous-coverage certificate were reported. |
| T+00:41 to T+00:59 | Local optimality was checked and the first unconditional lower bound was established. |
| T+01:19 | The model withdrew an early algebraic result after finding that the input parser had misread an expression. It corrected the input and reran the elimination. |
| T+02:40 to T+03:03 | The candidate's radius polynomial matched the published fingerprint. Exact checks connected the isolated radius to the coverage certificate. |
| T+07:49 | Replay of the last 29-disk case established that an improvement over the candidate would require all 30 disks. |
| T+12:01 to T+13:08 | The model resumed on the remaining Goal time. It eliminated further classes of configurations and completed the independent replay supporting the unconditional 0.215 lower bound. |
| T+13:13 | The final test report recorded the remaining gap in global optimality and the resulting zero score. |

The test used the public [n=30 prompt](prompts/n30.en.md), [fingerprint protocol](protocol.en.txt), and a published [n=20 proof](https://raw.githubusercontent.com/VonEquinox/DiskCoveringSolve/main/cover20/docs/r20_proof_zh.md) as a reference for geometric verification. The n=30 calculations and certificates were produced during this test.

## Verification and retained materials

The archived results include the ordered candidate centers, polynomial and root-isolation data, coverage and local optimality certificates, lower-bound arguments, source code, and replay logs. The exact checks cover the submitted candidate and the stated exclusion cases. Some placements of 30 disks still lie outside those exclusions, so the universal lower bound does not meet the candidate upper bound. The matching fingerprint checks the encoded candidate data. The mathematical verification reported here comes from the original run.

The public record follows the problem's fingerprint-only disclosure policy. The exact answer data, private certificates and raw session archive remain in the local test archive. This record is a historical demonstration with no formal ranking designation.
