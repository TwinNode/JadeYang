SELECT p.firstName, p.lastName, a.city, a.state
-- If a column name is unique, you don't need to specify its table alias.
FROM Person p 
LEFT JOIN Address a 
-- LEFT JOIN ensures all persons are listed, with NULLs where address data is absent.
ON p.personId = a.personId