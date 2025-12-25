-- 1. 모든 컬럼 조회
SELECT * FROM tCity;

-- 2. 컬럼 별칭(Alias) 사용
SELECT name AS 도시명
FROM tCity;

-- 3. 별칭에 공백이나 특수문자가 있을 경우 따옴표 사용
SELECT name AS "도시명"
FROM tCity; -- (참고: WHERE절은 별도 필터링 파일로 이동)

-- 4. 연산 결과를 포함한 조회
SELECT name, popu * 10000 AS "인구"
FROM tCity;

-- 5. 단순 수치 연산 (Dual)
SELECT 24 * 65;

-- 6. 문자열 결합 (CONCAT 함수)
SELECT CONCAT(ENAME, " 님의 직무는 ", JOB) AS Employee_Info
FROM EMP;
