# DevOps Flask CI/CD Project 1.0

A simple containerized Flask web application built as a DevOps learning project.
Code in Github. Github Actions deploy.

## Current Features

- Python Flask web app
- Dockerized application
- Docker Compose local deployment
- Health check endpoint

## Local Run

```bash
docker compose up --build
```

## Steps followed

Part 1: Local Flask app
Part 2: Docker + GitHub repo
Part 3: AWS EC2 manual deployment
Part 4: Nginx reverse proxy
Part 5: GitHub Actions CI/CDs

## Architecture
Developer (Mac mini)
        |
        | git push
        v

GitHub Repository
        |
        | GitHub Actions CI/CD
        v

AWS EC2 Ubuntu Server
 ├── Docker Engine
 ├── Docker Compose
 │
 ├── Nginx Container
 │     └── Public entry point :80
 │
 └── Flask App Container
       └── Internal application service :5000

## Learning Points
1. Docker Fundamentals
Dockerfile
image builds
containers
networking
Compose orchestration

2. Containerized Architecture
multiple services in containers
separation of layers
internal vs external traffic
service discovery

3. Reverse Proxy Concepts
what Nginx does
why reverse proxies exist
traffic routing
internal backend protection

4. Linux Server Operations
Ubuntu
SSH
package installation
permissions
services
logs

5. AWS EC2
instance provisioning
security groups
networking
public access
user-data bootstrap

6. Infrastructure Automation
Using EC2 User Data:
reduced manual setup
automated provisioning
introduced bootstrap concepts

7. CI/CD
deployment automation
GitHub Actions
pipelines
secrets management
automated SSH deployment

## Future Improvements

1. Terraform
Use to deploy AWS resources
CICD for maintaining provisioned resources

2. Do not enable Port 22 to 0.0.0.0/0
Currently require to do so for Github Actions to reach to EC2 instance
Possible options
- Use self-hosted GitHub runner locally in Mac Mini
- Use AWS SSM Session Manager
- Don't SSH deploy, instead build image and pull from registry

3. AWS Native
- CodeCommit instead of GitHub
- CodePipeline/Build/Deploy instead of GitHub Actions
- SSM Parameter Store instead of Github secrets