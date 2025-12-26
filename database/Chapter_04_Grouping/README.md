# 👬[DB] Grouping, Window Function & Advanced Techniques

## 1. 🔢 집계 함수 (Aggregate Function)

> 정의: 데이터를 그룹화하여 통계를 계산해주는 함수.
> 
> - **특징:** 숫자나 날짜 데이터에 주로 사용 (문자열은 `MIN`, `MAX` 가능).
> - **위치:** 그룹화 작업을 수행하므로 반드시 `GROUP BY` 절 뒤에 사용.
> - **NULL 처리:** 기본적으로 **NULL인 데이터를 제외**하고 연산 수행.

### 🔹 종류

- `SUM`: 합계
- `AVG`: 평균
- `MIN` / `MAX`: 최소값 / 최대값
- `COUNT`: 행의 개수
- `VAR_SAMP`: 분산
- `STDEV`: 표준편차

### 🔹 COUNT 함수 심화

| **함수 형태** | **설명** |
| --- | --- |
| **`COUNT(컬럼)`** | 해당 컬럼이 `NULL`이 아닌 행의 개수 |
| **`COUNT(*)`** | `NULL` 포함 모든 행의 개수 |
| **`COUNT(DISTINCT 컬럼)`** | 중복을 제거한 값의 개수 |

```sql
-- 1. COMM이 NULL이 아닌 데이터 개수
SELECT COUNT(COMM) 
FROM EMP;

--2. 전체 행의 개수
SELECT COUNT() 
FROM EMP;

-- 3. 부서(depart)의 종류 개수 (중복 제거)
SELECT COUNT(DISTINCT depart) 
FROM tStaff;
```

> 💡 [정보처리기사 기출 Point] Cardinality (카디널리티)
> 
> 
> **상황:** 인사팀(150명), 영업팀(200명), 총무팀(100명) 데이터 존재.
> 
> `SELECT COUNT(DISTINCT depart) FROM 테이블명;`
> 
> - **Q. 위 결과의 Cardinality는?**
> - **A. 1** (결과가 1행이 나오므로)
> - **해설:** Cardinality는 **행의 개수**를 의미하며, 이는 DB 성능(Join 등)에 큰 영향을 미칩니다.

### ⚠️ NULL 처리의 함정 (AVG)

`AVG` 함수 사용 시 NULL 처리 방식에 주의해야 합니다.

- **Case 1: NULL이 없는 경우 (`salary`)**
    - `AVG(salary)` == `SUM(salary)/COUNT(*)` (결과 일치)
- **Case 2: NULL이 있는 경우 (`score`)**
    - `AVG(score)`: NULL을 제외하고 평균 계산 (분모 감소)
    - `SUM(score)/COUNT(*)`: NULL을 개수에 포함하여 나눔 (분모 유지)
    - **결과 다름!**

**✅ 해결책 (NULL을 0으로 치환)**

```sql
-- 두 결과를 같게 하려면 IFNULL 사용
SELECT AVG(IFNULL(score, 0)) 
FROM tstaff;
```

---

## 2. 🔄 SQL 실행 순서 (Execution Order)

SQL은 작성 순서와 실제 실행 순서가 다릅니다. **이 순서를 알아야 쿼리 오류를 막을 수 있습니다.**

| **작성 순서** | **절 (Clause)** | **실행 순서** | **비고** |
| --- | --- | --- | --- |
| **1** | `SELECT` | **5** |  |
| **2** | `FROM` | **1** | 별칭(Alias) 정의 시점 |
| **3** | `WHERE` | **2** | **집계함수 사용 불가** |
| **4** | `GROUP BY` | **3** |  |
| **5** | `HAVING` | **4** | 집계함수 사용 가능 |
| **6** | `ORDER BY` | **6** | SELECT 별칭 사용 가능 |
| **7** | `LIMIT` / `OFFSET` | **7~8** |  |

> 🚫 주의사항
> 
> - `WHERE MAX(Salary)` ❌: WHERE절은 GROUP BY보다 먼저 실행되므로 집계함수 사용 불가.
> - `FROM`절의 별칭은 어디서든 사용 가능하지만, `SELECT`절의 별칭은 `WHERE`절에서 사용 불가.

---

## 3. 👥 GROUP BY & HAVING 절

데이터를 특정 기준(컬럼)으로 묶어서 통계를 내고 필터링합니다.

### 🔹 WHERE vs HAVING 차이

- **WHERE**: 그룹화 **전** 필터링 (집계함수 X)
- **HAVING**: 그룹화 **후** 필터링 (집계함수 O)

### 🔹 🚀 성능 최적화: Filtering 시점

**Q. 인사과와 영업부의 급여 최댓값을 구한다면?**

```sql
-- 방법 A: HAVING 사용 (그룹화 다 하고 거름)
SELECT depart, MAX(salary)
FROM tstaff
GROUP BY depart
HAVING depart IN ('인사과', '영업부');

-- 방법 B: WHERE 사용 (미리 거르고 그룹화) -> ⭐ 권장
SELECT depart, MAX(salary)
FROM tstaff
WHERE depart IN ('인사과', '영업부')
GROUP BY depart;
```

> 💡 Insight: 왜 WHERE가 더 좋은가? (MapReduce 원리)
> 
> - **순서:** `WHERE`가 먼저 실행됨.
> - **효율:** 불필요한 데이터를 미리 걸러내고(Filtering) 그룹화를 수행하므로 메모리 낭비가 적고 속도가 빠름.
> - **결론:** "걸러낼 수 있으면 **앞(WHERE)**에서 미리 걸러내자!" (옵티마이징의 기본)

---

## 4. 📈 고급 그룹화 기술 (Advanced Grouping)

### 4.1 🧾 WITH ROLLUP (중간/총 합계)

`GROUP BY`와 함께 사용하여 그룹별 소계(Subtotal)와 총계(Grand Total)를 한 번에 조회합니다.

- **특징:** 그룹핑된 컬럼의 값이 `NULL`로 표시되는 행이 합계 행입니다.

```sql
-- goodscd 별로 그룹화하여 qty 합계 조회 + 전체 총합 포함
SELECT goodscd, SUM(qty)
FROM order_d
GROUP BY goodscd WITH ROLLUP;
```

### 4.2 🔄 PIVOT (행 ➡️ 열 변환)

한 열에 포함된 여러 값(Rows)을 여러 열(Columns)로 변환하여 통계 테이블을 만드는 기법입니다.

**Step 1. 테이블 생성 및 데이터 입력**

```sql
CREATE TABLE pivotTest(
    uName CHAR(20),
    season CHAR(20),
    amount INT
);

INSERT INTO pivotTest VALUES 
('aespa', '겨울', 10), ('blackpink', '여름', 15), 
('aespa', '가을', 25), ('aespa', '봄', 3), 
('aespa', '봄', 37), ('blackpink', '겨울', 40), 
('aespa', '여름', 14), ('aespa', '겨울', 22), 
('blackpink', '여름', 64);
```

**Step 2. 피벗 쿼리 작성 (CASE문 또는 IF문 활용)**

- `uName`을 기준으로 그룹화하고, `season`의 값(봄, 여름, 가을, 겨울)을 컬럼으로 만듦.

```sql
SELECT uname, 
       SUM(IF(season = '봄', amount, 0)) AS '봄', 
       SUM(IF(season = '여름', amount, 0)) AS '여름', 
       SUM(IF(season = '가을', amount, 0)) AS '가을', 
       SUM(IF(season = '겨울', amount, 0)) AS '겨울', 
       SUM(amount) AS '합계'
FROM pivotTest
GROUP BY uname;
```

---

## 5. 🏆 WINDOW 함수 (순위 및 분석)

> 개요: 행과 행 사이의 관계를 정의하거나 순위를 매길 때 사용. (OVER 절 필수)
> 
> 
> 기본 형식: 함수명() OVER ([PARTITION BY 그룹] ORDER BY 정렬)
> 

### 5.1 순위 함수 (Ranking) 3대장 비교

`usertbl`에서 나이 순(`birthyear`)으로 순위 매기기

| **함수** | **특징** | **순위 예시 (동점자 처리)** |
| --- | --- | --- |
| **`ROW_NUMBER`** | **일련번호.** 동점자 있어도 무조건 1, 2, 3... | 1, 2, 3, 4, 5 |
| **`RANK`** | **공동 순위 O, 건너뜀 O.** (올림픽 방식) | 1, 2, **3, 3, 5**... |
| **`DENSE_RANK`** | **공동 순위 O, 건너뜀 X.** (빽빽한 순위) | 1, 2, **3, 3, 4**... |
| **`NTILE(N)`** | 전체 데이터를 **N등분**하여 그룹 번호 부여 | 1, 1, 2, 2, 3, 3 |

```sql
-- 1. 단순 순위 (전체 대상)
SELECT name, birthyear, ROW_NUMBER() OVER(ORDER BY birthyear ASC)
FROM usertbl;

-- 2. 그룹별 순위 (주소지 addr 별로 순위 매기기)
SELECT name, addr, ROW_NUMBER() OVER(PARTITION BY addr ORDER BY birthyear ASC)
FROM usertbl;

-- 3. 3등분 하기
SELECT name, birthyear, NTILE(3) OVER(ORDER BY birthyear ASC)
FROM usertbl;
```

### 5.2 분석 함수 (Analytic)

- **`LEAD(col, N)`**: 현재 행 기준 **다음 N번째** 행의 값
- **`LAG(col, N)`**: 현재 행 기준 **이전 N번째** 행의 값
- **`CUME_DIST`**: 누적 분포 (상위 몇 %인지 0~1 사이 값으로 반환)

```sql
-- 1. 다음 행과의 나이 차이 구하기
SELECT name, birthyear, birthyear  (LEAD(birthyear, 1) OVER(ORDER BY birthyear DESC)) AS diff_next
FROM usertbl;

-- 2. 누적 분포 (백분위)
SELECT name, birthyear, CUME_DIST() OVER(ORDER BY birthyear DESC) AS percentile
FROM usertbl;
```

---

## 6. 📚 참고 지식 (Deep Dive)

### 🧩 ORM (Object-Relational Mapping)

- **개념:** RDBMS를 프로그래밍 언어의 객체(Object)와 매핑하는 기술.
- **장점:** SQL 문법이 DB마다 달라도(Dialect) 코드 수정 없이 사용 가능. 유지보수 용이.
- **현황:** 생산성을 위해 널리 사용되나, 복잡한 쿼리 튜닝을 위해선 SQL 지식이 필수.
