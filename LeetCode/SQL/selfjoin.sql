SELECT curr.id
FROM weather as curr
JOIN weather as prev ON curr.recordDate = prev.recordDate + INTERVAL "1 day"
WHERE curr.temperature > prev.temperature