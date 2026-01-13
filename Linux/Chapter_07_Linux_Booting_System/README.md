# 🐧 리눅스 부팅 & 시스템 관리 (Linux Booting System)

## 1. 🚀 리눅스 부팅 (Booting)

### 1-1. 개요

- **정의:** PC 전원을 켜는 순간부터 리눅스가 완전히 동작하여 로그인 프롬프트가 출력될 때까지의 과정.
- **중요성:** 부팅 시 필요한 서비스를 결정하고, 부팅 문제 발생 시 트러블 슈팅을 위해 반드시 이해해야 함.

### 1-2. 부팅 과정 (Sequence)

> 전원 ON → BIOS 단계 → Boot Loader → Kernel Initialize → Systemd service → Login Prompt
> 
1. **⚡ BIOS (Basic Input Output System) 단계**
    - **ROM BIOS:** 하드웨어(키보드, 디스크 등) 상태 점검 (POST).
    - **MBR 로딩:** 부팅 디스크의 첫 번째 섹터(512 Byte, Master Boot Record)를 읽어 부트 로더의 위치를 파악하고 메모리에 로딩.

1. **🚛 부트 로더 (Boot Loader)**
    - 운영체제 선택 메뉴 제공 (멀티 부팅 등).
    - **GRUB:** 우분투 등 리눅스의 표준 부트 로더.
    - **커널 로딩:** `/boot/vmlinuz-버전` 커널 이미지를 메모리에 로드.

1. **🧠 커널 초기화 (Kernel Initialize)**
    - 하드웨어 사용 준비 및 제어권 획득.

1. **🏗️ Systemd Service 시작**
    - PID 1번 프로세스 실행. 소프트웨어 사용 준비 완료.

1. **👤 부팅 완료**
    - 로그인 프롬프트 출력 (GUI 환경에서는 `quiet splash` 설정으로 메시지 대신 로고 출력).

### 1-3. GRUB 설정 실습

> ⚠️ /boot/grub/grub.cfg는 직접 수정하지 않고 /etc/default/grub을 수정합니다.
> 
- **설정 파일 수정:**

```bash
sudo nano /etc/default/grub
```

<img width="838" height="749" alt="Image" src="https://github.com/user-attachments/assets/fce0f5ad-ecd2-4fa0-96aa-a5ab4da1c8d4" />

- `GRUB_TIMEOUT_STYLE=hidden` 주석 처리 → 메뉴 강제 출력
- `GRUB_TIMEOUT=10` → 메뉴 대기 시간 설정 (초 단위)
- `GRUB_CMDLINE_LINUX_DEFAULT='quiet splash'` → `quiet` 삭제 시 부팅 로그 출력 (디버깅용)

- **변경 사항 적용 (필수):**

```bash
sudo update-grub
```

- **부팅 로그 확인 경로:**
    - `/var/log/dmesg` (부팅 로그 확인)

- **(참고) 설치 로그**
    - `/var/log/bootstrap.log` (설치 로그)

---

## 2. ⚙️ Systemd Service

### 2-1. 개요

- **역할:** 리눅스 시스템의 서비스 및 자원 통합 관리자 (PID 1).
- **역사:** 과거 유닉스의 `init` 프로세스(순차적 실행)를 대체.
- **특징:**
    - 소켓 기반 동작 (inetd 호환).
    - **병렬 실행**으로 부팅 속도 빠름 (쉘과 독립적).
    - 마운트 및 파일 시스템 제어 (`fsck`, `mount`).
    - 시스템 상태 스냅샷 및 서비스 시그널 전송 가능.
    - 셧 다운전에 사용자 세션의 안전한 종료 가능

### 2-2. Systemd Unit 종류

관리 대상을 **`서비스이름.유닛종류`** 형태로 관리합니다.

| **유닛 종류** | **설명** |
| --- | --- |
| **.service** | 시스템 데몬 시작, 종료, 재시작 관리 (가장 중요 ⭐) |
| **.target** | 유닛들을 그룹화 (런레벨 개념 대체) |
| **.socket** | 소켓 관리 (IPC, 네트워크 등) |
| **.mount** | 마운트 포인트 관리 |
| **.device** | 커널에 의해 인식된 장치 관리 |
| **.timer** | 스케줄링 관리 (cron 대체 가능) |
| **.swap** | 스왑 메모리 관리 (쿠버네티스에서는 사용 안 함) |

### 2-3. systemctl 명령어 (필수 암기)

**형식:** `systemctl [옵션] [명령] [유닛 이름]`

- **주요 명령:**
    - `start`: 시작
    - `stop`: 중지
    - `restart`: 재시작
    - `reload`: 설정 파일 다시 읽기 (서비스 중단 없음)
    - `status`: 상태 확인
    - `enable`: 부팅 시 자동 실행 등록
    - `disable`: 부팅 시 자동 실행 해제
    - `isolate`: 특정 타겟으로 전환 (런레벨 변경 등)

**실습 예시 (Cron 데몬):**

```bash
systemctl status cron    # 상태 확인
```

<img width="823" height="502" alt="Image" src="https://github.com/user-attachments/assets/4154681b-51e6-4137-a4dd-e3544baf6258" />


```bash
systemctl stop cron      # 중지
systemctl is-active cron # 동작 여부 확인
```

<img width="832" height="627" alt="Image" src="https://github.com/user-attachments/assets/2cd344fb-119f-4e10-8ab7-cb08bab8f917" />

### 2-4. 런레벨(Runlevel)과 Target

과거 `init`의 런레벨을 `target` 유닛으로 매핑하여 관리합니다.

- `graphical.target`: 런레벨 5 (GUI 부팅)
- `multi-user.target`: 런레벨 3 (CLI 다중 사용자)
- `rescue.target`: 런레벨 1 (단일 사용자, 시스템 복구용)

```bash
# 기본 타겟 확인
systemctl get-default

# 긴급 복구 모드로 전환
systemctl isolate rescue
```

### 2-5. 서비스 등록 방법 (커스텀 서비스) ⭐

> /etc/systemd/system/ 경로에 .service 파일을 생성합니다.
> 

**파일 예시 (`myservice.service`):**

```bash
[Unit]
Description=My Custom Service
After=network.target  # 네트워크가 켜진 후 실행

[Service]
ExecStart=/path/to/script.sh
Restart=on-failure    # 실패 시 재시작

[Install]
WantedBy=multi-user.target # 다중 사용자 모드에서 실행
```

**등록 절차:**

1. 파일 생성 및 작성
2. `systemctl daemon-reload` (데몬 리로드)
3. `systemctl enable [서비스명]` (부팅 시 자동 실행)
4. `systemctl start [서비스명]` (즉시 시작)

---

## 3. 🛑 시스템 종료 (Shutdown)

### 3-1. 개요

서버 운영체제 특성상 비정상 종료 시 서비스 장애 및 데이터 손실이 발생할 수 있으므로 안전한 종료가 중요합니다.

### 3-2. 종료 명령어

1. **shutdown 명령:**

```bash
shutdown -h now       # 즉시 종료
shutdown -r 22:00     # 밤 10시에 재부팅
shutdown -c           # 예약 취소
```

1. **Target 변경 (systemd):**

```bash
sudo systemctl isolate poweroff.target # 종료
sudo systemctl isolate reboot.target   # 재부팅
```

1. **심볼릭 링크 (단축 명령):**
- `halt`, `poweroff`, `reboot` 명령어는 실제로는 `systemctl`을 가리키는 **심볼릭 링크**입니다.
- 확인: `ls -l /sbin/reboot`

<img width="836" height="193" alt="Image" src="https://github.com/user-attachments/assets/6187833a-dd18-4a86-85e3-00278b63d75d" />

---

## 4. 😈 데몬 프로세스 (Daemon Process)

### 4-1. 개요

- **정의:** 사용자와 직접 상호작용하지 않고 (터미널 입력 등)하지 않고, 백그라운드에서 동작하며 특정 서비스를 제공하는 프로세스.
- **동작 방식:**
    - **독자형 (Standalone):** 메모리에 상주하며 즉각 응답 (예: httpd, mysqld). 자원 점유율 높음.
    - **슈퍼 데몬 (inetd/xinetd):** 요청이 올 때만 해당 데몬을 실행. 자원 효율적, 응답 속도 느림.
    

### 4-2. 커널 스레드 데몬 (Kernel Thread Daemon)

- **특징:**
    - **커널 공간에서 실행**되는 백그라운드 프로세스.
    - PID 값이 매우 낮음 (PID 2 `kthreadd`가 조상).
    - `ps` 명령 시 이름이 **대괄호 `[ ]`** 로 감싸져 있음.
- **역할:** 메모리 관리(swap), 디스크 동기화, 입출력 처리 등.

<img width="824" height="692" alt="Image" src="https://github.com/user-attachments/assets/ab393229-ff6e-4fd7-b331-0c6635f430c6" />

### 4-3. 주요 데몬 목록

| **데몬 이름** | **역할** |
| --- | --- |
| `crond` | 주기적인 작업 예약 실행 |
| `atd` | 일회성 작업 예약 실행 |
| `sshd` | 원격 접속 보안 서비스 (SSH) |
| `httpd` | 웹 서버 서비스 |
| `ftpd` | 파일 전송 서비스 |
| `syslogd` | 시스템 로그 기록 |
| `ntpd` | 시간 동기화 |

---

## 5. 📦 부트 로더 (Boot Loader)

### 5-1. GRUB (GRand Unified Bootloader)

- **개요:** LILO의 단점을 보완한 현재 리눅스 표준 부트 로더.
- **장점:**
    - 파일 시스템을 직접 인식하여 설정 변경이 용이.
    - 멀티 부팅 지원 (Windows 등).
    - 부팅 시 커맨드 모드 진입 가능 (복구 용이).
- **참고:** 도커는 리눅스 커널 위에서 동작하므로, 윈도우에서 사용 시 **WSL**(리눅스 커널 역할) 설치가 필요함.

### 5-2. 주요 파일

- `/boot/grub/grub.cfg`: 최종 설정 파일 (**수정 금지** 🚫).
- `/etc/default/grub`: 사용자 설정 파일 (**수정 가능** ✏️).
- `/etc/grub.d/`: 스크립트 디렉토리.

### 5-3. 🔑 루트 비밀번호 분실 시 복구

1. 부팅 시 GRUB 메뉴에서 `E` 키 입력 (편집 모드).
2. `ro splash $vt_handoff` 부분을 찾아 `rw init=/bin/bash` 로 수정.
    - *Read-Only를 Read-Write로 바꾸고, 쉘을 바로 실행하겠다는 뜻.*
3. `F10` 또는 `Ctrl+X`로 부팅 → 루트 쉘 진입.
4. `passwd` 명령어로 비밀번호 재설정.

---

## 6. 🐳 컨테이너 기술 (Namespace & Cgroup)

### 6-1. 배경 (Why Container?)

- **가상머신(VM):** OS 전체를 설치해야 해서 무겁고 자원 낭비가 심함.
- **컨테이너:** 애플리케이션 실행에 필요한 라이브러리와 바이너리만 격리. OS 커널은 호스트와 공유. (매우 가볍고 빠름).

### 6-2. 컨테이너 핵심 기술 3대장 (중요 ⭐)

1. **🛡️ Namespace (격리)**
    - 프로세스에게 독립된 공간을 제공하는 기술.
    - 컨테이너 안에서는 자신이 시스템의 유일한 프로세스인 것처럼 보임 (PID, Network, Mount 격리).
    
2. **⚖️ Cgroup (Control Group, 제한)**
    - 프로세스가 사용하는 자원(CPU, Memory, I/O)의 양을 **제한**하고 격리하는 커널 기능.
    - *실습 예시 (주의):* `echo`와 `tee`를 이용해 시스템 파일 값을 수정.
    
    ```bash
    # 리다이렉션과 파이프를 이용한 시스템 설정 (root 권한 필요)
    echo "50000 100000" | sudo tee /sys/fs/cgroup/mygroup/cpu.max
    ```
    

1. **📂 Union Mount Filesystem (효율)**
    - **"사기 치는 기술"**: 물리적으로 다른 여러 디렉토리(Layer)를 겹쳐서, 마치 하나의 파일 시스템(`/`)처럼 보여줌.
    - 이미지를 층층이 쌓아 관리하므로 중복되는 파일은 공유하고 변경된 부분만 따로 저장 (저장 공간 절약).
