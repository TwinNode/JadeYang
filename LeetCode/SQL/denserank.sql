-- CTE: WITH()
-- WINDOW FUNC(): DENSE_RANK() Ranks without gaps for ties (e.g., 1, 2, 2, 3)
WITH RANKING AS(
    SELECT d.name AS Department,
           e.name AS Employee,
           salary AS Salary,
           DENSE_RANK() OVER (PARTITION BY d.name ORDER BY salary DESC) AS ranknum
    FROM Employee AS e 
    JOIN Department AS d ON e.departmentId = d.id
)

SELECT Department, Employee, Salary
FROM RANKING
WHERE ranknum <= 3

-- Traditional WHERE IN() : find the top 3 salary
SELECT d.name AS Department, e.name AS Employee, salary AS Salary
FROM Employee e JOIN Department d ON e.departmentId = d.id
WHERE salary IN (
                SELECT DISTINCT (salary)
                FROM Employee
                WHERE Employee.departmentId = d.id
                ORDER BY salary DESC
                LIMIT 3
)