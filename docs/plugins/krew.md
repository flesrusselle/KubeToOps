# 🛠️ Krew: kubectl Plugin Package Manager

Krew is the official plugin manager for `kubectl` maintained by SIG CLI.

---

## 1. Installation

```bash
# macOS (Homebrew)
brew install krew

# Add krew binaries to PATH (~/.zshrc or ~/.bashrc)
export PATH="${KREW_ROOT:-$HOME/.krew}/bin:$PATH"
```

---

## 2. Verification & Commands

```bash
# Verify installation
kubectl krew version

# Update plugin index
kubectl krew update

# Search available plugins
kubectl krew search

# Install a plugin
kubectl krew install neat

# Upgrade installed plugins
kubectl krew upgrade
```

### Safety Rating: 🟢 Safe
