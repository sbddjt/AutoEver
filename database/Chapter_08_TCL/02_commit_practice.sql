/* ====================================================
   [2. COMMIT 실습]
   목표: 작업을 완료하고 DB에 영구적으로 반영하는 과정과
        COMMIT 이후에는 되돌릴 수 없음을 이해합니다.
   ==================================================== */

-- [Step 1] 데이터 조작 (INSERT)
-- 60번 부서 '인사팀' 추가
INSERT INTO DEPTCOPY (DEPTNO, DNAME, LOC) 
VALUES (60, 'HR', 'SEOUL');

-- [Step 2] 변경 사항 확정 (COMMIT)
-- 이제 다른 사용자들도 이 데이터를 볼 수 있게 됩니다.
COMMIT;

-- [Step 3] 뒤늦은 후회 (ROLLBACK 시도)
-- 이미 COMMIT 된 데이터는 트랜잭션이 종료되었으므로 취소되지 않습니다.
ROLLBACK;

-- [Step 4] 결과 확인
-- 60번 데이터가 여전히 존재하는지 확인합니다.
SELECT * FROM DEPTCOPY WHERE DEPTNO = 60;
