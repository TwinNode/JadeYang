import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    counting = employee['managerId'].value_counts() # counting Id frequency
    target_id = counting[counting >= 5].index # return index of 'managerId' where its greater than equal to 5.
    # if needed to fetch the value, counting[counting>=5].values

    res = employee[employee['id'].isin(target_id)]

    return res[['name']] # return mgr's name as dataframe


## best practice
import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    managers = employee.groupby(
        'managerId', as_index=False
    ).agg(
        reporting = ('id', 'count')
    ).query(
        'reporting >= 5'
    )['managerId']

    return employee[employee['id'].isin(managers)][['name']]