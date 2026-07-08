
SELECT e.course_id, e.semester, COUNT(*) AS total_count, 
        SUM(CASE WHEN e.score >= c.pass_threshold THEN 1 ELSE 0 END) AS pass_count, 
        ROUND(CAST((AVG(CASE WHEN e.score >= c.pass_threshold THEN 1 ELSE 0 END)) AS FLOAT),2) AS pass_rate
FROM enrollments e
JOIN course_catalog c ON (e.course_id = c.course_id AND e.semester = c.semester)
GROUP BY e.course_id, e.semester
HAVING total_count >= 2
ORDER BY e.course_id, e.semester
