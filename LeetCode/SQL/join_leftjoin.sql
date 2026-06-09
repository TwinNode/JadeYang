SELECT product_name, year, price
FROM Sales as s
JOIN Product as p ON s.product_id = p.product_id
-- LEFT JOIN is recommended to list all product info.