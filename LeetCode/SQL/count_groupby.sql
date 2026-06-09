SELECT customer_id,
       COUNT(v.visit_id) AS count_no_trans
FROM Visits AS v
LEFT JOIN Transactions AS t ON v.visit_id = t.visit_id
WHERE transaction_id IS NULL -- find customer who didn't make purchase at a visit
GROUP BY customer_id