# 🧧 Redis (REmote Dictionary Server)

## 1. 특징 (Features)

### **📌 핵심: Memory Key-Value Data Store**

- **⚡ Upsert 방식 & Key-Value 구조**
    - Key는 통상적으로 항상 `String`으로 관리
    
- **🏎️ 싱글 스레드 (Single Threaded)**
    - Event Loop 방식 이용 (Node.js와 유사한 매커니즘)
    - 큐(Queue)를 만들어 하나씩 빼서 작동하므로 **속도가 매우 빠름**
    - *Atomic*한 처리가 가능
    
- **🛡️ 고가용성 (High Availability)**
    - **가용성:** 사용하고자 할 때 바로 사용할 수 있는 정도
    - 복제를 통해 데이터를 여러 서버에 분산
    - **Sentinel:** 장애 상황을 탐지해 자동으로 **Fail-over** 수행
        
        > Fail-over: 시스템 장애 발생 시 예비 시스템으로 업무를 즉시 전환하여 무중단 운영을 유지하는 기술
        > 
    
- **📈 확장성 (Scalability)**
    - **Cluster Mode:** 쉽게 확장 가능
    - 자동 **Sharding**(데이터 조각화) 및 복제본 생성
    - 이러한 데이터 분리는 DB 레이어에서 처리됨 (주요 클라우드 벤더가 서비스화하여 제공)
    

---

## 2. MSA와 Redis (Micro Service Architecture)

### 💾 데이터 저장소로서의 Redis

- **속도:** In-memory DB라 매우 빠름
- **영속성(Persistence) 관리:** 메모리 기반이므로 데이터 유실 방지책 필요
    - **📸 RDB (Redis DataBase):** 스냅샷 방식. 사진 찍듯이 통째로 복사해 디스크에 저장
    - **📝 AOF (Append Only File):** 모든 명령어를 텍스트 파일에 순차적으로 기록

### 📣 Message Broker로 활용

- **Pub/Sub 기능 내장:** 간단한 알림 서비스 구현에 유용

---

## 3. 사용 사례 (Use Cases)

> ⚠️ 주의: 주 데이터 저장소로 사용 가능하나, 용량이 매우 큰 데이터 저장에는 부적합
> 

- **🚀 Caching (캐싱)**
    - DB 앞에 배치하여 액세스 지연 시간 감소, 처리량 증대 (RDBMS/NoSQL 부담 경감)
    - **중앙 집중형 구조:** MSA 환경에서 수평 확장된 모든 앱이 하나의 Redis를 바라보므로 **데이터 일관성** 유지 유리
    - *Note:* Hit Ratio를 고려해야 함 (오히려 접근 속도가 느려질 수도 있음)
    
- **🔐 세션 관리 (Session Management)**
    - 게임, 전자상거래, 소셜 미디어 등에서 유저 세션 유지에 활용
    
- **🏆 실시간 순위표 (Leaderboard)**
    - `Z`가 붙는 자료구조(Sorted Set) 이용 시 점수에 따라 자동 정렬
    
- **🔒 분산 락 (Distributed Lock)**
    - 여러 서버에서 공유 자원에 접근할 때 동시성 제어
    
- **🚦 속도 제한 (Rate Limiting)**
    - 이벤트 발생 속도를 측정하고 제한 (API 호출 제한 등)
    
- **이벤트 대기열 (Queue)**
    - List 자료구조를 활용해 작업 큐 구현 가능 (싱글 스레드 특성 활용)

---

## 4. Architecture

### 🏗️ Redis Sentinel 아키텍처

- **구성:** Redis Sentinel, Redis Master, Redis Replica
- **동작 원리:**
    1. **Sentinel**이 Master와 Replica를 모니터링 관리
    2. 평상시 **Master** 서버 사용
    3. Master 문제 발생 시 **Replica**가 동작
- **Fail-over 프로세스:**
    - App/Client ➡️ Sentinel에 명령어 전달
    - Sentinel ➡️ Master에 질의 및 응답 반환
    - Master 무응답 시 ➡️ Sentinel이 Replica 중 새로운 Master 선정하여 연결
    

---

## 5. 설치 및 접속

### 🛠️ 설치 (Installation)

1. **Public Cloud:** AWS ElastiCache 등 사용
2. **직접 설치:** [Redis 공식 문서 참조](https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/)
3. **Windows 설치:**
    - WSL(우분투) 설치 후 APT 이용
    - Docker 컨테이너 실행
    - MSI 버전 다운로드 ([GitHub 링크](https://github.com/microsoftarchive/redis/releases))
    

### 🔌 접속 (Connection)

`redis-cli`를 이용하여 접속합니다.

```python
redis-cli -h <IP주소> -p <포트번호> -a <패스워드>
```

- IP 생략 시: `127.0.0.1`
- Port 생략 시: `6379`
- 연결 확인: `ping` 입력 시 `PONG` 출력되면 정상

---

## 6. 기본 명령어 & 데이터 관리

### 📥 데이터 저장 및 조회

```bash
# 1개 저장 (SET)
SET a adam
# -> OK

# 1개 조회 (GET)
GET a
# -> "adam" (대소문자 구별, 없으면 (nil))

# 삭제 (DEL)
DEL a
# -> (integer) 1

# 여러 개 저장 (MSET)
MSET a adam b eve

# 여러 개 조회 (MGET)
MGET a b

# 키 조회 (KEYS)
KEYS * # -> (운영 환경에서는 주의 필요)

# 반복 조회 (SCAN)
SCAN <cursor> <pattern> <count>
```

### ⏳ 유효 기간 설정 (TTL)

메모리 효율성을 위해 사용하지 않는 데이터 자동 삭제 (세션 만료 기능 등에 활용).

```bash
SET c lee
EXPIRE c 30  # 30초 후 만료
TTL c        # 남은 시간 확인
```

---

## 7. 자료구조 (Data Structures)

### 1) 🧵 String

- 가장 기본적인 자료구조 (최대 512MB)
- Key-Value 일대일 매핑

```bash
SET hello world
# 옵션 활용
SET hello mongodb NX  # Not Exist: 없을 때만 저장 (기존 값 유지)
SET hello mongodb XX  # eXist: 있을 때만 수정 (덮어쓰기)

# 숫자 연산 (Atomic)
SET counter 100
INCR counter        # 101 (1 증가)
INCRBY counter 50   # 151 (50 증가)
```

### 2) 📋 List

- 순서가 있는 문자열 목록 (Linked List / Deque 형태)
- 최대 43억 개 저장 가능, 인덱스로 접근
- Stack, Queue로 활용 가능

```bash
# 데이터 삽입 (LPUSH: 왼쪽, RPUSH: 오른쪽)
LPUSH mylist E
RPUSH mylist B
# 결과: E, B

# 데이터 조회 (LRANGE)
LRANGE mylist 0 -1  # 전체 조회
LRANGE mylist 0 3   # 인덱스 0~3 조회

# 데이터 꺼내기 (POP)
LPOP mylist         # 왼쪽에서 꺼냄 (Queue)
RPOP mylist         # 오른쪽에서 꺼냄 (Stack)

# 데이터 정리 (TRIM)
LTRIM mylist 0 1    # 0~1번 인덱스만 남기고 나머지 삭제

# 데이터 삽입/수정
LINSERT mylist BEFORE A E  # A 앞에 E 삽입
LSET mylist 2 F            # 2번 인덱스 값 수정
LINDEX mylist 2            # 2번 인덱스 값 조회
```

> Tip: 양 끝(PUSH/POP) 처리는 **O(1)**로 빠르지만, 중간 인덱스 접근은 **O(n)**이 소요됩니다.
> 

### 3) 🗝️ Hash

- Field와 Value 쌍을 가진 아이템 집합 (객체 저장에 유리)

```bash
# 데이터 추가 (HSET)
HSET product:123 Name "Happy Things"
HSET product:123 TypeID 35
# 한 번에 추가
HSET product:123 Name "Track Ball" TypeID 32

# 데이터 조회
HGET product:123 Name          # 특정 필드 조회
HMGET product:123 TypeID Name  # 여러 필드 조회
HGETALL product:123            # 전체 필드 조회
HLEN product:123               # 필드 개수 확인

# 데이터 삭제
HDEL product:123 Name
```

---
