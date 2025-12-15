# Repository Guidelines

Concise contributor guide for the Python LeetCode solutions in this repo.

## Project Structure & Module Organization
- Solutions are grouped by difficulty: `Easy/`, `Medium/`, `Hard/`, each containing Python files named `P<problemId>_<Title>.py` (e.g., `Medium/P48_RotateImage.py`).
- Every file defines a `Solution` class with the LeetCode method signature and often a quick runnable example at the bottom.
- `.vscode/` holds local editor settings; no other build assets or generated files are tracked.

## Build, Test, and Development Commands
- Run a specific solution: `python3 Easy/P1_TwoSum.py` (adjust path as needed).
- To add lightweight checks, prefer `python3 -m unittest discover -s tests` once you add tests under `tests/`.
- Windows users can use `leetcode_push.bat <problemId>` to stage, commit, and push with a standard message.

## Coding Style & Naming Conventions
- Python 3 code with type hints where helpful (`list[int]`, `List[List[int]]`); indent with 4 spaces and avoid tabs.
- Keep filenames in the `P<id>_<CamelCaseTitle>.py` pattern; use snake_case for helper functions/variables and `Solution` for the main class.
- Match LeetCode signatures exactly; avoid changing parameter orders or return types. Keep examples wrapped in `if __name__ == "__main__":` when you add new ones.
- Keep explanatory docstrings/comments concise and focused on the approach or edge cases.

## Testing Guidelines
- Add quick sanity checks near the bottom of the file or in `tests/` to cover core cases and edge constraints (empty inputs, single elements, large bounds).
- Prefer assertions over print-only output for new code; ensure functions are deterministic and side-effect free beyond logging/debug prints.
- If you introduce utilities shared across problems, add unit tests and note expected complexity/behavior in comments.

## Commit & Pull Request Guidelines
- Use the existing convention from `leetcode_push.bat`: `Solved <problem_number>`; include multiple IDs if the change spans several problems.
- PRs should state the problem link, approach summary (algorithm and complexity), and test evidence (commands run, sample cases). Add screenshots only when visual output is relevant.
- Keep commits focused on one problem/feature; avoid bundling unrelated refactors. Mention any deviations from LeetCode signatures or added dependencies in the PR description.
