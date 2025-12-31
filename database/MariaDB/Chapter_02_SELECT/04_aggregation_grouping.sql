-- 1. 중복 제거 (DISTINCT)
SELECT DISTINCT region
FROM tCity;

SELECT DISTINCT region, name
FROM tCity;

-- 2. 그룹화 (GROUP BY)
SELECT region
FROM tCity
GROUP BY region;

-- 3. 개수 세기 (COUNT)
-- NULL을 제외한 COMM 컬럼의 개수
SELECT COUNT(COMM)
FROM EMP;

-- 전체 행의 개수
SELECT COUNT(*)
FROM EMP;

-- 중복을 제거한 부서의 개수
SELECT COUNT(DISTINCT depart)
FROM tStaff;

-- 4. 평균 및 합계 (AVG, SUM)
SELECT AVG(salary)
FROM tStaff;

-- 평균을 직접 계산 (합계 / 전체 수)
SELECT SUM(salary) / COUNT(*)
FROM tStaff;

-- 5. NULL 처리 후 집계 (IFNULL)
-- score가 NULL이면 0으로 치환하여 평균 계산
SELECT AVG(IFNULL(score, 0))
FROM tStaff;

-- NULL을 고려하지 않은 계산과 비교
SELECT SUM(score) / COUNT(*)
FROM tStaff;
