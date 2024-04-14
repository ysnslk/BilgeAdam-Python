import pandas as pd

# Merge & Join
# İki veri setinde ortak olanrak bulnur sütunlardan faydalınarak bu iki veri setinin birleştirilme işlemlerini yaptığımız fonksiyonlar merge ve join'dir.ç SQL'de join mantığı bire bir bulunmaktadır.

customer = {
    'Customer ID': [1, 2, 3],
    'First Name': ['Burak', 'Hakan', 'İpek'],
    'User Name': ['beast', 'bear', 'keko']
}

orders = {
    'Order Id': [1001, 1002, 1003, 1004, 1005],
    'Customer ID': [1, 2, 3, 4, 5],
    'Order Date': ['2024-04-14', '2024-04-15', '2024-04-16', '2024-04-17', '2024-04-18']
}

df_customer = pd.DataFrame(customer)
df_orders = pd.DataFrame(orders)

# inner merge
# print = (pd.merge(
#     left=df_customer,
#     right=df_orders,
#     on='Customer ID',
#     how='inner'
# ))

# right merge
merged_df = pd.merge(
    left=df_customer,
    right=df_orders,
    on='Customer ID',
    how='right'
)

print(merged_df)
print("=============")
merged_df = pd.merge(
    left=df_orders,
    right=df_customer,
    on='Customer ID',
    how='right'
)
print(merged_df)

print(df_orders.merge(df_customer, how='left'))
