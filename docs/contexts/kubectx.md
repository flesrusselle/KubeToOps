# 🛠️ kubectx: Fast Context Switcher

`kubectx` is an essential utility for developers and SREs operating across multiple Kubernetes clusters.

---

## 1. What is it & Why Use It?

Instead of typing verbose commands like `kubectl config use-context gke_project_us-central1_prod-cluster`, `kubectx` allows you to list and switch cluster contexts with short names or fuzzy interactive selection.

---

## 2. Installation & Verification

```bash
# macOS (Homebrew)
brew install kubectx

# Verify installation
kubectx --help
```

---

## 3. Practical Usage Examples

```bash
# List all configured contexts
kubectx

# Switch context directly
kubectx dev-cluster

# Switch back to previous context
kubectx -

# Rename verbose context name to a friendly alias
kubectx prod=gke_my-company-prod_us-east1-a_production-cluster-v2
```

### Safety Rating: 🟢 Safe
