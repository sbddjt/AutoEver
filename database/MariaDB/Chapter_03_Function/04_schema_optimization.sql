-- [심화] 저장 구조 최적화: CHAR vs VARCHAR
-- 주제: Row Migration 방지와 저장 공간 효율성

CREATE TABLE t_optimization_test (
    id INT AUTO_INCREMENT PRIMARY KEY,
    
    -- 1. CHAR 사용 (고정 길이)
    -- 비밀번호(암호화된 해시값)나 코드값처럼 길이가 고정적인 경우
    -- 장점: 업데이트 시 길이가 변하지 않아 Row Migration이 발생하지 않음 (성능 유리)
    user_pw_hash CHAR(64), 
    country_code CHAR(2),

    -- 2. VARCHAR 사용 (가변 길이)
    -- 주소, 이름, 이메일처럼 길이가 들쑥날쑥한 경우
    -- 장점: 실제 데이터 길이만큼만 저장하므로 공간 효율적
    -- 단점: 잦은 수정으로 길이가 늘어나면 페이지 이동(I/O) 발생 가능성 있음
    address VARCHAR(100),
    email VARCHAR(50)
);
