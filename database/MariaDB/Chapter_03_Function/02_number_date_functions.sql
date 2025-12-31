-- [수치 및 날짜 함수 실습]

-- 1. 수치 함수 (반올림, 올림, 내림)
SELECT ROUND(123.456, 2) AS rounded, -- 소수점 둘째 자리까지 반올림
       CEILING(123.1)    AS celing_val, -- 올림
       FLOOR(123.9)      AS floor_val;  -- 내림

-- 2. MOD: 나머지 연산
-- 활용: 사원 번호가 홀수인 사람만 조회 (데이터 샘플링 시 유용)
SELECT *
FROM EMP
WHERE MOD(EMPNO, 2) = 1;

-- 3. 날짜 함수
-- 현재 시간 조회
SELECT NOW(), SYSDATE();

-- 날짜 차이 계산 (DATEDIFF)
-- 입사일로부터 현재까지 며칠 지났는지 계산
SELECT ENAME, HIREDATE, DATEDIFF(NOW(), HIREDATE) AS work_days
FROM EMP;

-- 날짜 더하기/빼기
SELECT ADDDATE(NOW(), INTERVAL 10 DAY) AS after_10_days,
       SUBDATE(NOW(), INTERVAL 1 MONTH) AS month_ago;
