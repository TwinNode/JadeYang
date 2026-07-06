-- INITCAP() : aBC -> Abc, ABC -> Abc
SELECT user_id, INITCAP(name) AS name
FROM Users