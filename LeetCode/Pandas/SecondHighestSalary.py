import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee[['salary']].drop_duplicates().sort_values(by='salary', ascending=False)
    if len(employee)>=2:
        return employee.rename(columns={'salary' : 'SecondHighestSalary'}).iloc[[1]]
    else: 
        return pd.DataFrame([[None]], columns=['SecondHighestSalary'])

#Pythonic Solution -1 #############
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee[['salary']].drop_duplicates().sort_values(by='salary', ascending=False)
    
    #✅Use .nth(1) for 2nd highest value
    second_salary = unique_salaries['salary'].nth(1) if len(unique_salaries) > 1 else None
    
    return pd.DataFrame({'SecondHighestSalary': [second_salary]})

#Pythonic Solution -2 #############
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    df = employee[['salary']].drop_duplicates().sort_values(by='salary', ascending=False)
    df = df.rename(columns={'salary': 'SecondHighestSalary'})
    
    #✅Use slicing : even if there's no 2nd row, no error
    res = df.iloc[1:2]
    
    #✅Use .empty to check if there's no value
    return res if not res.empty else pd.DataFrame({'SecondHighestSalary': [None]})
