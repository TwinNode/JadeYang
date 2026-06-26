SELECT a.product_id, COALESCE(b.new_price, 10) AS price -- fill null value with 10
FROM (SELECT DISTINCT product_id FROM Products) AS a
LEFT JOIN (
    SELECT product_id, new_price
    FROM Products
    WHERE (product_id, change_date) 
    IN (
        SELECT product_id, MAX(change_date)
        FROM Products
        WHERE change_date <= '2019-08-16'
        GROUP BY product_id
    )
) AS b ON a.product_id = b.product_id