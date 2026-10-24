# Disk Covering Benchmark

[中文](https://pikaaa345.github.io/disk-covering-benchmark/about.zh.html?lang=zh) · **English**

How small can n equal disks be while still covering the entire unit disk? This project uses that question to study AI mathematical research, from finding a configuration to proving the result, and records the time and cost required.

A complete solution must provide the optimal radius's minimal polynomial and rational root-isolating interval, exact centers, continuous coverage and a global optimality proof over all configurations.

## Problems and test records

**[Open the configuration gallery →](https://pikaaa345.github.io/disk-covering-benchmark/index.html?lang=en)**

Browse configurations by n and click a picture to open its problem page. Each page contains test scores, a copyable full prompt, the reference SHA256 and a local comparison form. Chinese and English are available. The gallery lists every n from 11 to 29, with 12 problems per page; unpublished reference answers are shown as Unknown.

Reference fingerprints are available for n = 11, 12, 14, 16, 19, 22, 25, 26 and 27. The global optimality proofs for n=25 and n=26 were accepted by the project’s local mathematical review on 2026-09-26. Independent review of the n=26 minimal-polynomial source remains pending; this is separate from global optimality. Fingerprint matching compares answer data and does not verify a submitted proof. Fingerprints were checked against exact root isolation and independently recomputed. Public submissions are closed; existing scores remain historical demonstrations, and the formal comparison contract is not frozen.

Scoring deadline: every n≤30 problem has a 12-hour (43200-second) limit. No valid result meeting the task's acceptance criteria by the deadline scores 0; late completion also scores 0. Untested runs are not scored as 0.

## Shared tools

All problems use the same tools. Read the [testing guide](https://pikaaa345.github.io/disk-covering-benchmark/guide.html?lang=en) for timing, scoring, acceptance criteria and the complete answer-to-hash procedure.

**[Download tools and materials (ZIP)](https://github.com/pikaaa345/disk-covering-benchmark/archive/refs/heads/main.zip)**

One download contains the answer checker, encoding protocol in both languages, score calculator, self-checks, report prompts, problem statements and usage instructions. It also includes qualified published record summaries. Website source and development history are maintained privately. No separate downloads are needed.

Extract the ZIP, open the project folder and follow the testing guide. The scripts require only Python 3.9+ and its standard library. Coefficients are ordered by increasing degree, and the radius is rounded to 20 decimal places. The checker normalizes and hashes the data; a match does not verify proofs or reported timing.

**For AI agents:** [Instructions](https://pikaaa345.github.io/disk-covering-benchmark/agents.html?lang=en) · [Machine-readable index](benchmark.json). The index locates prompts, records and protocols without navigating website menus.

## Publication and license

The public repository contains downloadable tools and testing materials. Website source and development history are maintained in a private repository; the website publishes approved pages only. Public downloads continue to have their own Git history.

The tools use the [MIT license](LICENSE). No private solver or exact reference answers are included.
