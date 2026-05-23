import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time']-employees['in_time']

    employees.rename(columns={'event_day':'day'}, inplace=True)
    
    result = employees.groupby(['day', 'emp_id'], as_index=False)['total_time'].sum()
    # as_index=False : not to make the columns into index, but remain as columns
    # result = employees.groupby(['emp_id', 'event_day'])['time_spent'].sum().reset_index()
    
    return result
    
