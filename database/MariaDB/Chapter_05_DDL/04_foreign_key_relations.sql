-- -----------------------------------------------------
-- 참조 무결성 (Foreign Key) 및 관계 설정
-- -----------------------------------------------------

-- 1. 부모 테이블 생성 (직원)
CREATE TABLE tEmployee ( 
    name CHAR(10) PRIMARY KEY, 
    salary INT NOT NULL, 
    addr VARCHAR(30) NOT NULL
);

-- 2. 자식 테이블 생성 (프로젝트) - FK 설정 포함
-- ON DELETE CASCADE: 부모(직원)가 삭제되면 자식(프로젝트)도 자동 삭제
CREATE TABLE tProject ( 
    projectID INT PRIMARY KEY, 
    name CHAR(10), 
    project VARCHAR(30) NOT NULL, 
    cost INT, 
    CONSTRAINT FK_emp FOREIGN KEY(name) REFERENCES tEmployee(name) ON DELETE CASCADE
);

-- -----------------------------------------------------
-- 테스트 데이터 삽입
-- -----------------------------------------------------
INSERT INTO tEmployee VALUES ('아이린', 500, '대구');
INSERT INTO tEmployee VALUES ('배수지', 700, '광주');

-- 정상 입력 (부모에 '배수지'가 있으므로 성공)
INSERT INTO tProject VALUES (1, '배수지', '광주콘서트', 5000);

-- -----------------------------------------------------
-- 무결성 위배 및 CASCADE 테스트
-- -----------------------------------------------------

-- [Error Case] 존재하지 않는 부모 참조
-- '카리나'는 tEmployee에 없으므로 에러 발생 (Error Code: 1452)
-- INSERT INTO tProject VALUES (2, '카리나', '서울콘서트', 3000);

-- [CASCADE Check] 부모 데이터 삭제
-- '배수지'를 삭제하면 tProject의 '광주콘서트' 데이터도 같이 사라짐
DELETE FROM tEmployee WHERE name = '배수지';
