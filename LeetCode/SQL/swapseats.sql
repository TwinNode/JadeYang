SELECT (
    CASE WHEN id % 2 = 1 AND id = (SELECT MAX(id) FROM Seat) THEN id -- id가 홀수고, 최대값일때
         WHEN id % 2 = 1 THEN id + 1 -- id가 홀수고, 최대값이 아닐 때 한칸 민다
         WHEN id % 2 = 0 THEN id - 1 -- id가 짝수일 때 한칸 당긴다.
    END) AS id, student
FROM Seat
ORDER BY id;

-- [solution 2] union : combine odd table with even table

SELECT (
    CASE WHEN (id+1) > (SELECT MAX(id) FROM Seat) THEN (SELECT MAX(id) FROM Seat) ELSE id+i END
    ) AS id, student
FROM Seat
WHERE id % 2 != 0 -- 홀수일때

UNION -- 합친다

SELECT id, student
FROM Seat
WHERE id % 2 = 0 -- 짝수일 때