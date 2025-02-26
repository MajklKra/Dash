
import dash
from dash import dcc, html, Input, Output, State
import mysql

def register_callbacks2(app):

    @app.callback(
              
        Output('input-box', 'value'),
        [Input(f'key-{char}', 'n_clicks') for char in "qwertyuiopasdfghjklzxcvbnm"] + 
        [Input('clear-button', 'n_clicks')],
        [State('input-box', 'value'), State('toggle-case-button', 'n_clicks')]

    )

    def update_output(*args):
        ctx = dash.callback_context
        if not ctx.triggered:
            return dash.no_update

        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if button_id == 'clear-button':
            return ''

        new_character = button_id.split('-')[1]  
        is_upper = args[-1] % 2 == 1  # Každé liché kliknutí přepíná mezi velkými/malými písmeny

        if is_upper:
            new_character = new_character.upper()
        else:
            new_character = new_character.lower()

        current_text = args[-2] if args[-2] else ''
        
        return current_text + new_character
    

    # Přidání dalšího callbacku, který používá výstup z update_output
    @app.callback(
        Output('t2', 'children'),  # Změňte na skutečný komponent
        Input('input-box', 'value')
        # [State('input-box', 'value')]
    )
    def use_update_output(input_value):
        # Logika pro použití výstupu z update_output
        # Například, můžete nějak zpracovat input_value a vrátit nový obsah


        # Konfigurace připojení k MySQL databázi
        db_config = {

        # 'host': '172.16.0.9',        # Název nebo IP adresa serveru

        'host': '172.30.0.10',         # Server číslo 2

        'user': 'CODACOUSER',          # Uživatelské jméno MySQL
        'password': 'trasq774JUMP',    # Heslo k databázi
        'database': 'CodacoG2',        # Název databáze
        'port': 3306                   # Port (standardně 3306)
        }

        if input_value != "":
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute("SELECT surname, name FROM Patients WHERE surname LIKE %s", (f'{input_value}%',))
            data = cursor.fetchall()
            cursor.close()
            conn.close()

            # Vytvoření záhlaví tabulky
            table_header = ["Příjmení", "Jméno"]
            header_row = html.Tr([html.Th(col) for col in table_header])

            # Vytvoření těla tabulky
            rows = [html.Tr([html.Td(cell) for cell in row]) for row in data]
            
            # Vytvoření tabulky
            table = [html.Thead(header_row), html.Tbody(rows)]

            return table
        
        else:

            return ""


def layout():  
        
        return html.Div(id = "hlavni", 
                children=[
                          
                    html.Div(id='keyboard', children=[

                        dcc.Input(id='input-box', type='text', value=''),
                     
                        html.Div(className='row', children=[
                            html.Button(char.upper(), id=f'key-{char}', n_clicks=0, className='key') for char in "qwertyuiop"
                        ]),
                        html.Div(className='row', children=[
                            html.Button(char.upper(), id=f'key-{char}', n_clicks=0, className='key') for char in "asdfghjkl"
                        ]),
                        html.Div(className='row', children=[
                            html.Button(char.upper(), id=f'key-{char}', n_clicks=0, className='key') for char in "zxcvbnm"
                        ]),

                        html.Div(className='row', children=[
                            html.Button('Vymazat', id='clear-button', n_clicks=0, className='key clear-btn'),
                            html.Button('A/a', id='toggle-case-button', n_clicks=0, className='key clear-btn')
                        ]),

                    ]),
                        
                    html.Div(id='keyboard2', children=[

                        html.Div( children=[
                            html.Button
                                (
                                    children=[
                                                # html.Img(src='assets/return.svg',),  
                                                html.A( html.Img(src='assets/return.svg',), href='/')    
                                            ],
                                    id='btn-return', title = "Cesta tam a zpět"
                                ),
                            ],id='c-btn-return'), 

                        html.Div(id='display', children=[
                            html.Table(id="t2")
                        ]),

                    ]),
            ])


