import pandas as pd

customers = pd.read_csv("data/raw/olist_customers_dataset.csv")
orders = pd.read_csv("data/raw/olist_orders_dataset.csv")
order_items = pd.read_csv("data/raw/olist_order_items_dataset.csv")
products = pd.read_csv("data/raw/olist_products_dataset.csv")
sellers = pd.read_csv("data/raw/olist_sellers_dataset.csv")

from sqlalchemy import create_engine
engine = create_engine(
    "postgresql://postgres:1234@localhost:5432/e_commercedb"
)
dim_customer = customers[[
    "customer_id",
    "customer_city",
    "customer_state"
]].drop_duplicates()
dim_customer.to_sql(
    "dim_customer",
    engine,
    if_exists="append",
    index=False
)
dim_product = products[[
    "product_id",
    "product_category_name"
]].rename(columns={
    "product_category_name" : "product_category"
}).drop_duplicates()

dim_product.to_sql(
    "dim_product",
    engine,
    if_exists="append",
    index= False
)
dim_seller = sellers[[
"seller_id",
"seller_city",
"seller_state"
]].drop_duplicates()

dim_seller.to_sql (
    "dim_seller",
    engine,
    if_exists="append",
    index= False
)

orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)
dim_date = pd.DataFrame()
dim_date["date_id"] = orders["order_purchase_timestamp"].dt.date
dim_date["year"] = orders["order_purchase_timestamp"].dt.year
dim_date["month"] = orders["order_purchase_timestamp"].dt.month
dim_date["day"] = orders["order_purchase_timestamp"].dt.day
dim_date["weekday"] = orders["order_purchase_timestamp"].dt.day_name()
dim_date = dim_date.drop_duplicates()

dim_date.to_sql(
    "dim_date",
    engine,
    if_exists="append",
    index=False
)
## orders + order_items birleşecek

sales = order_items.merge(
    orders, 
    on="order_id"
)

sales = sales [[
    "order_id",
    "product_id",
    "seller_id",
    "price",
    "freight_value",
    "order_purchase_timestamp"
]]
sales["date_id"] = pd.to_datetime(
    sales["order_purchase_timestamp"]
).dt.date
sales = sales.merge(
    orders[["order_id","customer_id"]],
    on="order_id"
)
fact_sales = sales[[
    "order_id",
    "customer_id",
    "product_id",
    "seller_id",
    "date_id",
    "price",
    "freight_value"
]]
fact_sales.to_sql(
    "fact_sales",
    engine,
    if_exists="append",
    index=False
)