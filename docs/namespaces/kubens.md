# 🛠️ kubens: Fast Namespace Switcher

`kubens` allows engineers to switch default target namespaces instantly without modifying context definitions by hand.

---

## Installation & Usage

```bash
# Installation (macOS Homebrew)
brew install kubectx

# List all namespaces in current cluster
kubens

# Switch active namespace to 'monitoring'
kubens monitoring

# Switch back to previous namespace
kubens -
```

### Safety Rating: 🟢 Safe
