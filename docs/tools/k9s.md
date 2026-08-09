# 🖥️ K9s: Kubernetes CLI Terminal UI

K9s is a terminal-based UI that accelerates cluster navigation, log tailing, container shell access, and resource management.

---

## 1. Installation & Verification

```bash
# macOS (Homebrew)
brew install derailed/k9s/k9s

# Verify installation
k9s version
```

---

## 2. Essential Navigation Shortcuts

| Key / Command | Action |
| :--- | :--- |
| `:pods` | Switch view to Pods |
| `:deploy` | Switch view to Deployments |
| `:svc` | Switch view to Services |
| `:ns` | Switch target Namespace |
| `:ctx` | Switch active Context |
| `l` | Tail logs for highlighted pod |
| `s` | Open shell inside highlighted container |
| `d` | Describe highlighted resource |
| `e` | Edit manifest in default `$EDITOR` |
| `Ctrl-A` | Filter resources across all namespaces |
| `/` | Filter/search resources in current view |
| `Ctrl-C` | Exit K9s UI |

---

## 3. Practical Workflow

1. Launch K9s: `k9s --context dev-cluster`
2. Type `:pods` to view all pods in default namespace.
3. Highlight target pod using arrow keys or `j`/`k`.
4. Press `l` to stream container logs in real time.
5. Press `Esc` to return to pod view, then press `s` to enter container shell.

### Safety Rating: 🟢 Safe (Read-only views) | 🟡 Caution (Editing/Shell) | 🔴 Destructive (Deleting resources)
