-- POSTGRE SQL

SELECT sell_date, COUNT(DISTINCT product) AS num_sold,
       STRING_AGG(DISTINCT product, ',' ORDER BY product) AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date

-- SQLite

SELECT sell_date, COUNT(product) as num_sold,
       GROUP_CONCAT(product) AS products
FROM (
    SELECT DISTINCT sell_date, product
    FROM Activities
    ORDER BY sell_date, product\
)
GROUP BY sell_date
ORDER BY sell_date