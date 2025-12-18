[← Back to Main Guide](../../README.md) | [Previous: Rules](../rules/README.md) | [Next: Memories →](../memories/README.md)

---

# ⚡ Workflows in Windsurf

Workflows are reusable sequences of actions you trigger with a simple command like `/workflow-name`. Instead of typing the same instructions repeatedly, create a workflow once and invoke it anytime.

---

## Scope Types

| Scope | Location | Use Case |
|-------|----------|----------|
| **Global** | Windsurf settings | Personal automations you use everywhere |
| **Workspace** | `.windsurf/workflows/` in project | Project-specific or team-shared workflows |

---

## Workflows vs Rules

| Aspect | Rules | Workflows |
|--------|-------|-----------|
| **Purpose** | Guide behavior | Automate tasks |
| **Activation** | Always active | Triggered on demand (`/name`) |
| **Nature** | Passive guidelines | Active sequences |

---

## Key Patterns for Effective Workflows

| Pattern | Why It Matters |
|---------|----------------|
| **Sequential thinking** | Keeps complex workflows organized and on track |
| **Tracking files** | Enables resume on failure, shows progress |
| **Output location** | Separate shareable workflows from local output |
| **User verification** | Always confirm before writing to external systems |
| **MCP integrations** | Connect to Discord, Slack, Google Drive, fetch - whatever you need |

---

## 💡 Let Your Agent Create Workflows For You

Don't write workflows from scratch. Describe what you want and let your AI agent build it for you!

---

## Example Workflow: `/tl-dr` - Home Server Changelog Summaries

If you run a home server with apps like Home Assistant, Tandoor, Immich, Nextcloud, or Pi-hole, you know Watchtower keeps everything updated automatically. But who has time to read all those changelogs?

This workflow gives you a quick summary of what's changed since you last checked.

**Prompt to create this workflow:**

> *"Create a workflow called `/tl-dr` for tracking my home server app updates. I run these apps via Docker with Watchtower auto-updating them: Home Assistant, Tandoor (recipes), Immich (photos), Nextcloud, and Pi-hole. The workflow should use @mcp:fetch to grab each app's changelog/release notes from their GitHub releases or docs site, track the last-seen version for each app in ~/tl-dr/tracking.md, and only summarize what's NEW since my last run. Output a brief summary to ~/tl-dr/YYYY-MM-DD-updates.md with app name, version changes, and key updates (new features, breaking changes, security fixes). Keep it concise - I just want the highlights."*

### The Workflow

```yaml
---
description: Summarize home server app updates since last check
---
Use @mcp:sequential-thinking to process each app methodically.

OUTPUT: ~/tl-dr/YYYY-MM-DD-updates.md

TRACKED APPS:
- Home Assistant: https://github.com/home-assistant/core/releases
- Tandoor: https://github.com/TandoorRecipes/recipes/releases  
- Immich: https://github.com/immich-app/immich/releases
- Nextcloud: https://github.com/nextcloud/server/releases
- Pi-hole: https://github.com/pi-hole/pi-hole/releases

1. Load tracking state
   - Read ~/tl-dr/tracking.md for last-seen versions per app
   - If no tracking file, this is first run - just capture current versions

2. For each tracked app:
   - @mcp:fetch the releases page
   - Extract current version and release notes
   - Compare to last-seen version in tracking file
   - If newer: summarize key changes (features, fixes, breaking changes)
   - If same: skip

3. Generate summary
   - Write ~/tl-dr/YYYY-MM-DD-updates.md with:
     - Apps that updated (version X → Y)
     - Brief highlights for each (2-3 bullet points max)
     - Any breaking changes or required actions flagged clearly
   - Update tracking.md with new versions

4. Quick verdict
   - End with a one-liner: "All good" or "Action needed: [app] requires [thing]"
```

---

> 💡 **Remember:** Workflows should match YOUR thinking process. This is just an example - build ones that fit how you work.

---
[← Back to Main Guide](../../README.md) | [Previous: Rules](../rules/README.md) | [Next: Memories →](../memories/README.md)
