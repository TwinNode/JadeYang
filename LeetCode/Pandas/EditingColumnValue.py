import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees.salary * 2 #improved: employee['salary] *= 2
    return employees
