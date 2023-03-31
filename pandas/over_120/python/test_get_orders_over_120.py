import pandas as pd
import numpy as np
import pytest
from over_120 import get_orders_over_120

def test_get_orders_over_120():
    np.random.seed(111)
    df_orders = pd.DataFrame({
        'order_id': list(range(1, 16)),  # 1-15
        'product_id': 10 - np.random.choice(10, 15, replace=True),  # 15 values between 1-10
        'quantity': 5 - np.random.choice(5, 15, replace=True)  # 15 values between 1-5
    })
    df_products = pd.DataFrame({
        'product_id': range(1, 11),  # 1-10
        'price': (np.random.random_sample(10) * 50).round(2)  # 10 random floats between 1-50
    })

    df = get_orders_over_120(df_orders, df_products)
    assert(sum(df.total_amount > 120) == len(df))  # all returned orders are > 120
    assert(df.shape == (2, 4))
    assert(np.array_equal(df.order_id, (9, 13)))
