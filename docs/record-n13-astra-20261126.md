### Proof sources and the model's contribution

The test started from the public English n=13 problem. The original log records consultation of online material, including [DiskCoveringSolve](https://github.com/VonEquinox/DiskCoveringSolve), and the use of numerical and exact-arithmetic software. The submitted package gives a finite certificate for the geometric lower bound and a separate integer calculation for the radius polynomial.

### Task and acceptance standard

Within 12 hours the solver had to provide exact centers, prove continuous coverage and global optimality over arbitrary centers, and give every coefficient of the irreducible radius polynomial and a rational interval isolating its physical root.

### Test information and timing

| Item | Record |
| --- | --- |
| Test ID | T_20261126T071720Z_01a216b7 |
| Model | gpt-6.2-astra/max |
| Time limit | 12 hours (43,200 seconds) |
| Scored elapsed time | 41,582 seconds (11 h 33 min 2 s) on the original completed Goal |
| Natural elapsed time | About 41,590 seconds from Goal creation to the recorded final response |
| Score | 106 |

### Computing conditions and usage

| Item | Recorded scope |
| --- | --- |
| Environment | Windows host and WSL2, SageMath 10.7 and FLINT 3.3.1 for the exact verifier |
| Goal usage | 2,177,728 tokens in the completed Goal's own counter |
| Actual billing | Unavailable |

### Main research phases

| Phase | Work | Recorded result |
| --- | --- | --- |
| Geometry | Exact configuration and full-disk coverage | 13 centers specified by a rational isolation box and polynomial equations |
| Global bound | Interval exclusion and rigidity for general center configurations | 3,802,825 search nodes replayed |
| Algebra | Irreducibility, root isolation and identification with the geometric solution | All 30 exact identities and the real-box comparison passed in the submitted run |

### Changes of emphasis and difficulties

The run isolated the geometric optimum before completing the scalar calculation. After producing the coefficient table, it established exact equality between the isolated polynomial root and the geometric radius using integer identities and local uniqueness.

### Verification, deliverables and limitations

The run reported a complete proof package with the coefficient table, geometric proof, code and verifier logs. The original run's own certificate checks passed. The published time-derived score is 106 under the benchmark formula. Independent project review of the mathematical submission remains pending, and the n=13 reference fingerprint is derived from this same submission. It is available for future answer comparisons under diskcover-minpoly-v1.

### Archive and downloadable records

The local project archive links the test ID to the available conversation, runtime metadata and the proof as delivered.

[Public JSON](record-n13-astra-20261126.json) · [English report](record-n13-astra-20261126.en.md) · [Record history](n13-astra-20261126-history.json)
