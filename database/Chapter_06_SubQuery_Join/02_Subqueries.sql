-- =====================================================
-- [Part 2] SUBQUERY (서브쿼리)
-- 내용: 단일 행, 다중 열, 다중 행(IN, ANY, ALL, EXISTS) 실습
-- =====================================================

-- -----------------------------------------------------
-- 1. 단일 행 서브쿼리 (Single Row)
-- -----------------------------------------------------
-- 설명: 서브쿼리의 결과가 단 하나의 값(Scalar)인 경우입니다.
-- 예제: 인구수가 가장 많은 도시의 이름을 조회합니다.
SELECT name
FROM tCity
WHERE popu = (SELECT MAX(popu) FROM tCity);

-- 예제: 전체 사원의 평균 급여보다 많이 받는 사원을 조회합니다.
SELECT ENAME, SAL
FROM EMP
WHERE SAL >= (SELECT AVG(SAL) FROM EMP);

-- -----------------------------------------------------
-- 2. 다중 열 서브쿼리 (Multi Column / Pairwise)
-- -----------------------------------------------------
-- 설명: 서브쿼리가 두 개 이상의 컬럼을 반환하며, 이를 쌍(Pair)으로 비교합니다.
-- 예제: '안중근'과 부서(DEPART) 및 성별(GENDER)이 모두 동일한 직원을 조회합니다.
SELECT *
FROM tStaff
WHERE (DEPART, GENDER) = (SELECT DEPART, GENDER FROM tStaff WHERE NAME = '안중근');

-- -----------------------------------------------------
-- 3. 다중 행 서브쿼리 (Multi Row)
-- -----------------------------------------------------
-- Case 1: IN 연산자 (OR 조건과 유사)
-- 설명: 부서별 최대 급여와 일치하는 급여를 가진 사원을 조회합니다.
-- 주의: 서브쿼리 결과가 여러 행이므로 '=' 연산자는 사용할 수 없습니다.
SELECT EMPNO, ENAME, SAL, DEPTNO 
FROM EMP
WHERE SAL IN (SELECT MAX(SAL) FROM EMP GROUP BY DEPTNO);

-- Case 2: ALL 연산자 (AND 조건과 유사)
-- 설명: 30번 부서의 모든 사원들보다 급여가 더 높은 사원을 조회합니다.
-- 의미: 30번 부서의 '최대 급여'보다 높아야 한다는 뜻과 같습니다.
SELECT ENAME, SAL 
FROM EMP
WHERE SAL > ALL (SELECT SAL FROM EMP WHERE DEPTNO = 30);

-- (참고) 위와 동일한 결과를 내는 단일행 변환 쿼리 (MAX 활용)
SELECT ENAME, SAL 
FROM EMP
WHERE SAL > (SELECT MAX(SAL) FROM EMP WHERE DEPTNO = 30);

-- Case 3: EXISTS 연산자 (존재 여부 확인)
-- 설명: 급여가 3000을 넘는 직원이 한 명이라도 존재한다면 쿼리를 실행합니다.
-- 특징: 데이터의 실제 값보다는 존재 여부(TRUE/FALSE)만을 판단할 때 효율적입니다.
SELECT ENAME, SAL 
FROM EMP
WHERE EXISTS (SELECT 1 FROM EMP WHERE SAL > 3000);
