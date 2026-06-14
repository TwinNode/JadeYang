SELECT manager.name
FROM Employee manager
LEFT JOIN Employee sub
ON manager.id = sub.managerId
GROUP BY manager.name, manager.id
HAVING COUNT(manager.id) >= 5

-- Best Practice: Subquery
SELECT manager.name
FROM Employee manager
JOIN (
    SELECT name
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(*) >= 5
) sub
ON manager.id = sub.managerId;