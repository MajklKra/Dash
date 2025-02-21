import dash
from dash import html

dash.register_page(__name__, path="/btn2_page")

layout = html.Div([
    html.H1("Toto je stránka 2"),
    html.P("Obsah druhé stránky."),
])
