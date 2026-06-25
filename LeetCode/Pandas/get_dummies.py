import pandas as pd
def encode_dept_onehot (employees: pd.DataFrame) -> pd.DataFrame:
    dept = pd.get_dummies(employees, columns = ['dept'], prefix='dept').astype(int) # int: return value 0 or 1
    # pd.get_dummies: Returns 0 or 1 (False/True) to indicate category membership.
    # Expands one column into multiple columns based on the number of unique values.
    # Whereas map() replaces values 1:1 and remains as a single column (no structural change)
    return dept [['emp_id', 'salary', 'age', 'dept_eng', 'dept_hr', 'dept_sales']].sort_values(by='emp_id').reset_index(drop=True)
