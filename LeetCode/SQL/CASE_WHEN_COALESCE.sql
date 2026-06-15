SELECT p.product_id, CASE WHEN SUM(s.units) is null THEN 0 
                     ELSE ROUND(SUM(s.units * p.price)/SUM(s.units)::numeric, 2) END 
                     as average_price -- COALESCE(ROUND(SUM(s.units * p.price)/SUM(s.units)::numeric, 2), 0)
FROM Prices p
LEFT JOIN UnitSold u 
ON p.product_id = u.product_id
   AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;

-- COALESCE has potential division error when () divided by 0. CASE WHEN is more preferable approach.

    