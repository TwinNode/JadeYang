SELECT x,y,z, CASE 
-- WHEN 최소값: LEAST(x,y,z) + 중간값: ((x+y+z) - GREATEST(x,y,z) - LEAST(x,y,z)) > 가장 큰 빗면 GREATEST(x,y,z)
WHEN (x+y+z) - GREATEST(x,y,z) > GREATEST(x,y,z) THEN 'Yes' ELSE 'No' END AS triangle
FROM Triangle
-- 삼각형: 두 변의 합은 가장 긴 빗면보다 커야 한다.