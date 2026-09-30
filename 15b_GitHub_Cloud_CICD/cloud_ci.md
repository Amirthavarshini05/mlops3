# Cloud CI/CD Demo

Example workflow:

Developer
  -> GitHub
  -> GitHub Actions
  -> Build/Test
  -> Docker Build
  -> Cloud Registry
  -> Cloud Deployment

Example GitHub Actions skeleton:

```yaml
name: Cloud CI/CD

on:
  push:
    branches: [main]

jobs:
  build-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: python --version
```

For a real cloud deployment, configure credentials using GitHub Secrets.
