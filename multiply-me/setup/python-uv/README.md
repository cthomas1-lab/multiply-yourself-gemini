[← Back to Main Guide](../../README.md)

---

# 🐍 Python uv & uvx Setup

`uv` is an extremely fast Python package installer and resolver (written in Rust). `uvx` is like `npx` but for Python—it runs Python tools in isolated environments.

---

## Installation

### macOS

```bash
# Install uv via Homebrew
brew install uv
```

### Windows (WSL/Ubuntu)

> ⚠️ **Verify you're in WSL first!** Check the bottom-left of Windsurf shows "WSL: Ubuntu"

```bash
# Install uv via the official installer
curl -LsSf https://astral.sh/uv/install.sh | sh

# Add to PATH (restart terminal or run this)
source $HOME/.local/bin/env
```

---

## Verify Installation

```bash
uv --version
uvx --version
```

Both commands should return version numbers.

---

## Test uvx

```bash
uvx cowsay "Hello from Python!"
```

This downloads and runs the Python `cowsay` package in an isolated environment.

---

## How uvx Works

`uvx` is useful for:

- **Running Python CLI tools** without installing them globally
- **Avoiding dependency conflicts** between tools
- **One-off commands** you don't need permanently

### Examples

```bash
# Run a Python tool
uvx black --check myfile.py

# Run a specific version
uvx ruff@0.1.0 check .

# Run with extra dependencies
uvx --with requests httpie https://api.github.com
```

---

## Why This Matters for Windsurf

Many MCP (Model Context Protocol) servers are distributed as Python packages. You'll use `uvx` to run them without managing virtual environments manually.

Example:
```bash
uvx mcp-server-fetch
```

---

## uv vs pip

| Feature | uv | pip |
|---------|-----|-----|
| Speed | 10-100x faster | Standard |
| Resolver | Modern, handles conflicts well | Can struggle with complex deps |
| Isolation | Built-in with `uvx` | Requires virtualenv |
| Written in | Rust | Python |

---

## Troubleshooting

**`uvx` command not found:**
```bash
brew reinstall uv
# Restart your terminal
```

**Cache issues:**
```bash
uv cache clean
```

---

## ✅ Verification

```bash
uv --version && uvx --version && uvx cowsay "Ready!"
```

---

[← Back to Main Guide](../../README.md)
