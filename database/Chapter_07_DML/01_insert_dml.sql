/* ====================================================
   [DB] 7장 DML - 데이터 삽입 (INSERT) 실습
   내용: 기본 INSERT, 다중 삽입, INSERT SELECT, CTAS, IGNORE
   ==================================================== */

-- 1. 기본 INSERT (단일 행 삽입)
-- 1-1. 필드 목록을 명시하는 경우 (권장: 안전함)
-- 순서가 바뀌어도 컬럼명과 매칭되면 상관없음
INSERT INTO tCity (name, area, popu, metro, region) 
VALUES ('목포', 22, 30, 'n', '전라');

-- 1-2. 필드 목록 생략 (모든 컬럼 순서대로)
-- 테이블 생성 시 정의된 컬럼 순서를 정확히 알아야 함
INSERT INTO tCity 
VALUES ('마산', 35, 50, 'n', '경상');


-- 2. 다중 데이터 삽입 (Bulk Insert)
-- 한 번의 쿼리로 여러 행을 삽입하여 성능상 유리함
INSERT INTO tCity 
VALUES ('울산', 95, 150, 'y', '경상'), 
       ('창원', 55, 100, 'y', '경상');


-- 3. INSERT ... SELECT (서브쿼리를 이용한 삽입)
-- tCity 테이블에서 '경기' 지역 데이터를 조회하여 tStaff 테이블로 복사
-- 주의: SELECT 하는 컬럼의 개수와 데이터 타입이 INSERT 대상과 맞아야 함
INSERT INTO tStaff (name, depart, gender, joindate, grade, salary, score)
SELECT name, region, metro, '20251229', '신입', area, popu
FROM tCity
WHERE region = '경기';


-- 4. CTAS (Create Table As Select) - 테이블 생성과 동시에 데이터 복사
-- 4-1. 테이블 구조 + 데이터 전체 복사
CREATE TABLE DEPT01 AS
SELECT * FROM DEPT;

-- 4-2. 테이블 구조만 복사 (데이터 제외)
-- WHERE 조건에 '0=1' (거짓)을 주어 데이터는 조회되지 않게 함
CREATE TABLE DEPT02 AS
SELECT * FROM DEPT
WHERE 0 = 1;


-- 5. INSERT IGNORE (에러 무시)
-- 중간에 에러가 발생해도 중단하지 않고 다음 구문을 실행하거나,
-- 들어갈 수 있는 만큼만 잘라서 넣음 (Data Truncation)

-- 5-1. 정상 실행되는 구문
INSERT IGNORE INTO DEPT2 VALUES (10, '영업부', '서울');

-- 5-2. 에러 발생 가능 구문 (예: 컬럼 길이 초과)
-- IGNORE가 없다면 여기서 멈추지만, IGNORE 때문에 경고만 뜨고 넘어감
INSERT IGNORE INTO DEPT2 VALUES (20, '총무부', '서울시양천구목동삼성쉐르빌1동203호');

-- 5-3. 정상 실행
INSERT IGNORE INTO DEPT2 VALUES (30, '인사부', '서울');
