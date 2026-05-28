import pandas as pd
def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
  count = orders['customer_number'].value_counts()
  top_customer = count.index[0]
  return pd.DataFrame({'customer_number' : [top_customer] })


# Use Mode : most frequent value
import pandas as pd
def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
  return orders['customer_number'].mode().to_frame()
