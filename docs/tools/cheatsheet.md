# 📄 External Tools Quick Cheatsheet

```bash
# Launch K9s in specific context and namespace
k9s --context prod -n default

# Tail logs across multiple pods matching pattern
stern "app-backend-.*" -n production

# Run Popeye cluster sanitizer
popeye

# Switch context via kubectx
kubectx staging

# Switch namespace via kubens
kubens monitoring
```
