import pandas as pd
import numpy as np # for np.where

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0 # fill all columns with 0 as default
    employees.loc[(employees['employee_id'] % 2 != 0) & (employees['name'].str[0] != "M"), 'bonus'] = employees['salary']

# Use np.where(condition, if, else) of numpy
    employees['bonus'] = np.where((employees['employee_id'] % 2 != 0) & (employees['name'].str[0] != "M"), employees['salary'], 0) 
    # if first letter is space or null : str[0] returns index error whereas startswith('M') returns False
    # (~employees['name'].str.startswith('M')) is recommended
    
    # str.strip() removes any space before and after "M" in name: 
    # ~employees['name'].str.strip().str.startswith('M')
    
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')
