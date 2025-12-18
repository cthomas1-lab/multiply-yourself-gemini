[← Back to Main Guide](../../README.md) | [Previous: LLMs & Context](../llms-and-context/README.md)

---

# 💡 Tips & Tricks

These are optional productivity boosters that will make you faster and more effective with Windsurf. None of these are required for setup, but they're game changers once you're comfortable with the basics.

---

## 🔄 Experiment and Iterate

When output isn't right, update your rules/prompts. **Hallucinations are learning opportunities.**

The AI won't be perfect on the first try. That's not failure—that's the process:
1. Try something
2. See what works and what doesn't
3. Refine your prompt, rule, memory, llm used, or approach
4. Repeat

> 💡 Every "wrong" output teaches you something about how to communicate with AI better. This is a skill not a tool.

---

## 🎤 Voice Input (Game Changer)

Stop typing everything - use your voice.

### How It Works

1. Click the **microphone/record button** in Windsurf
2. Speak naturally (fast speech is fine)
3. It records a WAV file, then uses an LLM to process speech-to-text
4. Result: ~95% accuracy, way better than Siri/Alexa

### Tips

- Recording stops after ~20 seconds
- **Workflow:** Record → copy text → paste → record more → paste again → build up your full prompt
- Voice is faster than typing - you can vibe code for hours without touching the keyboard
- The AI adapts to your speaking style over time

---

## 📎 Adding Context to Prompts

The more context you give, the better the output.

| Method | How |
|--------|-----|
| **Drag and drop** | Drag files directly into the chat |
| **Copy path** | Right-click file → Copy Path → paste into prompt |
| **Terminal output** | Highlight text in terminal → "Send to Chat" |
| **@ mentions** | Type `@` to reference files, MCP tools, conversations |
| **Open files** | Anything open in the editor can be read by the AI |

### Pro Tips

- Use `@filename` to explicitly reference a file
- Use `@tool-name` to direct prompts to specific MCP servers (e.g., `@fetch`, `@jira`)
- Close files you don't need to reduce context pollution

---

## ⏸️ Queuing Prompts

You don't have to wait for the AI to finish.

| Action | Key | What Happens |
|--------|-----|--------------|
| **Queue** | Enter | Your prompt runs after current task completes |
| **Interrupt** | Shift+Enter | Stops current task, processes your prompt immediately |

### Example

While running a long task:
> "After this finishes, send the summary to the team channel"

The AI queues your request and executes it when ready.

---

## ⏪ Rollback AI Changes

Watched Cascade go too far? No problem - you can rewind.

### How It Works

1. Scroll up in the conversation to find where things went wrong
2. Click on that **previous prompt**
3. Modify the prompt if needed (or just resend as-is)
4. Cascade warns you: *"If you resend from here, I'll undo all changes made after this point"*
5. Confirm, and you're back to that state

### When to Use This

- The AI made changes you didn't want
- You want to try a different approach from an earlier point
- A task spiraled in the wrong direction
- You want to resend the same prompt to a different LLM

> 💡 This is conversation-level rollback, not git. Cascade tracks what file changes it made and can undo them when you rewind.

---

## 🛑 Session Handoff (Stepping Away)

Need to step away but not at a clean stopping point? Don't lose your progress and gain your sanity! Step away often - this addiction hits hard!

**Before you leave:**
> "Document everything we're working on and what the next steps are into a .md file with an appropriate topic name"

**When you return:**
1. Start a fresh conversation (clean context)
2. Tell the AI: "Hey lets pick back up on topic-name.md and get back to the grindstone!"

You get all the ideas and context without the polluted conversation history. Works great for:
- End of day handoffs
- Context switching
- Taking a break mid-task
- Picking up work days later
- Abrupt interruptions

---

## 📁 Personal GitHub Repo (Highly Recommended)

Own a GitHub repo for storing outputs and notes. This is incredibly valuable.

### Use Cases

| Use Case | Example |
|----------|---------|
| **Work notes** | Daily journals, meeting notes, task tracking |
| **Workflow outputs** | Results from anything cool you produce - .md files can be quite easy for consumption  |
| **Shareable artifacts** | Files others can consume (reports, docs) |
| **Backup** | Version-controlled history of your work |

### How It Works

1. Create a personal repo (private or public)
2. Clone it to your workspace
3. Build a workflow to save files in that repo or even tell it to stash the above session-topic.md there
4. Commit and push - now it's saved, shareable and versioned!

---

## 🔀 Your AI is Your Git Expert

Whether you're a git pro or have never touched a command line - it doesn't matter. Your AI handles version control for you.

Git is powerful, but let's be honest: commands like `rebase -i`, `cherry-pick`, and `stash pop` intimidate most developers. With AI, you skip the mental overhead entirely. Describe what you want, and the AI picks the right commands:

- Stashes and unstashes
- Feature branches
- Selective commits and cherry picking
- Interactive rebases
- Conflict resolution

**Example prompt:**
> "These changes are independent thoughts - commit them separately with meaningful messages"

You focus on intent. The AI handles execution.

---

## 🎮 Want to Learn More? (Fun Stuff)

Beyond using AI in your IDE, here are some fun ways to deepen your understanding:

### Prompt Injection Games

**[Lakera Gandalf](https://gandalf.lakera.ai/)** - A game where you try to trick an LLM into revealing a secret password. Each level gets harder as the AI gets better defenses.

Why play?
- Learn how LLMs can be manipulated
- Understand prompt injection attacks
- Get creative with your prompting skills
- It's genuinely fun and addictive

### Further Exploration

- **[Windsurf Documentation](https://docs.codeium.com/windsurf)** - Official docs
- **[MCP Protocol](https://modelcontextprotocol.io/)** - Deep dive into Model Context Protocol

---

[← Back to Main Guide](../../README.md)
