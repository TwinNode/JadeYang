-- SELF JOIN: The optimal approach here. 'process_id' explicitly pairs the logs, making sorting unnecessary.
SELECT s.machine_id, ROUND(CAST(AVG(e.timestamp-s.timestamp) AS FLOAT, 3) AS processing_time
FROM Activity a
JOIN Activity e
    ON s.machine_id = e.machine_id
    AND s.process_id = e.process_id
    AND s.activity_type = 'start'
    AND e.activity_type = 'end'
GROUP BY s.machine_id


-- WINDOW & CTE: Ideal when 'process_id' is missing, requiring sorting by timestamp.
WITH TimeLog AS (
    SELECT machine_id, activity_type, timestamp AS start_time,
    LEAD(timestamp) OVER (
                            PARTITION BY machine_id, process_id,
                            ORDER BY timestamp
                        ) AS end_time
    FROM Activity
)

SELECT machine_id, ROUND(CAST(AVG(end_time - start_time) AS float), 3) AS processing_time
FROM TimeLog
WHERE activity_type = 'start'
GROUP BY machine_id;