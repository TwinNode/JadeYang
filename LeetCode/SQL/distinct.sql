    -- sqlite3
    SELECT page, COUNT(*) AS total_views, 
           COUNT(DISTINCT user_id || '_' || session_id) AS distinct_sessions
           -- either user_id or session_id is null, return value is null
           -- distinct ignores null values and count the rest
    FROM page_views
    GROUP BY page
    ORDER BY distinct_sessions DESC, page ASC;