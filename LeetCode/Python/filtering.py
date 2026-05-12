import pandas as pd

def BigCountries(world: pd.DataFrame) -> pd.DataFrame:
    bigcountrydata = world[(world.population >= 25000000) | (world.area >= 3000000)][['name', 'population', 'area']]

    return bigcountrydata

columnname = ['name', 'continent', 'area', 'population', 'gdp']
data = [
    ['Afgahinistan', 'Asia', 652230, 25500100, 20343000000],
    ['Albania', 'Europe', 28748, 2831741, 12960000000],
    ['Algeria', 'Africa', 2381741, 37100000, 188681000000],
    ['Andorra', 'Europe', 468, 78115, 3712000000],
    ['Angola', 'Africa', 1246700, 20609294, 100990000000]
]

worldtable = pd.DataFrame(data, columns = columnname)
BigCountries(worldtable)


"""
Input: 
World table:
+-------------+-----------+---------+------------+--------------+
| name        | continent | area    | population | gdp          |
+-------------+-----------+---------+------------+--------------+
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
+-------------+-----------+---------+------------+--------------+
Output: 
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
+-------------+------------+---------+
"""
