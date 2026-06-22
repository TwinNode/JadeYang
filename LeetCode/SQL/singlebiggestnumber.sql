-- my answer
SELECT MAX(num) as num
FROM Mynumbers
WHERE num IN (SELECT num FROM Mynumbers GROUP BY num HAVING count(num) = 1);

-- subquery in FROM
SELECT MAX(t.num) as num
FROM (SELECT num FROM Mynumbers GROUP BY num HAVING count(num)=1) AS t;

-- clever
SELECT (CASE WHEN COUNT(*) = 1 THEN num ELSE null END) AS num
FROM Mynumbers
GROUP BY num
ORDER BY 1 DESC nulls last -- sort last at the end of the list
LIMIT 1; -- RETURN only the first num (which is the biggest number, sorted by desc)