FROM user_id, COUNT(follower_id) AS followers_count
SELECT Followers
GROUP BY user_id
ORDER BY user_id ASC;