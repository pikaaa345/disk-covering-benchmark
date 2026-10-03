# Background

The unit disk consists of all points in the plane at distance at most 1 from the origin. Cover it with n closed disks of equal radius, allowing overlaps and extension beyond the boundary, and minimize their common radius. Every point, including the boundary, must be covered.

Erich Friedman's [Circles Covering Circles](https://erich-friedman.github.io/packing/circovcir/) illustrates known configurations by n and distinguishes configuration discoveries from some proofs of optimality. Its scale fixes the small disks' radius to 1 and maximizes the covered disk's radius. This benchmark instead fixes the covered disk's radius to 1 and minimizes the covering radius. Uniform rescaling relates the two formulations. Finding a good configuration and proving global optimality are distinct tasks.

The problem connects geometry and continuous optimization, combinatorial classification, rigorous pruning, algorithm design, exact algebra and verification. A candidate must become an exact algebraic answer, and computation must be linked to mathematical statements by proof.

Difficulty need not increase strictly with n: some sizes admit useful structure or simple algebraic expressions. The project does not label every task as an unsolved open problem, or treat a table of known candidates as a complete optimality proof. Each task needs its own status.

Minimal polynomials provide compact, exact and canonically encodable answer data. They do not replace proof: the correct polynomial of a good candidate still does not establish continuous coverage or a global lower bound. Mathematical completion and lightweight fingerprint comparison are separate.

The background link was checked on 2026-09-30. It contains known configurations and numerical information. Decide before a test whether the model may access it. This repository does not reproduce its numerical radii or images.
