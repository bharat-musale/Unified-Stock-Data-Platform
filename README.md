# 🚀 Unified Stock Data Platform

## 📌 Overview
Unified Stock Data Platform is a production-ready, multi-service system designed to aggregate, process, and serve stock market data efficiently. The project follows modern DevOps practices including containerization, reverse proxy architecture, and CI/CD automation.

---

## 🏗️ Architecture

```
Client → Nginx → Frontend (Next.js)
                ↓
         Backend (Node.js API)
                ↓
         FastAPI (Python Service)
                ↓
              MySQL
                ↓
         Docker Compose (Orchestration)
                ↓
             AWS EC2 (Deployment)
```

---

## 📁 Repository Structure

```
backend/        # Node.js API
frontend/       # Next.js frontend
python/         # FastAPI service
mysql/          # Database configs/init
nginx/          # Reverse proxy config

docker-compose.yml
.github/workflows/   # CI pipeline
README.md
```

---

## ⚙️ Tech Stack

### Backend
- Node.js (Express)
- FastAPI (Python)

### Frontend
- Next.js

### Database
- MySQL

### DevOps
- Docker & Docker Compose
- Nginx (Reverse Proxy)
- GitHub Actions (CI)
- AWS EC2

---

## 🚀 Key Features

- Multi-service microservice-like architecture
- Containerized deployment using Docker
- Reverse proxy routing using Nginx
- Healthcheck-based service dependency handling
- CI pipeline with GitHub Actions
- Environment-based configuration

---

## 🐳 Run Locally

```bash
docker compose up --build
```

Application will be available at:
```
http://localhost
```

---

## 🔐 Environment Configuration

Create a `.env` file in each service:

### Backend (.env)
```
DB_HOST=mysql
DB_USER=vap_user
DB_PASSWORD=vap_pass
```

### Python (.env)
```
DB_HOST=mysql
```

⚠️ Never commit `.env` files to GitHub.

---

## ☁️ Deployment (AWS EC2)

- Instance Type: t2.micro / t3.small
- Dockerized services
- Nginx exposed on port 80

### Deployment Steps

```bash
git clone https://github.com/bharat-musale/Unified-Stock-Data-Platform.git
cd Unified-Stock-Data-Platform
docker compose up -d --build
```

---

## 🔄 CI Pipeline (GitHub Actions)

Triggered on push to `main`:

- Checkout repository
- Build Docker services
- Validate container setup

File:
```
.github/workflows/docker-ci.yml
```

---

## 🧠 DevOps Highlights

- Multi-container orchestration using Docker Compose
- Reverse proxy architecture with Nginx
- CI integration using GitHub Actions
- Service dependency handling via healthchecks
- Clean environment separation

---

## 📈 Future Enhancements

- CI/CD with auto-deploy to EC2
- HTTPS with Nginx + SSL
- Monitoring (Prometheus + Grafana)
- Redis caching layer
- Kubernetes migration

---

## 📫 Contact

- GitHub: https://github.com/bharat-musale

---

## ⭐ Note

This project demonstrates real-world DevOps practices including containerization, CI integration, and scalable architecture design, aimed at production-level deployment scenarios.
