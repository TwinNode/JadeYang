import pandas as pd
def region_category_summary(orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:

    df = orders.merge(products, on='product', how='left').fillna({'category':'Unknown'})

    df['revenue'] = df['qty']*df['price']

    final = df.groupby(['region', 'category']).agg({'revenue' : 'sum', 'qty': 'mean'}).reset_index().rename(columns={'revenue' : 'total_revenue', 'qty':'avg_qty'}).round(2)

    final['above_avg'] = (final['total_revenue'] > final['total_revenue'].mean()).astype(int)
    
    #final.info()

    return final[['region', 'category', 'total_revenue', 'avg_qty', 'above_avg']].reset_index(drop=True)


orders = pd.DataFrame({
    'order_id': [1, 2, 3, 4, 5],
    'region':   ['North', 'North', 'South', 'North', 'South'],
    'product':  ['WidgetA', 'WidgetA', 'WidgetB', 'Gadget', 'Mystery'],
    'qty':      [2, 1, 3, 5, 2],
    'price':    [10.0, 10.0, 5.0, 4.0, 8.0],
})

# 데이터 품질 이슈: WidgetA가 products에 두 번 등록됨 (카테고리 다르게)
products = pd.DataFrame({
    'product':  ['WidgetA', 'WidgetA', 'WidgetB', 'Gadget'],
    'category': ['Tools', 'Premium', 'Tools', 'Electronics'],
})

region_category_summary(orders,products)