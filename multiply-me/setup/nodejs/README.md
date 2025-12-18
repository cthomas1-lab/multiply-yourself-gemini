[← Back to Main Guide](../../README.md)

---

# 📦 Node.js & npx Setup

`npx` is a tool that comes with Node.js/npm. It lets you run Node.js packages without installing them globally.

---

## Installation

### macOS

```bash
# Install Node.js via Homebrew
brew install node
```

### Windows (WSL/Ubuntu)

> ⚠️ **Verify you're in WSL first!** Check the bottom-left of Windsurf shows "WSL: Ubuntu"

```bash
# Install Node.js via NodeSource repository
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install -y nodejs
```

---

## Verify Installation

```bash
node --version
npm --version
npx --version
```

All three commands should return version numbers.

---

## Test npx

```bash
npx cowsay "Hello!"
```

This downloads and runs the `cowsay` package temporarily without installing it globally.

---

## How npx Works

`npx` is useful for:

- **Running CLI tools** without global installation
- **Running specific versions** of a tool
- **One-off commands** you don't need permanently

### Examples

```bash
# Run a package directly
npx create-react-app my-app

# Run a specific version
npx typescript@4.9.5 --version

# Run a GitHub gist
npx https://gist.github.com/some-gist
```

---

## Why This Matters for Windsurf

Many MCP (Model Context Protocol) servers are distributed as npm packages. You'll use `npx` to run them without cluttering your global npm installation.

Example:
```bash
npx @anthropic/mcp-server-fetch
```

---

## Troubleshooting

**`npx` command not found:**
```bash
brew reinstall node
# Restart your terminal
```

**Permission errors:**
```bash
# Check npm prefix
npm config get prefix

# Should be something like /opt/homebrew or /usr/local
# If it's in your home directory with permission issues, reset it:
npm config set prefix /opt/homebrew
```

---

## ✅ Verification

```bash
node --version && npx --version && npx cowsay "Ready!"
```

---

[← Back to Main Guide](../../README.md)
