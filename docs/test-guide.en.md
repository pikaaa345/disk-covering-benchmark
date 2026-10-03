# Testing guide

[中文](test-guide.md) · **English**

Choose a problem, copy its prompt and view its records in the [problem catalog](https://pikaaa345.github.io/disk-covering-benchmark/index.en.html). This guide describes the shared testing procedure.

Replace `N` in commands with the selected problem number. [Background](background.en.md) · [Scoring](scoring.en.md) · [Answer protocol](answer-protocol.en.txt).

## The mathematical task

Let

$$D=\{x\in\mathbb R^2:\|x\|_2\le1\},\qquad R_D(C)=\max_{x\in D}\min_{1\le i\le n}\|x-c_i\|_2,$$

$$r_D(n)=\inf_{C\in(\mathbb R^2)^n}R_D(C).$$

The covering disks may overlap and extend beyond D. A complete solution must provide the minimal polynomial of the optimal radius itself, in primitive integer form with positive leading coefficient, prove irreducibility, and give a rational interval containing exactly one real root. It must also specify the centers exactly and prove both coverage of the entire disk and a matching lower bound over all configurations. See the full prompt for the precise requirements.

Numerical optimization and finite sampling may help find candidates. They do not replace continuous coverage or a global optimality proof.


## Run one test

1. Choose a task and preserve its prompt and repository commit. Record the model and reasoning setting, starting materials, tools, network policy, hardware, time budget and cost budget. A single run can be reported; state the number of runs and do not infer repeatability from one result.
2. Give the full prompt to the model. Record natural elapsed time, including model work, computations, waiting and verification.
3. Keep the polynomial, isolating interval, configuration, proofs and certificates. Generate an answer fingerprint locally. Compare it only after a reference hash has been published.
4. Use the report prompt to summarize the actual record. Distinguish an answer match, a complete mathematical solution and independently checked proof materials.

## From answer to SHA256

Save the coefficients as a UTF-8 JSON integer array in `coefficients.json`, **in increasing order of degree**: constant coefficient first, leading coefficient last. Keep internal zeros. Do not sort by numerical value. Preserve large integers exactly; never pass them through JavaScript `Number` or floating point.

From the downloaded directory, replace the radius placeholder and run:

~~~text
python tools/diskcover_answer.py --n N --coefficients coefficients.json --radius YOUR_HIGH_PRECISION_RADIUS
~~~

After publication of a reference hash, add:

~~~text
python tools/diskcover_answer.py --n N --coefficients coefficients.json --radius YOUR_HIGH_PRECISION_RADIUS --expected-sha256 PUBLISHED_64_HEX_HASH
~~~

The script normalizes the polynomial to primitive integer form with positive leading coefficient, rounds the radius to **20 digits after the decimal point** using `ROUND_HALF_UP`, and hashes a fixed JSON encoding as UTF-8. Supply at least 30–40 decimal places as a practical starting point; near a rounding boundary, greater precision is necessary. The script outputs the normalized data, exact canonical JSON and SHA256.

A match produces `matches_reference: true` and exit code 0. A mismatch returns 1; invalid input returns 2. Without a reference hash, the script can generate your fingerprint but cannot establish a match.

**Matching fingerprints compare answer data only.** The checker does not verify irreducibility, root isolation, coverage, global optimality, model identity or timing. Keep proof materials separately and state whether they have been checked. The root-isolating interval is a mathematical deliverable but is not included in the v1 hash; 20 decimal places do not prove root uniqueness. Both languages use the same protocol and produce the same hash from the same answer.

## Scores

$$S=\operatorname{RoundHalfUp}\!\left(200+100\log_2\frac{21600}{T}\right),\qquad T>0\text{ seconds}.$$

Higher scores mean shorter completion times, with no upper cap. With a six-hour baseline, six hours scores 200, each halving adds 100 points, and three minutes scores 891. Round the result to an integer using `ROUND_HALF_UP`. The three-minute example is arithmetic, not an observed research run.

For n≤30, each problem has a fixed 12-hour (43200-second) time limit. No valid result meeting the task's acceptance criteria within 12 hours scores 0; later completion also scores 0. Only completion by the deadline, including the deadline itself, receives an efficiency score. Formal tests must also freeze acceptance criteria and timing endpoints; time limits for n>30 remain to be set. An untested task is not a zero score. Current historical demonstrations use different timing endpoints and acceptance scopes, so they are not a formal comparable leaderboard. See [historical records](../results/README.en.md).

Difficulty is not assumed to increase strictly with n. There is currently no combined ranking across different n values or costs.

## Publication status

The catalog contains prompts and reference fingerprints for n = 11, 12, 14, 16, 19, 22, 25, 26 and 27. The n=25 reference is for a fixed candidate radius without a proved matching global lower bound; the n=26 source global optimality proof still awaits complete review. Polynomial coefficients, radius decimals and isolating intervals remain private. Other tasks will be added after their materials are checked; a missing fingerprint does not imply that a problem is unsolved worldwide.

The publisher currently posts their own records. There is no public submission endpoint, independently audited leaderboard or reward commitment. Disclose use of known configurations, existing code or answers. Public prompts and hashes do not provide an anti-cheating guarantee.

## Tools and page publication

Run `python tools/check_tools.py` to check fingerprinting and scoring tools. These checks do not execute a mathematical solver or prove coverage or global optimality. Website source is maintained privately and only approved pages are deployed. The public repository supplies downloadable materials.
