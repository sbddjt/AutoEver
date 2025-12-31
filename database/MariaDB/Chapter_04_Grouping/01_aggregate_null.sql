-- 1. COMM이 NULL이 아닌 데이터 개수
SELECT COUNT(COMM) 
FROM EMP;

-- 2. 전체 행의 개수
SELECT COUNT(*) 
FROM EMP;

-- 3. 부서(depart)의 종류 개수 (중복 제거 - Cardinality 확인)
SELECT COUNT(DISTINCT depart) 
FROM tStaff;

-- 4. NULL 처리의 함정 해결 (AVG 사용 시 NULL을 0으로 치환)
SELECT AVG(IFNULL(score, 0)) 
FROM tstaff;
