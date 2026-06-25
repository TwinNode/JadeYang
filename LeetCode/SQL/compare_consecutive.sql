-- SELF JOIN (SLOW)
SELECT DISTINCT a.num AS ConsecutiveNums
FROM Logs a
JOIN Logs b ON a.id + 1 = b.id
JOIN Logs c ON a.id + 2 = c.id
WHERE a.num = b.num AND a.num = c.num

-- WINDOW FUNCTION: LAG() OVER (ORDER BY)
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT num AS a, 
           LAG(num, 1) OVER (ORDER BY id) AS b 
           LAG(num, 2) OVER (ORDER BY id) AS c
    FROM Logs
) AS Subquery
WHERE a = b AND a = c