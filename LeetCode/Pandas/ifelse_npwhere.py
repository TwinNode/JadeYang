import pandas as pd
import numpy as np 
# for np.where

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0 # fill all columns with 0 as default
    employees.loc[(employees['employee_id'] % 2 != 0) & (employees['name'].str[0] != "M"), 'bonus'] = employees['salary']

# Use np.where of numpy
    employees['bonus'] = np.where((employees['employee_id'] % 2 != 0) & (employees['name'].str[0] != "M"), employees['salary'], 0) 
    # np.where(condition, if, else)

    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')