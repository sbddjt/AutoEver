-- 1. 단순 순위 (전체 대상, ROW_NUMBER)
SELECT name, birthyear, ROW_NUMBER() OVER(ORDER BY birthyear ASC)
FROM usertbl;

-- 2. 그룹별 순위 (PARTITION BY 사용)
SELECT name, addr, ROW_NUMBER() OVER(PARTITION BY addr ORDER BY birthyear ASC)
FROM usertbl;

-- 3. 그룹 분할 (NTILE - 3등분)
SELECT name, birthyear, NTILE(3) OVER(ORDER BY birthyear ASC)
FROM usertbl;
