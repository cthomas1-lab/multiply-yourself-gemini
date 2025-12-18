[← Back to Main Guide](../../README.md)

---

# 🪟 Windows Setup with WSL

**WSL (Windows Subsystem for Linux) is highly recommended for Windows users.** While optional, most development environments, tools, and this guide assume a Linux-based environment. WSL provides a much smoother experience than native Windows.

---

## 💡 Recommended: Run Windsurf in WSL Mode

**For the best experience, connect Windsurf to WSL.** If you're seeing PowerShell in your terminal, you're in the native Windows environment.

### How to Verify You're in WSL

Look at the **bottom-left corner** of Windsurf:
- ✅ **Correct:** Shows "WSL: Ubuntu" or similar
- ❌ **Wrong:** Shows nothing or "Windows"

If you're not connected to WSL, **we recommend setting this up first** before continuing with other setup guides.

---

## Why WSL?

- Native bash terminal with Linux commands
- Run `apt install` like a real Linux system
- Compatible with all the tools in this guide and most that you will encounter

---

## Install WSL

### Step 1: Enable WSL

Open **PowerShell as Administrator** and run:

```powershell
wsl --install
```

This installs WSL 2 with Ubuntu by default. Restart your computer when prompted.

### Step 2: Set Up Ubuntu

After restart, Ubuntu will launch and ask you to create a username and password. This is your Linux user account.

### Step 3: Connect Windsurf to WSL

1. Open Windsurf
2. Look for **"Connect to WSL"** in the bottom-left corner (or press `F1` and search "WSL")
3. Click **"Connect to WSL"** to switch your environment
4. **Verify:** The bottom-left should now show "WSL: Ubuntu"

> 💡 If Ubuntu doesn't load automatically, you may need to install it from the Microsoft Store.

### Step 4: Verify Your Terminal is Linux

Open a terminal in Windsurf and run:

```bash
uname -a
```

You should see output containing "Linux" and "Ubuntu". If you see "MINGW" or "Windows", you're still in the wrong environment - go back to Step 3.

---

## ⚠️ VPN + WSL Issue (If Applicable)

> 💡 **Note:** This section only applies if you use a VPN. If you don't use a VPN, skip to [Verify WSL is Working](#verify-wsl-is-working).

**Problem:** Some VPN clients can sever WSL's internet connection when connected.

### Fix Option 1: PowerShell Command

Run in **PowerShell as Administrator**:

```powershell
Get-NetIPInterface -InterfaceAlias "Your interface name" | Set-NetIPInterface -InterfaceMetric 4000
```

Replace `"Your interface name"` with your actual network interface (e.g., "Ethernet" or "Wi-Fi").

> 💡 **Tip:** Ask your AI agent to help automate this when VPN connects.

### Fix Option 2: Use a Hardware VPN Solution

If you have a hardware VPN solution, use that instead of software VPN. This avoids the WSL networking issue entirely.

---

## Verify WSL is Working

```bash
# Check you're in Linux
uname -a

# Should show something like: Linux ... Ubuntu ...
```

---

## Set Up Your Workspace

This is critical for staying organized. Each workspace should represent a single context (a project, a troubleshooting session, a task).

### Step 1: Create a Workspaces Folder

```bash
mkdir -p ~/workspaces
```

### Step 2: Attach a Folder in Windsurf

1. In Windsurf (connected to WSL), go to **File > Open Folder**
2. Navigate to your project folder (e.g., `~/workspaces/my-project`)
3. This gives Windsurf access to that folder in your WSL environment

### Step 3: Save as a Workspace

1. Go to **File > Save Workspace As...**
2. Save it as `my-project.code-workspace` in your `~/workspaces` folder
3. Now you can reopen this exact state anytime

### Why This Matters

| Benefit | Description |
|---------|-------------|
| **Context isolation** | Each workspace has its own rules, workflows, and settings |
| **Quick switching** | File > Open Workspace from File to jump between contexts |
| **Mental clarity** | Close the workspace, close the mental context - move on to something else |

### Example Workspaces

```
~/workspaces/
├── vibelympics.code-workspace            # Main project work
├── supercharged.code-workspace           # This repository
├── home-server-management.code-workspace
└── personal-journal.code-workspace       # Daily journaling
```

> 💡 **Pro tip:** When you open a workspace, you're back exactly where you left off - open files, terminal state, everything. This lets you context-switch like a pro.

---

## Next Steps

Once WSL is set up, continue with:

1. [Container Runtime](../containers/README.md) - Docker in WSL
2. [Node.js & npx](../nodejs/README.md)
3. [Python](../python/README.md)
4. [Python uv & uvx](../python-uv/README.md)

All subsequent setup guides should be run **inside WSL**, not in Windows PowerShell.

---

## Troubleshooting

### WSL won't start
```powershell
# In PowerShell as Admin
wsl --update
wsl --shutdown
wsl
```

### No internet in WSL
Check if VPN is connected - see the [VPN fix above](#%EF%B8%8F-vpn--wsl-issue).

### Ubuntu not installed
```powershell
wsl --install -d Ubuntu
```

---

[← Back to Main Guide](../../README.md)
