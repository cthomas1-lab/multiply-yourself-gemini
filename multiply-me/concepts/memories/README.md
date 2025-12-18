[← Back to Main Guide](../../README.md) | [Previous: Workflows](../workflows/README.md) | [Next: MCP Servers →](../mcp-servers/README.md)

---

# 🧠 Memories in Windsurf

Memories allow Windsurf to retain context across conversations. They help the AI remember important information about you, your projects, and your preferences.

---

## What Are Memories?

Memories are pieces of information that Windsurf stores and retrieves to provide more personalized and context-aware assistance. They persist across chat sessions.

```
You: "Remember that we use Tailwind CSS in this project"
     ↓
Windsurf stores: "Project uses Tailwind CSS" (workspace memory)
     ↓
Future sessions: Windsurf suggests Tailwind classes automatically
```

---

## Scope Types

| Scope | Applies To |
|-------|------------|
| **Global** | All workspaces and projects |
| **Workspace** | Single project only |

---

## What to Store and how to scope it

| Global (everywhere) | Workspace (project-specific) |
|---------------------|------------------------------|
| Your name, preferences | Project architecture |
| Coding style choices | Tech stack details |
| Tool preferences | API endpoints |

---

## Memory Retrieval

Memories are **automatically retrieved** when relevant to your current task. You don't need to explicitly ask for them.

| Trigger | Example |
|---------|---------|
| Related topic | Asking about styling → retrieves "uses Tailwind" |
| Similar context | Working on API → retrieves endpoint info |
| Direct reference | "How do I know Frank?" → retrieves memory about your friend Frank |

---

## Managing Memories

### Creating Memories (Prompt-Driven)

Memories are created through conversation. Just tell Windsurf what to remember:


> *"Remember I'm vegetarian - no meat in any recipe suggestions."*

> *"Remember when I say 'the cabin' I mean my family's lake house in northern Minnesota."*

These are facts and context - not instructions. Memories help Windsurf understand *you* so conversations feel more natural and you don't have to repeat yourself.

**Why this matters:**
- Ask "what should I get Frank for his birthday?" and Windsurf already knows who Frank is
- Request a recipe and it won't suggest chicken
- Mention "heading to the cabin" and it knows what you mean

### Updating & Deleting Memories (IDE Settings)

Once created, memories are managed through the Windsurf UI:

1. Open **Windsurf Settings** (gear icon or `Cmd/Ctrl + ,`)
2. Navigate to **Cascade** → **Memories**
3. Find the memory you want to edit or delete
4. Click to edit the text directly, or delete it

This gives you full control to refine memories after they're created, fix any misinterpretations, or remove outdated information.

---

[← Back to Main Guide](../../README.md) | [Previous: Workflows](../workflows/README.md) | [Next: MCP Servers →](../mcp-servers/README.md)
