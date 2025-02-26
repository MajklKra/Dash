from dash import html, dcc, Output, Input, callback
from dash.dependencies import Input, Output

import mysql

def register_callbacks(app):

        @app.callback(Output('t1', 'children'),
        Input('submit-btn', 'n_clicks'),
        Input('db-input', 'value'))

        def databaze(n, fullname):


                jmeno = ""
                prijmeni = ""

                if n>0 and fullname !="":
                        

                        text = fullname.split()    

                        if len(text) > 0:
                                prijmeni = text[0]
                        else:
                                prijmeni = '""'

                        if len(text) > 1:
                                jmeno = text[1]
                        else:
                                jmeno = ''    

                        # Konfigurace připojení k MySQL databázi
                        db_config = {

                        # 'host': '172.16.0.9',        # Název nebo IP adresa serveru

                        'host': '172.30.0.10',         # Server číslo 2

                        'user': 'CODACOUSER',          # Uživatelské jméno MySQL
                        'password': 'trasq774JUMP',    # Heslo k databázi
                        'database': 'CodacoG2',        # Název databáze
                        'port': 3306                   # Port (standardně 3306)
                        }

                        conn = mysql.connector.connect(**db_config)
                        cursor = conn.cursor()
                        cursor.execute("SELECT * FROM Patients WHERE surname = %s AND name = %s", (prijmeni, jmeno))
                        data = cursor.fetchall()
                        cursor.close()
                        conn.close()

                        # Vytvoření záhlaví tabulky
                        table_header = ["PatientID", "PatientUniqueID", "SortOrder", "BedID" , "Jméno" , "Příjmení", "PatientTypeID", "CriticalPatient"]
                        header_row = html.Tr([html.Th(col) for col in table_header])

                        # Vytvoření těla tabulky
                        rows = [html.Tr([html.Td(cell) for cell in row]) for row in data]
                        
                        # Vytvoření tabulky
                        table = [html.Thead(header_row), html.Tbody(rows)]

                        return table

def layout():  
        
        return html.Div(
                className="db",  
                children=[
                    html.H1('Toto je stránka databáze '),
                    html.Br(),
                    html.Div( id = "cont1",
                            children=[
                                # dcc.Input(id='db-input', type='text', value='', placeholder='Příjmení pacienta'),
                                # html.Br(),
                                # html.Button('Odeslat', id='submit-btn', n_clicks=0),
                                # html.Br(),

                                html.Div( id = "cont3",
                                children=[
                                        dcc.Input(id='db-input', type='text', value='', placeholder='Příjmení pacienta'),
                                        html.Br(),
                                        html.Button('Odeslat', id='submit-btn', n_clicks=0),
                                        html.Br(),
                                ]
                            )
                        ]
                    ),
                    html.Br(),
                    html.H1('Tabulka'),
                    html.Br(),
                    html.Div( id = "cont2",
                            children=[
                                html.Div(id='output-div2'),
                                html.Table(id="t1")
                            ]
                    )
                ]
        )