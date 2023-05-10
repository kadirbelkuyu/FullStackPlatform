# DevOps Workflow - A Flask & React Application

## Overview

This project demonstrates a full DevOps workflow for a simple web application. The application consists of a Flask backend, a React frontend, and a PostgreSQL database. The application is containerized using Docker, and is deployed and orchestrated using Kubernetes. The infrastructure is managed using Terraform and Ansible. CI/CD is implemented using Jenkins. Application security and static code analysis are done using SonarQube and OWASP ZAP. Monitoring is achieved with Prometheus and Grafana.

## Prerequisites

- Docker
- Kubernetes (k8s)
- AWS CLI
- Jenkins
- SonarQube
- OWASP ZAP
- Ansible
- Terraform
- Kubespray
- Prometheus
- Grafana

## Local Setup

1. Clone the repository:

```bash
git clone https://github.com/kadirbelkuyu/FullStackPlatform
cd FullStackPlatform
````
## Run the Flask backend:

```bash
cd backend
docker build -t flask-backend:latest .
docker run -p 5000:5000 flask-backend:latest
````
## Run the React frontend:
```bash
cd frontend
docker build -t react-frontend:latest .
docker run -p 3000:3000 react-frontend:latest
````
## Run the PostgreSQL database:
```bash 
cd db
docker build -t postgres-db:latest .
docker run -p 5432:5432 postgres-db:latest
````
# Infrastructure Setup

### Set up the infrastructure with Terraform and Ansible:

```bash 
cd terraform
terraform init
terraform apply
cd ..
cd ansible
ansible-playbook -i hosts site.yml
````
### Set up the Kubernetes cluster with Kubespray:
```bash 
cd k8s
ansible-playbook -i inventory/mycluster/hosts.yaml --become --become-user=root cluster.yml
```

### Deploy the application on the Kubernetes cluster:

```bash 
kubectl apply -f backend-deployment.yaml
kubectl apply -f frontend-deployment.yaml
kubectl apply -f db-deployment.yaml
````
### Set up monitoring with Prometheus and Grafana:

```bash 
kubectl apply -f prometheus-config.yaml
kubectl apply -f grafana-dashboards/dashboard.json
````

### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

### License

MIT