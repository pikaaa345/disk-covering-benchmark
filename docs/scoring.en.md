# Scoring and timing

The current scores are historical demonstrations. A uniform contract for formal comparisons has not yet been frozen.

## Scoring standard and baseline

**Higher is better. The current historical n=11 display uses a 6-hour (21600-second) reference: valid completion in 6 hours scores 200; halving the time adds 100 points and doubling it subtracts 100 points.**

$$
S=\operatorname{RoundHalfUp}\!\left(200+100\log_2\frac{T_{\mathrm{ref}}}{T}\right).
$$

$T_{\mathrm{ref}}$ is the task's predeclared reference time and $T$ is the actual time to a valid result under the agreed acceptance criteria. Use the same unit for both. Scores are rounded to integers using `ROUND_HALF_UP` and have no upper cap. Use each task's published reference time; the 6-hour example does not imply equal difficulty across n or freeze the reference for other tasks.

### Time-to-score table (6-hour reference)

These are arithmetic examples assuming valid completion, not measured model results. A run with a shorter agreed budget must also meet that budget.

| Time to valid completion | Score |
|---|---:|
| 12 hours | 100 |
| 9 hours | 142 |
| 7 hours | 178 |
| 6 hours 30 minutes | 188 |
| 6 hours (baseline) | 200 |
| 3 hours | 300 |
| 2 hours | 358 |
| 1 hour | 458 |
| 30 minutes | 558 |
| 10 minutes | 717 |
| 5 minutes | 817 |
| 3 minutes | 891 |
| 1 minute | 1049 |
| More than 12 hours; failure or no valid result by the deadline | 0 |
| Not tested | Not tested |

**Valid completion at exactly 12 hours scores 100; completion after 12 hours scores 0.**

## Fixed time limit for n≤30

Every problem with n≤30 has a 12-hour (43200-second) time limit. If no valid result meeting that problem's acceptance criteria is obtained within 12 hours, the score is 0; completion after the deadline also scores 0. Completion at the deadline is allowed, so T≤43200 seconds. Untested runs remain "not tested", not 0. This rule appears on every problem page and in its machine-readable data; newly added n≤30 problems inherit it automatically. Time limits for n>30 will be set separately.

## Efficiency on one task

When the agreed completion criteria are met within budget, S = RoundHalfUp(200 + 100 × log₂(T_ref / T)). Use the same time unit, with T strictly positive. Round the score to an integer using `ROUND_HALF_UP`. Higher is better; there is no cap. T_ref is a predeclared scale, not an automatic estimate of task difficulty.

| Status | Display |
|---|---|
| Completed under the agreed contract within budget | Efficiency score |
| Failure or timeout | 0, with the reason stated |
| Not tested | Not tested |
| Reference hash unpublished | Process and own fingerprint may be reported; match status remains pending |
| Historical run with different timing or acceptance scope | Historical demonstration, excluded from formal rankings |

The script does not judge mathematical completion or proof validity. The publisher must determine completion before declaring a status. An answer-match contract and a complete-proof contract must not be combined in one ranking.

~~~text
python tools/score.py --n 11 --reference-seconds 21600 --elapsed-seconds 180 --status completed
~~~

This synthetic arithmetic example produces 891. For n≤30 the script automatically applies the 12-hour limit; omitting `--n` also defaults to 12 hours. `--budget-seconds` may set a shorter budget but cannot extend the n≤30 limit. Explicit n>30 has no automatic budget and requires a task-specific contract. The script does not certify completion.

## Timing

A formal run should measure natural elapsed time from task delivery to obtaining all required deliverables, including model work, program execution, waiting and verification. Record any system cumulative timer separately; it is not interchangeable with natural elapsed time.

Time independent additional tasks separately. If an additional stage is necessary for the same acceptance criteria, sum the relevant intervals using the same timing basis and exclude the gap between tasks. Do not mix system cumulative time with natural elapsed time. Do not sum parallel program runtimes as total task time. Record mathematical completion and fingerprint completion separately; the contract must state which endpoint determines the score.

A single run is allowed. Disclose the number of runs, costs and failures; ten-run averages are not required. One result cannot establish a success rate or statistical significance for a difference of several tens of minutes.

## Still to be frozen

Each task's reference hash, acceptance criteria, reference time, timing endpoints, starting materials, tool and network rules, hardware and cost reporting. Maximum budgets for n>30 remain to be set. Cross-task aggregation and repeated-run policies remain future work. No combined ranking across n or cost is generated at present.
