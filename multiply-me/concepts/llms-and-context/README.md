[← Back to Main Guide](../../README.md) | [Previous: MCP Servers](../mcp-servers/README.md) | [Next: Tips & Tricks →](../tips-and-tricks/README.md)

---

# 🧠 LLMs and Context Windows

Understanding how LLMs work and how to manage context windows is key to getting the most out of Windsurf.

---

## What Are LLMs?

LLM stands for **Large Language Model** - the AI that powers Windsurf's Cascade. Different LLMs have different strengths, costs, and capabilities.

---

## LLM Families

| Model | Best For | Reasoning |
|-------|----------|-----------|
| **Claude Opus 4.5** | Complex reasoning, architecture decisions, difficult bugs | High |
| **Claude Sonnet 4.5** | General coding, good balance of speed and quality | High |
| **GPT 5.2 Low** | General coding, versatile | Low |
| **GPT 5.2 Medium** | More complex tasks | Medium |
| **GPT 5.2 Reasoning** | Deep analysis, architecture | High |
| **Gemini 3 Pro** | General coding, fast | Low |
| **Gemini 3 Pro Reasoning** | Complex problems, thorough analysis | High |
| **SWE-agent** | Automated code fixes, issue resolution(randomness beware) | Medium |

> ⭐ **shrobbin's favorite:** Claude Opus 4.5 - fast AF, efficient, smooth like butta! Backup with Sonnet

---

## Thinking Models vs Standard Models

| Aspect | Thinking Models | Standard Models |
|--------|-----------------|-----------------|
| **Shows reasoning** | Yes - you see the thought process | No - just the answer |
| **Speed** | Slower | Faster |
| **Token cost** | Higher | Lower |
| **Best for** | Complex problems, learning | Routine tasks, quick edits |

**When to use thinking models:**
- Debugging difficult issues
- Architecture decisions
- When you want to understand the reasoning
- Learning how to approach problems

**When to use standard models:**
- Simple code changes
- Routine tasks
- When speed matters more than explanation

---

## Context Windows

The **context window** is the amount of text (measured in tokens) the LLM can "see" at once. Think of it as the AI's working memory.

### What Counts as Context?

Everything in your conversation:
- Your prompts
- The AI's responses
- Files you've opened or referenced
- **MCP tool descriptions** (loaded at the start of every conversation)
- Code snippets
- Terminal output

### Context Window Sizes

| Model Family | Standard Context | Extended/Thinking |
|--------------|------------------|-------------------|
| **Claude** | ~200K tokens | Up to 1M tokens |
| **GPT** | ~128K tokens | Up to 1M tokens |
| **Gemini** | ~128K tokens | Up to 2M tokens |
| **SWE models** | Varies | Typically 32K-128K |

> 💡 Thinking/reasoning models generally have larger context windows to accommodate their step-by-step processing.

### Why Size Matters

When context gets too large:
- Windsurf auto-grooms (removes content)
- Important information might get dropped
- Responses can become less accurate or frustrate you - breath, learn, train

---

## 🔄 When to Start a New Conversation

**Start fresh conversations frequently.** This is important because:

1. **Clean context** - No stale information from previous tasks
2. **Better accuracy** - The AI isn't confused by unrelated earlier work
3. **Faster responses** - Less context to process - less tokens used

### Signs You Should Start Fresh

- The AI seems confused or references "old" context 
- You're getting unexpected or inconsistent responses
- AI agent keeps trying things that you have already told it not to do(could be the wrong LLM for the job or rules/memories needed)

> 💡 **shrobbin's philosophy:** Treat context windows like cattle, not pets. Kill them often. Start fresh. Don't get attached.

---

## Chat Mode vs Code Mode

Windsurf has two modes in the Cascade panel:

### 💬 Chat Mode

| Capability | Available |
|------------|-----------|
| Read files | ✅ Yes |
| Write/modify files | ❌ No |
| Run commands | ❌ No |

**Use for:** Questions, explanations, planning, understanding code

### 💻 Code Mode

| Capability | Available |
|------------|-----------|
| Read files | ✅ Yes |
| Write/modify files | ✅ Yes |
| Run commands | ✅ Yes |

**Use for:** Actual development work, making changes, running scripts

### Toggling Modes

Look for the mode toggle in the Cascade panel. Switch to **Code Mode** when you want the AI to actually do work, not just talk about it.

> 🎯 Remember: If the AI is giving suggestions instead of doing the work, use the master prompt: *"No, you do it!"*

---

## Switching LLMs

You can change which LLM you're using:

1. Look for the model selector in Windsurf
2. Choose a different model
3. You can even switch mid-conversation and resend a prompt

### Switching Mid-Conversation

Don't like the output? Try a different model without starting over:

1. Click on a **previous prompt** in the conversation
2. Change the **LLM dropdown** to a different model
3. Hit **resend** - it will rollback changes and reprocess with the new model

This is great for:
- Trying a smarter model when the current one struggles
- Switching to a cheaper model for simple follow-ups
- Comparing outputs between models

**Tips:**
- Start with a highly capable model (like Opus) for complex tasks - have it output the steps to complete the task in a file
- Switch to faster/cheaper models for simple follow-ups - have it use the file ^^ to process the tasks sequetially 
- Ask the AI to teach you: *"Which LLM would be best for this task?"*

---

## 💰 Cost & Credits

Different models cost different amounts of credits. You can see credit costs in the **model selector dropdown** - each model shows its relative cost before you select it. Check your usage history in **Windsurf Settings → Account**.

### Tips

- **Check for promos!** Models frequently run promotional pricing - sometimes even free. Great opportunity to experiment with different LLMs and learn their strengths.
- Thinking models use more tokens but show their reasoning and have larger context windows
- Keep context windows clean to avoid wasting tokens
- Start fresh conversations for new topics

---

## Key Takeaways

| Concept | Key Point |
|---------|-----------|
| **LLM choice** | LLMs are like a car - everyone has their own preference. Go for test drives! |
| **Thinking models** | Show reasoning, cost more, good for learning |
| **Context window** | Start fresh often, don't let it get bloated |
| **Chat vs Code** | Use Code mode when you want actual changes |
| **MCP tools** | Their descriptions load into every new conversation |

---

## 🔗 LLM Resources

- **[OpenRouter.ai](https://openrouter.ai/)** - LLM usage statistics, model comparison, and market share data. Great for seeing which models are winning and how they compare.

---

[← Back to Main Guide](../../README.md) | [Previous: MCP Servers](../mcp-servers/README.md)
