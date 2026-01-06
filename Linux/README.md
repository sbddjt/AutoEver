# 🐧 Linux & Ubuntu System Administration

> **Hyundai AutoEver Mobility SW Academy - Cloud Track** > 클라우드 인프라 구축의 핵심인 Linux(Ubuntu) 운영체제의 구조를 이해하고, 시스템 관리, 네트워크 설정 및 쉘 스크립팅 능력을 배양하는 공간입니다.

<div align="center">
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"/>
  <img src="https://img.shields.io/badge/OpenSSH-000000?style=for-the-badge&logo=openssh&logoColor=white"/>
  <img src="https://img.shields.io/badge/VirtualBox-183A61?style=for-the-badge&logo=virtualbox&logoColor=white"/>
  <img src="https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white"/>
</div>

---

## 📖 Overview

클라우드 엔지니어로서 필수적으로 갖춰야 할 **Server OS Operation** 능력을 함양합니다.
Linux 커널과 쉘의 동작 원리부터 파일 시스템 관리, 사용자 권한 제어, 그리고 **SSH 원격 제어**까지 실무 중심의 환경 구성을 목표로 합니다.
이후 학습할 **Docker, Kubernetes** 컨테이너 환경을 능숙하게 다루기 위한 기초 체력을 다지는 과정입니다.

## 🛠️ Environment

* **Host OS**: Windows 10/11 (VirtualBox Host)
* **Guest OS**: Ubuntu 22.04 LTS (Server & Desktop)
* **Virtualization**: Oracle VM VirtualBox
* **Terminal**: Git Bash / PowerShell / Built-in Terminal
* **Remote Access**: OpenSSH

---

## 📅 Curriculum & Progress

현대오토에버 클라우드 트랙 커리큘럼 및 학습한 내용을 기반으로 정리된 로드맵입니다.

### 1️⃣ Linux Introduction & Installation

* [x] **Linux 개요**: UNIX의 역사, 커널(Kernel)과 쉘(Shell)의 역할, 배포판 계열(Debian vs RedHat)
* [x] **가상화(Virtualization)**: VM(Hypervisor) vs Container(Docker) 개념 비교
* [x] **환경 구축**: VirtualBox 설치, Ubuntu Server/Desktop 이미지(ISO) 설치 및 초기 설정

### 2️⃣ System Management & Commands

* [ ] **기본 명령어**: 디렉토리 이동(`cd`), 목록 확인(`ls -al`), 파일 조작(`cp`, `mv`, `rm`)
* [ ] **디렉토리 구조**: `/bin`, `/etc`, `/home`, `/var`, `/tmp` 등 주요 디렉토리 역할
* [ ] **프로세스 관리**: `ps`, `kill`, `top`/`htop`을 이용한 리소스 모니터링
* [ ] **시스템 제어**: `shutdown`, `reboot`, 런레벨(Runlevel) 및 `systemd` 타겟 이해

### 3️⃣ User & Permission Management

* [ ] **사용자 관리**: `useradd`, `passwd`, `/etc/passwd` 파일 구조
* [ ] **권한(Permission)**: `chmod`(8진수/심볼릭), `chown`, `chgrp`
* [ ] **특수 권한**: `sudo` 설정 및 `/etc/sudoers` 관리

### 4️⃣ Network & Remote Access

* [ ] **네트워크 기초**: IP(Public/Private), Port, NAT/Bridge 모드 이해
* [ ] **OpenSSH**: `ssh` 클라이언트 접속, `sshd` 서버 설정, 포트 포워딩
* [ ] **방화벽 설정**: `ufw` 활성화 및 포트(Allow/Deny) 정책 관리

---

## 📝 Key Concepts Summary

### 🔍 VM vs Container

클라우드 인프라의 핵심인 가상화 기술의 차이를 이해합니다.

| 분류 | Virtual Machine (VM) | Container |
| --- | --- | --- |
| **기반 기술** | Hypervisor (하드웨어 가상화) | Container Engine (OS 가상화) |
| **격리 수준** | 완벽한 격리 (Guest OS 포함) | 프로세스 격리 (Host OS 커널 공유) |
| **특징** | 무겁지만 호환성이 높음 | 가볍고 배포가 빠름 (Docker) |

### 🚦 Run Levels (Systemd Targets)

시스템 부팅 시 운영 모드를 결정하는 단계입니다.

| Level | Target | 설명 |
| --- | --- | --- |
| **0** | `poweroff.target` | 시스템 종료 |
| **3** | `multi-user.target` | **CLI 모드** (서버 운영 표준, 네트워크 지원) |
| **5** | `graphical.target` | **GUI 모드** (데스크탑 환경) |
| **6** | `reboot.target` | 시스템 재부팅 |

### 💡 Core Keyword Notes

* **Shell**: 사용자의 명령어를 해석하여 커널에 전달하는 인터페이스 (Bash, Zsh 등).
* **Prompt**: 쉘이 사용자의 입력을 대기하는 표시줄 (예: `user@host:~$`).
* **SSH (Secure Shell)**: 네트워크 상의 다른 컴퓨터에 로그인하거나 원격 시스템에서 명령을 실행하고 파일을 복사할 수 있도록 해주는 프로토콜.
* **NAT (Network Address Translation)**: 사설 IP를 공인 IP로 변환하거나, 포트 포워딩을 통해 외부 접속을 가능하게 하는 기술.

---

## 📂 Directory Structure

```bash
linux/
├── 01_intro/           # 리눅스 개요 및 설치 로그
├── 02_commands/        # 파일/디렉토리 조작 명령어 실습
├── 03_system/          # 프로세스, 런레벨, 시스템 종료/재부팅
├── 04_permissions/     # chmod, chown 등 권한 관리 실습
├── 05_network/         # SSH 설정, IP 확인, 포트 포워딩
└── shell_scripts/      # 업무 자동화를 위한 기초 쉘 스크립트 모음

```

---
