## Over 120 dollars total transactions

### Description  
orders and products are two dataframes holding order and product details respectively.

**The orders dataframe:**

| Column      | dType |
|-------------|-------|
| order_id    | int   |
| product_id  | int   |
| quantity    | float |

<br>

**The products dataframe:**  

| Column     | dType |
|------------|-------|
| product_id | int   |
| price      | float |


Each order corresponds only to one product. That is, different products are ordered as separate orders. 

<br>

### Task
Given the two dataframes above, write a function to return a dataframe containing orders with a total 
of over $120. Include the total value of the transaction as a new column (total_amount) in the dataframe.
Return the dataframe sorted by order id.

<br>

### Solutions
Solutions are provided in Python and R. First, the dataframes are merged, and the total amount is calculated 
by multiplying quantity with price. Then the orders are filtered for total amount > 120.

<br>  

### Tests

**Python:**   
Using _pytest_.  
Run `py.test` from `katas/programming/over_120/python`

**R**  
Using _testthis_.  
Run `testthat::test_file('test-get_orders_over_120.R')` from `katas\programming\over_120\R`

<br><br>
