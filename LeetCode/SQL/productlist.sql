SELECT product_name, SUM(unit) as unit
FROM Orders
JOIN Products USING(product_id) -- alias is unneccessary
WHERE TO_CHAR(order_date, 'YYYY-MM') = '2020-02'
GROUP BY product_id, product_name
HAVING SUM(unit) >= 100;