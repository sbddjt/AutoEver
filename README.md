# ☁️ Hyundai Autoever Mobility SW School | Cloud Track

> **현대오토에버 모빌리티 SW 스쿨 3기 클라우드 트랙 (Cloud Engineering)** > 모빌리티 서비스에 최적화된 **Cloud Native Architecture** 설계 및 운영 역량을 쌓는 학습 저장소입니다.  
> CS 전공 지식을 바탕으로 **안정적이고 확장 가능한(Scalable) 인프라** 구축을 지향합니다.

<br>

## 👨‍💻 Author Info
* **Name**: 조성윤 (Jo Seong-yun)
* **Affiliation**: Hyundai Autoever Mobility SW School 3rd
* **Duration**: 2025.12.18 ~ 2026.06.28
* **Focus**: Cloud Architecture, Backend Engineering, DevOps, MSA
* **Goal**: 모빌리티 데이터 파이프라인 구축 및 고가용성 클라우드 인프라 운영

---

## 🛠️ Tech Stack & Tools
본 과정에서 다루는 기술 스택과 제가 주력으로 학습하고 있는 도구들입니다.

| Category | Technology Stack |
| :--- | :--- |
| **Languages** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=c%2B%2B&logoColor=white) ![Shell](https://img.shields.io/badge/Shell_Script-121011?style=flat-square&logo=gnu-bash&logoColor=white) |
| **Backend & DB** | ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white) ![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=flat-square&logo=mariadb&logoColor=white) ![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=flat-square&logo=mongodb&logoColor=white) ![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white) |
| **Infra & OS** | ![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black) ![AWS](https://img.shields.io/badge/AWS-%23232F3E.svg?style=flat-square&logo=amazon-aws&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-%232496ED.svg?style=flat-square&logo=docker&logoColor=white) ![K8s](https://img.shields.io/badge/Kubernetes-%23326CE5.svg?style=flat-square&logo=kubernetes&logoColor=white) |
| **DevOps & IaC** | ![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat-square&logo=jenkins&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white) ![Terraform](https://img.shields.io/badge/Terraform-%23623CE4.svg?style=flat-square&logo=terraform&logoColor=white) |
| **Monitoring** | ![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white) ![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white) |

---

## 🗺️ Curriculum Roadmap

현대오토에버 클라우드 트랙의 학습 로드맵에 따라 **단계별 심화 학습**을 진행하고 있습니다.

### [Phase 1: Foundation & Application]
> **"튼튼한 기초 위에 서비스를 올립니다."**
- **Linux & Network**: 리눅스 커널 이해, 쉘 스크립팅, 네트워크 프로토콜(TCP/IP, HTTP) 심화
- **Python & Backend**: Python 고급 문법, 웹 프레임워크(FastAPI/Django)를 활용한 RESTful API 개발
- **Database**: RDBMS(MariaDB) 설계 및 SQL 튜닝, NoSQL 활용

### [Phase 2: Cloud Native & Container]
> **"서비스를 컨테이너화하고 유연하게 관리합니다."**
- **Docker**: 컨테이너 이미지 최적화, Docker Compose를 이용한 멀티 컨테이너 관리
- **Kubernetes (K8s)**: Pod 라이프사이클 관리, Deployment/Service/Ingress 리소스 활용, Helm 패키징
- **Microservices**: Monolithic 아키텍처를 MSA로 전환하는 전략 및 실습

### [Phase 3: Public Cloud & DevOps]
> **"자동화된 인프라 위에서 서비스를 운영합니다."**
- **AWS Cloud**: VPC 네트워크 설계, EC2/RDS/S3 등 코어 서비스 아키텍처 구축
- **IaC (Infrastructure as Code)**: Terraform을 활용한 인프라 프로비저닝 자동화
- **CI/CD Pipeline**: Jenkins 및 GitHub Actions를 활용한 빌드/배포 자동화 파이프라인 구축

---

## 📂 Repository Structure

이 저장소는 학습 주제별로 모듈화되어 관리됩니다.

```bash
.
├── 01_Language/            # Python, C++ Core & Algorithm
├── 02_Linux_Network/       # Linux System Programming & Network Log
├── 03_Database/            # MariaDB SQL, Data Modeling (ERD)
├── 04_Backend_Web/         # FastAPI/Django Projects & API Docs
├── 05_Docker_K8s/          # Dockerfile, K8s Manifests (YAML)
├── 06_AWS_Cloud/           # AWS Architecture Diagrams & Setup
├── 07_DevOps_IaC/          # Terraform Code, CI/CD Scripts
└── Projects/               # Mobility Domain Team Projects
    ├── Mini_Project/       # Web Service Project
    └── Final_Project/      # MSA Cloud Architecture Project
