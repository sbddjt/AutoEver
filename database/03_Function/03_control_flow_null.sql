-- [NULL 처리 및 제어 흐름]
-- Insight: 복잡한 비즈니스 로직은 백엔드(Java)에서 처리하는 추세지만,
-- NULL 처리만큼은 DB에서 확실하게 해주는 것이 좋음.

-- 1. IFNULL (Oracle의 NVL 대응)
-- 보너스(COMM)가 NULL이면 0으로 치환하여 계산 오류 방지
SELECT ENAME, 
       SAL + IFNULL(COMM, 0) AS total_salary
FROM EMP;

-- 2. NVL2 (Oracle 호환)
-- 식(COMM)이 NULL이 아니면 앞의 값, NULL이면 뒤의 값 반환
SELECT ENAME,
       NVL2(COMM, 'Bonus Exists', 'No Bonus') AS status
FROM EMP;

-- 3. IF 함수 (단일 분기)
-- 엑셀의 IF와 동일 구조
SELECT ENAME,
       SAL,
       IF(SAL >= 3000, 'High', 'Low') AS salary_grade
FROM EMP;

-- 4. CASE WHEN (다중 분기)
-- 직무에 따른 보너스율 차등 적용 예시
SELECT ENAME, JOB, SAL,
       CASE JOB
           WHEN 'ANALYST' THEN SAL * 1.2
           WHEN 'CLERK'   THEN SAL * 1.05
           ELSE SAL
       END AS adjusted_salary
FROM EMP;
