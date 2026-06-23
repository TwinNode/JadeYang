import pandas as pd
def grade(salary, age):
    if salary >= 80000 and age < 40: return 'High'
    elif salary >= 80000 and age >= 40: return 'Mid'
    elif salary < 80000: return 'Low'

def classify_salary_level(employees: pd.DataFrame) -> pd.DataFrame:
    emp = employees.copy()
    emp['salary_level'] = emp.apply(lambda row: grade(row['salary'], row['age']), axis=1).astype(str)
    
    return emp[['emp_id', 'dept', 'salary', 'age', 'salary_level']]

data = [
    [1, 'sales', 90000, 35], 
    [2, 'sales', 90000, 45],
    [3, 'eng', 70000, 28]
    ]
columns = ['emp_id', 'dept', 'salary', 'age']

df = pd.DataFrame(data, columns=columns)


classify_salary_level(df)
