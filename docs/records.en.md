# Historical n=11 records


These are historical demonstrations with checked record fields, not a formal leaderboard under the current strict prompt. Mathematical proofs were not rerun for this publication. Model labels use “name/reasoning setting”.

| Model | Test date (UTC) | Recorded natural elapsed time | Score (higher is better) |
|---|---|---|---:|
| [gpt-6 astra/max](record-n11-astra-20260930.html) | 2026-09-30 | Main task 5h 34m 29.011s + independent minimal-polynomial stage 13m 46.178s; total 5h 48m 15.189s | 205 |
| [gpt-6.1 sol/max](record-n11-sol-20260930.html) | 2026-09-30 | Goal creation to completion: 6h 17m 28s | 193 |

The timing endpoints differ. The original main tasks preceded the current minimal-polynomial requirement: SOL's historical report did not certify irreducibility, while Astra's report included a separate additional minimal-polynomial stage. Both runs missed their original 60-minute limit; completion during continuation does not change that timeout outcome. This table therefore does not establish that both models passed the same formal contract, or that the difference is stable across runs.

**n=11 reference hash:** published on the problem page; historical runs have not been rerun against this reference. [Public test reports](https://github.com/pikaaa345/disk-covering-benchmark/blob/main/docs/records.html) now describe the original inputs, hardware, main stages and acceptance status. The full originals and proof packages contain mathematical answers and remain unpublished.

Machine-readable history is in [n11.json](https://github.com/pikaaa345/disk-covering-benchmark/blob/main/results/n11.json), with [detailed timelines and input provenance](https://github.com/pikaaa345/disk-covering-benchmark/blob/main/docs/records.json). CPU and memory come from queries during preparation of the original SOL report. Astra uses that shared test-machine record; no separate task-start snapshot was preserved. Cost is unrecorded and remains null.

Test dates identify when each run took place relative to the availability of public material. Future comparisons should also record browsing rules and sources actually used, so changes in accessible material are not attributed directly to model capability.

## n=12 model test records

| Model | Test date (UTC) | Main natural elapsed time | Score (higher is better) |
|---|---|---|---:|
| [gpt-6 astra/max](record-n12-astra-20261001.html) | 2026-10-01 | 52 min 55.402 s (3175.402 s) | 477 |
| [gpt-6.1 sol/max](record-n12-sol-20261001.html) | 2026-10-01 | 1 h 30 min 57.272 s (5457.272 s) | 398 |

Both reference fingerprints match, and both mathematical deliveries were within the original 12-hour deadline. The publisher clarified that the ban covers only local materials existing before the test; files newly downloaded or generated during the task may be read. Existing reviews found no explicit reads of pre-task research materials, skills or other chats. The scores above are retained and the conditional label removed under this rule.

Both models reused online configurations, proof code and certificates, adding algebraic data or stronger exact checks. These runs do not establish discovery of the complete optimality proof from scratch. Each report gives provenance, added work, CPU, memory, original input and stage records. Single retrospective records are not a formal ranking; the proofs were not rerun for this website edit.

[Machine-readable records for both runs](https://github.com/pikaaa345/disk-covering-benchmark/blob/main/results/n12.json). Mathematical answers are withheld; full original reports, audits and proofs remain local.

## Algorithm system runs

These records describe local runs of algorithms developed and optimized through human–AI collaboration. They use the same scoring formula as the model tests above: higher is better, and scores compare completion efficiency on the same scale. See the reports for the recorded run conditions. The displayed minimum is selected from 40 complete observations in the three checked archives. Each entry is a single observation.

| n | Algorithm | Score (higher is better) | Report |
|---:|---|---:|---|
| 11 | DGC v62-F · MinPoly v9 | 994 | [Run report](record-n11-algorithm-run-20261001.html) |
| 12 | DGC v62-G · MinPoly v15 | 1117 | [Run report](record-n12-algorithm-run-20261001.html) |
| 14 | DGC v62-G · MinPoly v15 | 1138 | [Run report](record-n14-algorithm-run-20261001.html) |
| 16 | DGC v62-F · MinPoly v13 | 892 | [Run report](record-n16-algorithm-run-20261001.html) |
| 19 | DGC v62-G · MinPoly v15 | 1123 | [Run report](record-n19-algorithm-run-20261001.html) |
| 22 | DGC v62-G · MinPoly v15 | 1018 | [Run report](record-n22-algorithm-run-20261001.html) |
| 25 | DGC v62-G · MinPoly v15 | 883 | [Run report](record-n25-algorithm-run-20261001.html) |
| 26 | DGC v62-G · MinPoly v15 | 760 | [Run report](record-n26-algorithm-run-20261001.html) |

n=25 remains a candidate upper bound; n=26 source global-proof review is incomplete. Scores do not imply acceptance of these two full problems. Reports give CPU, memory, proof/algebra versions, stage timings and the latest 32-core reruns.