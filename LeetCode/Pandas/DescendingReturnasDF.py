import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    animals = animals.loc[(animals.weight > 100)].sort_values(by='weight', ascending = False)
    return animals[['name']] # to return as DataFrame

  #one-liner
  return animals[animals['weight'] > 100].sort_values(['weight'],ascending=False)[['name']]

  #method chaining
  return (animals
            [animals['weight'] > 100]
            .sort_values(by='weight', ascending=False)
            [['name']])

"""
Example 1:

Input: 
DataFrame animals:
+----------+---------+-----+--------+
| name     | species | age | weight |
+----------+---------+-----+--------+
| Tatiana  | Snake   | 98  | 464    |
| Khaled   | Giraffe | 50  | 41     |
| Alex     | Leopard | 6   | 328    |
| Jonathan | Monkey  | 45  | 463    |
| Stefan   | Bear    | 100 | 50     |
| Tommy    | Panda   | 26  | 349    |
+----------+---------+-----+--------+
Output: 
+----------+
| name     |
+----------+
| Tatiana  |
| Jonathan |
| Tommy    |
| Alex     |
+----------+
"""
    
