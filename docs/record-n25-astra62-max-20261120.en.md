# n=25 · gpt-6.2 astra/max

**478 points** in **3,140 seconds** (52 min 20 s) of scored natural elapsed time.

### Proof sources and the model's contribution

The candidate is credited to Jeremy Tan in [Friedman's covering table](https://erich-friedman.github.io/packing/circovcir/). The run adapted the public [20-disk proof](https://github.com/VonEquinox/DiskCoveringSolve/blob/089584973f41e6374ce110f6e5b5ee456df19352/cover20/docs/r20_proof_zh.md), developed the inner-cycle reduction and generated a fresh enumeration, rigidity check and certificate collection.

### Task and acceptance standard

The [n=25 prompt](n25.html) requires the radius's minimal polynomial, an exact configuration, coverage of the closed disk, a global lower bound, and replayable materials for computer-assisted steps. The user allowed public web sources and files generated in the working directory during solving.

### Test information and timing

| Item | Record |
|---|---|
| Test ID | T_20261120T010001Z_01a1f677 |
| Time limit | 43,200 seconds under the benchmark rubric |
| Scored elapsed time | 3,140 seconds, from 01:00:01 to 01:52:21 UTC on 2026-11-20 |
| Goal meter | 3,139 seconds |

### Computing conditions and usage

| Item | Recorded scope |
|---|---|
| Model | gpt-6.2-astra, max reasoning, from the original turn context |
| Exact replay | Windows x86-64, Python 3.13.13, MinGW-w64 GCC 13.2.0, 24 workers |
| Goal meter | 460,391 tokens |
| Thread through the final test response | 15,683,540 input tokens, 15,322,624 of them cached, 103,734 output tokens, 15,787,274 total |
| Cost | Unavailable |

### Main research phases

| Phase | Work | Recorded result |
|---|---|---|
| Before 00:22 | Exact configuration and full-disk coverage | Algebraic construction and proof by triangles and circular caps |
| About 00:22–00:43 | Exhaustive lower bound | Voronoi reduction, inner-cycle screening, integer force certificates and rigidity |
| About 00:43–00:52 | Clean replay and packaging | 216.098-second full replay included in the scored time |

### Changes of emphasis and difficulties

The matching lower bound required excluding continuous families of asymmetric placements. A separate exact rigidity argument treated the neighborhood of equality.

### Verification, deliverables and limitations

The final replay rebuilt the enumeration and checked 8,583,814 retained records and 8,624,620 strict force leaves, with zero unresolved records. It checked a 146-dimensional rigidity matrix. The answer fingerprint matched the published reference. The run's written proof and replay serve as its underlying mathematical evidence.

### Archive and downloadable records

[record-n25-astra62-max-20261120.json](record-n25-astra62-max-20261120.json) · [Markdown](record-n25-astra62-max-20261120.en.md) · [History](n25-astra62-max-20261120-history.json)
