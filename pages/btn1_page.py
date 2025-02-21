import dash
from dash import html

dash.register_page(__name__, path="/btn1_page")

layout = html.Div([
    html.H1("Toto je stránka 1"),
    html.P("Obsah první stránky."),
])