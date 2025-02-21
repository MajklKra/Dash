import dash
from dash import html


def layout(): 
        return html.Div(
                    className="page3",

                    children = [
                
                        html.H1('Toto je stránka č. 3'),
                        html.P(' Hello World bez Putina!!!'),

                        html.P('tohle je fakt konec !!!' )
                ])