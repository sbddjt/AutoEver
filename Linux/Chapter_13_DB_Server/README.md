# 🐧 Linux Database Server Setup Guide

## 1. MariaDB (RDBMS) 🐬

### 🛠️ 설치 및 서비스 관리

**설치**

```bash
sudo apt install mariadb-server
```

**서비스 활성화 및 상태 확인**

```bash
sudo systemctl start mariadb   # 서비스 시작
sudo systemctl enable mariadb  # 부팅 시 자동 시작 설정
sudo systemctl status mariadb  # 상태 확인
```

### 🔐 접속 및 계정 관리

**로컬 접속**

```bash
sudo mysql
# 빠져나갈 때는: exit
```

**관리자(root) 비밀번호 설정**

```bash
# MariaDB 버전 및 상태 확인
sudo mysqladmin status
sudo mysqladmin version

# root 패스워드 설정
sudo mysqladmin -u root password '비밀번호'

# 변경된 비밀번호로 접속
sudo mysql -u root -p
```

**유저 생성 및 권한 부여 (SQL)**

```sql
- 유저 생성 (%는 모든 IP 허용, 보안상 특정 IP 권장)
CREATE USER '계정'@'%' IDENTIFIED BY '비밀번호';

- 예시: root는 로컬에서만, USER1은 모든 곳에서 linux 비번으로 접속
CREATE USER 'USER1'@'%' IDENTIFIED BY 'linux';

- 권한 부여 (모든 DB의 모든 테이블)
GRANT ALL PRIVILEGES ON . TO '계정'@'접속위치';
FLUSH PRIVILEGES;

- 예시: USER1에게 모든 권한 부여
GRANT ALL PRIVILEGES ON . TO 'USER1'@'%';
FLUSH PRIVILEGES;
```

### 🌐 외부 접속 설정

**설정 파일 수정 (바인딩 주소 변경)**

```bash
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf
# bind-address 부분을 0.0.0.0 으로 수정하거나 주석 처리
```

**재시작 및 방화벽 설정**

```bash
sudo systemctl restart mariadb
sudo ufw allow 3306/tcp
```

### 💾 백업 및 복원

**백업 (Dump)**

```bash
mysqldump -u [사용자계정] -p [비밀번호] [원본DB명] > 파일경로
```

**복원 (Restore)**

```bash
mysql -u [사용자계정] -p [비밀번호] [복원할DB명] < 파일경로
```

---

## 2. MongoDB (NoSQL) 🍃

### 🛠️ 설치 (7.0 버전 기준)

**필수 패키지 및 GPG 키 등록**

```bash
# 패키지 업데이트 및 필수 툴 설치
sudo apt update && sudo apt install gnupg curl

# GPG 키 등록
curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | \
sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor

# 저장소 리스트 추가
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | \
sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
```

**설치 및 서비스 실행**

```bash
sudo apt update
sudo apt install -y mongodb-org

# 서비스 시작 및 활성화
sudo systemctl start mongod
sudo systemctl enable mongod
sudo systemctl status mongod
```

### ⚙️ 설정 및 보안

**접속 테스트**

```bash
mongosh
```

**외부 접속 허용 설정**

```bash
sudo nano /etc/mongod.conf
# bindIp: 127.0.0.1 -> 0.0.0.0 으로 수정

# 재시작 및 방화벽
sudo systemctl restart mongod
sudo ufw allow 27017/tcp
```

> 접속 URL: mongodb://IP주소:포트번호
> 

**관리자 계정 생성 (보안 강화)**

```jsx
// mongosh 접속 후 실행
use admin
db.createUser({
  user: "adminUser",
  pwd: "password123",
  roles: [
    { role: "userAdminAnyDatabase", db: "admin" },
    "readWriteAnyDatabase"
  ]
})
```

**인증 모드 활성화 (mongod.conf)**

```yaml
# /etc/mongod.conf 파일 수정
security:
  authorization: enabled
```

*설정 후 `sudo systemctl restart mongod` 필수*

> 인증 접속 URL: mongodb://계정:비밀번호@서버주소:포트번호/
> 

---

## 3. Redis (In-Memory DB) 🧧

### 🛠️ 설치 및 실행

**설치**

```bash
sudo apt install redis-server
```

**접속**

```bash
redis-cli
```

### 🔒 설정 및 외부 접속

**설정 파일 수정**

```bash
sudo nano /etc/redis/redis.conf
```

- `bind 0.0.0.0` (외부 접속 허용)
- `requirepass 비밀번호` (비밀번호 설정)

**재시작 및 방화벽**

```bash
sudo systemctl restart redis-server
sudo ufw allow 6379/tcp
```

### 🔑 접속 방법

**로컬 인증**

```bash
redis-cli
> AUTH 비밀번호
# 인증 후 명령어 사용 가능
```

**외부 접속**

```bash
redis-cli -h 서버IP -p 포트번호 -a 암호
```

> **💡 Security Tip**
> 
> 
> Redis는 URL에 비밀번호를 직접 입력하는 것을 권장하지 않습니다. 접속 후 AUTH 명령어를 사용하고, 보안을 위해 기본 포트(6379)를 변경하여 사용하는 것이 좋습니다.
> 

---
