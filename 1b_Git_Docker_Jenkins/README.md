# 1b - Git + Docker + Jenkins

Create a Jenkins Pipeline job pointing to this project. Jenkins checks out the Git repository,
builds the Docker image and runs the container.

Prerequisites:
- Git
- Docker Desktop
- Jenkins
- Jenkins Docker permissions

Build locally:
docker build -t git-docker-jenkins-app .
docker run -d --name git-docker-jenkins-app -p 8081:80 git-docker-jenkins-app
Open http://localhost:8081
