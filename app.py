import dash
from dash import dcc, html, Input, Output
from pages.page_1 import layout as page_1_layout
from pages.page_2 import layout as page_2_layout
from pages.home import layout as home_layout
from pages.page_3 import layout as page_3_layout
from pages.page_4 import layout as page_4_layout
import ssl

app = dash.Dash(__name__, suppress_callback_exceptions=True)  # Přidání suppress_callback_exceptions

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Funkce pro načítání obsahu na základě URL
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))

def display_page(pathname):
    if pathname == '/' or pathname is None:  # Pokud je prázdná, jdeme na '/pokus'
        return home_layout()

    elif pathname == '/page1':
        return page_1_layout()  # Načtení obsahu z page_1.py
    
    elif pathname == '/page2':
        return page_2_layout()  # Načtení obsahu z page_2.py
    
    elif pathname == '/page3':
        return page_3_layout()  # Načtení obsahu z page_2.py
    
    elif pathname == '/page4':
        return page_4_layout()  # Načtení obsahu z page_2.py
    
if __name__ == '__main__':
    app.run_server(host="0.0.0.0",port=8080,debug=True, ssl_context='adhoc')


