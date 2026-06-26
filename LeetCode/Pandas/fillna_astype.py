import pandas as pd
def clean_and_filter_employees (employees: pd.DataFrame) -> pd.DataFrame:
    emp = employees.copy()

    emp = emp.fillna({'salary':0, 'age':0}).astype({'salary':int, 'age':int}).rename(columns={'dept':'department'})

    return emp.loc[(emp['salary'] > 0) & (emp['age'] >= 18), ['emp_id', 'name', 'department', 'salary', 'age']].sort_values(by='emp_id').reset_index(drop=True)