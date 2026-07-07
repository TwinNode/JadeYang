SELECT "name"
FROM Customer
WHERE COALESCE(refree_id, 0) != 2
-- WHERE refree_id != 2 OR refree_id IS NULL