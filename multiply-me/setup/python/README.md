[← Back to Main Guide](../../README.md)

---

# 🐍 Python Setup (Fedora)

Python is essential for writing scripts and general development with Gemini.

---

## Installation

Python 3 is usually pre-installed on Fedora. These commands will ensure it's up to date and that `pip` (the Python package installer) is also installed.

```bash
# Update your system
sudo dnf update -y

# Install Python 3 and pip
sudo dnf install python3 python3-pip -y
```

---

## Verify Installation

```bash
python3 --version
pip3 --version
```

You should see version numbers for both Python and pip.

---

## Create Aliases (Optional but Recommended)

Add these to your `~/.bashrc` file for convenience, so you can use `python` and `pip` directly instead of `python3` and `pip3`.

```bash
echo 'alias python=python3' >> ~/.bashrc
echo 'alias pip=pip3' >> ~/.bashrc
source ~/.bashrc
```

---

## Virtual Environments

For project isolation, it's a best practice to use virtual environments.

```bash
# Create a virtual environment
python -m venv myproject-env

# Activate it
source myproject-env/bin/activate

# Install packages (they will be isolated to this environment)
pip install requests

# Deactivate when you're done
deactivate
```

---

## Why This Matters for Gemini

You'll often use Python to write scripts that interact with the Gemini API or to build tools that extend its functionality.

---

## Common Packages

Install some commonly used packages for interacting with APIs and handling data.

```bash
pip install requests httpx pydantic
```

---

## Troubleshooting

**`python3` or `pip3` command not found:**

If you get a "command not found" error, run the installation command again:
```bash
sudo dnf install python3 python3-pip -y
```

**Permission errors with pip:**

If you get permission errors when using `pip`, it's a strong sign you should be using a virtual environment (see above). Avoid using `sudo pip install` as it can lead to system conflicts.

---

## ✅ Verification

```bash
python --version && pip --version && python -c "print('Python is ready!')"
```

---

[← Back to Main Guide](../../README.md)
