-- [문자열 함수 실습]

-- 1. CONCAT: 문자열 결합
-- 실무 Tip: 게시판 제목이 너무 길 경우 DB에서 잘라서 가져오기 (프론트엔드 처리 최소화)
SELECT CONCAT(LEFT(name, 3), ' . . . ') AS short_name
FROM user_tbl;

-- 2. UPPER / LOWER: 대소문자 변환
-- 검색 정확도를 높이기 위해 데이터를 대문자로 통일하여 비교
SELECT *
FROM EMP
WHERE UPPER(ename) = 'SCOTT';

-- 3. TRIM: 공백 제거
-- 입력 실수로 들어간 좌우 공백 제거
SELECT TRIM('  Hello  ') AS clean_text,
       LTRIM('  Hello')  AS left_clean,
       RTRIM('Hello  ')  AS right_clean;

-- 4. SUBSTRING: 문자열 추출
-- 날짜(문자열)에서 '년도'나 '월'만 필요할 때
-- 예: 2025-12-25 -> 12 (5번째 자리부터 2글자)
SELECT SUBSTRING('2025-12-25', 5, 2) AS month_part;
