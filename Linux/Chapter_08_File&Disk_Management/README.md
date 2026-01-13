# 🐧 Linux File System & Disk Management

## 1. Linux File System (리눅스 파일 시스템)

### 📂 개요

> **디스크 기반 파일 시스템**
> 
> 
> 파일과 디렉터리를 관리하기 위한 필수 시스템입니다.
> 
- **Minix File System (MFS):** 리눅스 초기 사용
- **ext (Extended File System):** 리눅스 고유의 파일 시스템 (현재 **ext4**까지 발전)
- **XFS:** 대용량 파일 시스템을 위해 실리콘 그래픽스가 개발

### 🗂️ 종류

**1. ext4 (Extended File System 4)**

- **지원 용량:** 1EB(Exabyte) 이상의 볼륨, 16TB 이상의 파일 지원
- **디렉토리 개수:** 64,000개까지 지원 (기존 32,000개에서 확장)
- **기능:** 온라인 조각 모음 제공
    
    💡시스템을 중단하거나 드라이브 연결을 끊지 않고, 운영체제가 작동 중인 상태에서 실시간으로 파일을 정리해주는 것
    

**2. XFS**

- **개요:** 1993년 실리콘 그래픽스 개발, 고성능 저널링 파일 시스템
- **특징:** 64비트 파일 시스템, 16EB까지 지원
- **설치:** 우분투에서는 `xfsprogs` 패키지 필요

**3. 기타 지원 파일 시스템 💿**

| **이름** | **설명** |
| --- | --- |
| **msdos** | MS-DOS 파티션 지원 |
| **iso9660** | CD-ROM, DVD 등 읽기 전용 파일 시스템 |
| **nfs** | Network File System (원격 서버 디스크 연결) |
| **ntfs** | Windows 기본 파일 시스템 |

**👻 특수 용도 가상 파일 시스템**

- **swap**: RAM 부족 시 디스크를 메모리처럼 사용하여 시스템 안정성 확보
- **tmpfs**: 메모리에 임시 파일 저장 (재부팅 시 소멸, `/tmp` 등)
- **ramfs**: 디스크 대신 메모리를 저장 공간으로 활용 (tmpfs와 달리 swap 사용 안 함)
- **rootfs**: 시스템 초기화 및 관리에 필요한 내용 저장
- **proc**: `/proc` 디렉토리 ⭐
    - 커널의 현재 상태를 나타내는 가상 파일 시스템 (메모리에 존재)
    - **주요 정보 파일**
        - `/proc/cpuinfo`: CPU 정보
        - `/proc/meminfo`: 메모리 정보
        - `/proc/uptime`: 부팅 후 경과 시간
        - `/proc/loadavg`: 시스템 평균 부하
        - `/proc/[PID]/status`: 특정 프로세스 상태
        - `/proc/sys/net/ipv4/ip_forward`: 패킷 포워딩 여부

**현재 지원 파일 시스템 확인**

```bash
cat /proc/filesystems
```

<img width="838" height="694" alt="Image" src="https://github.com/user-attachments/assets/164de899-4ba0-4909-a850-76eafc2b02d0" />

---

## 2. Inode & ext4 구조

### 🏗️ ext4 파일 시스템 구조

- 효율적 디스크 사용을 위해 저장 장치를 **논리적 블록(Block)**의 집합으로 구분
- **Block Size:** 일반적으로 4KB
- **Block Group:** 장치 크기 / 블록 그룹 크기

### ℹ️ Inode (Index Node) 구조

파일에 대한 메타데이터를 저장하는 핵심 자료구조입니다.

- **구성 요소:**
    1. **파일 정보:** 종류, 권한, 소유자, 시간 정보 등 (`ls -l`로 확인되는 메타데이터)
    2. **데이터 블록 주소:** 실제 데이터가 저장된 블록의 위치 (직접, 간접, 이중 간접 등)
- **파일 참조 체계:** `파일 이름` → `inode` → `데이터 블록`

**🔗 링크(Link)의 개념**

- **Symbolic Link:** 파일의 이름과 경로를 참조 (윈도우의 바로가기)
- **Hard Link:** Inode 자체를 참조 (동일한 파일 시스템 내에서만 생성 가능)
    - **삭제 메커니즘:**
        - 파일 삭제 명령 시: `Inode Reference Count -= 1`
        - 실제 삭제 시점: `Inode Reference Count == 0` 일 때
        - Inode 삭제 시 연결된 데이터 블록 읽기 불가 (할당 해제)

---

## 3. 디렉토리 계층 구조 & 마운트

### 🌳 계층 구조 비교

- **Windows:** 드라이브(파티션) 별로 파일 시스템 연결 (`C:\`, `D:\`)
- **Linux:** **하나의 트리 구조** (`/` 루트 디렉토리 기준)
    - 파일 시스템 하나는 `/`에, 다른 하나는 `/usr`에 연결하는 방식 가능
    - 물리적으로 다른 디스크여도 하나의 폴더처럼 사용 가능
    

### 🔗 파일 시스템 마운트 (Mount)

**기본 개념**

**마운트 (Mount)**
: 물리적인 저장 장치 (USB, HDD 등)를 디렉토리 계층 구조의 **특정 디렉토리 (마운트 포인트)**에 연결하여 사용자가 접근할 수 있게 만드는 작업

**설정 파일** 

- **역할:** 리눅스 부팅 시 파일 시스템을 **자동으로 마운트**하도록 설정하는 파일
- **경로:** `/etc/fstab`
- **구조 예시:**

```bash
# <장치>  <마운트포인트>  <타입>  <옵션>  <덤프>  <순서>
/dev/sda1       /         ext4   defaults    0      1
```

<img width="843" height="396" alt="Image" src="https://github.com/user-attachments/assets/87fd6f25-f0f7-4fcc-b4a4-90424d274d99" />

- **주요 옵션**
    
    
    | **옵션** | **설명** |
    | --- | --- |
    | **defaults** | 일반적인 파일 시스템 옵션으로 `rw`, `nouser`, `auto`, `exec`, `suid` 속성을 모두 포함함 |
    | **auto / noauto** | 부팅 시 자동으로 마운트할지(`auto`) 여부를 결정함 |
    | **exec / noexec** | 해당 파일 시스템에서 실행 파일의 실행을 허용(`exec`)할지 여부 |
    | **suid / nosuid** | `SetUID`, `SetGID`의 사용을 허용(`suid`)할지 여부 |
    | **ro / rw** | 읽기 전용(`ro`)으로 마운트할지, 읽기 및 쓰기 가능(`rw`)으로 마운트할지 설정함 |
    | **user / nouser** | 일반 사용자가 마운트할 수 있는지(`user`) 아니면 root만 가능한지(`nouser`) 설정함 |
    | **usrquota / grpquota** | 사용자별(`usrquota`) 또는 그룹별(`grpquota`)로 디스크 사용량(쿼터)을 제한할 때 사용함 |

### 🛠️ 마운트 명령어

**형식:** `mount [옵션] [장치명] [마운트포인트]`

- **옵션**
    - `t`: 파일 시스템 종류 지정
    - `o`: 마운트 옵션 지정 (`ro` 등)
    - `f`: 마운트 가능 여부 점검

**사용 예시**

```bash
# CD-ROM 마운트
mount -t iso9660 /dev/cdrom /mnt/cdrom

# USB 메모리 (리눅스 포맷)
mount /dev/sdc1 /mnt

# USB 메모리 (윈도우 포맷)
mount -t vfat /dev/sdc1 /mnt

# 마운트 해제
umount /mnt
```

---

## 4. 디스크 관리 실습

### 🔌 새로운 디스크 추가 및 파티셔닝

1. **디스크 인식 확인**

```bash
sudo fdisk -l
# 보통 sda(기본), sdb(추가1), sdc(추가2) 순서로 명명
```

1. **파티션 생성 (`fdisk`)**

```bash
sudo fdisk /dev/sdb
```

- `m`: 도움말
- `d`: 파티션 삭제
- `n`: 새 파티션 생성
- `p`: 파티션 종류 선택 (Primary)
- `1`: 파티션 번호
- `w`: 저장 및 종료

1. **파일 시스템 생성 (포맷)**

```bash
# ext4로 포맷
sudo mke2fs -t ext4 /dev/sdb1
# 또는
sudo mkfs -t ext4 /dev/sdb1
```

1. **마운트 및 사용**

```bash
sudo mount /dev/sdb1 /mnt
ls /mnt
sudo cp /etc/hosts /mnt  # 파일 복사 테스트
```

---

## 5. LVM (Logical Volume Manager)

### 🧩 개요

여러 개의 하드디스크를 합쳐서 한 개의 파티션처럼 구성하거나, 크기를 유연하게 조절하는 기술.

- **장점:** 유연한 용량 조절, 데이터 이전 없이 크기 변경 가능, 스트라이핑/미러링 지원

### 🧱 구성 요소

1. **PV (Physical Volume):** 실제 하드디스크 파티션 (`/dev/sdb1`)
2. **VG (Volume Group):** 여러 PV를 묶은 그룹 (거대한 저장소 풀)
3. **LV (Logical Volume):** VG에서 사용자가 필요한 만큼 잘라낸 논리적 파티션
4. **PE / LE:** 물리적/논리적 블록 단위

### 🔄 생성 과정

<img width="843" height="396" alt="Image" src="https://github.com/user-attachments/assets/cd30c983-7e15-46eb-a4a0-67e9e089ab82" />

1. **파티션 타입 변경:** `fdisk` (LVM 타입으로)
2. **PV 생성:** `pvcreate /dev/sdb1`
3. **VG 생성:** `vgcreate myVG /dev/sdb1`
4. **VG 활성화:** `vgchange -a y myVG`
5. **LV 생성:** `lvcreate`
6. **파일 시스템 생성:** `mkfs`
7. **마운트:** `mount`

---

## 6. 디스크 관리 도구

### 📊 디스크 사용량 확인

**1. df (Disk Free) - 파일 시스템 전체 용량**

```bash
df -h  # -h: 알기 쉬운 단위(GB, MB)로 출력
df -T  # 파일 시스템 종류 함께 출력
```

1. **du (Disk Usage) - 디렉터리별 용량**

```bash
du -sh /home/user  # -s: 요약(총합), -h: 알기 쉬운 단위
```

### 🩺 파일 시스템 검사 및 복구

> **주의:** 검사 전 **반드시 언마운트(umount) 상태**여야 합니다.
> 

**1. fsck / e2fsck**

```bash
fsck -y /dev/sdb1   # -y: 질문에 모두 yes
fsck -f /dev/sdb1   # -f: 강제 점검
```

**2. badblocks (배드 섹터 검사)**

```bash
badblocks -v /dev/sdb1
```
