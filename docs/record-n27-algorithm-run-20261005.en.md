# n=27 best recorded run: DGC v62 + MinPoly v8

Algorithm versions: DGC v62 for automated proof and MinPoly v8 for minimal-polynomial computation (execution binding: 20261004-v8). This run uses their third shared 32-core scheduling revision (Shared32 v3), identified as optimized-32-03.

This joint pipeline completed in **882.4296346960001 seconds** (14 min 42.43 s, including a fresh build), for a website score of **661**. It is filed under Best recorded run. The entry describes inherited research algorithms, AI orchestration and local computation; one observation does not establish stable performance.

## Starting information, hardware and timing

Inputs were n=27 and the research project’s existing research programs and verification materials, with prior research results available as starting information. Execution used daily Ubuntu WSL, SageMath, Python and locally compiled C++. The host was an AMD Ryzen 9 8945HX with 16 physical and 32 logical cores. Memory was 32 GiB DDR5 according to the existing same-machine hardware record, without a fresh launch-time measurement.

The total includes a fresh program build lasting 7.407230013 seconds and a joint controller interval of 874.888980938 seconds, including startup and shutdown overhead. Proof generation took 642.518606473 seconds, independent verification 206.224039099 seconds and the algebra branch 637.358080255 seconds. Concurrent stages overlap and their times are not summed. The score uses program runtime, excluding prior research, AI interaction, archiving, publication and later reference-fingerprint comparison. It does not measure model elapsed time or solving the full public problem from scratch.

## Resource allocation and algorithms

CPUs 0–31 were available. A shared controller assigned 16 logical cores to parallel algebra phases and two to serial phases, with the rest assigned to proof work. Proof work received all 32 once algebra finished. Changes checked actual descendant processes and thread affinities. Proof admission followed the current budget while admitted jobs continued. Runtime scheduling receipts and thread budgets remain in the private archive. A host sample reached 100%; this does not establish continuous full utilization. That sample was retained in tool output, without a separate sampling file.

The proof branch handled covering research and proof verification; the algebra branch produced exact algebraic results for the radius and checked their consistency. The branches ran together under shared resource management and completed the prescribed work and final checks. The verification scope was not reduced to obtain the reported runtime. Detailed solving procedures and internal computational structures remain in the private research and execution archive.

Final acceptance materials and execution records are stored separately. The result relies on the applicability assumptions of the inherited research and establishes no new independent unconditional global-optimality proof or formal proof. Existing research and verification materials contributed to result acceptance; this runtime must not be presented as the time to conduct all research from scratch.

## Official answer fingerprint and evidence

The official diskcover-minpoly-v1 checker normalizes ascending integer coefficients to a primitive polynomial with positive leading coefficient, rounds the interval-determined radius to 20 decimal places using ROUND_HALF_UP, and hashes canonical JSON with SHA-256. Both interval endpoints round identically, without floating-point conversion. The computed fingerprint matches the website reference:

`c31dce1e3cac5f00d12105435f9f7c61a0456844a01867efbc69011f90473b55`

Checked at 2026-10-05 (UTC). The fingerprint checks answer data, not the global proof, authorship or timing. The raw coefficient-file digest and answer-protocol fingerprint are recorded separately. Exact answers, isolation certificates, code, execution receipts and public-conversation exports remain in a local private ZIP. The website publishes this run's score and report.

Stable test ID: `T_20261005T042916Z_01a10823`. Run ID: `optimized-32-03`. The conversation archive is marked partial; compacted or truncated content is not reconstructed. Costs and complete development time were not recorded under one common scope.
