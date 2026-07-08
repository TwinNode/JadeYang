import pandas as pd
import numpy as np

orders = pd.DataFrame({
    'order_id': [1, 2, 3, 4, 5, 6],
    'cust_id':  [101, 101, 102, 103, 103, 104],
    'amount':   [100.0, 50.0, 200.0, np.nan, 80.0, 30.0],
    'status':   ['completed', 'completed', 'cancelled', 'completed', 'pending', 'cancelled']
})

def active_customer_summary(orders: pd.DataFrame) -> pd.DataFrame:
    
    #df = orders.loc[(orders['status'] != 'cancelled')]
    #df = orders[orders['status'] != 'cancelled'] # []로 필터링

    df = orders[orders['status'] != 'cancelled'].fillna({'amount':0})

    final = df.groupby('cust_id').agg(
        order_count = ('order_id', 'count'),
        total_amount = ('amount', 'sum'),
        avg_amount = ('amount', 'mean')
    ).reset_index()

    final['total_amount'] = final['total_amount'].round(2)
    final['avg_amount'] = final['avg_amount'].round(2)

    columns = ['cust_id', 'order_count', 'total_amount', 'avg_amount']
    return final[columns].sort_values(by='total_amount', ascending=False).reset_index(drop=True)

result = active_customer_summary(orders)
print(result)
print(result.dtypes)
