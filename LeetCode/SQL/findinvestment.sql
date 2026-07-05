-- CTE, window ()
WITH latlon AS (
    SELECT tiv_2016,
            COUNT(*) OVER (PARTITION BY lat, lon) AS count,
            COUNT(*) OVER (PARTITION BY tiv_2015) AS tiv_count
    FROM Insurance
)

SELECT ROUND(SUM(tiv_2016) :: numeric, 2) AS tiv_2016
FROM latlon
WHERE count = 1 AND tiv_count > 1;



-- traditional way using IN
SELECT ROUND(SUM(tiv_2016)::numeric, 2) AS tiv_2016 
FROM Insurance
WHERE tiv_2015 
    IN (
        SELECT tiv_2015 
        FROM Insurance
        GROUP BY tiv_2015
        HAVING COUNT(*) > 1            
    ) AND
    IN (
        SELECT lat, lon
        FROM Insurance
        GROUP BY lat, lon
        HAVING COUNT(*) = 1
    )