SELECT a.person_name
FROM Queue AS a
JOIN (
    SELECT person_id, SUM(weight) OVER (ORDER BY turn) as total
    FROM Queue
    ORDER BY turn
) AS b ON a.person_id = b.person_id
WHERE b.total <= 1000
ORDER BY turn DESC
LIMIT 1;