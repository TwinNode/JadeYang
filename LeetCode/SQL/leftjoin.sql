SELECT unique_id, A.name
FROM Employee as A 
LEFT JOIN EmployeeUNI as B ON A.id = B.id; -- Default Join: INNER JOIN
-- LEFT JOIN: Show data including where (unique_id is NULL)
