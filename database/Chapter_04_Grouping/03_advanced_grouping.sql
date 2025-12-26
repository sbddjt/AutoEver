-- 1. WITH ROLLUP (소계 및 총계 구하기)
SELECT goodscd, SUM(qty)
FROM order_d
GROUP BY goodscd WITH ROLLUP;

-- 2. PIVOT 실습을 위한 테이블 생성 및 데이터 입력
CREATE TABLE pivotTest(
    uName CHAR(20),
    season CHAR(20),
    amount INT
);

INSERT INTO pivotTest VALUES 
('aespa', '겨울', 10), ('blackpink', '여름', 15), 
('aespa', '가을', 25), ('aespa', '봄', 3), 
('aespa', '봄', 37), ('blackpink', '겨울', 40), 
('aespa', '여름', 14), ('aespa', '겨울', 22), 
('blackpink', '여름', 64);

-- 3. PIVOT 쿼리 (행 -> 열 변환)
SELECT uName, 
       SUM(IF(season = '봄', amount, 0)) AS '봄', 
       SUM(IF(season = '여름', amount, 0)) AS '여름', 
       SUM(IF(season = '가을', amount, 0)) AS '가을', 
       SUM(IF(season = '겨울', amount, 0)) AS '겨울', 
       SUM(amount) AS '합계'
FROM pivotTest
GROUP BY uName;
