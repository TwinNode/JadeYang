import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:

    result = activities.groupby('sell_date').agg(
        num_sold = ('product', 'nunique'),
        products = ('product', lambda x: ','.join(sorted(x.unique())))
    ).reset_index()

    return result

# best practice
import pandas as pd
def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
  return activities.groupby('sell_date')['product'].agg([
    ('num_sold', 'nunique'),
    ('products', lambda x: ','.join(sorted(x.unique())))
  ]).reset_index()

    
