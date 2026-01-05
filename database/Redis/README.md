# ⚡ In-Memory Data Store (Redis)

> **Hyundai AutoEver Mobility SW Academy - Cloud Track** > 초고속 데이터 처리를 위한 인메모리 키-값 저장소 Redis의 핵심 자료구조를 익히고, 대용량 트래픽 처리를 위한 캐싱(Caching) 전략을 학습하는 공간입니다.

<div align="center">
<img src="[https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)"/>
<img src="[https://img.shields.io/badge/Cache-005571?style=for-the-badge&logo=c&logoColor=white](https://www.google.com/search?q=https://img.shields.io/badge/Cache-005571%3Fstyle%3Dfor-the-badge%26logo%3Dc%26logoColor%3Dwhite)"/>
<img src="[https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white](https://www.google.com/search?q=https://img.shields.io/badge/Docker-2496ED%3Fstyle%3Dfor-the-badge%26logo%3Ddocker%26logoColor%3Dwhite)"/>
</div>

---

## 🧧 Overview

디스크 기반 데이터베이스의 부하를 줄이고, 마이크로서비스 간의 **고속 데이터 공유** 및 **세션 클러스터링**을 구현하기 위해 Redis를 학습합니다.
메모리(RAM) 상에서 동작하는 **Key-Value** 구조를 이해하고, 다양한 **Data Types**를 활용하여 모빌리티 서비스의 실시간 랭킹, 위치 좌표 캐싱 등을 효율적으로 처리하는 방법을 실습합니다.

## 🛠️ Environment

* **OS**: Windows 10/11 (WSL2) or Linux (Ubuntu)
* **Server**: Redis Stack / Redis 7.x (Docker Container)
* **Client Tool**: RedisInsight, redis-cli
* **Library**: `redis-py` (Python) or `Lettuce`/`Jedis` (Java)

---

## 📅 Curriculum & Progress

현대오토에버 클라우드 트랙 커리큘럼에 맞춘 학습 진행 상황입니다.

### 1️⃣ Redis Basic & Setup

* [x] In-Memory DB의 특징 및 Cache의 필요성 (Look aside / Write back)
* [x] Redis 설치 및 Docker 컨테이너 구성
* [x] **Redis-cli** 기본 명령어 및 **RedisInsight** 연결
* [x] Single Thread 기반 아키텍처의 이해

### 2️⃣ Data Types (Key Structures)

* [x] **Strings**: 기본 캐싱, 세션 키 관리 (`SET`, `GET`, `MSET`)
* [x] **Lists**: 메시지 큐(Queue) 구현 (`LPUSH`, `RPOP`, `BLPOP`)
* [x] **Sets**: 중복 제거, 좋아요/태그 관리 (`SADD`, `SMEMBERS`, `SINTER`)
* [x] **Sorted Sets (ZSet)**: 실시간 순위(Leaderboard) 구현 (`ZADD`, `ZRANGE`)
* [x] **Hashes**: 객체(Object) 저장 (`HSET`, `HGETALL`)

### 3️⃣ Caching & Persistence

* [x] **Expiration (TTL)**: 데이터 수명 주기 관리 (`EXPIRE`, `TTL`)
* [x] **Eviction Policies**: 메모리 부족 시 데이터 축출 정책 (LRU, LFU)
* [x] **Persistence**: 데이터 영속성 보장 - **RDB** (Snapshot) vs **AOF** (Log)
* [x] **Transaction**: 원자성 보장 (`MULTI`, `EXEC`, `WATCH`)

### 4️⃣ Advanced & Architecture

* [x] **Pub/Sub**: 실시간 메시지 발행/구독 패턴 (채팅 시스템 기초)
* [x] **Redis Streams**: 대용량 로그 스트림 처리
* [x] **High Availability**: Sentinel(장애 조치) 및 Cluster(샤딩) 개념
* [x] **Geospatial**: 모빌리티 위치 데이터 처리 (`GEOADD`, `GEODIST`)

---

## 📝 Key Concepts Summary

### 🔍 Redis Data Types vs Use Cases

| Data Type | 특징 (Feature) | 활용 사례 (Use Case) |
| --- | --- | --- |
| **String** | 1:1 매핑, 바이너리 안전 | 단순 캐싱, 세션 저장, 카운터 |
| **List** | 순서가 있는 문자열 목록 (Linked List) | 작업 대기열(Queue), 타임라인 |
| **Set** | 순서 없고 중복 없는 집합 | 고유 방문자 수, 친구 목록, 태그 |
| **Sorted Set** | 점수(Score)를 포함한 정렬된 집합 | **실시간 랭킹**, 우선순위 큐 |
| **Hash** | Field-Value 쌍의 컬렉션 | 사용자 프로필, 상품 상세 정보 |
| **Geospatial** | 위도/경도 좌표 데이터 | **차량 위치 추적**, 근처 맛집 찾기 |

### 💡 Important Notes

* **Single Threaded**: Redis는 기본적으로 싱글 스레드로 동작하므로, `KEYS *`와 같이 **O(N)** 시간이 걸리는 무거운 명령어를 운영 환경에서 실행하면 안 됨 (`SCAN` 권장).
* **Volatile**: 메모리 기반이므로 전원 차단 시 데이터가 휘발됨. 중요 데이터는 RDB/AOF 설정을 통해 디스크에 저장해야 함.
* **Atomic**: Redis의 모든 연산은 원자적(Atomic)으로 수행되어 동시성 문제(Race Condition)를 최소화함.

---

## 📂 Directory Structure

```bash
redis/
├── 01_setup/           # Docker Compose 설정 및 설치 가이드
├── 02_datatypes/       # 5대 자료구조 실습 스크립트 (.txt / .py)
├── 03_caching/         # TTL 설정 및 캐시 전략 예제
├── 04_persistence/     # RDB, AOF 설정 파일 및 테스트
├── 05_advanced/        # Pub/Sub, Transaction, Geo 실습
└── project_apply/      # 스프링/파이썬 프로젝트 연동 코드 (Session, Cache)

```

---

**Would you like me to help you create the directory folders or draft the `01_setup` guide first?**
