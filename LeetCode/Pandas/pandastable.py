import pandas as pd

def enrich_orders_with_category_avg(orders, products):

    df = orders.merge(products, how='left', on='product_id').fillna({'category' : 'Unknown', 'price': 0})

    df['revenue'] = df['qty'] * df['price']

    df['category_avg_revenue'] = df.groupby('category')['revenue'].transform('mean').round(2)

    df['above_avg'] = (df['revenue'] > df['category_avg_revenue']).astype(int)

    columns = ['order_id', 'product_id', 'qty', 'category', 'price', 'revenue',  'category_avg_revenue', 'above_avg']

    # df.info() # check dtype for each column

    return df[columns].sort_values(['category', 'revenue'], ascending=[True, False]).reset_index(drop=True)

orders = pd.DataFrame({
    'order_id':   [1, 2, 3, 4],
    'product_id': ['P1', 'P2', 'P1', 'P3'],
    'qty':        [3, 5, 2, 1],
})
products = pd.DataFrame({
    'product_id': ['P1', 'P1', 'P2'],   # P1 중복(가격 다름) → 카테시안 폭발
    'category':   ['Elec', 'Elec', 'Home'],
    'price':      [10.0, 12.0, 20.0],
})

enrich_orders_with_category_avg(orders, products)