# Enunciado del problema

A year's worth of sales from a fictitious pizza place, including the date
and time of each order and the pizzas served, with additional details 
on the type, size, quantity, price, and ingredients.
## Recommended Analysis

    How many customers do we have each day? Are there any peak hours?

    How many pizzas are typically in an order? Do we have any bestsellers?

    How much money did we make this year? Can we indentify any seasonality in the sales?

    Are there any pizzas we should take of the menu, or any promotions we could leverage?

Want feedback on your solutions?

    Share visualizations (and any applicable pivot tables, code, etc) on LinkedIn and mention @Maven Analytics. We would love to see your work and give our thoughts!

En españó
  * Número de clientes al día, cuál es la hora pico? 
  * Número de pizzas por pedido
  * Hay alguna que sea la más vendida?
  * Cuanto dinero hemos hecho este año?
  * Estacionalidad en los resultados?
    * Hay alguna pizza que deberíamos sacar del menú o alguna 
# Revisión del conjunto de datos:

* order_details.csv
  * order_details_id
  * order_id
  * pizza_id
  * quantity
* order.csv
  * order_id
  * date
  * time
* pizzas
  * pizza_type_id
  * size
  * price
* pizza_types: tipo de pizzas, las categorías y los ingredientes
  * pizza_type_id
  * name
  * category
  * ingredients
El fichero de pizza types no se puede abrir porque da un error de formato. 

### ¿Cómo lo arreglamos?

he abierto el documento con libre office y he creado el mismo sin el carácter problemático


# Datos a presentar en el dashboard

## 1ª Sección
una seccoón horizontal con tarjetas indicando los valores principales del año en el que 
se han recopilado los datos:

* Número de ventas
* Número de pizzas vendidas
* Dinero ganado
* Número medio de pizzas por pedido
* Día de la semana con más pedidos

## 2ª Sección

En esta sección se va a tener un selector por mes (o periodo?)

En el que se va a mostrar la información anterior junto con datos 
de ventas diarias