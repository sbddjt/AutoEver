-- -----------------------------------------------------
-- 무결성 제약조건 실습 (Integrity Constraints)
-- -----------------------------------------------------

-- 1. NOT NULL (필수 입력)
CREATE TABLE tNullable ( 
    name CHAR(10) NOT NULL, -- 필수 입력
    age INT                 -- NULL 허용
);

-- 2. CHECK (유효성 검사 - 도메인 무결성)
CREATE TABLE tCheckTable ( 
    gender CHAR(3) CHECK(gender = '남' OR gender = '여'), 
    origin CHAR(3) CHECK(origin IN ('동', '서', '남', '북')), 
    grade INT CHECK(grade >= 1 AND grade <= 5), 
    name CHAR(10) CHECK(name LIKE '박%') -- '박'씨만 입력 가능
);

-- 3. UNIQUE (중복 금지)
-- Case 1: 개별 컬럼 UNIQUE
CREATE TABLE tUniqueTest (
    name CHAR(10),
    area INT UNIQUE, 
    popu INT UNIQUE
);

-- Case 2: 복합 컬럼 UNIQUE (두 컬럼의 조합이 유일해야 함)
CREATE TABLE tUniqueTest2 (
    name CHAR(10),
    area INT,
    popu INT,
    CONSTRAINT uk_area_popu UNIQUE(area, popu) 
);

-- 4. PRIMARY KEY (기본키)
-- 테이블 레벨 정의 방식 (제약조건 이름 부여 가능)
CREATE TABLE tPKTest ( 
    name CHAR(10), 
    area INT, 
    popu INT, 
    CONSTRAINT PK_tPKTest PRIMARY KEY(name) -- 제약조건 명시
);

-- 5. DEFAULT (기본값 설정)
CREATE TABLE tEmployeeDefault (
    name CHAR(10) PRIMARY KEY,
    salary INT DEFAULT 0,    -- 입력 안 하면 0 자동 저장
    addr VARCHAR(30) NOT NULL
);
