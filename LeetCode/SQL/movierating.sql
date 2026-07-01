-- TABLE 1
(
    SELECT name AS results
    FROM MovieRating
    JOIN Users
    USING (user_id)
    GROUP BY user_id, name
    ORDER BY COUNT(*) DESC, name ASC
    LIMIT 1
)

UNION ALL -- shows dupes

-- Table 2
(
    SELECT title AS results
    FROM MovieRating
    JOIN Movies
    USING (movie_id)
    WHERE TO_CHAR(created_at, 'YYYY-MM') = '2020-02'
    GROUP BY movie_id, title
    ORDER BY AVG(rating) DESC, title ASC
    LIMIT 1
)

