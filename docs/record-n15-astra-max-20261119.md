# n=15 · gpt-6.2 astra/max (12h) test report

[Back to n=15](n15.html?lang=en) · [Test records](records.html)

This run asked the model to determine the exact minimum radius for covering the closed unit disk with fifteen congruent closed disks. The model submitted a proof package within the twelve-hour limit. The submitted answer fingerprint matched the published reference. The website records a **self-reported score of 261**.

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
| Test ID | `T_20261119T030604Z_01a1f1c4` |
| Model | `gpt-6.2-astra / max` |
| Test date (UTC) | 2026-11-19 |
| Time limit | 12 hours |
| Independent runs | One |
| Submitted result | Proof package delivered within the limit |
| Scored elapsed time | 14,127 seconds (3 h 55 min 27 s), solving Goal accounting |
| Natural elapsed time | Approximately 14,163 seconds from Goal activation to the thread completion event |
| Website score | **261 (self-reported)** |
| Actual cost | Unavailable |

The logarithmic score uses a 21,600-second reference and a 43,200-second limit. Archiving and publication followed the test.

### Computing conditions and usage

| Item | Recorded scope |
| --- | --- |
| Execution environment | Codex Desktop on Windows, with computation in Ubuntu under WSL |
| Main tools | Python and exact polynomial arithmetic using FLINT in the SageMath environment |
| Computation | Numerical exploration followed by integer, rational and finite-field verification |
| Goal usage | 1,305,257 tokens for the original solving Goal |
| Thread cumulative usage | 78,092,140 input tokens, including 77,211,136 cached input, plus 425,817 output tokens. Total 78,517,957 |
| Billing evidence | Actual charges were unavailable |

The Goal and thread figures cover different scopes. Cached input is included in the input count.

### Main research phases

| Phase | Work | Recorded result |
| --- | --- | --- |
| Configuration | Locate a candidate and specify its centers using an isolated system of algebraic equations | Exact data for fifteen ordered centers |
| Coverage and lower bound | Verify whole-disk coverage and examine all configurations that could beat the candidate | A feasible covering and a computer-assisted global lower bound |
| Minimal polynomial | Recover the integer coefficients and check irreducibility and rational root isolation | A degree-2869 polynomial and all 2,870 coefficients |
| Root identification | Link the univariate root to the exact geometric configuration using algebraic and interval certificates | Exact congruence checks at 5,186 primes, with a bound that lifts the congruences to a rational identity |
| Submission verification | Replay the geometric and algebraic certificates from the delivery directory | Recorded successful replay |

### Changes of emphasis and difficulties

The geometric proof was in place before the univariate coefficients were recovered. Early coefficient reconstruction did not converge. The run corrected the normalization of a linear factor and reconstructed the coefficients again. It then checked irreducibility, isolated the real root and verified the identity connecting that root to the geometric system. The timings above describe the run as a whole.

### Verification, deliverables and limitations

| Item | Evidence in the original delivery | Verification scope |
| --- | --- | --- |
| Ordered centers | Algebraic equations and rational isolation data | Exact ordered configuration and uniqueness checks |
| Closed-disk coverage | Finite geometric checks and a proof of their sufficiency | Includes interior points and the boundary |
| Global lower bound | Classification, exclusion and matrix comparison certificates | Covers arbitrary center tuples |
| Minimal polynomial | All coefficients and four finite-field factorization certificates | Primitive normalization, positive leading coefficient and rational irreducibility |
| Isolating interval and linkage | Exact root count, interval checks and congruence certificates | Identifies the isolated real root with the candidate radius |
| Computational materials | Code, inputs, certificates, environment and replay logs | The original delivery records a full replay |
| Answer fingerprint | `diskcover-minpoly-v1` output checked after the run | Matched the reference for the coefficient vector and rounded radius |

The fingerprint checks the encoded answer fields. The mathematical evidence is in the proof package and its replay record. This publication summarizes the submission and its checks.

### Archive and downloadable records

The local archive binds the public conversation, available usage metadata, the tool-call index and the original proof package to the stable test ID. It is a partial export because it omits complete tool arguments and response bodies. The downloadable website files provide the report and structured test record.

[Machine-readable record](record-n15-astra-max-20261119.json) · [Report Markdown](record-n15-astra-max-20261119.en.md) · [n=15 run index](n15-astra-max-20261119-history.json)
