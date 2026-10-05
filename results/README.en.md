# n=11 test records

[中文](README.md) · **English**

The table includes two historical demonstrations and an independently reviewed incorrect DeepSeek submission; it is not a formal comparable leaderboard. Historical global proofs were not rerun; the exact DeepSeek coverage counterexample was replayed. Model labels use “name/reasoning setting”.

| Model | Test date (UTC) | Recorded natural elapsed time | Score (higher is better) |
|---|---|---|---:|
| [gpt-6 astra/max](https://pikaaa345.github.io/disk-covering-benchmark/record-n11-astra-20260930.html) | 2026-09-30 | Main task 5h 34m 29.011s + independent minimal-polynomial stage 13m 46.178s; total 5h 48m 15.189s | 205 |
| [gpt-6.1 sol/max](https://pikaaa345.github.io/disk-covering-benchmark/record-n11-sol-20260930.html) | 2026-09-30 | Goal creation to completion: 6h 17m 28s | 193 |
| [deepseek-v4-pro/max](https://pikaaa345.github.io/disk-covering-benchmark/record-n11-deepseek-v4-pro-max-20261002.html) | 2026-10-02 | Goal creation to final submission: 10 h 57 min 27.149 s; incorrect proof submitted within its deadline | 0 |

The timing endpoints differ. The original main tasks preceded the current minimal-polynomial requirement: SOL's historical report did not certify irreducibility, while Astra's report included a separate additional minimal-polynomial stage. Both runs missed their original 60-minute limit; completion during continuation does not change that timeout outcome. This table therefore does not establish that both models passed the same formal contract, or that the difference is stable across runs.

DeepSeek had a 12-hour deadline and submitted within it. Its exact centers and radius leave a rigorously uncovered point, and its global lower bound is unproved, so it scored 0. The report identifies the affected sections, programs and reversed bound. The complete session and answer-containing evidence remain local. Its hardware was queried during preparation of this report.

**n=11 reference hash:** published on the problem page; historical runs have not been rerun against this reference. [Public test reports](../docs/records.html) now describe the original inputs, hardware, main stages and acceptance status. The full originals and proof packages contain mathematical answers and remain unpublished.

Machine-readable history is in [n11.json](n11.json), with [detailed timelines and input provenance](../docs/records.json). CPU and memory come from queries during preparation of the original SOL report. Astra uses that shared test-machine record; no separate task-start snapshot was preserved. Cost is unrecorded and remains null.

Test dates identify when each run took place relative to the availability of public material. Future comparisons should also record browsing rules and sources actually used, so changes in accessible material are not attributed directly to model capability.

## n=12 model test records

| Model | Test date (UTC) | Main natural elapsed time | Score (higher is better) |
|---|---|---|---:|
| [gpt-6 astra/max](https://pikaaa345.github.io/disk-covering-benchmark/record-n12-astra-20261001.html) | 2026-10-01 | 52 min 55.402 s (3175.402 s) | 477 |
| [gpt-6.1 sol/max](https://pikaaa345.github.io/disk-covering-benchmark/record-n12-sol-20261001.html) | 2026-10-01 | 1 h 30 min 57.272 s (5457.272 s) | 398 |

Both reference fingerprints match, and both mathematical deliveries were within the original 12-hour deadline. The publisher clarified that the ban covers only local materials existing before the test; files newly downloaded or generated during the task may be read. Existing reviews found no explicit reads of pre-task research materials, skills or other chats. The scores above are retained and the conditional label removed under this rule.

Both models reused online configurations, proof code and certificates, adding algebraic data or stronger exact checks. These runs do not establish discovery of the complete optimality proof from scratch. Each report gives provenance, added work, CPU, memory, original input and stage records. Single retrospective records are not a formal ranking; the proofs were not rerun for this website edit.

[Machine-readable records for both runs](n12.json). Mathematical answers are withheld; full original reports, audits and proofs remain local.

## n=13 test records

| Model | Test date (UTC) | Scoring observation window | Score (higher is better) |
|---|---|---|---:|
| [gpt-6 astra/max](https://pikaaa345.github.io/disk-covering-benchmark/record-n13-codex-20261001.html) | 2026-10-01 | 12 hours (43200 seconds); incomplete, not a valid completion time | 0 |
| [gpt-6.1 sol/max](https://pikaaa345.github.io/disk-covering-benchmark/record-n13-sol-20261001.html) | 2026-10-01 | 12 hours (43200 seconds); incomplete, not a valid completion time | 0 |

Neither run submitted the radius's minimal polynomial and a complete valid proof by the deadline, so both scores are 0. Both models are verified from their own original Goal runtime metadata. All 14 Astra configuration records identify gpt-6-astra/max, and its report follows the n=11 Astra structure. Tools, stage timestamps and system counters are kept separately. Publication performs no new mathematical replay and makes no formal ranking claim.

[Machine-readable records](n13.json) · [SOL scoring output](n13-sol-score-output.json) · [The other record's scoring output](n13-score-output.json).

## Algorithm system runs

These records describe local runs of algorithms developed and optimized through human–AI collaboration. They use the same scoring formula as the model tests above: higher is better, and scores compare completion efficiency on the same scale. See the reports for the recorded run conditions. The displayed minimum is selected from 40 complete observations in the three checked archives. Each entry is a single observation.

| n | Algorithm | Score (higher is better) | Report |
|---:|---|---:|---|
| 11 | DGC v62-F · MinPoly v9 | 994 | [Run report](https://pikaaa345.github.io/disk-covering-benchmark/record-n11-algorithm-run-20261001.html) |
| 12 | DGC v62-G · MinPoly v15 | 1117 | [Run report](https://pikaaa345.github.io/disk-covering-benchmark/record-n12-algorithm-run-20261001.html) |
| 14 | DGC v62-G · MinPoly v15 | 1138 | [Run report](https://pikaaa345.github.io/disk-covering-benchmark/record-n14-algorithm-run-20261001.html) |
| 16 | DGC v62-F · MinPoly v13 | 892 | [Run report](https://pikaaa345.github.io/disk-covering-benchmark/record-n16-algorithm-run-20261001.html) |
| 19 | DGC v62-G · MinPoly v15 | 1123 | [Run report](https://pikaaa345.github.io/disk-covering-benchmark/record-n19-algorithm-run-20261001.html) |
| 22 | DGC v62-G · MinPoly v15 | 1018 | [Run report](https://pikaaa345.github.io/disk-covering-benchmark/record-n22-algorithm-run-20261001.html) |
| 25 | DGC v62-G · MinPoly v15 | 883 | [Run report](https://pikaaa345.github.io/disk-covering-benchmark/record-n25-algorithm-run-20261001.html) |
| 26 | DGC v62-G · MinPoly v15 | 760 | [Run report](https://pikaaa345.github.io/disk-covering-benchmark/record-n26-algorithm-run-20261001.html) |

The global optimality proofs for n=25 and n=26 were accepted by the project’s local mathematical review on 2026-09-26. Independent review of the n=26 minimal-polynomial source remains pending; this is separate from global optimality. Fingerprint matching compares answer data and does not verify a submitted proof.

## n=25 model test

| Model | Test date (UTC) | Observation window | Score |
|---|---|---|---:|
| [gpt-6 astra/max](https://pikaaa345.github.io/disk-covering-benchmark/record-n25-astra-20261002.html) | 2026-10-02 | 12 hours, incomplete | 0 |

The fingerprint matches the n25 reference radius. This Astra test did not submit a complete global optimality proof by its deadline; the score remains zero. The reference’s proof status was corrected on 2026-10-03. [Machine record](n25.json).

## n=25 model test record

| Model | Test date (UTC) | Natural elapsed time | Score |
|---|---|---|---:|
| [gpt-6.1 sol/max](https://pikaaa345.github.io/disk-covering-benchmark/record-n25-sol-20261002.html) | 2026-10-02 | 4 h 52 min 19 s (17539 seconds) | 230 |

This test's complete computer-assisted proof is accepted after written review and a full exact replay; its canonical answer fingerprint matches. The report states online sources, original runtime metadata, post-test review scope and timing. This is separate from earlier candidate-configuration algorithm records.


