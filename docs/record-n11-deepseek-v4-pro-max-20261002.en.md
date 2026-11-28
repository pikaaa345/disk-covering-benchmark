# n=11 · deepseek-v4-pro/max test report

[Back to n=11](n11.html) · [Test record directory](records.html)

**Score: 0. Acceptance: failed; the submitted proof is incorrect.** The test took place on 2026-10-02 (UTC). The model submitted within 12 hours and claimed completion. Its exact algebraic configuration fails to cover the unit disk, and its global optimality argument is invalid. An incorrect submission receives zero.

An independent reviewer prepared this report from the local DeepSeek Harness session, programs and deliverables without requesting a report from DeepSeek. Radius values, coefficients, centers and counterexample coordinates are withheld. Full conversations and mathematical evidence remain local. This is one run.

### Task and completion

The actual task required the primitive, positive-leading, irreducible integer minimal polynomial of the optimal radius with a rational isolating interval; uniquely specified algebraic data for 11 ordered centers; full-disk coverage and a global lower bound over all configurations; and executed code, inputs, certificates and verification results.

The model delivered solution.md, SUMMARY.md, coord_polys_verified.json and programs for optimization, relation searches, coverage and type analysis. Several programs ran, but an exact counterexample refutes submitted coverage. Exhaustive classification and certified global lower bounds were not established. The task was not completed.

### Task and timing

T+00:00:00 is the first goal/change: create event. Submission ends at the final substantive assistant/message.

| Measure | Record |
|---|---|
| Natural elapsed time to final submission | **10 h 57 min 27 s (39447.149 seconds)** |
| Time to that turn's end | 39447.192 seconds, approximately 0.04 seconds later |
| Goal marked complete | T+10:57:13; system state, not mathematical acceptance |
| System accumulated task time | Unavailable; the saved get_goal result contains no such field |
| Sum of first five turn intervals | 10 h 17 min 8 s (37027.526 seconds), calculated from events; includes tool waits and is not system accumulated work or inference time |
| Difference from natural time | About 40 min 20 s, principally inter-turn intervals following two transport errors |
| Original limit | 12 hours; submission within the limit, complete correct result not obtained |
| Sixth turn | A stale background notice triggered it around T+11:58:49; the user aborted it, with no new substantive mathematical submission |

The first turn ended with a TRANSPORT error around T+01:08:30 and resumed around T+01:27:05. The fourth ended similarly around T+10:33:09 and resumed around T+10:54:54. Fourteen retry events are saved. The intervals cannot all be assigned to server computation or user pauses.

Goal continuations and resumptions are the same test. The final turn's approximately 153 seconds cannot replace total task time. Independent review and report preparation are subsequent work.

Report-preparation duration was not separately measured. The evidence-package creation time is saved, but cannot establish the full preparation duration.

### Computing conditions

| Item | Record |
|---|---|
| CPU | AMD Ryzen 9 8945HX with Radeon Graphics |
| Memory | DDR5, 32 GB |
| Execution | Local Windows and Ubuntu WSL; core commands use local WSL, with no recorded core remote computation |
| Hardware evidence | Windows CIM query during report preparation, not a start-of-test snapshot |
| Model | deepseek-v4-pro; reasoningEffort=max; provider=deepseek-official |
| Harness mode | agentPreset=standard; screenshot label DeepSeek-V4-Pro Max |

The opening query records WSL **Python 3.12.3**, pip and GCC, without finding Sage or PARI/GP. This was a limited query, not a complete inventory.

Installation commands ran during the task. Actual output at T+00:27:53 reports **NumPy 2.5.3, SciPy 1.18.1, SymPy 1.14.0 and mpmath 1.3.0**, used for numerical geometry, local optimization, polynomial operations, high-precision arithmetic and relation searches. Which packages were preinstalled is unknown. pypdf, Pillow and OpenCV supported document or image processing; some versions are unavailable.

**PARI/GP 2.15.4**, as printed in the log, was obtained for algdep and lattice searches. Installation of **fplll-tools**, an integer lattice reduction tool, began around T+09:46:47; its exact version was not saved. Core use of SageMath, Wolfram or a remote cluster is not recorded.

### Tokens and monetary cost

| Field | Sum over 373 model messages with usage |
|---|---:|
| inputTokens | 983,404 |
| cacheReadTokens | 161,620,608 |
| outputTokens | 567,001 |
| cacheWriteTokens | 0 |
| totalTokens | **163,171,013** |
| Monetary cost | No invoice or charge record obtained; unknown |

Here totalTokens = inputTokens + cacheReadTokens + outputTokens, and inputTokens excludes cache reads. Cache reads account for about **99.40%** of all input, consistent with “163M tok / Cache hit 99%”. Repeated context contributes to accumulated input; this is not 163 million newly generated tokens. Reasoning output is not separately reported. Failed requests, background searches and title generation may have other unconfirmed usage; these sums are not a complete invoiced cost.

The saved session has six turns, 376 steps and 374 assistant-message events; the last message has no usage. Report preparation introduced no DeepSeek requests.

### Actual input

[Download the task text saved in the Goal](reports/n11-deepseek-main-prompt.original.txt). The local evidence package also preserves the original /goal command arguments. The following text changes only line endings and presentation.

Additional restrictions prohibit local reference material, skills, chats and archived chats; permit the web and WSL tools but prohibit existing stored material or files; and declare failure for any violation or failure to obtain a complete correct result within 12 hours. Mathematical failure is already decisive. No complete file-access audit was performed, so full resource compliance is not certified.

<details><summary>Expand the actual input in its original language</summary>

"单位圆盘的 11 圆最优覆盖问题

设

$$

D=\{x\in\mathbb R^2:\|x\|_2\le1\},\qquad

R_D(C)=\max_{x\in D}\min_{1\le i\le11}\|x-c_i\|_2,

$$

其中 $C=(c_1,\ldots,c_{11})\in(\mathbb R^2)^{11}$，并定义

$$

r_D(11)=\inf_{C\in(\mathbb R^2)^{11}}R_D(C).

$$

覆盖圆盘均为闭圆盘，允许相互重叠和超出 $D$；圆心不预先限制在 $D$ 内。

确定 $r_D(11)$，并完成以下要求：

1. **最小多项式与根隔离区间：**实际列出最优半径 $r_D(11)$ 在 $\mathbb Q$ 上的最小多项式的规范化整系数表示 $P(t)\in\mathbb Z[t]$ 的全部系数：要求 $P$ 非常数、本原、首项系数为正，并证明其在 $\mathbb Q[t]$ 中不可约。给出具体有理数 $0\le a<b$，证明 $P(a)P(b)\ne0$，且 $P$ 在 $(a,b)$ 内恰有一个实根 $\alpha$；结合以下构型与证明，确定 $r_D(11)=\alpha$。

2. **具体构型：**给出一组确定的有序圆心坐标 $C_*=(c_1^*,\ldots,c_{11}^*)$，采用根式、多项式与有理隔离区间，或其他实际列出的、具有唯一性证明的有限代数数据精确指定。这里的唯一性指所提交的数据唯一指定该组圆心坐标，不要求证明最优构型唯一。

3. **覆盖性：**严格证明

   $$

   \forall x\in D,\quad\exists i\in\{1,\ldots,11\},\quad

   \|x-c_i^*\|_2\le\alpha.

   $$

   若将连续覆盖归约为有限检查，须证明该归约充分，并严格完成全部检查。

4. **全局最优性：**严格证明

   $$

   \forall C\in(\mathbb R^2)^{11},\quad R_D(C)\ge\alpha,

   $$

   从而 $R_D(C_*)=r_D(11)=\alpha$。不得未经证明限制构型的对称性、接触关系或组合结构。任何规范化、分类、枚举或剪枝都须证明不会遗漏可能的更优构型，并处理圆心重合、冗余圆盘及其他相关退化情形。

5. **计算机辅助证明：**若证明依赖计算，须交付实际使用的完整代码、输入、证书、必要环境说明及实际核验结果，并说明核验结果为何推出上述数学命题。

**最终提交：**明确列出 $P(t)$ 的全部系数与有理根隔离区间 $(a,b)$，并附上上述构型、完整证明及必要核验材料。必须提交最优半径本身的最小多项式；仅给出半径平方或其他辅助量的多项式，或未证明不可约的消元多项式，不满足要求。

允许任何严格方法，但仅证明存在性、代数性，或仅给出尚未完成的枚举、求解算法、数值候选，均不视为完成。数值优化成功、程序输出“通过”及未经严格误差控制的浮点结果不能代替证明；只检查有限采样点、边界或数值图像，也不能代替整个闭圆盘被覆盖的证明。" 限制：不允许使用任何本地资料、技能、chat、archived chat等资料、可以使用网络、本地的WSL当中的工具（但是绝对不能访问其中任何已经存储的资料或文件），一旦违反任何一条规则即视为任务失败。任务限时12小时，超时没有得到完整且正确的结果也视为失败。完成时间越短越好。

</details>

### Main stages

Times are natural elapsed time, including interruptions and parallel waits. Nodes come from timestamped messages or actual tool results, rounded to seconds; intervals are not exclusive activity accounting.

| Natural elapsed interval | Work | State at the end |
|---|---|---|
| T+00:00:00–T+00:27:53 | Sources, image reconstruction and environment setup | Read the configuration collection, Handbook and Fejes Tóth paper; obtain no applicable complete global proof for n=11. |
| T+00:27:53–T+00:55:10 | Optimization and high-precision contact equations | Improve image-derived starting data after a poor local result, correct the radius evaluator, and obtain a better numerical candidate. |
| T+00:55:10–T+02:46:24 | Coverage programs and type analysis | Coverage programs report success; local numerical searches examine interior-disk counts and consecutive groups of boundary disks, without certified global lower bounds. |
| T+02:46:24–T+09:45:30 | Relation searches and repeated recomputation | Raise precision, try PSLQ and PARI/GP, reject several spurious relations, abandon a Krawczyk root-certification approach with a singular equation system, and acknowledge the missing minimal polynomial in the first delivery. |
| T+09:45:30–T+10:30:22 | fplll and subsequent checks | Add asymmetric local searches, find a degree-eight large-coefficient relation, and obtain passing factorization/Sturm outputs after correcting coefficient order; no exact connection to the optimum is proved. |
| T+10:30:22–T+10:57:27 | Algebraic centers and final delivery | Generate coordinate polynomials, fix a missing sqrt import and a precision setting, and claim completion. Subsequent exact review refutes coverage. |

### Sources and contribution

Around T+00:05 the model read [Erich Friedman's configuration collection](https://erich-friedman.github.io/packing/circovcir/), then downloaded and processed the n=11 image for starting data. Around T+00:11–00:13 it acquired and extracted the [Handbook covering chapter](http://www.csun.edu/~ctoth/Handbook/chap2.pdf). Around T+00:22:31 it downloaded and read [Fejes Tóth's 2005 paper](https://library.slmath.org/books/Book52/files/18fejes.pdf), attempting to extend methods for smaller n.

The model inferred “no published n=11 proof” from unsuccessful searches; this report does not adopt that inference as current literature status. No acquisition and replay of the complete DiskCoveringSolve package used in the September 30 reports is recorded. Earlier models' external-proof replays cannot be credited to this run.

New work comprised numerical reconstruction, contact equations, precision and relation searches, local coverage/type code, algebraic data and a final argument. Code, tiny residuals and historical coarse bounds do not themselves establish a proof.

### Route changes and specific errors

After a poor local result, the model improved image-derived starting data and corrected a radius evaluator that did not minimize over all centers. It subsequently rejected several spurious integer relations, with recorded evidence.

The final degree-eight large-coefficient relation was nevertheless promoted to a true minimal polynomial using a tiny residual. Factorization and isolation establish properties of that polynomial, not equality of its root with the optimum. Coordinate generation only projected onto contact equations without the corresponding stationarity minimization. Radius and centers came from different numerical procedures without a certified exact connection.

The lower-bound argument used single-start, finite-step local descent as if it computed a family's global minimum. A feasible local value generally bounds that infimum from above, opposite to the lower bound needed to exclude better configurations. Transport errors do not explain these mathematical failures.

### Verification, delivery and acceptance

**Verdict: incorrect proof; certification refused; score 0.** The locations below refer to the submitted proof and programs. The radius, centers, coefficients, root-isolation endpoints and counterexample coordinates remain local and are withheld from this webpage.

#### 1. An exact uncovered point refutes the submitted configuration — §§2.2 and 3

The review uses the radius specified by the polynomial in §1 and the centers specified by §2.2 and <code>coord_polys_verified.json</code>. Each scalar is interpreted as the unique real root of its polynomial in the stated interval, rather than a nearby floating-point number.

The reviewer enclosed all twelve scalar roots in rational intervals of width $10^{-75}$. Exact endpoint sign changes establish existence, and a derivative of constant sign throughout each original isolating interval establishes uniqueness. These checks identify the very roots specified in the submission. Python's standard-library <code>Fraction</code>, which performs exact rational arithmetic, then verifies a rational point $p$ strictly inside the unit disk such that

$$
\forall i\in\{1,\ldots,11\},\qquad
\|p-c_i\|^2-\alpha^2>5.4\times10^{-36}>0.
$$

Thus none of the eleven submitted closed disks contains $p$. The comparison uses exact rational lower and upper bounds; it is not a floating-point discrepancy. A small positive gap still refutes coverage of the entire disk. Replaying the independent verifier returns **VERIFIED_EXACT_COUNTEREXAMPLE**. This finding alone warrants score 0.

The mismatch can also be traced to line 85 of <code>coord_polys_final.py</code>: it projects initial data onto a solution set of ten contact equations in twelve unknowns and immediately generates coordinate polynomials, without minimizing the radius on that set. Contact equations require selected distances to equal the radius; satisfying them does not establish minimality. The radius comes from a separate optimization process, without an exact proof connecting the two. The displayed decimal centers also differ from the polynomial-defined centers.

#### 2. The finite reduction omits possible boundary maxima — §3.1

Section 3.1 lists only circumcenters of triples of centers and intersections of pairwise perpendicular bisectors with the unit circle. It omits circle-boundary points where a single center determines the farthest nearest-center distance.

A Voronoi region is the region assigned to its nearest center. Intersecting it with the unit disk can leave a smooth circular arc on the boundary. A distance maximum can occur in the middle of that arc, away from any corner. For example, with eleven distinct centers on the positive horizontal axis, the leftmost unit-circle point can be the farthest point. Its nearest center is unique; it is neither a triple circumcenter nor on any pairwise perpendicular bisector. The submitted candidate list is therefore incomplete.

A sufficient reduction must also include distance maxima on smooth boundary arcs and handle coincident or collinear centers. The existing exact coverage tool consulted in the review includes these points. The theorem that a convex function attains its maximum at an extreme point does not repair the omission: points on a smooth circular arc can themselves be extreme points.

#### 3. Passing coverage output does not certify the final inputs — §§3.3–3.4

The original coverage program did report “239 subdivisions, 0 failed boxes.” A box here is a rectangular region that the program tries to certify as covered. However, <code>coverage_bb.py</code> reads a different input, <code>config_hp1200.txt</code>, without rigorous interval bounds linking it to the final submitted algebraic centers.

<code>coverage_certs.py</code> also uses ordinary NumPy floating-point arithmetic for triple points and local coverage conditions. <code>coverage_bb.py</code> then skips rectangles inside those local regions without certifying the required premises. More decimal digits, or shrinking one radius constant, cannot control every center and contact-point error.

Rigorous interval arithmetic must enclose the true value at every step, rounding lower endpoints downward and upper endpoints upward. The submitted programs provide no such guarantee. Their passing output therefore does not establish coverage for the final algebraic configuration; the exact counterexample in finding 1 refutes it directly.

#### 4. The classification is unproved, and local optimization gives the wrong bound — §4

The “criticalization lemma” in §4 claims that every potentially better covering can be transformed into one of the listed contact types without increasing its radius. This transformation is not proved, and other contact structures, coincident centers and redundant disks are not fully treated. Arguments for smaller disk counts do not automatically supply an exhaustive classification for $n=11$.

The implementation also falls short of the claims. <code>types_m1.py</code> solves a single mirror-symmetric system; it does not implement the other advertised cases. <code>types_m2.py</code> and <code>types_m2_general.py</code> perform finite local searches from selected initial data, without covering the whole parameter domain or every solution branch. The latter changes the groups of boundary disks while retaining some contact indices, so the resulting equations need not even describe the claimed type.

Even an exactly feasible point $u_0$ in a configuration family $\mathcal F$ establishes only

$$
\inf_{u\in\mathcal F}r(u)\le r(u_0).
$$

This is an **upper bound** on the family's minimum. Excluding better coverings requires a **lower bound**, proving that every member has radius at least the target. Treating a local output as the whole family's minimum reverses the needed inequality. Higher precision or large observed gaps between local outputs cannot supply the missing proof.

#### 5. A tiny residual does not certify the claimed minimal polynomial — §1

<code>fplll_search3.py</code> produces a large-coefficient polynomial through an integer-relation search, and numerical substitution in <code>verify_P_final.py</code> gives a tiny residual. That establishes only a value close to zero at a numerical approximation, not an exact zero at the true geometric optimum.

Even correct factorization, irreducibility checks and real-root counting concern the polynomial and its specified root. A separate rigorous connection must establish that this root equals the optimal covering radius. The submission does not provide it. The review uses the specified root to refute the submitted covering; it does not certify it as the optimum's minimal polynomial.

**Review scope and evidence:** the proof and directly supporting programs were read, original bytes and hashes preserved, the exact counterexample replayed, and timing and usage records checked. Thousands-of-digit optimization and integer-relation searches were not rerun in full. The complete session, original input, mathematical review, root-enclosure certificate and verifier remain local. DeepSeek was not asked to generate or upload this report.

A separate rational configuration with a slightly enlarged radius passed the existing exact coverage tool, establishing only a weaker upper bound. It does not repair global optimality. The refutation concerns this submission's exact data and reasoning; it does not establish that the true optimum differs from the reported numerical approximation.

### Downloadable records

[Machine record](record-n11-deepseek-v4-pro-max-20261002.json) · [Report Markdown](record-n11-deepseek-v4-pro-max-20261002.en.md)
