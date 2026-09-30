# 6a - Jenkins Docker CI Pipeline

Three required stages:
1. Checkout
2. Build Image
3. Deploy & Verify

The image is tagged:
jenkins-app:build-${BUILD_NUMBER}

Container name:
jenkins-app

Port:
8081:80

The Dockerfile has a HEALTHCHECK and the pipeline validates with curl.
