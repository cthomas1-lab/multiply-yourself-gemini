[← Back to Main Guide](../../README.md)

---

# 🐳 Container Runtime Setup

You need a container runtime to run Docker containers.

---

## Choose Your Platform

| Platform | Recommended Option | Alternative |
|----------|-------------------|-------------|
| **macOS** | [Docker Desktop](#macos-docker-desktop-recommended) | [Colima + Docker CLI](#macos-colima--docker-cli-alternative) |
| **Windows (WSL)** | [Docker in WSL](#windows-docker-in-wsl) | - |

> 💡 **Note:** Docker Desktop is free for individuals and small businesses (under 250 employees and $10M revenue). For larger organizations, alternatives like Colima are fully free.

---

## Prerequisites

### macOS: Install Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

After installation, follow the on-screen instructions to add Homebrew to your PATH.

### Windows (WSL): Verify You're in WSL

> ⚠️ **Before continuing:** If using WSL, check the bottom-left of Windsurf shows "WSL: Ubuntu". If not, click "Connect to WSL" first!

---

# macOS Options

## macOS: Docker Desktop (Recommended)

Docker Desktop is the easiest way to get started on macOS. It's free for individual use.

### Installation

1. Download Docker Desktop from [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/)
2. Open the `.dmg` file and drag Docker to Applications
3. Launch Docker from Applications
4. Wait for Docker to start (you'll see the whale icon in your menu bar)

### Verify Installation

```bash
docker --version
docker run hello-world
```

You should see a "Hello from Docker!" message.

### Daily Usage

Docker Desktop starts automatically on login by default. You can change this in Docker Desktop preferences.

---

## macOS: Colima + Docker CLI (Alternative)

Colima provides a lightweight VM to run containers on macOS without a desktop application. Great for those who prefer CLI-only workflows.

### Installation

```bash
# Install Homebrew if you haven't already
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Docker CLI and Colima
brew install docker docker-compose colima
```

### Start Colima

```bash
# Start the Colima VM
colima start

# Verify Docker works
docker run hello-world
```

You should see a "Hello from Docker!" message.

### Daily Usage

```bash
# Start Colima (run after reboots or when needed)
colima start

# Stop Colima when done
colima stop

# Check status
colima status
```

### Optional: Auto-start Colima

```bash
brew services start colima
```

### Troubleshooting

**Colima won't start:**
```bash
colima delete
colima start
```

**Docker socket not found:**
```bash
# Ensure Colima is running
colima status

# If not running, start it
colima start
```

---

# Windows Options

## Windows: Docker in WSL

> ⚠️ **Prerequisite:** Complete the [Windows/WSL Setup](../windows-wsl/README.md) first.

I recommend installing Docker directly in WSL rather than using Docker Desktop on Windows. This approach:
- Runs Docker natively in Linux (no Windows↔WSL bridging complexity)
- Keeps your Windows environment clean (no desktop app needed)
- Works seamlessly with AI agents managing your container environment via CLI

### Installation

Run these commands **inside WSL** (not PowerShell):

```bash
# Update package list and install prerequisites
sudo apt update
sudo apt install -y ca-certificates curl

# Add Docker's official GPG key
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add Docker repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Add yourself to the docker group (avoids needing sudo)
sudo usermod -aG docker $USER

# Start Docker service
sudo service docker start
```

**Log out and back into WSL** for the group change to take effect.

### Verify Installation

```bash
docker --version
docker run hello-world
```

### Auto-start Docker in WSL

Add this to your `~/.bashrc` or `~/.zshrc`:

```bash
# Start Docker if not running
if ! pgrep -x "dockerd" > /dev/null; then
    sudo service docker start
fi
```

### Troubleshooting

**Permission denied:**
```bash
# Make sure you're in the docker group
groups

# If docker isn't listed, re-add and restart WSL
sudo usermod -aG docker $USER
# Then close and reopen WSL
```

**Docker daemon not running:**
```bash
sudo service docker start
```

---

## ✅ Verification

Run this from a WLS terminal to confirm your container runtime is working:

```bash
docker --version
docker run hello-world
```

---

[← Back to Main Guide](../../README.md)
