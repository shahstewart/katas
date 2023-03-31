# df_orders and df_products are the provided dataframes.
getOrdersOver120 <- function (df_orders, df_products) {
    df <- merge(df_orders, df_products, by='product_id')
    df['total_amount'] <- df$quantity * df$price
    ret <- subset(df, total_amount > 120)
    ret[order(ret$order_id),]
}
