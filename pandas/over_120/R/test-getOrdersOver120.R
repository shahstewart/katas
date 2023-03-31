library(testthat)
source('over120.R')

test_that('Returns orders with total amount over 120', {
    set.seed(111)
    df_products <- data.frame(
        product_id = 1:10,
        price = round(40 - (runif(10) * 30), 2)
    )
    df_orders <- data.frame(
        order_id = 1:15,
        product_id = sample.int(10, 15, replace=T),
        quantity = sample.int(5, 15, replace=T)
    )
    data <- getOrdersOver120(df_orders, df_products)

    expect_true(sum(data$total_amount > 120) == nrow(data))  # all returned orders are > 120
    expect_equal(dim(data), c(4, 5))
    expect_equal(data$order_id, c(4,  7,  11, 12))
})
