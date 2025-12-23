[← Back to Main Guide](../../README.md)

---

# 📦 Node.js & npx Setup (Fedora)

`npx` is a tool that comes with Node.js/npm. It lets you run Node.js packages without installing them globally.

---

## Installation

These commands will install Node.js and npm on your Fedora system.

```bash
# Update your system
sudo dnf update -y

# Install Node.js and npm
sudo dnf install nodejs -y
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

## Why This Matters for Gemini

Some tools and libraries used with Gemini might be distributed as npm packages. You'll use `npx` to run them without cluttering your global npm installation.

Example:
```bash
npx some-gemini-related-tool
```

---

## Troubleshooting

**`npx` command not found:**

```bash
sudo dnf install nodejs -y
# Restart your terminal
```

**Permission errors:**
If you encounter permission errors with npm, it's often best to use a Node.js version manager like `nvm` or ensure your npm prefix is set to a user-writable directory. However, for a basic system-wide installation on Fedora, the `dnf` installation should handle permissions correctly.

---

## ✅ Verification

```bash
node --version && npx --version && npx cowsay "Ready!"
```

---

[← Back to Main Guide](../../README.md)
