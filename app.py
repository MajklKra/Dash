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
                            html.Button
                            (
                                children=[
                                            html.Img(src='assets/nurse.svg',  # Vložte cestu k vašemu obrázku
                                            )
                                        ],
                                id='c1',
                            ),
                            html.Button
                            (
                                children=[
                                            html.Img(src='assets/caduceus.svg',  # Vložte cestu k vašemu obrázku
                                            )
                                        ],
                                id='c2',
                            ),
                            html.Button
                            (
                                html.Img(src='assets/nurse2.svg',  # Vložte cestu k vašemu obrázku
                                            ),
                                id='c3',
                            ),
                            html.Button
                            (
                                html.Img(src='assets/nurse3.svg',  # Vložte cestu k vašemu obrázku
                                        ),
                                id='c4',
                            )
                        ],   
                )
    
    ]
)

# ****************************************************************



if __name__ == '__main__':
    app.run_server(debug=True)

