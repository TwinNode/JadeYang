#Creating a new column
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.salary*2
    return employees

#without Pandas
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(bonus = 2 * employees['salary'])
