# 7a - Secure Jenkins Docker Hub Publishing

Create Jenkins Global Credentials:
Kind: Username with password
ID: dockerhub-credentials

Use a Docker Hub access token as the password where possible.

Replace YOUR_USERNAME in Jenkinsfile.

The pipeline builds, securely logs in with withCredentials, tags and pushes.
