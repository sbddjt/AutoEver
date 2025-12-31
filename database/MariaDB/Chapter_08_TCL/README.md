# 🧱 [DB] Transaction & TCL

## 1. 📌 Transaction (트랜잭션) 개요

### 1.1 정의 및 목적

- **정의**: 데이터베이스 작업의 **논리적인 단위** (Logical Unit of Work).
    - SQL 문장 하나하나가 아니라, 작업을 묶은 단위가 중요함.
- **목적**: 데이터의 **일관성(Consistency)**을 유지하기 위해 도입.

### 1.2 트랜잭션의 성질 (ACID)

데이터베이스의 안정성을 보장하기 위한 4가지 핵심 성질입니다.

1. **Atomicity (원자성)**
    - **ALL OR NOTHING**: 트랜잭션 내의 모든 연산은 모두 수행되거나, 아예 수행되지 않아야 함.
2. **Consistency (일관성)**
    - 트랜잭션 수행 전과 수행 후의 데이터 상태가 일관되어야 함. (제약조건 위배 등 금지)
3. **Isolation (격리성)**
    - 현재 수행 중인 트랜잭션은 다른 트랜잭션의 연산에 끼어들거나 영향을 받으면 안 됨.
4. **Durability (영속성)**
    - 한 번 완료(Commit)된 트랜잭션의 결과는 시스템이 고장 나더라도 영원히 반영되어야 함.

---

## 2. 🏗️ 임시 작업 영역 (Temporary Workspace)

데이터베이스의 변경 작업은 디스크(원본)에 바로 쓰는 것이 아니라, 메모리 상의 **임시 작업 영역**에서 먼저 이루어집니다.

- **작동 원리**:
    - 데이터베이스는 실행한 결과를 임시 영역에 기억하거나, 로그(Log)로 기록합니다.
    - **비유**: 파워포인트(PPT) 작업 시 복사본(임시 파일)에서 작업하다가, '저장' 버튼을 눌러야 원본에 반영되는 것과 유사함.
- **효과**: 이 임시 작업 영역 덕분에 `ROLLBACK`(되돌리기)이 가능하며, 트랜잭션의 일관성이 유지됩니다.

---

## 3. 🎮 관련 명령어 (TCL)

| **명령어** | **설명** | **비고** |
| --- | --- | --- |
| **COMMIT** | 작업 완료 | 임시 영역의 데이터를 원본(DB)에 영구 저장 |
| **ROLLBACK** | 작업 취소 | 임시 영역의 작업을 취소하고 마지막 커밋 시점으로 복귀 |
| **SAVEPOINT** | 중간 저장점 | 전체 취소가 아닌 특정 지점까지만 롤백하기 위한 마킹 |

---

## 4. ⚖️ COMMIT과 ROLLBACK 되는 상황

### 4.1 ✅ COMMIT 되는 상황 (영구 저장)

1. **명시적 수행**: 사용자가 `COMMIT` 명령어를 직접 입력한 경우.
2. **DDL / DCL 수행**: `CREATE`, `ALTER`, `DROP`, `GRANT` 등의 구문 실행 시.
    - *주의*: DDL/DCL은 기본적으로 Auto Commit 속성을 가짐 (되돌릴 수 없음).
3. **정상 종료**: 데이터베이스 접속 도구(Client)가 정상적으로 종료된 경우.

### 4.2 🔙 ROLLBACK 되는 상황 (취소)

1. **명시적 수행**: 사용자가 `ROLLBACK` 명령어를 직접 입력한 경우.
2. **비정상 종료**: 정전, 컴퓨터 다운, 접속 도구의 강제 종료 등.

---

## 5. 💻 트랜잭션 모드 및 실습

### 5.1 트랜잭션 모드

- **자동(Auto Commit)**: SQL 문장을 수행할 때마다 자동으로 Commit 됨 (편리하나 위험).
- **수동(Manual Commit)**: 명시적으로 `COMMIT`을 수행해야만 저장됨 (실무 권장).

### 5.2 실습 시나리오

> 실습을 위해 DEPT 테이블을 복사한 DEPTCOPY 생성
> 

```sql
CREATE TABLE DEPTCOPY AS
SELECT * FROM DEPT;
```

### Case 1: 데이터 삽입 후 ROLLBACK

```sql
-- 1. 데이터 삽입
INSERT INTO DEPTCOPY VALUES (50, '비서', '서울');

-- 2. 확인 (내 세션에서는 보임)
SELECT * FROM DEPTCOPY;

-- 3. 롤백 수행
ROLLBACK;

-- 4. 결과 확인
SELECT * FROM DEPTCOPY;
-- 결과: 50번 데이터 사라짐 (Manual 모드였으므로 취소됨)
```

### Case 2: 데이터 삽입 후 COMMIT 하고 ROLLBACK

```sql
-- 1. 데이터 삽입
INSERT INTO DEPTCOPY VALUES (50, '비서', '서울');

-- 2. 커밋 수행 (영구 저장)
COMMIT;

-- 3. 롤백 수행
ROLLBACK;

-- 4. 결과 확인
SELECT * FROM DEPTCOPY;
-- 결과: 50번 데이터 존재함 (이미 Commit 했으므로 Rollback 영향 없음)
```

### Case 3: 데이터 삽입 후 DDL 수행 (Auto Commit 주의)

```sql
-- 1. 데이터 삽입
INSERT INTO DEPTCOPY VALUES (60, '비서', '서울');

-- 2. DDL 수행 (TRUNCATE: 테이블 내용 비우기)
TRUNCATE TABLE DEPTCOPY;
-- ⚠️ DDL은 수행되는 순간 앞선 작업까지 강제로 COMMIT 해버림

-- 3. 롤백 수행
ROLLBACK;

-- 4. 결과 확인
SELECT * FROM DEPTCOPY;
-- 결과: 데이터가 복구되지 않음 (DDL에 의해 Auto Commit 됨)`
```

### Case 4: SAVEPOINT 사용

```sql
-- 1. 70번 삽입
INSERT INTO DEPTCOPY VALUES (70, '비서', '서울');

-- 2. 저장점 S1 설정
SAVEPOINT S1;

-- 3. 80번 삽입
INSERT INTO DEPTCOPY VALUES (80, '비서', '서울');

-- 4. S1 지점으로 롤백
ROLLBACK TO S1;

-- 5. 결과 확인
SELECT * FROM DEPTCOPY;
-- 결과: 70번은 남아있고, 80번만 취소됨.`
```

<aside>
💡

SAVEPOINT 기능은 DB에 따라 안되는 경우도 있음.

유료버전에만 사용가능 할 수도

</aside>

---

### 💡 Insight & Tips

- **성능 vs 안정성**:
    - `COMMIT`을 너무 자주 하면: 디스크 I/O가 잦아져 작업 속도가 느려짐.
    - `COMMIT`을 너무 적게 하면: 문제 발생 시 `ROLLBACK` 해야 할 범위가 너무 커짐.
    - **해결**: 적절한 단위로 묶어서 `COMMIT` 하거나 중간중간 `SAVEPOINT`를 활용.
- **개발 환경 설정**:
    - 나중에 DB 연동 App 개발 시, 프레임워크가 **Auto Commit**인지 **Manual Commit**인지 반드시 확인해야 함.
    - **DBeaver**: 기본값이 Auto Commit임. 실습 시에는 `Manual Commit` (Connection type: None)으로 변경하여 트랜잭션 제어를 연습하는 것이 좋음.
