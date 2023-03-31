import pandas as pd

def get_orders_over_120(df_orders: pd.DataFrame, df_products: pd.DataFrame):
    df = pd.merge(left=df_orders, right=df_products, how='left', on='product_id')
    df['total_amount'] = df.quantity * df.price
    return df[['order_id', 'product_id', 'quantity', 'total_amount']][df.total_amount > 120]
