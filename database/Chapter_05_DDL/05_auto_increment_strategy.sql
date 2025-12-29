-- -----------------------------------------------------
-- 5. Auto Increment (일련번호 자동 생성) 실습
-- 주제: PK 자동 생성 원리, 번호 건너뛰기(Gap) 현상 이해, 초기값 변경
-- -----------------------------------------------------

-- 1. 테이블 생성 (Auto Increment 적용)
-- 특징: MySQL/MariaDB 전용 기능. PK 또는 Unique 컬럼에만 적용 가능.
DROP TABLE IF EXISTS tSale;

CREATE TABLE tSale (
    saleno INTEGER AUTO_INCREMENT PRIMARY KEY, -- 1부터 자동 증가
    customer VARCHAR(10),
    product VARCHAR(30)
);

-- [참고] 제약조건 명시적 정의 방식
-- CREATE TABLE tSale (
--     saleno INTEGER AUTO_INCREMENT,
--     customer VARCHAR(10),
--     product VARCHAR(30),
--     CONSTRAINT pk_tSale PRIMARY KEY(saleno)
-- );

-- -----------------------------------------------------
-- 2. 데이터 삽입 및 동작 확인
-- -----------------------------------------------------

-- saleno 컬럼은 자동 생성이므로 입력하지 않음 (또는 NULL 입력)
INSERT INTO tSale (customer, product) VALUES ('쥬니', '탁상캘린더');
INSERT INTO tSale (customer, product) VALUES ('군계', '러닝화');

-- 결과 확인: saleno가 1, 2로 생성됨
SELECT * FROM tSale;

-- -----------------------------------------------------
-- 3. 중간 데이터 삭제 시 번호 변화 (Gap 현상)
-- -----------------------------------------------------

-- 3-1. 데이터 추가
INSERT INTO tSale (customer, product) VALUES ('쥬니', '두부'); -- 3번 생성

-- 3-2. 방금 넣은 3번 데이터 삭제
DELETE FROM tSale WHERE product = '두부';

-- 3-3. 새로운 데이터 추가
INSERT INTO tSale (customer, product) VALUES ('쥬니', '사과');

-- [결과 확인]
-- 예상: 3번이 지워졌으니 다시 3번이 나올까?
-- 실제: 4번이 생성됨. (1, 2, 4 순서)
-- 이유: Auto Increment는 되돌아가지 않고 계속 전진하는 성질(Static)이 있음.
SELECT * FROM tSale;

-- -----------------------------------------------------
-- 4. Auto Increment 초기값 변경 (ALTER)
-- -----------------------------------------------------

-- 다음 번호부터는 100번부터 시작하도록 강제 설정
ALTER TABLE tSale AUTO_INCREMENT = 100;

INSERT INTO tSale (customer, product) VALUES ('헨리', '소주');

-- 결과: 1, 2, 4, 100 순서로 저장됨
SELECT * FROM tSale;

-- -----------------------------------------------------
-- 5. 마지막으로 생성된 ID 확인 (LAST_INSERT_ID)
-- -----------------------------------------------------
-- 방금 내가 INSERT 하면서 생성된 PK 값을 조회
-- 용도: 이 값을 가져와서 자식 테이블(상세 주문 등)에 FK로 넣을 때 사용
SELECT LAST_INSERT_ID();
