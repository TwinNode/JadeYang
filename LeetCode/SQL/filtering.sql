SELECT id, movie, description, rating
FROM Cinema
WHERE id % 2 = 1 AND description != 'boring' -- filter: id is odd number
ORDER BY rating DESC;