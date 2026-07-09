import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')
conn.execute('''
    CREATE TABLE enrollments (
        student_id INTEGER,
        dept TEXT,
        score REAL
    )
''')
conn.executemany('INSERT INTO enrollments VALUES (?,?,?)', [
    (1, 'A', 85),
    (2, 'A', 90),
    (3, 'A', None),
    (4, 'B', 60),
    (5, 'B', 40),
    (6, 'B', 70),
    (7, 'C', 95),
])
conn.commit()

query = """
SELECT dept,
       COUNT(*) AS student_count,
       SUM(CASE WHEN score >= 70 THEN 1 ELSE 0 END) AS pass_count,
       ROUND(AVG(SCORE),2) AS avg_score  

FROM enrollments
GROUP BY dept -- even if there's no GROUP BY, sqlite doesn't impute an error.
HAVING student_count >= 2

ORDER BY dept;
"""

result = pd.read_sql(query, conn)
print(result)