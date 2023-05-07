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
    dbc.Row(
            [
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
            ]
        ),
    dbc.Row([
        dbc.Col(card21, width=4),
        dbc.Col(card21, width=4),
        dbc.Col(card21, width=4)
    ],id='second-row'),
],id = 'mainContainer')

