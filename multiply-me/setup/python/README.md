[← Back to Main Guide](../../README.md)

---

# 🐍 Python Setup

Python is essential for writing scripts, running MCP servers, and general development.

---

## Installation

### macOS

```bash
# Install Python 3 via Homebrew
brew install python

# Verify installation
python3 --version
pip3 --version
```

### Windows (WSL/Ubuntu)

> ⚠️ **Verify you're in WSL first!** Check the bottom-left of Windsurf shows "WSL: Ubuntu"

```bash
# Python 3 is usually pre-installed in Ubuntu, but ensure it's up to date
sudo apt update
sudo apt install -y python3 python3-pip python3-venv

# Verify installation
python3 --version
pip3 --version
```

### Option: pyenv (Multiple Python Versions)

If you need to manage multiple Python versions (works on both macOS and WSL):

**macOS:**
```bash
brew install pyenv
```

**WSL/Ubuntu:**
```bash
# Install dependencies first
sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
  libreadline-dev libsqlite3-dev curl libncursesw5-dev xz-utils tk-dev \
  libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

# Install pyenv
curl https://pyenv.run | bash
```

**Then for both platforms:**
```bash
# Add to your shell config (~/.zshrc or ~/.bashrc)
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# Restart terminal or source config
source ~/.bashrc

# Install a Python version
pyenv install 3.12.0

# Set as global default
pyenv global 3.12.0

# Verify
python --version
```

---

## Verify Installation

```bash
python3 --version
pip3 --version
```

You should see version numbers like `Python 3.12.x` and `pip 24.x`.

---

## Create Aliases (Optional)

Add to your `~/.zshrc` for convenience:

```bash
echo 'alias python=python3' >> ~/.zshrc
echo 'alias pip=pip3' >> ~/.zshrc
source ~/.zshrc
```

Now you can use `python` and `pip` directly.

---

## Virtual Environments

For project isolation, use virtual environments:

```bash
# Create a virtual environment
python3 -m venv myproject-env

# Activate it
source myproject-env/bin/activate

# Install packages (isolated to this env)
pip install requests

# Deactivate when done
deactivate
```

---

## Why This Matters for Windsurf

Some MCP servers run as native Python scripts rather than through `uvx`. You'll also likely write Python scripts during development.

**Examples:**
```bash
# Running a Python MCP server directly
python mcp_server.py

# Writing and running scripts
python my_script.py
```

---

## Common Packages

Install commonly used packages:

```bash
pip3 install requests httpx pydantic
```

---

## Troubleshooting

**`python3` command not found:**
```bash
brew reinstall python
# Restart your terminal
```

**`pip3` command not found:**
```bash
python3 -m ensurepip --upgrade
```

**Permission errors with pip:**
```bash
# Use --user flag
pip3 install --user package-name

# Or use a virtual environment (recommended)
```

---

## ✅ Verification

```bash
python3 --version && pip3 --version && python3 -c "print('Python is ready!')"
```

---

[← Back to Main Guide](../../README.md)
