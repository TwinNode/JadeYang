-- Best Practice Approach: if login day -1 day = first login day
SELECT ROUND(COUNT(DISTINCT player_id)/COUNT(DISTINCT plyer_id FROM Activity), 2) AS fraction
FROM Activity
WHERE (player_id, DATE_SUB(event_date, INTERVAL 1 DAY)) 
    IN(
        SELECT player_id, MIN(event_date) AS first_longin FROM Activity GROUP BY player_id
    )

-- my answer: slower due to LEFT JOIN : if first login day + 1 = login day (exist?)
SELECT ROUND(COUNT(tmrw.event_date)*1.0/COUNT(curr.player_id, 2) AS fraction
FROM Activity curr
LEFT JOIN Activity tmrw ON curr.event_date + 1 = tmrw.event_date AND curr.player_id = tmrw.player_id
WHERE (curr.player_id, curr.event_date)
    IN (SELECT player_id, MIN(event_date) FROM Activity GROUP BY player_id);
