/* ====================================================
   [1. ROLLBACK 실습]
   목표: 작업을 수행했지만, 문제 발생 또는 변심으로 인해
        원래 상태로 되돌리는 과정을 이해합니다.
   ==================================================== */

-- [Step 1] 테이블 상태 확인 (초기 상태)
SELECT * FROM DEPTCOPY;

-- [Step 2] 데이터 조작 (INSERT)
-- 50번 부서 '개발팀' 추가 (아직 메모리에만 존재)
INSERT INTO DEPTCOPY (DEPTNO, DNAME, LOC) 
VALUES (50, 'DEVELOP', 'PANGYO');

-- [Step 3] 중간 확인
-- 내 세션에서는 추가된 데이터가 보입니다.
SELECT * FROM DEPTCOPY WHERE DEPTNO = 50;

-- [Step 4] 작업 취소 (ROLLBACK)
-- 트랜잭션 시작 전 상태로 되돌립니다.
ROLLBACK;

-- [Step 5] 결과 확인
-- 50번 데이터가 사라졌는지 확인합니다.
SELECT * FROM DEPTCOPY WHERE DEPTNO = 50;
