[← Back to Main Guide](../../README.md) | [Previous: Memories](../memories/README.md) | [Next: LLMs & Context →](../llms-and-context/README.md)

---

# 🔌 MCP Servers in Windsurf


## 🚀 Why MCP Servers Are a Game Changer

Your AI agent is already powerful - it knows your files, has vast LLM knowledge, and learns from your conversations. But MCP servers take it to another level entirely.

With MCP servers, your agent can:
- **Read any web page** and instantly have that as context
- **Remember things** across sessions with persistent memory
- **Interact with external services** - your calendar, your home automation, your notes
- **Interact with your other high touch tools** - discord, webex, jira, confluence, etc 

This is where things get really exciting. You're not just chatting with an AI anymore - you're working with an agent that can reach out into the world and do things.

---

## What Are MCP Servers?

MCP servers are external processes that provide additional tools and resources to Windsurf. They follow a standard protocol that allows AI assistants to interact with external systems.

**Think of them as plugins** that give Windsurf new abilities:
- Fetch web pages
- Store persistent memories
- Break down complex reasoning
- Interact with external APIs

---

## How MCP Works

```
┌─────────────┐     MCP Protocol     ┌─────────────┐
│  Windsurf   │ ◄──────────────────► │ MCP Server  │
│  (Cascade)  │                      │  (Plugin)   │
└─────────────┘                      └─────────────┘
                                            │
                                            ▼
                                     ┌─────────────┐
                                     │  External   │
                                     │   Service   │
                                     └─────────────┘
```

---

## ⚠️ Important: MCP Tools and Context Windows

**Every MCP server you enable adds its tool descriptions to your context window at the start of each conversation.**

This means:
- More MCP servers = more context used before you even start = more tokens used
- Disable MCP servers you're not actively using

---

## Finding & Installing MCP Servers

Windsurf has a built-in **MCP Marketplace** that makes discovering and installing servers easy:

1. Open **Windsurf Settings** (gear icon or `Cmd/Ctrl + ,`)
2. Navigate to **Cascade** → **MCP**
3. Click **Add Server** to browse the marketplace
4. Search for servers by name or browse categories
5. Click to install - Windsurf handles the configuration

For servers not in the marketplace:
- Check the public registry: [https://github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
- Search npm/PyPI - many MCP servers are published as packages
- Ask your AI agent - it can help you find and configure servers

**Can't find what you need?** Pick up [The Forge](../../../the-forge/README.md) - a developer toolkit I created - and tell your agent to write the MCP server for you. Seriously, it can do that.

---

## Configuration

MCP servers in Windsurf are configured **globally** - they're available in all your workspaces. I firmly believe they need to change this to allow workspace scoping mcp server config and I am activly pressing this issue. 

| Aspect | Details |
|--------|---------|
| **Configuration File** | `~/.codeium/windsurf/mcp_config.json` |
| **Management** | Settings → Cascade → MCP |

---

## Recommended MCP Servers

These three servers are referenced throughout this guide and provide basic but essential capabilities:

---

### 🧠 Memory
Persistent memory storage for the AI.

**✅ Available in the windsurf MCP Marketplace** - easiest install method!

```json
{
  "memory": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-memory"],
    "env": {
      "MEMORY_FILE_PATH": ""
    }
  }
}
```

**Use cases:** Storing project context, remembering decisions, building knowledge over time

**Setup:** No tokens required. Just needs Node.js/npx installed.

---

### 🤔 Sequential Thinking
Helps with complex reasoning tasks. Monster prompts that you don't want your LLM to mess up and skip over stuff - tell it to use squential thinking to process the prompt.

**✅ Available in the windsurf MCP Marketplace** - easiest install method!

```json
{
  "sequential-thinking": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"],
    "env": {}
  }
}
```

**Use cases:** Breaking down complex problems, step-by-step analysis, workflows

**Setup:** No tokens required. Just needs Node.js/npx installed.

---

### 🌐 Fetch
Fetches web pages and extracts content. Tell your LLM to read any web pages or documents you need it to and its now context to be aware of.

```json
{
  "fetch": {
    "command": "docker",
    "args": [
      "run",
      "-i",
      "--rm",
      "mcp/fetch",
      "--ignore-robots-txt"
    ]
  }
}
```

**Use cases:** Reading documentation, fetching changelogs, web research

**Setup:** Just needs a container manager running.

---

## Full Example Config

Now this file is json so if you hand edit and mess it up - just tell your agent to fix it if you are not a json expert.
Here's what a complete `~/.codeium/windsurf/mcp_config.json` looks like: 

```json
{
  "mcpServers": {
    "memory": { ... },
    "sequential-thinking": { ... },
    "fetch": { ... }
  }
}
```

---

## Key Takeaways

| Aspect | Details |
|--------|---------|
| **What** | External tools that extend Windsurf |
| **How** | Install via Marketplace, or configure manually |
| **Config** | `~/.codeium/windsurf/mcp_config.json` (global only) |
| **Top 3** | Memory, Sequential Thinking, Fetch |

---

## Learn More

- [MCP Protocol Documentation](https://modelcontextprotocol.io/)
- [MCP Server Registry](https://github.com/modelcontextprotocol/servers)

---

[← Back to Main Guide](../../README.md) | [Previous: Memories](../memories/README.md) | [Next: LLMs & Context →](../llms-and-context/README.md)
