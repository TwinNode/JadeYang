import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    
    condition = result.customerId.isna()

    output = result[condition].rename(columns={'name':'Customers'})[['Customers']]

    return output


#best answer
import pandas as pd
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    df = customers[~customers['id'].isin(orders['customerId'])]

    df = df[['name']].rename(columns={'name': 'Customers'})

    return df
