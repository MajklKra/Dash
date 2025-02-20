import dash
from dash import html

from datetime import datetime  # aktuální čas a datum

app = dash.Dash(__name__)

# *********************** Prvni pokus **************************

# app.layout = html.Div( id= 'hc', 
#     children=[
#         html.Div(
#             children='Toto je vnitřní div.',
#             id='c1',
#         ),
#         html.Div(
#             children='Toto je vnitřní div.',
#             id='c2',
#         ),
#         html.Div(
#             children='Toto je vnitřní div.',
#             id='c3',
#         ),
#         html.Div(
#             children='Toto je vnitřní div.',
#             id='c4',
#         )
#     ]
# )

# *********************** Druhý pokus **************************


# ---------------------- Čas --------------------------------------------------------------

aktualni_cas = datetime.now()

formatovany_cas = aktualni_cas.strftime("%Y-%m-%d %H:%M:%S")

cas = aktualni_cas.strftime("%H:%M")

datum = aktualni_cas.strftime("%d.%m.%Y")

# Získání dne v týdnu (0 = pondělí, 6 = neděle)
den_v_tydnu = aktualni_cas.weekday()

# Převod čísla dne na název
dny = ["Pondělí", "Úterý", "Středa", "Čtvrtek", "Pátek", "Sobota", "Neděle"]
nazev_dne = dny[den_v_tydnu]

# ------------------------------------------------------------------------------------


# Definování SVG jako řetězec s možností měnit barvy
svg_string = '''
<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
    <circle cx="50" cy="50" r="40" style="fill:red; stroke:blue; stroke-width:5;" />
</svg>
'''



app.layout = html.Div(
    
        id = 'hc1',

        children = [

                html.Div([
                    html.Span("KF1", style={"font-weight": "bold", "color": "White", "font-size": "22px", "margin-right": "20px"}),
                    "Oddělení Kufr HCC-20"],
                    id = 'p1'),

                html.Div([

                                html.Span(f"{nazev_dne} {datum}", id = "sp1"),
                                html.Br(),
                                html.Span(f"{cas}", id = "sp2"),
                                html.Br(),
                                html.Span('Místnost sester 2', id = "sp3")
                            ],
                            id = 'p2',
                ),

                html.Div(

                        id= 'p3',
                        children = 
                        [
                            html.Div
                            (
                                children=[
                                            html.Img(src='assets/nurse.svg',  # Vložte cestu k vašemu obrázku
                                            style={
                                                'filter': 'brightness(0) saturate(100%) invert(39%) sepia(98%) saturate(5264%) hue-rotate(20deg)',  # Změní barvu obrázku
                                                'width': '100%',  # Změňte velikost podle potřeby
                                                'height': '100%',
                                                'object-fit' : 'contain'})
                                        ],
                                id='c1',
                            ),
                            html.Div
                            (
                                children=[
                                            html.Img(src='assets/caduceus.svg',  # Vložte cestu k vašemu obrázku
                                            style={
                                                'filter': 'brightness(0) saturate(100%) invert(30%) sepia(70%) saturate(5597%) hue-rotate(208deg) brightness(93%) contrast(101%)',  # Změní barvu obrázku
                                                'width': '100%',  # Změňte velikost podle potřeby
                                                'height': '100%',
                                                'object-fit' : 'contain'})
                                        ],
                                id='c2',
                            ),
                            html.Div
                            (
                                html.Img(src='assets/nurse2.svg',  # Vložte cestu k vašemu obrázku
                                            style={
                                                'filter': 'brightness(0) saturate(100%) invert(96%) sepia(75%) saturate(7489%) hue-rotate(337deg) brightness(95%) contrast(109%)',  # Změní barvu obrázku
                                                'width': '100%',  # Změňte velikost podle potřeby
                                                'height': '100%',
                                                'object-fit' : 'contain'}),
                                id='c3',
                            ),
                            html.Div
                            (
                                html.Img(src='assets/nurse3.svg',  # Vložte cestu k vašemu obrázku
                                            style={
                                                'filter': 'brightness(0) saturate(100%) invert(34%) sepia(56%) saturate(1095%) hue-rotate(78deg) brightness(105%) contrast(83%)',  # Změní barvu obrázku
                                                'width': '100%',  # Změňte velikost podle potřeby
                                                'height': '100%',
                                                'object-fit' : 'contain'}),
                                id='c4',
                            )
                        ],   
                )
    
    ]
)

# ****************************************************************



if __name__ == '__main__':
    app.run_server(debug=True)

