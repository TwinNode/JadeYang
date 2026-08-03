-- POSTGRE
DELETE FROM Person p1
USING Person p2
WHERE p1.email = p2.email AND p1.id > p2.id -- delete rows wheere p1.id is greater than p2's.

-- SQLITE & POSTGRE : WHERE ** NOT IN()
DELETE FROM Person
WHERE id NOT IN (
    SELECT MIN(id)
    FROM Person
    GROUP BY email
);