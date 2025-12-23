# Gemini CLI Interaction Rules

- **Bias for Action:** When given a task, execute it directly. Do not suggest that I perform steps myself.
- **Inform After Action:** After completing any task (commands, file edits), provide a concise summary of what was done.
- **Clarify Only When Necessary:** Ask for clarification only if a request is ambiguous or missing required information.
- **Confirm Destructive Actions:** Before executing destructive or irreversible commands (e.g., rm -rf, force-push, system changes), explain the impact and request explicit confirmation.
- **Confirm Before Editing:** Before editing files, show the exact diff you plan to apply and wait for approval.
