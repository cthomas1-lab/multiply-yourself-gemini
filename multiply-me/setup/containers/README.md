[← Back to Main Guide](../../README.md)

---

# 🐳 Container Runtime Setup (Fedora)

You need a container runtime to run Docker containers. This guide provides the steps to install Docker on Fedora.

---

## Installation

These commands will install Docker Engine on your Fedora system.

```bash
# Update your system
sudo dnf update -y

# Remove old Docker versions (if any)
sudo dnf remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-selinux \
                  docker-engine-selinux \
                  docker-engine -y

# Install the dnf-plugins-core package
sudo dnf -y install dnf-plugins-core

# Add the Docker repository
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo

# Install Docker Engine
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

# Start and enable the Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Add your user to the docker group (to run docker commands without sudo)
sudo usermod -aG docker $USER
```

After running these commands, you will need to **log out and log back in** for the group change to take effect.

---

## ✅ Verification

Run these commands to confirm your container runtime is working:

```bash
docker --version
docker run hello-world
```

You should see a "Hello from Docker!" message.

---

[← Back to Main Guide](../../README.md)