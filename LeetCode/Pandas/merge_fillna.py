import pandas as pd

def enrich_orders_full(orders, customers, products):

    df = orders.merge(customers, how='left', on='cust_id').fillna({'name': 'Unknown'})
    
    final = df.merge(products, how='left', on='product_id').fillna({'category': 'Unknown', 'price':0})
    final['revenue'] = final['qty'] * final['price']

    columns = ['order_id', 'cust_id', 'name', 'product_id', 'category', 'price', 'qty', 'revenue']
    
    # final.info() # check dtype to meet the requirements

    return final[columns].sort_values(by=['order_id', 'category']).reset_index(drop=True)

orders = pd.DataFrame({
    'order_id':   [1, 2, 3, 4],
    'cust_id':    [1, 2, 3, 1],
    'product_id': [10, 20, 10, 30],
    'qty':        [2, 1, 3, 1],
})

customers = pd.DataFrame({
    'cust_id': [1, 2],       # cust_id=3은 없음 → 미매칭
    'name':    ['Alice', 'Bob'],
})

products = pd.DataFrame({
    'product_id': [10, 10, 20],   # product_id=10 중복! (30은 아예 없음 → 미매칭)
    'category':   ['Electronics', 'Gadgets', 'Books'],
    'price':      [100.0, 150.0, 20.0],
})

enrich_orders_full(orders, customers, products)