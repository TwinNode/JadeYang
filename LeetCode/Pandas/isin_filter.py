import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    counting = employee['managerId'].value_counts() # counting Id frequency
    target_id = counting[counting >= 5].index # return index of 'managerId' where its greater than equal to 5.

    res = employee[employee['id'].isin(target_id)]

    return res[['name']] # return mgr's name as dataframe