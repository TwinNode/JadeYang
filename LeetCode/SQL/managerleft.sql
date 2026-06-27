SELECT employee_id
FROM Employees
WHERE (salary < 30000) AND (manager_id is not null) AND 
      manager_id NOT IN (SELECT employee_id FROM Employees) -- MANAGER ID is not listed in employee_id
ORDER BY employee_id;