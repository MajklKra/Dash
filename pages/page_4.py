import dash
from dash import html


def layout(): 
        return html.Div(
                
                    className = "page4",

                    children=[
                
                    html.H1('Toto je stránka č. 4'),
                    html.P(' Hello World bez Trumpa !!!!'),

                    html.P('tohle je fakt konec !!!' )
                ])
