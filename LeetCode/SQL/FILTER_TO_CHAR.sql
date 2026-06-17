SELECT TO_CHAR(trans_date, 'YYYY-MM') AS month, country,
        COUNT(*) AS trans_count, COUNT(state) FILTER (WHERE state = 'approved') AS approved_count,
        SUM(amount) AS trans_total_amount,
        COALESCE(SUM(amount) FILTER (WHERE state = 'approved'), 0) AS approved_total_amount
        -- COALESCE() in case if there's null, replace it with 0.
FROM Transactions
GROUP BY "month", country;
-- "month" means this is a column name not a function name.