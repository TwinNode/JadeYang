SELECT g.student_id, g.student_name, g.subject_name,
       COUNT(e.student_id) as attended_exams
FROM (Students CROSS JOIN Subjects) as g -- Cross join doesn't have 'On'
LEFT JOIN Examinations as e
ON g.student_id = e.student_id
   AND g.subject_name = e.subject_name
GROUP BY g.student_id, g.student_name, g.subject_name -- all selected columns must be listed in GROUP BY
ORDER BY g.student_id, g.subject_name