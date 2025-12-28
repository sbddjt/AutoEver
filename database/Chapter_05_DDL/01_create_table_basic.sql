-- -----------------------------------------------------
-- 1. 테이블 생성 실습 (CREATE)
-- 주제: 연락처(contact) 테이블 생성
-- 특징: MyISAM 엔진 사용(읽기 전용 최적화), utf8mb4(이모지 지원)
-- -----------------------------------------------------
CREATE TABLE contact (
    num INT AUTO_INCREMENT PRIMARY KEY,          -- 순번: 자동 증가 PK
    name VARCHAR(20),                            -- 이름: 가변 길이 (메모리 효율)
    address CHAR(100),                           -- 주소: 자주 변경됨 (고정 길이로 Row Migration 방지)
    tel VARCHAR(20),                             -- 전화번호: 변경 잦음
    email CHAR(100) COLLATE utf8mb4_bin,         -- 이메일: 대소문자 구분(bin) 필수
    birthday DATE                                -- 생일: 날짜 타입
) ENGINE = MyISAM AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8mb4;

-- -----------------------------------------------------
-- 2. 테이블 삭제 및 초기화
-- -----------------------------------------------------
-- 테이블의 모든 데이터 삭제 (구조는 유지, 로그 적게 남김, 속도 빠름)
TRUNCATE TABLE contact;

-- 테이블 완전 삭제 (구조까지 삭제, 복구 불가)
DROP TABLE contact;
