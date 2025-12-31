# 🗄️ [DB] SQL Advanced: Set, Subquery & Join

## 1. ➕ SET OPERATOR (집합 연산자)

### 1) 📌 개요

- **정의**: 2개 이상의 테이블에서 데이터를 추출하여 결합하는 연산.
- **특징**: 여러 개의 `SELECT` 문장을 결합해서 결과를 얻어냄.
- **기본 형식**:

```sql
SELECT 구문
SET operator
SELECT 구문;
```

### 2) 📏 Guide Line (작성 규칙)

- **열 매칭**: 첫 번째 SELECT 구문과 두 번째 SELECT 구문의 열 개수와 자료형이 일치해야 함.
- **테이블**: 대상 테이블은 달라도 상관없음.
- **컬럼명**: 최종 출력되는 컬럼명은 **첫 번째 SELECT 구문**의 것을 따름.
- **정렬(ORDER BY)**: 문장의 맨 마지막에 **한 번만** 기술 가능.
- **🚫 사용 제한**: 대용량 파일(`BLOB`, `CLOB`, `BFILE`, `LONG`) 컬럼에는 사용 불가 (시스템 부하).

### 3) 🧮 연산자 종류

| **연산자** | **설명** | **특징** |
| --- | --- | --- |
| **UNION** | 합집합 | **중복 제거** |
| **UNION ALL** | 합집합 | **중복 포함** (속도 빠름) |
| **INTERSECT** | 교집합 | 양쪽 모두 존재하는 데이터 |
| **EXCEPT** | 차집합 | 한쪽에만 존재하는 데이터 |

### 4) 💻 실습 (EMP & DEPT)

> 데이터 전제: EMP (10, 20, 30 부서 존재), DEPT (10, 20, 30, 40 부서 존재)
> 

**① UNION (중복 제거)**

```sql
-- DISTINCT 불필요 (기본적으로 중복 제거됨)
SELECT DEPTNO 
FROM EMP
UNION
SELECT DEPTNO 
FROM DEPT;
-- 결과: 10, 20, 30, 40`
```

**② UNION ALL (중복 포함)**

```sql
SELECT DEPTNO FROM EMP
UNION ALL
SELECT DEPTNO FROM DEPT;
-- 결과: 10, 20, 30, 10, 20, 30, 40 (전체 출력)
```

**③ INTERSECT (교집합)**

```sql
SELECT DEPTNO FROM EMP
INTERSECT
SELECT DEPTNO FROM DEPT;
-- 결과: 10, 20, 30
```

**④ EXCEPT (차집합)**

```sql
-- EMP에는 있고 DEPT에는 없는 것 (없음)
SELECT DEPTNO 
FROM EMP 
EXCEPT 
SELECT DEPTNO 
FROM DEPT;

-- DEPT에는 있고 EMP에는 없는 것 (40 출력)
SELECT DEPTNO 
FROM DEPT 
EXCEPT 
SELECT DEPTNO 
FROM EMP;
```

---

## 2. 🔍 SUBQUERY (서브쿼리)

### 1) 📝 개요

- **정의**: 하나의 Query 안에 존재하는 또 다른 Query.
    - 포함하는 쿼리: **Main Query**
    - 포함된 쿼리: **Sub Query**
- **사용 위치**: `SELECT`, `FROM`, `WHERE`, `HAVING`, `INSERT`, `UPDATE`, `DELETE` 등.
- **규칙**: 연산자 오른쪽에 기술하며, 반드시 **괄호 `()`*로 감싸야 함.
- **실행 순서**: Main Query 실행 전 **한 번만 먼저 실행**됨.
- **분류**:
    - `FROM` 절 사용: **INLINE VIEW**
    - 그 외: 단일 행 / 다중 행 서브쿼리

### 2) ☝️ 단일 행 서브쿼리

- **특징**: 결과가 하나의 값(Scalar).
- **연산자**: `=`, `>`, `<`, `>=`, `<=`, `!=` 등 단일행 연산자 사용.

**[예제] 인구수(popu)가 최대인 도시 이름 조회**

```sql
-- ❌ 잘못된 방식 (표준 SQL 에러)
SELECT MAX(popu), NAME 
FROM tCity;
-- MariaDB에서는 에러는 안 나지만, 엉뚱한 매칭 결과(부산) 출력.- ✅ 서브쿼리 활용

SELECT name
FROM tCity
WHERE popu = (SELECT MAX(popu) FROM tCity);
-- 결과: 서울 (정확한 매칭)
```

**[예제] 평균 급여 이상인 사원 조회**

```sql
SELECT ENAME, SAL
FROM EMP
WHERE SAL >= (SELECT AVG(SAL) FROM EMP);
```

### 3) ✌️ 다중 열 서브쿼리

- **특징**: 서브쿼리 결과가 2개 이상의 열(Column)인 경우.
- **Pairwise 비교**: 두 컬럼을 묶어서 한 번에 비교 가능.

```sql
-- 안중근과 부서, 성별이 동일한 사람 조회
SELECT *
FROM tStaff
WHERE (DEPART, GENDER) = (SELECT DEPART, GENDER FROM tStaff WHERE NAME = '안중근');
```

### 4) 📚 다중 행 서브쿼리

- **특징**: 결과 행이 2개 이상.
- **주의**: 단일행 연산자 사용 불가 (`=` 등 사용 시 에러).

| **연산자** | **설명** |
| --- | --- |
| **IN** | 목록 중 하나와 일치 (OR 조건) |
| **ANY / SOME** | 목록 중 **하나라도** 만족하면 리턴 (MIN/MAX 비교와 유사) |
| **ALL** | 목록 **모두** 만족해야 리턴 |
| **EXISTS** | 데이터 존재 여부만 확인 (TRUE/FALSE) |

**[실습] 부서별 최대 급여자와 일치하는 사원 (IN)**

```sql
--❌ 에러: Subquery returns more than 1 row (= 사용 불가)
SELECT EMPNO, ENAME, SAL, DEPTNO 
FROM EMP
WHERE SAL = (SELECT MAX(SAL) FROM EMP GROUP BY DEPTNO);

-- ✅ 해결: IN 사용
SELECT EMPNO, ENAME, SAL, DEPTNO 
FROM EMP
WHERE SAL IN (SELECT MAX(SAL) FROM EMP GROUP BY DEPTNO);
```

**[실습] 30번 부서의 모든 사원보다 급여가 큰 사원 (ALL)**

```sql
-- 방법 1: ALL 사용
SELECT ENAME, SAL 
FROM EMP
WHERE SAL > ALL (SELECT SAL FROM EMP WHERE DEPTNO = 30);

-- 방법 2: MAX 사용 (단일행 변환)
SELECT ENAME, SAL 
FROM EMP
WHERE SAL > (SELECT MAX(SAL) FROM EMP WHERE DEPTNO = 30);
```

**[실습] 존재 여부 확인 (EXISTS)**

```sql
-- SAL > 3000인 데이터가 존재하면 실행
SELECT ENAME, SAL 
FROM EMP
WHERE EXISTS (SELECT 1 FROM EMP WHERE SAL > 3000);
```

---

## 3. 🤝 JOIN (조인)

### 1) 📌 개요

- **정의**: 2개 이상의 테이블을 합쳐서 하나의 테이블로 만드는 작업.
- **특징**: 동일한 테이블끼리 조인도 가능(Self Join). 정규화로 분리된 데이터를 연결하여 조회할 때 필수.

### 2) 📋 종류

- **CROSS JOIN**: 모든 경우의 수 조합 (Cartesian Product).
- **EQUI JOIN**: `=` 연산자 사용.
- **NON EQUI JOIN**: `=` 이외의 연산자(`BETWEEN` 등) 사용.
- **OUTER JOIN**: 일치하지 않는 데이터도 포함.
- **SELF JOIN**: 자기 자신과 조인.
- **SEMI JOIN**: 서브쿼리를 이용한 조인.

### 3) ✖️ CROSS JOIN

- **개요**: 조건 없이 양쪽 테이블의 모든 행을 결합.
- **결과**: 행 개수 = A행 × B행 (시스템 부하 주의).

```sql
SELECT * 
FROM emp, dept;
```

### 4) 🔗 EQUI JOIN (등가 조인)

- **개요**: 동일한 의미를 갖는 컬럼을 `=`로 연결.
- **주의**: 컬럼명이 같을 경우 반드시 **`테이블명.컬럼명`*으로 명시해야 함 (Ambiguous Error).

```sql
-- ❌ 에러 (deptno가 모호함)
SELECT *
FROM EMP, DEPT 
WHERE emp.deptno = dept.deptno;

-- ✅ 정상 (테이블명 명시)
SELECT ename, dname
FROM emp, dept
WHERE emp.deptno = dept.deptno AND ename = 'MILLER';
```

> 👨‍🏫 Insight: JOIN vs SUBQUERY (성능 최적화)
> 
> - **조회 컬럼이 여러 테이블에 분산됨** 👉 **JOIN** 필수.
> - **조회 컬럼이 한 테이블에만 있음** 👉 **SUBQUERY** 권장.
>     - *이유*: JOIN은 테이블을 합쳐 메모리에 올린 뒤 필터링하므로 느릴 수 있음. Subquery는 먼저 걸러내고 조회하므로 메모리 효율이 좋음.
> - **정규화의 역설**: 테이블을 쪼갤수록 데이터 무결성은 좋아지지만, 빈번한 JOIN으로 **READ 속도**는 떨어짐. (NoSQL, 반정규화 등으로 해결)

### 5) 🏷️ Alias (테이블 별칭)

- 테이블 이름이 길거나 Self Join 시 필수.

```sql
SELECT ename
FROM emp e, dept d
WHERE e.deptno = d.deptno AND loc = 'DALLAS';
```

### 6) 📏 NON EQUI JOIN

- **개요**: `=`이 아닌 범위(`BETWEEN`) 등으로 조인.
- **예시**: 급여 등급표(SALGRADE) 참조.

```sql
SELECT ename, sal, grade
FROM emp, salgrade
WHERE emp.sal BETWEEN losal AND hisal;
```

### 7) 🔄 SELF JOIN

- **개요**: 동일 테이블을 두 번 참조. (예: 사원과 관리자)
- **필수**: 반드시 서로 다른 별칭(Alias)을 사용해야 함.

```sql
-- 사원(e1)의 관리자(e2) 이름 조회
SELECT e1.ename AS 사원, e2.ename AS 관리자
FROM emp e1, emp e2
WHERE e1.mgr = e2.empno;
```

### 8) 🇺🇸 ANSI JOIN (표준 문법)

- **특징**: 조인 조건(`ON`)과 필터링 조건(`WHERE`)을 분리하여 가독성 향상.
- **종류**:
    - **CROSS JOIN**: `SELECT * FROM emp CROSS JOIN dept;`
    - **INNER JOIN**: EQUI JOIN 대체.

**① ON 절 사용 (가장 권장)**

```sql
SELECT *
FROM EMP INNER JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO;
```

**② USING 절 (컬럼명 같을 때)**

```sql
-- 조인된 컬럼(DEPTNO)은 한 번만 출력됨
SELECT *
FROM EMP INNER JOIN DEPT
USING (DEPTNO);
```

**③ NATURAL JOIN**

```sql
-- 이름이 같은 모든 컬럼 자동 조인 (위험할 수 있음)
SELECT *
FROM EMP NATURAL JOIN DEPT;
```

### 9) 🌓 OUTER JOIN

- **개요**: 한쪽에만 존재하는 데이터도 출력.
- **종류**:
    - `LEFT OUTER JOIN`: 왼쪽 테이블 데이터 모두 출력.
    - `RIGHT OUTER JOIN`: 오른쪽 테이블 데이터 모두 출력.
    - `FULL OUTER JOIN`: 양쪽 모두 출력 (MariaDB 미지원 → UNION으로 구현).

```sql
-- LEFT OUTER JOIN (부서 없는 사원도 출력)
SELECT *
FROM EMP LEFT OUTER JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO;

-- FULL OUTER JOIN 구현 (UNION 활용)
SELECT * 
FROM EMP LEFT OUTER JOIN DEPT 
ON EMP.DEPTNO = DEPT.DEPTNO
**UNION**
SELECT *
FROM EMP RIGHT OUTER JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO;
```

### 10) ⛓️ 다중 조인

- **개요**: 3개 이상의 테이블 연결.
- **방법**: JOIN을 연속해서 사용.

```sql
SELECT *
FROM CCAR C 
INNER JOIN TMAKER M ON C.MAKER = M.MAKER
INNER JOIN tCity T ON M.factory = T.name;
```
