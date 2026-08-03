SELECT user_id, UPPER(SUBSTR(name, 1, 1)) || LOWER(SUBSTR(name, 2)) AS name
FROM Users;
-- in PostgreSQL : INITCAP(name) AS name
-- first letter Upper, the rest (starting from second letter) is in lowercase connected with ||