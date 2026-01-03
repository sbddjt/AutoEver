# 🍃 NoSQL Database (MongoDB)

> **Hyundai AutoEver Mobility SW Academy - Cloud Track** > 비정형 데이터 처리에 특화된 도큐먼트 지향 데이터베이스 MongoDB의 원리를 이해하고, 유연한 데이터 모델링 및 쿼리 최적화를 학습하는 공간입니다.

<div align="center">
  <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white"/>
  <img src="https://img.shields.io/badge/Compass-116149?style=for-the-badge&logo=mongodb&logoColor=white"/>
  <img src="https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white"/>
</div>
---

## 📖 Overview

클라우드 네이티브 환경과 마이크로서비스 아키텍처(MSA)에서 필수적인 **유연성(Flexibility)**과 **확장성(Scalability)**을 확보하기 위해 NoSQL을 학습합니다.
**Schema-less** 구조를 가진 MongoDB를 활용하여 JSON 형태의 데이터를 효율적으로 저장·조회하고, **Aggregation Framework**를 통한 복잡한 데이터 집계 처리를 실습합니다. 이는 향후 비정형 모빌리티 데이터(로그, 센서 데이터 등) 처리를 위한 기반이 됩니다.

## 🛠️ Environment

* **OS**: Windows 10/11 (or macOS, Linux)
* **Database Server**: MongoDB Community Server (v6.0+) or MongoDB Atlas (Cloud)
* **Client Tool**: MongoDB Compass, Mongosh (Shell)
* **Data Format**: BSON (Binary JSON)

---

## 📅 Curriculum & Progress

현대오토에버 클라우드 트랙 커리큘럼에 맞춘 학습 진행 상황입니다.

### 1️⃣ NoSQL Basic & Environment

* [ ] NoSQL의 개념 및 RDBMS와의 차이점 (CAP 이론)
* [ ] MongoDB 설치 및 환경 설정 (Local/Docker)
* [ ] MongoDB Compass 연결 및 기본 UI 익히기
* [ ] JSON/BSON 데이터 구조의 이해

### 2️⃣ CRUD Operations (Basic Query)

* [ ] **Create (Insert)**: `insertOne`, `insertMany`
* [ ] **Read (Find)**: `find`, `findOne`, Projection (필드 선택)
* [ ] **Update**: `updateOne`, `updateMany`, `$set`, `$inc` 연산자
* [ ] **Delete**: `deleteOne`, `deleteMany`

### 3️⃣ Advanced Querying & Indexing

* [ ] **Comparison Operators**: `$eq`, `$gt`, `$lt`, `$in`, `$ne`
* [ ] **Logical Operators**: `$or`, `$and`, `$not`, `$nor`
* [ ] **Element & Array**: `$exists`, `$type`, `$size`, `$elemMatch`
* [ ] **Indexing**: Single Field, Compound Index, Index를 활용한 성능 최적화

### 4️⃣ Aggregation & Modeling

* [ ] **Aggregation Pipeline**: `$match`, `$group`, `$sort`, `$project`
* [ ] **Data Modeling**: Embedded(비정규화) vs Reference(정규화) 패턴 설계
* [ ] **Relations**: `$lookup` (Left Outer Join 유사 기능)
* [ ] **Transaction**: 다중 문서 트랜잭션(Multi-document ACID)

---

## 📝 Key Concepts Summary

### 🔍 SQL vs MongoDB Terminology Mapping

| RDBMS (SQL) | MongoDB (NoSQL) | 설명 |
| --- | --- | --- |
| **Database** | **Database** | 데이터베이스 컨테이너 |
| **Table** | **Collection** | 도큐먼트들의 그룹 |
| **Row** | **Document** | 하나의 데이터 레코드 (JSON 유사) |
| **Column** | **Field** | 데이터의 키(Key) |
| **Primary Key** | **_id** | 고유 식별자 (자동 생성 가능) |
| **Join** | **$lookup** / **Embedding** | 데이터 간 관계 연결 |

### 💡 Important Notes

* **Schema-less**: 고정된 스키마가 없어 필드 추가/삭제가 자유로우나, 애플리케이션 레벨에서의 데이터 관리가 중요함.
* **BSON**: MongoDB는 내부적으로 JSON의 바이너리 형태인 BSON을 사용하여 날짜, 이진 데이터 등을 효율적으로 처리함.
* **Replica Set**: 고가용성(High Availability)을 위한 데이터 복제 구조.

---

## 📂 Directory Structure

```bash
mongodb/
├── 01_setup/           # 설치 가이드 및 환경설정 메모
├── 02_crud_basic/      # 기본 CRUD 쿼리 실습 (.js)
├── 03_operators/       # 비교, 논리, 배열 연산자 예제
├── 04_indexing/        # 인덱스 생성 및 실행 계획 분석
├── 05_aggregation/     # 집계 파이프라인 및 $lookup 실습
└── modeling/           # 스키마 설계 패턴 및 모빌리티 데이터 예제

```
