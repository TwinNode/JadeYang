import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red = company[company['name']=="RED"]['com_id'].values
    salesid = orders[orders['com_id'].isin(red)]['sales_id'].unique()
    # Finds salesperson's id who sold to "RED"
    # Finds salesperson's id who did not sold to "RED" using ~ 
    return sales_person[~sales_person['sales_id'].isin(salesid)][['name']]

# best practice
import pandas as pd
def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return sales_person[
        ~sales_person['sales_id'].isin(
            pd.merge(
                left = orders,
                right = company[company['name'] == "RED"],
                on = 'com_id',
                how = 'inner' # intersection
            )['sales_id'].unique()
        )
    ][['name']]