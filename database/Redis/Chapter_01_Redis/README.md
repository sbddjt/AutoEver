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
    - **Sentinel:** 장애 상황을 탐지해 자동으-로 **Fail-over** 수행
        
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

### 4) 🫂 Set

- 정렬되지 않은 문자열의 모임
- 데이터를 중복해서 저장하지 않음 (Unique)
- **집합 연산 제공**: `SUNION`(합), `SINTER`(교), `SDIFF`(차)

```bash
# 데이터 저장 (SADD)
SADD myset A
SADD myset A A A D D B B B B E E  # 중복 제거됨

# 조회 및 삭제
SMEMBERS myset  # 전체 데이터를 조회
SREM myset B    # 데이터 삭제
SPOP myset      # 랜덤하게 하나 골라서 삭제
```

### 5) 🥇 Sorted Set

- 스코어(Score) 값에 따라 정렬되는 문자열의 집합
- **특징**:
    - Set과 유사 (중복 없는 데이터) + Hash와 유사 (아이템이 스코어에 연결됨)
    - List처럼 인덱스로 접근 가능하지만, **O(log(n))**으로 처리됨
    - *데이터 접근 빈도가 높다면 List보다 효율적일 수 있음*
    

```bash
# 데이터 저장
ZADD score:260105 100 user:B
ZADD score:260105 150 user:A 150 user:C 200 user:F 300 user:E

# 옵션 설명
# XX: 존재하는 경우 스코어를 업데이트
# NX: 존재하지 않을 때만 삽입
# LT: 업데이트할 스코어가 기존보다 작을 때만 업데이트 (없으면 삽입)
# GT: 업데이트할 스코어가 기존보다 클 때만 업데이트 (없으면 삽입)
```

```bash
# 데이터 조회 (ZRANGE)

# 인덱스로 조회
ZRANGE score:260105 1 3 WITHSCORES
ZREVRANGE score:260105 1 3 WITHSCORES  # 역순

# 스코어로 조회
ZRANGEBYSCORE score:260105 100 150 WITHSCORES
# ( 값 앞에 '('를 추가하면 해당 값 제외 (초과/미만)
# 최솟값: -inf, 최댓값: +inf 사용 가능
```

### 6) 🔴 Bitmap

- String 자료구조에 Bit 연산을 수행할 수 있도록 확장한 형태
- 메모리 공간을 획기적으로 절약할 수 있음 (출석 체크 등에 활용)

### 7) 🧩 HyperLogLog

- **개념**: 집합의 원소 개수인 Cardinality를 추정할 수 있는 자료구조
- **특징**:
    - 대량의 데이터에서 중복되지 않는 고유한 값을 집계할 때 유용 (ex. 웹사이트 방문자 수)
    - 입력 데이터를 저장하지 않고 자체 방법으로 변경해 처리하므로 메모리 매우 효율적
    - 오차율: 약 **0.81%**

```bash
PFADD members 123
PFADD members 500
PFADD members 123
PFADD members 12

PFCOUNT members  # 개수 추정 결과 반환
```

### 8) 🗺️ Geospatial

- **개념**: 경도(Longitude)와 위도(Latitude) 데이터 쌍의 집합
- **특징**:
    - 지리 데이터 저장에 이용
    - 내부적으로는 **Sorted Set**으로 저장 (키 중복 불가)

```bash
GEOADD travel 14.3996 50.099242 Prague
GEOADD travel 127.0016 37.5642 Seoul -122.4345 37.7853 Sanfrancisco
```

### 9) 🌊 Stream

- **개념**: Redis를 메시지 브로커로서 사용할 수 있게 하는 자료구조
- **특징**:
    - **Kafka**의 영향을 받아 만들어짐 (소비자 그룹 개념 도입)
    - 데이터를 계속해서 추가(Append)하는 방식의 로그 데이터 처리에 적합
    - 데이터 분산 처리 가능

---

## 8. 레디스에서 키를 관리하는 방법

### 1) 키의 자동 생성과 삭제

⇒ stream이나 set, sorted set, hash와 같이 하나의 키가 여러 개의 아이템을 가지고 있는 자료구조에서는 명시적으로 키를 생성하거나 삭제하지 않아도 알아서 생성되고 삭제됩니다.

⇒ 키가 존재하지 않을 때 아이템을 넣으면 아이템을 삽입하기 전에 빈 자료구조를 생성합니다.

DEL mylist # mylist 삭제

LPUSH mylist 1 2 3 # mylist를 list로 생성하고 1 2 3을 삽입

이미 만들어진 자료구조(키)에 다른 자료구조의 명령어를 사용하면 에러 발생

SET hello world # string 자료구조

LPUSH hello 1 2 3 # 에러 발생 LPUSH는 list 자료구조에 데이터를 삽입하는 명령

⇒ 모든 아이템을 삭제하면 키도 자동으로 삭제되는데 **stream은 예외**

- 키의 존재 여부는 EXISTS로 확인 가능

DEL mylist

LPUSH mylist 1 2 3

EXISTS mylist # 있음 1 출력

LPOP mylist

LPOP mylist

LPOP mylist

EXISTS mylist # 없음 0 출력

⇒ 키가 없는 상태에서 키 삭제, 아이템 삭제, 자료 구조 크기를 조회하면 에러가 아니라 키는 있으나 데이터가 없는 것처럼 동작합니다.

DEL mylist 

LLEN mylist # 0이 출력됨

LPOP mylist # nil이 출력됨

### 2) key 관련 명령

⇒ 존재 여부 확인 : 

EXISTS key [key …]

⇒ 패턴을 가지고 키를 조회:

KEYS pattern

- 패턴
    
    키 이름 *: 모든 key를 조회
    
    키 이름에 ?를 추가하면 1글자의 와일드카드
    
    h?llo: hello, hallo 등과 매칭
    
    키 이름에 *을 추가하면 글자 수 상관없는 와일드카드
    
    h*llo: hllo hello, heello 등과 매칭
    
    [ ]안에 나열을 하면 그 중 하나가 됩니다.
    
    h[ae]llo는 hallo나 hello와 매칭이 됩니다.
    
    ^는 제외하고
    
    h[^e]llo는 hello와 매칭이 되지 않습니다.
    

⇒ KEYS는 위험한 command

- redis는 100만 개의 키가 저장되어 있다면 모든 키의 정보를 반환함
- redis는 싱글 스레드 기반이라서 실행 시간이 오래 걸리는 커맨드를 수행하면 다른 모든 커맨드가 차단됩니다.
- 이렇게 오래 걸리는 명령을 redis에 수행하게 되면 다른 클라이언트에서 redis에 데이터를 저장할 수 없고 그동안 대기열이 늘어날 수 있으며 모니터링 도구가 마스터 노드로 보낸 health check에 응답할 수 없어서 의도하지 않은 failover가 발생할 수 있습니다.

⇒ SCAN

- 커서를 기반으로 특정 범위의 키만 조회할 수 있는 커맨드
- SCAN cursor [MATCH pattern] [COUNT count] [TYPE type]
- SCAN 했을 때 리턴하는 값은 다음 cursor의 위치
- 기본적으로 10개의 key만 반환

⇒ SORT

- list, set, sorted set에서만 사용할 수 있는 커맨드
- 키 내부의 아이템을 정렬해서 반환
- LIMIT 옵션을 이용해서 원하는 개수만큼 반환 가능
- ASC와 DESC를 이용해서 오름차순과 내림차순 설정 가능
- 숫자와 문자열이 섞인 경우 ALPHA 옵션을 이용해서 문자열로 변환해서 정렬 가능

DEL mylist

LPUSH mylist a

LPUSH mylist b

LPUSH mylist c

SORT mylist # 오류 발생 문자열은 기본적으로 정렬이 안됨

LPUSH mylist HELLO

SORT mylist alpha # 이렇게 하면 정렬됨

⇒ 키이름  변경

RENAME key newkey

SET a apple

RENAME a aa

GET aa

⇒ 키 복제

COPY source destination [REPLACE]

- 키가 존재하면 에러인데 REPLACE 옵션을 사용하면 기존의 키를 지우고 생성해서 복제

SET B BANANA

COPY B BB

GET B

GET BB

⇒ TYPE

- 자료구조 확인
    
    TYPE KEY
    

⇒ 키 전체 삭제

FLUSHALL [ASYNC | SYNC] 

⇒ 키 삭제

DEL 키

⇒ 키 연결 해제

UNLINK 키

⇒ 키의 만료시간 확인

TTL 키

- 유효시간이 없으면 -1 키가 없으면 -2를 반환

---

# 8. Redis에서 키를 관리하는 방법

> **💡 핵심 요약**
> 
> 
> Redis는 키-값(Key-Value) 구조이지만, **자료구조(List, Set 등)를 사용할 때 명시적인 생성/삭제가 필요 없는 편리한 특징**을 가지고 있습니다. 단, **싱글 스레드** 특성상 주의해야 할 명령어들이 있습니다.
> 

---

## 🔴 1. 키의 자동 생성과 삭제

Redis의 컨테이너형 자료구조(`Stream`, `Set`, `Sorted Set`, `Hash`)는 별도의 생성/삭제 명령 없이 아이템의 유무에 따라 자동으로 관리됩니다.

### 📌 자동 생성 및 삭제 규칙

- **자동 생성:** 키가 없을 때 아이템을 넣으면 빈 자료구조를 생성 후 삽입합니다.
- **자동 삭제:** 모든 아이템이 삭제되면 키(자료구조) 자체도 삭제됩니다. (단, `Stream`은 예외)
- **타입 불일치 에러:** 이미 생성된 키의 자료구조와 다른 명령어를 사용하면 에러가 발생합니다.

```bash
# 1. 자동 생성 예시
DEL mylist           # mylist 삭제 (초기화)
LPUSH mylist 1 2 3   # mylist를 List로 생성하고 1, 2, 3 삽입

# 2. 타입 에러 예시
SET hello world      # string 자료구조 생성
LPUSH hello 1 2 3    # 에러 발생! LPUSH는 list 자료구조 명령
```

### 📌 키 존재 여부와 빈 키 처리 (Empty Key)

키가 존재하지 않을 때 조회나 삭제를 시도해도 에러가 발생하지 않고, **"마치 데이터가 없는 빈 키"**처럼 동작합니다.

```bash
# 1. 키 존재 여부 확인 (EXISTS)
DEL mylist
LPUSH mylist 1 2 3
EXISTS mylist        # 1 출력 (있음)

LPOP mylist
LPOP mylist
LPOP mylist
EXISTS mylist        # 0 출력 (없음, 아이템이 비어 자동 삭제됨)

# 2. 없는 키에 대한 동작 (에러 아님)
DEL mylist
LLEN mylist          # 0 출력 (길이 0 취급)
LPOP mylist          # nil 출력 (데이터 없음 취급)
```

---

## 🚨 2. Key 조회 및 패턴 검색 (주의!)

### 📍 기본 조회

- `EXISTS key [key ...]` : 키의 존재 여부를 확인합니다.

### 📍 패턴 매칭 (KEYS)

와일드카드를 사용하여 특정 패턴의 키를 검색할 수 있습니다.

- : 글자 수 상관없는 와일드카드 (예: `h*llo` → `hllo`, `hello`, `heello` 매칭)
- `?` : 1글자 와일드카드 (예: `h?llo` → `hello`, `hallo` 매칭)
- `[]` : 괄호 안의 문자 중 하나 매칭 (예: `h[ae]llo` → `hello`, `hallo` 매칭)
- `^` : 제외 (예: `h[^e]llo` → `hello` 제외)

```bash
KEYS * # 모든 Key 조회
KEYS user:* # user: 로 시작하는 모든 Key 조회
```

> **⛔️ KEYS 명령어 사용 시 주의사항 (매우 중요)**
> 
> - Redis는 **싱글 스레드(Single Thread)** 기반입니다.
> - 데이터가 많을 때(예: 100만 개) `KEYS`를 수행하면 모든 키를 찾을 때까지 **다른 커맨드가 차단(Block)**됩니다.
> - **위험성:** 대기열 증가, 서비스 장애, 헬스 체크 실패로 인한 의도치 않은 Failover 발생 가능.
> - **결론:** 운영 환경에서는 절대 `KEYS`를 사용하지 마세요.

### 📍 대안: SCAN

`KEYS` 대신 커서(Cursor) 기반으로 조금씩 나누어 조회하는 `SCAN`을 사용해야 합니다.

- **특징:** 실행 시간이 짧아 다른 명령을 차단하지 않습니다.
- **반환:** 다음 조회를 위한 `cursor` 위치와 키 목록(기본 10개)을 반환합니다.

```bash
# SCAN 구문
SCAN cursor [MATCH pattern] [COUNT count] [TYPE type]
```

---

## 🎒 3. 데이터 조작 및 관리 명령

### 📍 SORT (정렬)

`List`, `Set`, `Sorted Set` 내부의 아이템을 정렬하여 반환합니다.

- **기본:** 숫자로 취급하여 정렬.
- **ALPHA:** 문자열로 취급하여 정렬 (문자열 데이터일 경우 필수).
- **옵션:** `ASC`(오름차순), `DESC`(내림차순), `LIMIT`(개수 제한).

```bash
DEL mylist
LPUSH mylist a
LPUSH mylist b
LPUSH mylist c

SORT mylist          # 오류 발생! (문자열은 기본적으로 정렬 안 됨)

LPUSH mylist HELLO
SORT mylist alpha    # 정상 정렬됨 (문자열 모드 사용)
```

### 📍 RENAME (이름 변경)

키의 이름을 변경합니다. 변경하려는 이름이 이미 존재하면 덮어씌웁니다.

```bash
SET a apple
RENAME a aa
GET aa               # apple 출력
```

### 📍 COPY (복제)

키를 새로운 이름으로 복사합니다.

- **기본:** 목적지 키가 있으면 에러 발생.
- **REPLACE:** 목적지 키가 있어도 삭제하고 덮어씌움.

```bash
SET B BANANA
COPY B BB            # B를 BB로 복제
GET B
GET BB               # BANANA 출력
```

### 📍 TYPE (타입 확인)

해당 키가 어떤 자료구조인지 알려줍니다. (string, list, set 등)

```bash
TYPE mykey
```

---

## 🗑️ 4. 삭제 및 만료 관리

### 📍 데이터 삭제

- `DEL key`: 동기(Sync) 방식으로 키를 삭제합니다. (삭제되는 동안 블로킹 발생 가능)
- `UNLINK key`: **비동기(Async)** 방식으로 키와 데이터의 연결을 끊고, 실제 메모리 해제는 별도 스레드에서 수행합니다. (대용량 키 삭제 시 권장)
- `FLUSHALL [ASYNC | SYNC]`: Redis 내의 **모든 키**를 삭제합니다.

### 📍 TTL (Time To Live, 만료 시간)

키의 남은 유효 시간을 확인합니다.

```bash
TTL 키
```

- **양수:** 남은 시간 (초 단위)
- **1:** 유효 시간 없음 (무제한)
- **2:** 키가 존재하지 않음

---
