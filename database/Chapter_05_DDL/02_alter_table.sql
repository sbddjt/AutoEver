-- -----------------------------------------------------
-- 테이블 구조 변경 (ALTER) 실습
-- -----------------------------------------------------

-- 1. 컬럼 추가 (ADD)
-- age 컬럼(정수형)을 테이블 맨 뒤에 추가
ALTER TABLE contact ADD age INT;

-- 2. 컬럼 삭제 (DROP)
-- age 컬럼 삭제
ALTER TABLE contact DROP age;

-- 3. 컬럼 변경 (CHANGE: 이름 + 타입)
-- tel 컬럼의 이름을 phone으로 바꾸고 타입을 INT로 변경
ALTER TABLE contact CHANGE tel phone INT;

-- 4. 컬럼 속성 변경 (MODIFY: 타입 + 제약조건)
-- name 컬럼을 5글자 고정(CHAR), NULL 입력 불가로 변경
ALTER TABLE contact MODIFY name CHAR(5) NOT NULL;

-- 5. 컬럼 위치 변경
-- phone 컬럼을 email 컬럼 뒤로 이동
ALTER TABLE contact MODIFY COLUMN phone INT AFTER email;

-- 6. 테이블 이름 변경 (RENAME)
ALTER TABLE contact RENAME contact1;

-- 7. 테이블 주석(Comment) 추가
ALTER TABLE contact COMMENT = '고객 연락처 정보';
