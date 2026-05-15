import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    df = employee[['salary']].drop_duplicates().sort_values(by='salary', ascending=False)
    df = df.rename(columns={'salary':f'getNthHighestSalary({N})'})

    if len(df) >= N and N > 0:
        return df.iloc[[N-1]] 
    else:
        return pd.DataFrame({f'getNthHighestSalary({N})' : [None]})

    
