# 🍃 1. MongoDB 개요 및 설치

## 1. MongoDB란?

> NoSQL의 대표 주자, Document 지향 데이터베이스
> 
- **정의**: C++ 언어로 작성된 크로스 플랫폼 도큐먼트 지향(Document-oriented) 데이터베이스 시스템
- **주요 특징**:
    - **Schema-less**: 고정된 스키마가 없어 데이터 저장이 자유롭고, 필요할 때마다 필드를 추가/제거 가능
    - **JSON & BSON**: JSON과 유사한 동적 스키마형 문서를 선호하며, 실제 저장은 BSON(Binary JSON) 포맷 사용
    - **고가용성 & 확장성**:
        - **복제(Replication)**: 데이터 복제본을 저장하여 안정성 확보
        - **샤딩(Sharding)**: 데이터를 여러 서버(샤드)에 분산 저장하여 수평적 확장 가능

---

## 2. RDBMS vs MongoDB 구조 비교

관계형 DB와 용어가 다르므로 매핑하여 이해하는 것이 중요합니다. 

| **RDBMS (SQL)** | **MongoDB (NoSQL)** | **설명** |
| --- | --- | --- |
| **Database** | **Database** | 데이터 저장소  |
| **Table** | **Collection** | 도큐먼트들의 그룹  |
| **Row** | **Document** | 데이터의 기본 단위 (레코드)  |
| **Column** | **Field** | 도큐먼트 내의 키-값 쌍 (속성)  |
| **Join** | **Embedding & Linking** | 데이터를 포함하거나 참조하는 방식  |

---

## 3. 설치 (Installation) 🛠️

### 💻 Windows 설치

- **설치 방식**: [MongoDB Community Download 센터](https://www.mongodb.com/try/download/community)에서 `.msi` 설치 파일을 다운로드하여 실행
- **특징**:
    - 서버는 **Windows 서비스**로 자동 등록되어 관리됨 (`Install MongoD as a Service` 체크)
    - 설치 시 공식 GUI 도구인 **Compass**가 함께 설치됨
- **⚠️ 주의사항 (별도 설치 필요)**:
    1. **Shell (mongosh)**: 서버 설치 시 포함되지 않음. 별도 다운로드 필요
        - 🔗 [MongoDB Shell 다운로드](https://www.mongodb.com/try/download/shell)
    2. **Database Tools**: 외부 파일 Import/Export 등을 위한 도구. 기본 설치 제외됨
        - 🔗 [MongoDB Database Tools 다운로드](https://www.mongodb.com/try/download/database-tools)

### 🍎 Mac / 🐧 Linux 설치

- **설치 방식**: 터미널(Homebrew 등)을 통해 패키지로 설치하거나 [MongoDB 공식 문서](https://www.google.com/search?q=https://www.mongodb.com/docs/manual/administration/install-on-linux/) 참고
- **특징**: GUI 도구(Compass)가 포함되어 있지 않으므로 필요 시 직접 다운로드 받아야 함
    - 🔗 [MongoDB Compass 다운로드 (GUI)](https://www.mongodb.com/try/download/compass)
- **명령어 (Mac)**:
    - 설치: `brew install mongodb-community`
    - 실행: `brew services start mongodb-community`

---

## 4. 네트워크 및 접속 설정 🌐

### IP 주소 설정 (bindIp)

외부 접속 허용을 위해 설정 파일(`mongod.conf`)의 `bindIp` 수정 필요

- **127.0.0.1**: Localhost IP (Loopback). 내 컴퓨터에서만 접속 가능
- **0.0.0.0**: 모든 IP 허용. 외부 컴퓨터에서 접속 가능하게 하려면 이 설정으로 변경

### DB 접속 도구 비교 (CLI & GUI)

개발자들은 편의성을 위해 DBeaver나 전용 GUI 툴을 많이 사용합니다.

| **데이터베이스** | **CLI (명령 줄 도구)** | **비고** |
| --- | --- | --- |
| **Oracle** | SQL PLUS |  |
| **MySQL, MariaDB** | Command Line Tools | 직접 DB에 접속 |
| **MongoDB** | mongosh (Mongo Shell) | 별도 설치 필요 |

💡 **Tip**: **DBeaver**는 다양한 DB를 지원하며 복사 공간에서 작업이 가능해 개발자들이 널리 사용합니다.
