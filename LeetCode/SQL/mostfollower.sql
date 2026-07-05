WITH freq (
    (SELECT requester_id as id FROM RequestAccepted)
UNION ALL
    (SELECT accepter_id as id FROM RequqestAccepted)
)

SELECT id, COUNT(id) num
FROM freq
GROUP BY id
ORDER BY num DESC
LIMIT 1