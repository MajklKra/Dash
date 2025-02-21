import dash
from dash import html


def layout(): 
        return html.Div(
                className="page2",  

                children = [
                    html.H1('Toto je stránka č. 2'),
                    html.P('Ať žije Framework Dash a Python !'),

                    html.P('tohle je fakt konec !!!' )
                ]
                )
