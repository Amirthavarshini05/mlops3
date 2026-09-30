# 5b - Jenkins 5-stage Python CI Pipeline

Stages:
Checkout -> Install Deps -> Run Unit Tests -> Static Analysis -> Deploy to Staging

Windows Jenkins uses bat commands.

For GitHub webhook:
Settings -> Webhooks -> Add webhook
Payload URL: https://YOUR-JENKINS/github-webhook/
Content-Type: application/json
Event: push

Jenkins Build Trigger:
GitHub hook trigger for GITScm polling
