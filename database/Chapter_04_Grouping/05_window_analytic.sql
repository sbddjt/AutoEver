-- 1. LEAD: 다음 행과의 나이 차이 구하기
SELECT name, birthyear, 
       (birthyear - LEAD(birthyear, 1) OVER(ORDER BY birthyear DESC)) AS diff_next
FROM usertbl;

-- 2. CUME_DIST: 누적 분포 (백분위 상위 몇 %인지)
SELECT name, birthyear, CUME_DIST() OVER(ORDER BY birthyear DESC) AS percentile
FROM usertbl;
