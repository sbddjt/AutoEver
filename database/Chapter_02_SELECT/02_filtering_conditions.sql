-- 1. 기본 WHERE 조건절
SELECT name AS "도시명"
FROM tCity
WHERE name = "부산";

SELECT *
FROM tCity
WHERE name = "서울";

-- 2. 문자열 조건 및 Collation 변경 (대소문자 구분 등 필요시)
SELECT *
FROM tCity
WHERE metro = 'y';

-- (참고: Collation 변경 DDL은 필요시에만 실행)
-- ALTER TABLE tCity MODIFY metro VARCHAR(50) COLLATE utf8mb4_bin;

-- 3. NULL 값 확인
SELECT *
FROM tStaff
WHERE score IS NOT NULL;

-- 4. LIKE 연산자 (패턴 매칭)
-- '천'이 포함된 도시
SELECT *
FROM tCity
WHERE name LIKE '%천%';

-- 1981년으로 시작하는 입사일
SELECT *
FROM EMP
WHERE HIREDATE LIKE '1981%';

-- 이름이 3글자이며 가운데 글자가 '신'인 경우 (와일드카드 _)
SELECT *
FROM tStaff
WHERE name LIKE '__신%';

-- 이름이 정확히 4글자인 경우
SELECT *
FROM tStaff
WHERE name LIKE '____';

-- 5. IN 연산자 및 OR 조건
-- 목록에 포함된 지역 조회 (권장)
SELECT *
FROM tCity
WHERE region IN ('경상', '전라');

-- OR 연산자 사용 (위와 동일 결과)
SELECT *
FROM tCity
WHERE region = '경상' OR region = '전라';
