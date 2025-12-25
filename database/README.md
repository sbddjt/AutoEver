# 🗄️ Database (MariaDB & SQL)

> **Hyundai AutoEver Mobility Embedded SW Academy - Cloud Track** > 데이터베이스의 원리를 이해하고 MariaDB와 DBeaver를 활용하여 효율적인 데이터 관리 및 설계를 학습하는 공간입니다.

<div align="center">
  <img src="https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white"/>
  <img src="https://img.shields.io/badge/DBeaver-382923?style=for-the-badge&logo=dbeaver&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQL-CC2927?style=for-the-badge&logo=microsoftsqlserver&logoColor=white"/>
</div>

---

## 📖 Overview
클라우드 네이티브 애플리케이션 개발의 핵심인 **데이터 지속성(Persistence)**을 관리하기 위해 RDBMS(관계형 데이터베이스)를 학습합니다.  
오픈소스 데이터베이스인 **MariaDB**를 서버로 구축하고, GUI 툴인 **DBeaver**를 통해 SQL 쿼리를 실습하며, 향후 Spring Boot 프로젝트와의 연동 및 AWS RDS 환경에서의 운용을 위한 기초를 다집니다.

## 🛠️ Environment
- **OS**: Windows 10/11 (or macOS)
- **Database Server**: MariaDB (Version 10.x 이상)
- **Client Tool**: DBeaver Community Edition
- **Character Set**: UTF-8 (General/Unicode)

---

## 📅 Curriculum & Progress
현대오토에버 클라우드 트랙 커리큘럼에 맞춘 학습 진행 상황입니다.

### 1️⃣ Database Basic & Environment
- [x] DBMS의 개요 및 RDBMS의 이해
- [x] MariaDB 설치 및 환경 설정 (Root 계정 관리)
- [x] DBeaver 설치 및 Connection 연결
- [x] 데이터베이스 사용자(User) 생성 및 권한 부여 (DCL)

### 2️⃣ SQL Fundamentals (DML, DQL)
- [ ] **SELECT 문법**: 데이터 조회, Alias, DISTINCT
- [ ] **조건절(WHERE)**: 비교 연산자, 논리 연산자, BETWEEN, IN, LIKE
- [ ] **정렬 및 제한**: ORDER BY, LIMIT
- [ ] **단일 행 함수**: 문자, 숫자, 날짜, 형변환 함수 (NULL 처리)

### 3️⃣ Advanced SQL & Aggregation
- [ ] **그룹 함수**: COUNT, SUM, AVG, MAX, MIN
- [ ] **GROUP BY & HAVING**: 데이터 그룹화 및 필터링
- [ ] **JOIN**: Inner Join, Outer Join(Left/Right), Self Join, Cross Join
- [ ] **Subquery**: 단일행/다중행 서브쿼리, 인라인 뷰

### 4️⃣ Data Modeling & Management (DDL, TCL)
- [ ] **테이블 생성 및 수정**: CREATE, ALTER, DROP
- [ ] **제약조건(Constraints)**: PK, FK, UK, NOT NULL, DEFAULT
- [ ] **데이터 조작**: INSERT, UPDATE, DELETE
- [ ] **트랜잭션 관리**: COMMIT, ROLLBACK, Savepoint
- [ ] **데이터 모델링**: 정규화(Normalization) 과정 및 ERD 작성 실습

---

## 📝 Key Concepts Summary

### 🔍 SQL Commands Classification
| 분류 | 명령어 | 설명 |
|:---:|:---:|:---|
| **DQL** | `SELECT` | 데이터 조회 (질의) |
| **DML** | `INSERT`, `UPDATE`, `DELETE` | 데이터 삽입, 수정, 삭제 |
| **DDL** | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` | 데이터 정의 (테이블 등 구조 생성/변경) |
| **DCL** | `GRANT`, `REVOKE` | 데이터 제어 (권한 부여/회수) |
| **TCL** | `COMMIT`, `ROLLBACK` | 트랜잭션 제어 |

### 💡 Important Notes
- **MariaDB vs MySQL**: MariaDB는 MySQL에서 파생된 오픈소스로 명령어 호환성이 높음.
- **Transaction**: 데이터 무결성을 보장하기 위한 논리적 작업 단위 (ACID 성질).
- **Indexing**: 조회 속도 향상을 위한 인덱스 설정의 중요성과 Trade-off.

---

## 📂 Directory Structure
```bash
database/
├── 01_setup/          # 설치 및 환경설정 관련 메모
├── 02_basic_select/   # 기초 SELECT 문법 실습 (.sql)
├── 03_functions/      # 내장 함수 활용 실습
├── 04_joins/          # 조인 및 서브쿼리 예제
├── 05_ddl_dml/        # 테이블 생성 및 데이터 조작
└── assignments/       # 과제 및 ERD 다이어그램 파일
