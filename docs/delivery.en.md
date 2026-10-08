# Runtime and delivery

This is source and documentation, not an installable AI skill or a disk-covering solver. It needs no administrator privileges, GUI or third-party Python packages. Downloading requires network access; fingerprinting, scoring, self-checks and static-page generation work offline.

| Target | Requirement | Actual verification |
|---|---|---|
| Windows x64 | Python 3.9+, standard library | Tool self-check executed with Python 3.13.13 |
| Linux | Python 3.9+, standard library | Standard-library code and relative paths; not executed |
| macOS | Python 3.9+, standard library | Standard-library code and relative paths; not executed |

Run `python --version` and `python tools/check_tools.py`. On Linux/macOS, the executable may be `python3`; on Windows, `py -3` may be available. If Python is missing or too old, use an environment chosen by the operator. This project does not install software automatically. For input errors, check paths, the UTF-8 JSON integer array and command arguments against the answer protocol.

Human entry point: README.en.md. AI entry point: AGENTS.en.md. Machine entry point: benchmark.json. Run commands from the extracted repository directory. File names are case-sensitive. There are no machine-specific absolute paths or installation state; removing your own download removes the local copy.

The package contains public prompts, protocols, tools, synthetic checks, report prompts, an illustrative configuration and qualified historical summaries. It does not contain reference coefficients, radius decimals, root-isolating intervals, a private solving algorithm, transcripts or original proof packages. Tool self-checks do not establish mathematical research performance.
