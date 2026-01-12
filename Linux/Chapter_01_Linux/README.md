# 🐧 Linux & Ubuntu

## 1. 개요

### 1) Linux란?

- **기원**: 리누스 토발즈(Linus Torvalds)가 **MINIX**(교육용 OS)를 참조하여 개발
- **정의**: 유닉스(UNIX) 계열의 운영체제
- **어원**: Linux = Linus + UNIX

> **📜 UNIX 역사**
> 
> - 1969년 AT&T 벨 연구소에서 어셈블리어로 처음 개발
> - 이후 **C언어**로 재개발 (Linux 커널도 대부분 C언어로 개발됨)

### 2) 리눅스 계통도 (Distributions)

<img width="846" height="379" alt="Image" src="https://github.com/user-attachments/assets/fdb34d79-3766-4a7a-b728-ec9d30e4802f" />

- **데비안(Debian) 계열**: 우분투(Ubuntu) Linux → *플랫폼 기업 선호*
- **레드햇(RedHat) 계열**: 페도라(Fedora), CentOS(Rocky), RHEL → *대기업 선호*
- **슬랙웨어(Slackware) 계열**: SuSE → *Java 계열*

### 3) 운영체제의 구조 🏗️

<img width="369" height="189" alt="Image" src="https://github.com/user-attachments/assets/567ff793-83ca-4e07-b7dd-e6858e6e9acd" />

1. **Kernel (커널)**
    - 운영체제의 핵심 (Core)
    - **기능**: 프로세스, 메모리, 파일 시스템, 장치 관리 등
    - 컴퓨터의 모든 자원 초기화 및 제어
2. **Shell (쉘)**
    - 명령어 해석기
    - 유저의 명령을 해석하여 커널에 전달
3. **Application (애플리케이션)**
    - 개발 도구, 유틸리티 등

---

## 2. Ubuntu Linux

### 1) 개요

- **특징**: 데비안 계열 중 가장 성공한 배포판

### 2) 가상화 (Virtualization) ☁️

- **정의**: 하나의 물리적 컴퓨터 자원(CPU, Memory, Storage 등)을 논리적으로 나누거나 묶어서 효율적으로 사용하는 기술
- **방식**:
    - **VM (Virtual Machine)**: 하이퍼바이저를 이용 (무거움, 완벽한 격리)
    - **Container**: OS 수준에서 프로세스를 격리 (가벼움, Docker 등)
    

### 3) 가상 머신 (Virtual Machine) 소프트웨어 비교

Host OS에 Guest OS를 설치할 수 있게 해주는 소프트웨어

| **이름** | **Host OS** | **Guest OS** | **비고** |
| --- | --- | --- | --- |
| **VMWare** | Windows, Linux, Mac | Windows, Linux, Solaris, Mac | 유료/무료 |
| **Virtual PC** | Windows | Windows, Linux, Solaris | MS 제품 |
| **VirtualBox** | Win, Linux, Mac, Solaris | Win, Linux, Solaris, Mac, OpenBSD | **무료 (Oracle)** |
| **UTM** | Mac (Apple Silicon) | Linux, Windows | M1/M2/M3 맥💡 **Windows WSL (Windows Subsystem for Linux)** |
- PowerShell에서 설치 가능.
- Ubuntu 커널을 설치하여 윈도우 내에서 리눅스 환경을 가상화하는 효과.

---

## 3. 가상 머신(Virtual Box)을 이용한 설치

### 1) 우분투 이미지 다운로드 💿

- **Server (CLI 환경)**
    - 다운로드: [Ubuntu Server Download](https://ubuntu.com/download/server)
    - ***Tip:** 나중에 GUI 설치 가능*
    
    ```bash
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install --no-install-recommands ubuntu-desktop
    ```
    

- **Desktop (GUI 환경)**
    - 다운로드: [Ubuntu Desktop Download](https://ubuntu.com/download/desktop)

### 2) Virtual Box 설치 📦

- 다운로드: [VirtualBox.org](https://www.virtualbox.org/wiki/Downloads)
- *주의*: 설치 시 Visual C++ 재배포 패키지 요구 가능
![image.png](attachment:c7d369f4-90af-45d6-8a31-fac77260f61f:image.png)

### 3) 설치 프로세스 및 설정 ✅
![image.png](attachment:8c71535d-3137-4156-8a5e-54b332eac021:image.png)

1. **VM 생성**
![image.png](attachment:9372f548-c261-4464-b82d-17af973921b6:image.png)
- `새로 만들기` 클릭 → 이름 및 경로 설정
- ISO Image 선택 (다운로드 받은 파일)
- **⚠️ 중요**: `Proceed with Unattended Installation` (무인 설치) **해제**
    - **계정 설정:** `vboxuser` 대신 **내가 원하는 ID와 비밀번호**를 쓰기 위해
    - **세부 제어:** 언어, 키보드, 파티션 등을 **직접 설정(학습)**하기 위해
    - **오류 방지:** 자동 설치 스크립트 충돌로 인한 **설치 오류를 막기 위해**
    
2. **하드웨어 및 디스크 사이즈 설정**
![image.png](attachment:9372f548-c261-4464-b82d-17af973921b6:image.png)
    - CPU/Memory 설정
    - 📌 **K8s(쿠버네티스) 마스터 노드 권장**: **CPU 2코어 이상**

3. **초기 설정 (부팅 후)**
    - 언어 선택 (Server 버전은 한국어 ❌)
   ![image.png](attachment:7553fede-4deb-45ed-a266-867d805e7e65:image.png)
    - **네트워크(NIC) 확인**: `enp0s3` (기본 NIC 이름) / `dhcpv4` (IP 자동 할당)
   ![image.png](attachment:fe39a1c5-5652-460b-b810-d5772bbfc8d2:image.png)
    - **Proxy:** 설정 없음 (Done)
        - Proxy란? 클라이언트와 서버 사이에서 데이터 전달하는 중재자 역할 (보안)
   ![image.png](attachment:5e4fa1f6-44a4-402d-87fb-c27a21e08f53:image.png)
    - 디스크 및 파일시스템 설정
   ![image.png](attachment:c32c29f7-aa97-4a21-bc5e-2154283f997a:image.png)
    - 계정 설정 (컴퓨터 이름, 유저명)
   ![image.png](attachment:8561f9be-591a-40bd-8d1a-d79f52c21d35:image.png)
    - **SSH Server 설치 여부 체크 (스페이스바)**
        - Windows에서 원격 접속하기 위함 (Putty, OpenSSH 등)
   ![image.png](attachment:bea78094-c2d6-4675-a0d1-898201b5a0f8:image.png)

---

## 4. Ubuntu Server에 Open SSH 설치 및 접속

### 1) 설치 및 실행

**OpenSSH-Server 설치**

```bash
sudo apt update
sudo apt install openssh-server
```

**SSH 서비스 실행 및 확인**

```bash
sudo systemctl start ssh
sudo systemctl status ssh
```

**방화벽 포트 개방**

```bash
sudo ufw allow ssh
```

### 2) IP 확인 및 포트포워딩 설정

**IP 확인**

- Linux (Guest): `hostname -I` (예: `10.0.2.15`)
- Windows (Host): `ipconfig` (예: `192.168.201.176`)
- Mac (Host): 설정 메뉴 또는 `ifconfig`

**Virtual Box NAT 포트포워딩 설정**

- 경로: [설정] - [네트워크] - [포트포워딩]
- 설정 예시:
    - 호스트 IP: `192.168.201.176` / 호스트 포트: `2222` (임의 지정)
    - 게스트 IP: `10.0.2.15` / 게스트 포트: `22` (SSH 기본 포트)

### 3) 접속

```bash
# ssh 계정@호스트IP -p 호스트포트번호
ssh user@192.168.201.176 -p 2222
```

---

## 5. 시스템 종료 및 재부팅 명령어 🛑

### 1) 종료 (Shutdown)

- **GUI**: 오른쪽 상단 아이콘 클릭하여 종료
- **터미널 명령어:**

```bash
poweroff
shutdown -P now
halt -p
init 0
```

- **shutdown 옵션**:

```bash
shutdown -P +10   # 10분 뒤 종료
shutdown -r 22:00 # 22시에 재부팅
shutdown -k +5    # 실제 종료 X, 사용자에게 알림만 전송
shutdown -c       # 예약 취소
```

### 2) 재부팅 (Reboot)

```bash
reboot
shutdown -r now
init 6
```

---

## 6. Run Level (런레벨)

- 시스템을 가동하는 방법(Mode)을 정의한 것.
    
    (`init` 명령과 함께 사용.)
    

| **레벨** | **모드** | **설명** |
| --- | --- | --- |
| **0** | **Power Off** | 시스템 종료 |
| **1** | **Rescue** | 시스템 복구 모드 (단일 사용자, 네트워크 X) |
| **2** | **Multi-User** | NFS 없는 다중 사용자 모드 (잘 안 씀) |
| **3** | **Multi-User** | **텍스트 모드 (CLI)**, 서버 표준 |
| **4** | **Unused** | 사용 안 함 |
| **5** | **Graphical** | **그래픽 모드 (GUI)**, 데스크탑 표준 |
| **6** | **Reboot** | 시스템 재부팅 |

---

## 7. 명령어 입력 및 Shell 기초

### 1) 주요 개념

- **Shell (쉘)**: 사용자의 명령을 해석해 커널로 전달하거나 결과를 사용자에게 보여주는 요소.
    - **Login Shell 확인**: `echo $SHELL`
- **Prompt (프롬프트)**: `seongyun@myserver:~$`
    - `seongyun`: 사용자
    - `myserver`: 호스트 이름
    - `~`: 현재 디렉토리 (홈 디렉토리)
    - `$`: 일반 사용자 / `#`: 슈퍼 사용자(root)

### 2) 명령행 편집 단축키 (Shortcut)

| **기능** | **단축키** |
| --- | --- |
| **커서 이동** | `Ctrl`+`b`(뒤), `Ctrl`+`f`(앞), `Ctrl`+`a`(맨 앞), `Ctrl`+`e`(맨 뒤) |
| **단어 이동** | `Esc`+`b`(단어 뒤), `Esc`+`f`(단어 앞) |
| **지우기** | `Ctrl`+`w`(단어 삭제), `Ctrl`+`u`(맨 앞까지 삭제), `Ctrl`+`k`(맨 뒤까지 삭제) |
| **기타** | `Ctrl`+`y`(붙여넣기), `Ctrl`+`l`(화면 클리어), `Ctrl`+`c`(강제 종료) |

### 3) 명령의 구조

**형식**: `명령어 [옵션] [인자]`

- **옵션**:  (단일 문자) 또는 `-` (단어)로 시작. 순서 상관없음, 결합 가능.
    - 예: `ls -a -l` = `ls -la` = `ls -al`
- **실습 예제 (`ls`)**:
    
    ```bash
    ls -al /tmp
    # 목록보기(ls) + 모두(-a) + 상세히(-l) + 대상폴더(/tmp)
    ```
    

### 4) 자동 완성 및 History

- **자동 완성 (Tab)**
    - Tab 1번: 명령어가 유일할 때 자동 완성 (예: `egerp` → `eg`+Tab)
    - Tab 2번: 해당 문자로 시작하는 모든 명령어 목록 출력
- **History (이력 관리)**
    - `↑` (`Ctrl+p`): 이전 명령 / `↓` (`Ctrl+n`): 다음 명령
    - `Ctrl+r`: 이전에 실행한 명령어 검색 (증분 검색)
    - `history`: 명령어 수행 내용 전체 출력
    - `!!`: 직전 명령어 재실행
    - `!번호`: 해당 번호의 명령어 실행
    - `history -d 라인번호`: 특정 라인 삭제
    - `history -c`: 목록 전부 삭제
    - *저장 위치:* `~/.bash_history`

### 5) 도움말 및 경로 확인

- **도움말 (`-help`)**
    - 명령어의 사용법, 개요, 옵션 목록 출력
    - 예: `cat --help`
- **환경변수 PATH**
    - `echo $PATH`: Shell이 명령어를 찾는 위치
    - **현재 디렉토리의 파일 실행 시 `./명령어` 사용 (중요)**
- **명령어 위치 확인**
    - `whereis [옵션] [명령어]`: 실행 파일, 소스, 매뉴얼 위치 검색
        - `b`: 바이너리만, `s`: 소스만, `m`: 매뉴얼만
    - `which [옵션] [명령어]`: PATH 내에서 명령어 위치 검색
        - `a`: 모든 내용 출력

---

## 8. 기본 명령어

### 🔐 계정 및 시스템 관리

- **`passwd [계정]`**: 비밀번호 변경
    - `passwd`: 현재 계정 비번 변경
    - `passwd user1`: user1의 비번 변경 (관리자 권한 필요)
- **`exit`**: 터미널 종료
- **`clear`**: 화면 지우기
- **`alias`**: 별명 설정
    - 확인: `alias`
    - 설정: `alias ls='ls -F'`
    - 해제: `unalias ls`
    - *원본 실행:* `\ls`, `command ls`, `/usr/bin/ls`
    - `type 명령어`: 별명 여부 확인

### 🕒 시간 및 정보 확인

- **`date`**: 현재 시간/날짜 출력
- **`timedatectl`**: 시간 관련 설정 전체 출력
- **시스템 사용자 정보**
    - `logname`: 로그인 네임
    - `users`: 접속한 모든 아이디
    - `who`: 접속자 상세 정보 (계정, 시간, 위치 등)
    - `whoami`: 현재 사용자 확인
- **시스템 정보 (`uname`)**
    - `uname -a`: 모든 정보
    - `uname -r`: OS 릴리즈 번호
    - `hostname`: 호스트 네임
    - `env`: 환경변수 출력

### 👑 권한 관리 (sudo vs su)

- **`sudo` (Substitute User Do)**
    - 관리자(root)의 권한을 빌려 명령어 실행
    - 입력하는 비밀번호: **현재 사용자의 비밀번호**
- **`su` (Switch User)**
    - `su 계정`: 환경변수 **유지**하며 계정 전환
    - `su - 계정`: 환경변수 **초기화**하며 계정 전환 (권장)
    - *계정 미입력 시 root로 전환*

---

## 9. Ubuntu Server에 GUI 설치

```bash
sudo apt update
sudo apt install ubuntu-desktop
```

---

## 📚 (참고) 네트워크 기초

### 1. 주요 개념

- **IP (Internet Protocol)**: 컴퓨터(NIC)를 구분하기 위한 주소
- **Port**: 컴퓨터 내에서 동작하는 **프로세스(Application)**를 구분하기 위한 번호
    - 접속 예시: `IP주소 : Port번호`

### 2. Port 구분

- **Known Port (0 ~ 1023)**: 용도가 확정된 포트 (예: `80` HTTP, `443` HTTPS)
- **Unknown Port**: 사용자가 임의로 지정 가능 (PID와 다르게 지정 가능)

### 3. IPv4 주소 체계

- **구조**: 32bit (8bit씩 4구역, 0.0.0.0 ~ 255.255.255.255)
- **Classful Addressing (과거)**

| **클래스** | **시작 숫자** | **서브넷 마스크** | **용도** |
| --- | --- | --- | --- |
| **A Class** | 0 ~ 127 | 255.0.0.0 | 대규모 (국가/기업) |
| **B Class** | 128 ~ 191 | 255.255.0.0 | 중규모 (대학/기업) |
| **C Class** | 192 ~ 223 | 255.255.255.0 | 소규모 (가정/사무실) |
| **D Class** | 224 ~ 239 | - | 멀티캐스트 (방송용) |
- ***현재**: Classless 방식 사용 (CIDR)*

### 4. 사설 IP와 외부 접속

- **NAT/PAT**: IP 부족 및 보안 문제 해결
- **Private IP (사설 IP)**: 내부망 전용, 중복 가능
    - **Class A**: `10.0.0.0` ~ `10.255.255.255` (대규모)
    - **Class B**: `172.16.0.0` ~ `172.31.255.255` (중규모)
    - **Class C**: `192.168.0.0` ~ `192.168.255.255` (가정/소규모) → 가장 흔함
- **Public IP (공인 IP)**: 외부망 전용, 유일무이
- **Port Forwarding**: 외부에서 공인 IP로 들어온 요청을 내부 사설 IP로 연결해주는 기술 (공유기 설정)
    - *내 Private IP로는 외부에서 직접 접근 불가*
