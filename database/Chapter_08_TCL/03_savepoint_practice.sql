/* ====================================================
   [3. SAVEPOINT 실습]
   목표: 트랜잭션 내에서 특정 지점을 설정하고,
        원하는 지점까지만 부분적으로 복구하는 방법을 익힙니다.
   ==================================================== */

-- [Step 1] 첫 번째 작업 (70번 부서 추가)
INSERT INTO DEPTCOPY VALUES (70, 'SALES', 'BUSAN');

-- [Step 2] 첫 번째 저장점 생성 (S1)
SAVEPOINT S1;

-- [Step 3] 두 번째 작업 (80번 부서 추가 - 실수라고 가정)
INSERT INTO DEPTCOPY VALUES (80, 'MARKETING', 'JEJU');

-- [Step 4] 데이터 확인
-- 70번, 80번 모두 보입니다.
SELECT * FROM DEPTCOPY;

-- [Step 5] 부분 취소 (S1 지점으로 복귀)
-- 80번을 넣기 전(S1) 상태로 돌아갑니다. 70번은 살립니다.
ROLLBACK TO S1;

-- [Step 6] 결과 확인
-- 70번은 존재, 80번은 삭제됨.
SELECT * FROM DEPTCOPY;

-- [Step 7] 최종 확정
-- 살아남은 70번 데이터를 영구 저장합니다.
COMMIT;
