# 📊[DB] MariaDB SELECT 문 기초 및 실습

## 1. SQL 실습 핵심 TIP 💡

- **효율적인 조건 필터링:** 성능 최적화를 위해 가능한 `WHERE` 절에서 먼저 데이터를 걸러내야 합니다. (`HAVING`은 그룹화 이후 필터링)
- **대소문자 구분:** `SELECT`, `FROM` 같은 예약어는 대소문자를 구분하지 않습니다.
- **데이터 구분:** MariaDB/MySQL은 기본적으로 `WHERE` 내 데이터 값의 대소문자를 구분하지 않으나, 필요 시 `BINARY` 설정을 통해 구분 가능합니다.
- **비절차적 언어:** SQL은 작성 순서대로 실행되지 않습니다. 
(**실행 순서: FROM → WHERE → SELECT**를 항상 유념!)
- **메모장 선작성 습관:** 사고 방지와 기록 관리를 위해 **메모장에 먼저 쿼리를 쓰고** 검토 후 DBMS에 옮겨 실행합니다. 📝
- **데이터의 가치:** 인프라는 복구 가능해도 **데이터는 유실되면 끝**입니다. 항상 신중하게 다뤄야 합니다. 💎

---

## 2. SELECT의 기본 형식과 데이터 조회 ⚙️

조회를 위한 가장 기본적인 SQL 구문이며, 테이블에서 원하는 컬럼을 선택해 가져옵니다.

### 1) 구문 형식

```sql
SELECT     [DISTINCT] * 또는 {컬럼이름 [별명]}  -- 조회할 컬럼
FROM       테이블이름 [새로운 이름]            -- 대상 테이블
[WHERE]    조건식                             -- 행 필터링
[GROUP BY] 그룹핑할 컬럼                       -- 데이터 그룹화
[HAVING]   그룹핑 후 조건                      -- 그룹 조건
[ORDER BY] 정렬할 컬럼 [ASC | DESC]           -- 결과 정렬
[LIMIT]    행 개수 [OFFSET 시작위치]           -- 출력 제한
```

### 2) 전체 및 특정 컬럼 조회 실습 💻

```sql
-- ① 테이블의 모든 컬럼을 조회할 때는 * 사용
SELECT *
FROM tCity;

-- ② 특정 컬럼(도시이름, 인구)만 나열하여 조회
SELECT name, popu
FROM tCity;

-- ③ 특정 컬럼(이름, 부서, 직급)만 조회
SELECT name, depart, grade
FROM tStaff;
```

---

## 3. SQL 실행 순서와 별명(Alias)의 관계 ⭐

쿼리는 작성 순서가 아닌 내부적인 절차에 따라 실행됩니다.

이 순서를 알아야 별명(Alias)의 사용 범위를 이해할 수 있습니다.

### 1) 실행 순서 (중요)

**FROM** ➔ **WHERE** ➔ **GROUP BY** ➔ **HAVING** ➔ **SELECT** ➔ **ORDER BY** ➔ **LIMIT**

### 2) SELECT 절에서의 별명(Alias) 활용

- **특징:** 결과 화면에 표시될 컬럼명을 변경할 수 있습니다.
    
    (`컬럼명 [AS] "별명"`)
    
- **주의:** 별명에 공백/특수문자가 있으면 **큰따옴표(" ")**가 필수입니다.
- **제약:** 별명은 **SELECT 단계 이후**에만 인식되므로, 이전 단계인 **WHERE 절에서는 사용할 수 없습니다.**

```sql
-- ✅ 올바른 별명 사용 (공백이 있으면 " " 필수)
SELECT name AS "도시 명"
FROM tCity;

-- ❌ 실행 순서에 따른 별명 오류 케이스
SELECT name AS "도시명"
FROM tCity
WHERE "도시명" = '부산';
-- 오류 발생 이유: WHERE 단계는 SELECT(별명 부여)보다
-- 먼저 실행되므로 '도시명'을 찾지 못함
```

---

## 4. 연산식 출력 및 별명 활용 🔢

컬럼 이름 대신 산술 연산(+, -, *, /, %)을 수행한 결과를 조회할 수 있습니다.

### 1) 연산식 실습

연산 결과의 컬럼명은 복잡해지기 때문에 가독성을 위해 반드시 **별명(Alias)**을 함께 사용하는 것이 좋습니다.

```sql
-- tCity 테이블에서 인구수(popu)에 10,000을 곱해 '인구'라는 별명으로 조회
SELECT name, popu  10000 AS "인구"
FROM tCity;

-- 단순 계산식 출력
SELECT 24 * 365;
```

---

## 5. 컬럼 연결 조회 (CONCAT) 🔗

`CONCAT()` 함수를 사용하여 컬럼 이름이나 문자열을 합쳐서 출력할 수 있습니다.

```sql
-- EMP 테이블에서 이름과 직무를 문장으로 연결
SELECT CONCAT(ENAME, " 님의 직무는 ", JOB) AS "직무 안내"
FROM EMP;
```

---

## 6. DISTINCT (중복 제거) 🚫

- `SELECT` 절에 한 번만 사용 가능합니다.
- 컬럼이 2개 이상이면 모든 컬럼의 값이 일치하는 경우만 제거됩니다.

```sql
-- ① region 중복 제거
SELECT DISTINCT region FROM tCity;
-- GROUP BY를 이용해서 중복을 제거
SELECT region FROM tCity GROUP BY region;

-- ② 두 컬럼 모두 같은 경우만 중복 제거
SELECT DISTINCT region, name FROM tCity;
```

---

## 7. 데이터 정렬 (ORDER BY) ↕️

데이터를 특정 기준에 따라 나열합니다. `ORDER BY` 절이 없으면 기본적으로 **기본키(Primary Key)** 순으로 조회됩니다.

- **ASC**: 오름차순 (기본값, 생략 가능)
- **DESC**: 내림차순
- **유연성**: 별명(Alias) 사용 가능, 컬럼 인덱스 번호 사용 가능(권장하지 않음).

```sql
-- ① 기본 정렬 (인구 오름차순)
SELECT * FROM tCity ORDER BY popu ASC;

-- ② 별칭 사용 가능 (ORDER BY는 SELECT 이후에 실행되므로 가능)
SELECT name, popu AS "인구수"
FROM tCity
ORDER BY 인구수 DESC;

-- ③ 인덱스 사용 (2번째 컬럼 기준 정렬)
SELECT name, popu FROM tCity ORDER BY 2 DESC;

-- ④ 정렬 기준에 없는 컬럼으로도 정렬은 가능하나 가독성을 위해 지양
SELECT name FROM tCity ORDER BY popu DESC;
```