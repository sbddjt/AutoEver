-- 1. 오름차순 정렬 (ASC)
SELECT *
FROM tCity
ORDER BY popu ASC;

-- 2. 컬럼 순번을 이용한 내림차순 정렬 (DESC)
-- 두 번째 컬럼(popu) 기준으로 내림차순
SELECT name, popu AS "인구수"
FROM tCity
ORDER BY 2 DESC;

-- 3. 상위 N개 레코드 조회 (LIMIT)
-- 면적이 넓은 순서대로 상위 4개
SELECT *
FROM tCity
ORDER BY area DESC
LIMIT 4;

-- 4. 페이징 처리 (LIMIT & OFFSET)
-- 면적 순위 3등부터 3개 조회 (앞에 2개 건너뜀)
SELECT *
FROM tCity
ORDER BY area DESC
LIMIT 3 OFFSET 2;
