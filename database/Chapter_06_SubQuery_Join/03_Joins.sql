-- =====================================================
-- [Part 3-2] Advanced JOINs (ANSI Standard)
-- 내용: INNER JOIN, OUTER JOIN, MULTI JOIN (표준 문법)
-- =====================================================

-- -----------------------------------------------------
-- 1. ANSI INNER JOIN (표준 등가 조인)
-- -----------------------------------------------------
-- [ON 절 사용] - 가장 권장되는 방식
-- 설명: 조인 조건은 ON 절에, 데이터 필터링 조건은 WHERE 절에 분리하여 작성합니다.
SELECT *
FROM EMP INNER JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO;

-- [USING 절 사용]
-- 설명: 조인하려는 두 테이블의 컬럼명이 완벽히 같을 때 사용합니다.
-- 특징: 결과셋에서 조인된 컬럼(DEPTNO)이 중복되지 않고 한 번만 출력됩니다.
SELECT *
FROM EMP INNER JOIN DEPT
USING (DEPTNO);

-- -----------------------------------------------------
-- 2. OUTER JOIN (외부 조인)
-- -----------------------------------------------------
-- [LEFT OUTER JOIN]
-- 설명: 왼쪽 테이블(EMP)의 모든 데이터를 출력하고, 매칭되는 부서가 없으면 NULL로 표시합니다.
SELECT *
FROM EMP LEFT OUTER JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO;

-- [FULL OUTER JOIN 구현] (MariaDB 등 미지원 시)
-- 설명: LEFT JOIN과 RIGHT JOIN의 결과를 UNION으로 합쳐서 전체 데이터를 조회합니다.
SELECT * FROM EMP LEFT OUTER JOIN DEPT 
ON EMP.DEPTNO = DEPT.DEPTNO
UNION
SELECT *
FROM EMP RIGHT OUTER JOIN DEPT
ON EMP.DEPTNO = DEPT.DEPTNO;

-- -----------------------------------------------------
-- 3. MULTI JOIN (다중 조인)
-- -----------------------------------------------------
-- 설명: 3개 이상의 테이블을 연속적으로 연결할 때는 JOIN 구문을 나열하여 작성합니다.
-- 구조: 차량(CCAR) -> 제조사(TMAKER) -> 공장(tCity) 순서로 연결
SELECT *
FROM CCAR C 
INNER JOIN TMAKER M ON C.MAKER = M.MAKER
INNER JOIN tCity T ON M.factory = T.name;
