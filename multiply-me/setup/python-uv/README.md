[← Back to Main Guide](../../README.md)

---

# 🐍 Python uv & uvx Setup (Fedora)

`uv` is an extremely fast Python package installer and resolver (written in Rust). `uvx` is like `npx` but for Python—it runs Python tools in isolated environments.

---

## Installation

This command will install `uv` on your Fedora system using the official installer script.

```bash
# Install uv via the official installer
curl -LsSf https://astral.sh/uv/install.sh | sh

# Add to PATH (restart terminal or run this)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
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
uvx cowsay -t "Hello from Python!"
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

## Why This Matters for Gemini

You can use `uvx` to run Python-based tools that extend Gemini's functionality without polluting your global Python environment.

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

If you get a "command not found" error, make sure that `~/.local/bin` is in your `PATH`. You can add it to your `~/.bashrc` with:
```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

**Cache issues:**
```bash
uv cache clean
```

---

## ✅ Verification

```bash
uv --version && uvx --version && uvx cowsay -t "Ready!"
```

---

[← Back to Main Guide](../../README.md)
