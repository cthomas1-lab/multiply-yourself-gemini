[← Back to Main Guide](../../README.md) | [Next: Workflows →](../workflows/README.md)

---

# 📜 Rules in Windsurf

Rules are instructions that guide how Windsurf (Cascade) behaves. They can be scoped globally or to specific workspaces.

---

## What Are Rules?

Rules are persistent instructions that Windsurf follows during your coding sessions. Think of them as "preferences" or "guidelines" that shape how the AI assistant works with you.

---

## Rules Scopes

### 🌍 Global Rules

**Apply to ALL workspaces and projects.**

| Aspect | Details |
|--------|---------|
| **Location** | Windsurf settings / global config |
| **Use Case** | Personal preferences that apply everywhere |
| **Examples** | Coding style, communication preferences, safety rules |

**When to use global rules:**
- You want the same behavior across all projects
- Personal preferences (e.g., "be concise", "explain your reasoning")
- Universal safety guidelines

---

### 📁 Workspace Rules

**Apply only to a specific project/workspace.**

| Aspect | Details |
|--------|---------|
| **Location** | `.windsurf/rules/` in your project |
| **Use Case** | Project-specific guidelines |
| **Examples** | Framework conventions, team standards, project architecture |

**When to use workspace rules:**
- Project-specific coding standards
- Team conventions for a particular codebase
- Technology-specific guidelines (e.g., "use React hooks, not class components")

---

## Rule Priority

When rules conflict, **workspace rules take precedence** over global rules for that workspace.

```
Global Rule: "Use tabs for indentation"
Workspace Rule: "Use 2 spaces for indentation"

→ In that workspace: 2 spaces will be used
→ In other workspaces: tabs will be used
```

---

## Key Takeaways

| Scope | Applies To | Location | Priority |
|-------|------------|----------|----------|
| Global | All workspaces | Windsurf settings | Lower |
| Workspace | Single project | `.windsurf/rules/` | Higher |

---

## 💡 Let Your Agent Create Rules For You

Don't write rules from scratch - let your AI agent interview you and build them! Here are some starter prompts that will walk you through creating personalized rules:

### 🗣️ Communication Style Rules

> *"I want to create a global rule for how you communicate with me. Interview me with 3-5 questions about my communication preferences - things like how verbose I want responses, whether I prefer you to ask questions or just do the work, how you should handle uncertainty, and what tone works best for me. Then create a rule file based on my answers."*

### 💻 Coding Preferences Rules

> *"Help me create a global rule for my coding preferences. Ask me a few questions about my style - things like how I feel about comments, what languages or frameworks I use most, how I handle error handling, my thoughts on testing, and any patterns I love or hate. Then generate a rule file from my answers."*

### 🎭 Personality & Vibe Rules

> *"I want to set up some personality rules for how you interact with me. Interview me about things like: Do I want humor in our conversations? How should you respond when I'm frustrated? Should you celebrate wins with me? Any pet peeves I have? Create a fun personality rule file based on what you learn."*

### 📁 Workspace-Specific Rules

> *"I'm starting a new project for [describe project]. Ask me questions about the tech stack, folder structure, coding conventions, and any specific patterns I want to follow. Then create a workspace rule file in .windsurf/rules/ for this project."*

The agent will ask you questions, learn your preferences, and create properly formatted rule files in the right locations.

---

## Example Rules

Here are some fun and practical rules to inspire you:

### Global Rule Examples (Personal Preferences)

```markdown
# Communication Style
- Be concise and direct - no fluff
- Always ask before deleting files
```

```markdown
# Coding Preferences  
- Use descriptive variable names, not single letters
- Add comments only when the "why" isn't obvious from the code
```

```markdown
# Fun Personality
- Occasionally use dry humor
- Celebrate wins with me (but keep it brief)
```

### Workspace Rule Examples (Project-Specific)

**For a personal journaling:**
```markdown
# Journal Project Rules
- Ask me how certain events made me feel to capture more than just the event itself because I don't talk about feelings
- Always include title, date, and tags when writing a journey entry as a unique file
- When I mention new names of people ask me if I want to add them to the journal and validate the name spelling and nicknames
```

**For home server assistance:**
```markdown
# Home Server Rules
- Recommend infrastructure as code as the primary method for application deployment
- Always create a backup before modifying configs
- My home server can be accessed using ssh name "home-server" 
```

---

[← Back to Main Guide](../../README.md) | [Next: Workflows →](../workflows/README.md)
