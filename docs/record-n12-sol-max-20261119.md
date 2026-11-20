This single run submitted an exact solution and replayable certificates. The answer fingerprint matched and the same assistant replayed the geometry and algebra checks. The demonstrative score is **711** under the existing benchmark formula. This run has no independent mathematical review or formal ranking.

### Existing proof reused and work performed in this test

The run reused geometry and topology certificates from the [pinned public Cover12 proof](https://github.com/VonEquinox/DiskCoveringSolve/tree/089584973f41e6374ce110f6e5b5ee456df19352/cover12). It added radius elimination, a link to the configuration root, and irreducibility over a finite field.

### Task and timing

| Timing basis | Record |
|---|---|
| Main natural elapsed time | **625.204 s** through completed final delivery |
| Goal accumulated time | 595 s before final delivery |
| Original deadline | 12 hours, met |

The run began on November 19, 2026 at 19:35 in New York (November 20 at 00:35 UTC). The geometry replay took 52.95 seconds within the main time. Subsequent archiving and publishing are separate.

### Computing conditions

Windows x64, CPython 3.13.13, SymPy 1.14.0, NumPy 2.3.5 and SciPy 1.17.0. A read-only host query during report preparation reported an AMD Ryzen 9 8945HX and approximately 31.2 GiB of usable physical memory. Hardware at task start and actual cost were not recorded.

### Input prompt

The request referenced the [n=12 problem](n12.html?lang=en), asked for a proof as quickly as possible, allowed public Internet material, and restricted local inputs to the chat workspace and excluded local skills.

### Main stages

All eight geometry modules passed, including the continuous covering complex, 38,208 topology orbits, 38,076 Farkas exclusions, 131 graph-energy exclusions and one convexity certificate. Exact integer and rational checks associated the isolated radius with the minimal polynomial.

### Route changes and issues

The website prompt was obtained through the benchmark repository after the Pages fetch failed. The upstream archive download timed out after the required members arrived. The needed files were recovered locally and 21 upstream input hashes were verified before replay.

### Verification, delivery and limits

The diskcover-minpoly-v1 fingerprint matched the reference. The exact solution and the replay package remain in the private test archive. The evidence covers a single run and its executed checks.

### Downloadable records

[Structured test record](record-n12-sol-max-20261119.json) · [English report](record-n12-sol-max-20261119.en.md) · [Machine-readable history](n12-sol-max-20261119-history.json).
