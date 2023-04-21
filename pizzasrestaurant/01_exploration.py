import pandas as pd

df_dictionary = pd.read_csv('Pizza+Place+Sales/data_dictionary.csv')

print(df_dictionary.head())

df_dictionary.info()

df_pizza_types = pd.read_csv('Pizza+Place+Sales/pizza_sales/pizza_types_corregido.csv')

df_pizza_types.info()
print(f"Tipos de pizza únicos {df_pizza_types.name.nunique()} \n")

print(df_pizza_types.pizza_type_id.unique())
print(f"Catgorías diferentes de pizzas {df_pizza_types.category.unique()}")

## REVISIÓN DE ORDERS

df_orders = pd.read_csv('Pizza+Place+Sales/pizza_sales/orders.csv')

df_orders.info()
print(df_orders.head(10))

print(f"Número de ordenes recibidas: {df_orders.shape[0]}")