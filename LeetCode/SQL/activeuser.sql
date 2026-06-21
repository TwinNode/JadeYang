SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN '2019-07-27' :: date - 29 AND '2019-07-27' :: date 
-- ::date change to date type
GROUP BY activity_date