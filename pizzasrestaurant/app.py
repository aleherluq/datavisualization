import pandas as pd
from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc

# Carga de datos
# Datos de los diferentes tipos de pizzas
df_pizza_types = pd.read_csv('Pizza+Place+Sales/pizza_sales/pizza_types_corregido.csv')

#Pedidos -> se supone un pedido por cliente
df_orders = pd.read_csv('Pizza+Place+Sales/pizza_sales/orders.csv')

#Pizzas -> info del tamaño de la pizza con el tipo y el precio
df_pizzas = pd.read_csv('Pizza+Place+Sales/pizza_sales/pizzas.csv')

# Detalle de los pedidos
df_order_details = pd.read_csv('Pizza+Place+Sales/pizza_sales/order_details.csv')

# Tratamiento de datos
# Unión de las tablas
df_detail_order = pd.merge(df_order_details, df_orders, how='left', left_on='order_id', right_on='order_id')
df_detail_order_pizza = pd.merge(df_detail_order, df_pizzas, how='left', on='pizza_id')
df_detail_order_pizza_types = pd.merge(df_detail_order_pizza, df_pizza_types, how='left', on='pizza_type_id')
df_detail_order_pizza_types['order_price'] = df_detail_order_pizza_types['quantity']*df_detail_order_pizza_types['price']
# día semana
df_detail_order_pizza_types['fecha'] = pd.to_datetime(df_detail_order_pizza_types['date'])
#df_detail_order_pizza_types['dia_sem'] = df_detail_order_pizza_types['fecha'].dt.day_name()
df_detail_order_pizza_types['dia_semana'] = pd.to_datetime(df_detail_order_pizza_types['fecha']).dt.day_name(locale='es_ES.utf8')
#df_detail_order_pizza_types['num_dia_semana'] = df_detail_order_pizza_types['dia_semana'].map(dict_dia_semana)
df_detail_order_pizza_types['año']= df_detail_order_pizza_types['fecha'].dt.year
df_detail_order_pizza_types['mes']= df_detail_order_pizza_types['fecha'].dt.month
df_detail_order_pizza_types['mes_nombre']= df_detail_order_pizza_types['fecha'].dt.month_name(locale='es_ES.utf8')

df_detail_order_pizza_types['dia']= df_detail_order_pizza_types['fecha'].dt.day


## Ventas totales
vt = df_detail_order_pizza_types['order_price'].sum()
media_y = vt/12
##Agrupar por meses
ventas_mes = df_detail_order_pizza_types.groupby(['mes', 'mes_nombre'])['order_price'].sum()
venta_max_mes = ventas_mes.idxmax()[1]

## mejor mes


# Definir alguno de los componentes que se van a usar

card21 = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Ingresos Anuales", className="card-title"),
            html.P(str(round(vt/1000, 2)) + 'k €'),
            html.P('Media anual: '+ str(round(media_y/1000,2)) + ' k€ al mes')

        ]
    )
)
card22 = dbc.Card([
    dbc.CardBody(
        [
            html.H5("Mejores mes" + str(ventas_mes.idxmax()[1]), className="card-title"),
            html.P(str(round((ventas_mes.max())/1000, 2)) + 'k €'),
            html.P(str(round((( ventas_mes.max()-media_y)/media_y)*100, 2)) + ' %'),

        ]
    )
])
card23 = dbc.Card([])
## DASH

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout =html.Div([

    dbc.Row([
        html.Div([
            html.Div([
                html.H3('Pizza Restaurant', style={'margin-bottom': '0px', 'color': 'red'}),
                html.H5('2019 Analysis', style={'margin-bottom': '0px', 'color': 'black'})
            ])

        ], className='one-half column', id = 'title'),

    ], id='header', className= 'row flex-display', style={'margin-bottom': '25px'}),

    ## Contenido de la primera franja relacionada con los  datos genéricos

    dbc.Row([
        dbc.Col(card21, width=2),
        dbc.Col(card22, width=2),
        dbc.Col(card21, width=2)
    ],id='second-row', className='d-flex justify-content-center'),
],id = 'mainContainer')
if __name__ == '__main__':
    app.run_server(debug=True, port=8051)