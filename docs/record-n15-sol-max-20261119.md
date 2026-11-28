# n=15 · gpt-6.2 sol/max (12h) test report

[Back to n=15](n15.html?lang=en) · [Test records](records.html)

This run asked the model to determine the exact minimum radius for covering the closed unit disk with fifteen congruent closed disks. The model submitted a proof package within the twelve-hour limit. The submitted answer fingerprint matched the published reference. The website records a **self-reported score of 207**.

### Proof sources and the model's contribution

The source for the problem was the English n=15 benchmark prompt. The user allowed data from the current conversation workspace and prohibited local skills and pre-existing research materials during the test. The run produced its own proof, algebraic data and verification programs. The reference fingerprint was checked during archiving, after the test had ended.

### Task and acceptance standard

For the closed unit disk $D$ and the ordered centers $C=(c_1,\ldots,c_{15})$, the problem asks for the infimum of the covering radius over all such center tuples.

$$
R_D(C)=\max_{x\in D}\min_{1\le i\le15}\|x-c_i\|_2,
\qquad r_D(15)=\inf_C R_D(C).
$$

| Requirement | Standard for this test |
| --- | --- |
| Radius minimal polynomial | List every coefficient of the primitive integer polynomial with positive leading coefficient and prove irreducibility over the rationals |
| Root identification | Give rational isolation endpoints, prove that the interval contains exactly one root and identify it with the optimal radius |
| Exact configuration | Give an ordered list of fifteen centers through finite algebraic data with a uniqueness proof |
| Continuous coverage | Prove coverage of the whole closed disk and justify and verify any reduction to finitely many cases |
| Global lower bound | Prove the bound for arbitrary centers, including relevant degeneracies |
| Computational evidence | Provide the actual code, inputs, certificates, execution environment and results, with their role in the proof |

The [n=15 problem page](n15.html?lang=en) gives the complete prompt.

### Test information and timing

| Item | Record |
| --- | --- |
| Test ID | `T_20261119T104331Z_01a1f367` |
| Model | `gpt-6.2-sol / max` |
| Test date (UTC) | 2026-11-19 |
| Time limit | 12 hours |
| Independent runs | One |
| Submitted result | Proof package delivered within the limit |
| Scored elapsed time | 20,567.922 seconds (5 h 42 min 48 s), recorded turn wall time |
| Natural elapsed time | 20,567.922 seconds from original task start to completion |
| Website score | **207 (self-reported)** |
| Actual cost | Unavailable |

The logarithmic score uses a 21,600-second reference and a 43,200-second limit. Archiving and publication followed the test.

### Computing conditions and usage

| Item | Recorded scope |
| --- | --- |
| Execution environment | Codex Desktop on Windows, with computation in Ubuntu under WSL |
| Main tools | Python, C++ interval checks and exact polynomial arithmetic with SageMath 10.7 and python-flint 0.9.0 |
| Computation | Numerical exploration followed by integer, rational and finite-field verification |
| Goal usage | Separate Goal token usage unavailable |
| Thread cumulative usage | See the archived usage event for the original thread |
| Billing evidence | Actual charges were unavailable |

The score uses the original turn timestamps. Tool and deployment time from this publication is outside the solving time.

### Main research phases

| Phase | Work | Recorded result |
| --- | --- | --- |
| Configuration | Locate a candidate and specify its centers using an isolated system of algebraic equations | Exact data for fifteen ordered centers |
| Coverage and lower bound | Verify whole-disk coverage and examine all configurations that could beat the candidate | A feasible covering and a computer-assisted global lower bound |
| Minimal polynomial | Recover the integer coefficients and check irreducibility and rational root isolation | A degree-2869 polynomial and all 2,870 coefficients |
| Root identification | Link the univariate root to the exact geometric configuration using algebraic and interval certificates | Exact circuit relations and certified root identification |
| Submission verification | Collect the geometric and algebraic verifier inputs and execution logs | Original verification logs supplied |

### Changes of emphasis and difficulties

The original run moved from numerical configuration discovery to exact geometric certificates and then to the radius polynomial. The geometric work excluded smaller coverings with certified interval tests and handled the remaining candidate configurations. The algebraic work checked rational irreducibility and identified the root with the radius of the exact configuration.

### Verification, deliverables and limitations

| Item | Evidence in the original delivery | Verification scope |
| --- | --- | --- |
| Ordered centers | Algebraic equations and rational isolation data | Exact ordered configuration and uniqueness checks |
| Closed-disk coverage | Finite geometric checks and a proof of their sufficiency | Includes interior points and the boundary |
| Global lower bound | Classification, exclusion and matrix comparison certificates | Covers arbitrary center tuples |
| Minimal polynomial | All coefficients and finite-field factorization certificates | Primitive normalization, positive leading coefficient and rational irreducibility |
| Isolating interval and linkage | Certified endpoint signs, derivative bounds and exact circuit checks | Identifies the isolated real root with the candidate radius |
| Computational materials | Code, inputs, certificates, environment and replay logs | Original logs include geometric exclusion, irreducibility, root endpoint and exact circuit checks |
| Answer fingerprint | `diskcover-minpoly-v1` output checked after the run | Matched the reference for the coefficient vector and rounded radius |

The fingerprint checks the encoded answer fields. The mathematical evidence is in the proof package and the original execution logs. Publication verified the answer fingerprint and inspected those logs. A fresh proof replay was outside this publication check.

### Archive and downloadable records

The local archive binds the public conversation, available usage metadata, the tool-call index and the original proof package to the stable test ID. It is a partial export because it omits complete tool arguments and response bodies. The downloadable website files provide the report and structured test record.

[Machine-readable record](record-n15-sol-max-20261119.json) · [Report Markdown](record-n15-sol-max-20261119.en.md) · [n=15 run index](n15-sol-max-20261119-history.json)
