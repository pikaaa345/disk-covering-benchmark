# Use the public source package

This ZIP contains the public benchmark tools, protocols, prompts, qualified record summaries. Website source is maintained privately. It is a source package, not an installable agent skill or a disk-covering solver.

Read README.md and package-manifest.json first. Extract into a user-owned directory, open that directory, discover the operating system and available Python executable, and run `python --version` (or `python3 --version`). Python 3.9+ and its standard library are sufficient. No administrator access, package manager, GUI or network is required after downloading. If Python is unavailable or too old, report that fact and obtain the user's approval before installing anything.

Run `python -B tools/check_tools.py`. Exit 0 reports synthetic protocol and scoring checks; it does not establish a mathematical result. Run the checker as documented in docs/test-guide.en.md. The answer checker returns 0 for successful generation or a match, 1 for a mismatch, and 2 for invalid input. Preserve exact integer coefficients and supply the radius as a decimal string.

The score tool verifies integer rounding with exact rational arithmetic. Supported positive times have decimal adjusted exponents between -1000 and 1000; values outside this implementation range produce an input error.

If a command fails, check the working directory, Python version, case-sensitive paths and protocol inputs first. Use `python3` when that is the local executable. Preserve the original files, document any adaptation, and rerun the checks. Do not change hash encoding or scoring rules, install tools, alter network settings or publish answers automatically.

No installation state is created. To remove the package, remove only your own extracted directory; preserve any answers or proof files you placed there. Windows x64 was tested from a clean extraction with spaces and non-ASCII characters in its path. Linux and macOS were not executed in this delivery check. See AGENTS.en.md or AGENTS.md for the mathematical testing workflow.
