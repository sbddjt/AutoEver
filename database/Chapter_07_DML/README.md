# 🛠️ [DB] 7장 DML (Data Manipulation Language)

## 1. 📌 개요

- **정의**: 데이터 조작 언어.
- **분류**:
    - 예전에는 `SELECT`, `INSERT`, `DELETE`, `UPDATE` 4가지로 분류.
    - 최근에는 **SELECT**를 **DQL (Data Query Language)**로 분리하는 경우가 많음.
- **트랜잭션(Transaction)**:
    - `INSERT`, `DELETE`, `UPDATE`는 트랜잭션과 밀접한 관련이 있음 (데이터의 상태를 변화시킴).

---

## 2. 📥 데이터 삽입 (INSERT)

### 2.1 기본 형식

```sql
INSERT INTO 테이블이름 (필드 목록) VALUES (값을 나열);
```

- **Guide Line**:
    - **필드 목록 생략 시**: 모든 값을 테이블 생성 시 정의된 순서대로 대입해야 함.
    - **AUTO_INCREMENT**: 값을 생략하면 자동 일련번호 부여.
    - **DEFAULT**: 값을 생략하면 설정된 기본값 대입.
    - **그 외**: 값을 생략하면 `NULL` 대입.

**💻 실습 (tCity 테이블)**

> name, area, popu, metro, region으로 구성
> 

```sql
-- 필드 목록 명시
INSERT INTO tcity (name, area, popu, metro, region) VALUES ('목포', 22, 30, 'n', '전라');

-- 필드 목록 생략 (모든 값 순서대로)
INSERT INTO tcity VALUES ('마산', 35, 50, 'n', '경상');
```

### 2.2 다중 데이터 삽입

여러 개의 데이터를 한꺼번에 삽입할 때 사용합니다.

```sql
INSERT INTO 테이블이름 (필드목록) VALUES (값1..), (값2..);
```

**💻 실습**

```sql
INSERT INTO tcity VALUES ('울산', 95, 150, 'y', '경상'), ('창원', 55, 100, 'y', '경상');
```

### 2.3 SELECT 구문의 결과를 이용한 삽입

`VALUES` 대신 `SELECT` 구문을 사용하여 다른 테이블의 데이터를 복사해 넣습니다.

```sql
INSERT INTO tStaff(name, depart, gender, joindate, grade, salary, score)
SELECT name, region, metro, '20251229', '신입', area, popu
FROM tCity
WHERE region = '경기';
```

### 2.4 🏗️ SELECT 구문을 이용한 테이블 생성 (CTAS)

`CREATE TABLE ... AS SELECT` 구문을 사용합니다 (`AS` 생략 가능).

**1) 테이블 복사 (데이터 포함)**

DEPT 테이블의 모든 데이터를 소유하는 DEPT01 테이블 생성

```sql
CREATE TABLE DEPT01 AS
SELECT *
FROM DEPT;`
```

**2) 테이블 구조만 복사 (데이터 미포함)**

WHERE 절에 거짓 조건을 주어 데이터는 가져오지 않고 껍데기만 복사

```sql
CREATE TABLE DEPT02 AS
SELECT *
FROM DEPT
WHERE 0 = 1; -- 절대로 참일 수 없는 조건
```

### 2.5 ⚠️ INSERT IGNORE

여러 삽입 구문을 스크립트로 실행할 때, 중간에 오류가 발생해도 무시하고 계속 실행하게 합니다.

**🚫 일반적인 경우 (에러 발생)**

```sql
-- DEPT2 테이블 컬럼 크기보다 긴 문자열 입력 시도
INSERT INTO DEPT2 VALUES (10, '영업부', '서울');

-- 여기서 에러 발생 및 중단
INSERT INTO DEPT2 VALUES (20, '총무부', '서울시양천구목동삼성쉐르빌1동203호');

-- 실행 안 됨
INSERT INTO DEPT2 VALUES (30, '인사부', '서울');
```

**✅ IGNORE 사용 (에러 무시)**

```sql
INSERT IGNORE INTO DEPT2 VALUES (10, '영업부', '서울');
INSERT IGNORE INTO DEPT2 VALUES (20, '총무부', '서울시양천구목동삼성쉐르빌1동203호');
INSERT IGNORE INTO DEPT2 VALUES (30, '인사부', '서울');
```

> Note:
> 
> - 에러가 있어도 무시하고 다음 구문을 실행함.
> - 데이터 길이가 넘칠 경우, 들어갈 수 있는 만큼만 잘려서 들어감 (예: '...쉐르빌'까지만 저장).
> - **주의**: 테이블 구조와 맞지 않는 데이터를 강제로 넣는 것이므로 위험할 수 있음.

---

## 3. 🗑️ 데이터 삭제 (DELETE)

### 3.1 기본 형식

```sql
DELETE FROM 테이블이름
[WHERE 조건];
```

- **주의**: `WHERE` 절이 없으면 테이블의 **모든 데이터**가 삭제됩니다.

### 3.2 실습

**특정 조건 데이터 삭제**

```sql
-- DEPT2 테이블에서 DEPTNO가 10인 데이터 삭제
DELETE FROM DEPT WHERE DEPTNO = 10;
```

**모든 데이터 삭제**

```sql
DELETE FROM DEPT;
```

---

## 4. 🔄 데이터 수정 (UPDATE)

### 4.1 기본 형식

```sql
UPDATE 테이블이름
SET 수정할 내용 (컬럼 = 값, ...)
[WHERE 조건];
```

- **주의**: `WHERE` 조건이 없으면 테이블의 **모든 데이터**가 수정됩니다.

### 4.2 실습

**특정 데이터 수정**

```sql
-- DEPT1 테이블에서 DEPTNO가 10인 데이터의 LOC를 '제주', DNAME을 '비서실'로 수정
UPDATE DEPT1
SET LOC = '제주', DNAME = '비서실'
WHERE DEPTNO = 10;
```
