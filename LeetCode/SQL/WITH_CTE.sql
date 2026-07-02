WITH

Daily AS (
    SELECT visited_on, SUM(amount) as dailytotal
    FROM Customer
    GROUP BY visited_on
),

Calculated AS 
(
    SELECT visited_on, 
           SUM(dailytotal) OVER (
                ORDER BY visited_on
                ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
           ROUND(
                AVG(dailytotal) OVER (
                    ORDER BY visited_on
                    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)
                )::numeric, 2 AS average_amount
    FROM Daily
)

SELECT visited_on, amount, average_amount
FROM Calculated
WHERE visited_on >= (SELECT MIN(visited_on) FROM Customer) + INTERVAL '6 day'
ORDER BY visited_on;