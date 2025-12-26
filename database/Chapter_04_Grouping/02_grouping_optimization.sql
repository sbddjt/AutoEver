-- [방법 A] HAVING 사용 (그룹화 후 필터링 - 비효율)
SELECT depart, MAX(salary)
FROM tstaff
GROUP BY depart
HAVING depart IN ('인사과', '영업부');

-- [방법 B] WHERE 사용 (그룹화 전 필터링 - 권장 ⭐)
SELECT depart, MAX(salary)
FROM tstaff
WHERE depart IN ('인사과', '영업부')
GROUP BY depart;
