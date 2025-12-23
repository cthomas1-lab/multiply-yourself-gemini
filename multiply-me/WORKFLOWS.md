# Gemini Workflows

## debug-to-fix
When I paste an error, log output, or describe a problem:

1. Identify the most likely root cause(s).
2. Propose 1–3 fixes, ordered from least invasive to most invasive.
3. For each fix:
   - Explain what it does
   - Show the exact commands to run
   - Explain what success looks like
4. Ask before running destructive or system-wide commands (sudo, dnf, rm).
5. After applying a fix, re-run the failing command or test and summarize results.


## commit-crafter
When I ask for a commit message:

1. Run `git diff --staged`.
2. Analyze the changes.
3. Draft a commit message using Conventional Commits format:
   - Short imperative subject (≤50 chars)
   - Optional body explaining *why*
4. Do NOT run `git commit`.
5. If changes are too large, suggest splitting into multiple commits.


## feature-kickstart
When I start a new feature:

1. Analyze the repository structure to determine correct locations and naming.
2. Propose the exact list of files to create and wait for approval.
3. Create minimal implementation files and corresponding tests.
4. List created file paths and how to run tests.