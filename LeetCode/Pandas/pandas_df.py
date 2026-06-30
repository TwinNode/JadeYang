import pandas as pd
def enrich_orders_with_avg(orders : pd.DataFrame, customers : pd.DataFrame) -> pd.DataFrame:
    df = orders.merge(customers, on = 'cust_id', how = 'left').fillna({'name' : 'Unknown', 'amount' : 0.0})
    df['cust_avg_amount'] = df.groupby('cust_id')['amount'].transform('mean').round(2)

    # [sol1] Vector series comparion : fast than apply() 
    df['above_avg'] = (df['amount'] > df['cust_avg_amount']).astype(int) # True or False to 1 or 0

    # [sol2] using apply() : when compare with if-else.
    # df['above_avg'] = df.apply(lambda x: x['amount'] > x['cust_avg_amount'], axis=1).astype(int)

    df = df[['order_id', 'cust_id', 'name', 'amount', 'cust_avg_amount', 'above_avg']] # column order

    return df.astype({'order_id': int, 'cust_id' : int}).sort_values(['cust_id', 'order_id']).reset_index(drop=True)