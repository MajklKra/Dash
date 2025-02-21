# home.py
import dash
from dash import html, dcc, State, callback
from dash.dependencies import Input, Output 

from datetime import datetime  # aktuální čas a datum

# dash.register_page(__name__, path='/')  # Registrace domovské stránky


# ********************************** EXPERIMENT *****************************************

# import dash
# from dash import html

# def layout():
#     return html.Div([
#         html.H1('O nás'),
#         html.P('Toto je stránka O nás.'),

#         html.P('tohle je fakt konec !!!' )
#     ])



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


def layout():  
    
    return html.Div(

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

                    # dcc.Link(
                    #     html.Button(
                    #         children=[
                    #             html.Img(src='assets/nurse.svg', id='img1')
                    #         ],
                    #         id='c1',
                    #         className='',
                    #         style={'background-color' : 'yellow'}
                    #     ),
                    #     href='/o-nas',  # URL, kam se má navigovat
                    #     style = {'background-color' : 'red', 'height': '100%', 'width' : '100%', 'display':'flex', 'flex-direction' : 'row', 
                    #              'align-items': 'flex-end', 'justify-content' : 'space-evenly', 'padding-bottom': '5%'}
                    # ),
         
                    html.Button
                    (
                        children=[
                                    # html.Img(src='assets/nurse.svg', id = 'img1',),
                                    html.A(html.Img(src='assets/nurse.svg', id = 'img1',), href='/page1', style={'color': 'yellow'})
                                ],
                      
                        id='c1',
                        className='',
                    ),
                    html.Button
                    (
                        children=[
                                    # html.Img(src='assets/caduceus.svg', id = 'img2')
                                    html.A( html.Img(src='assets/caduceus.svg', id = 'img2'), href='/page2', style={'color': 'yellow'})
                                ],
                        id='c2',
                        className='',
                    ),
                    html.Button
                    (
                        children=[
                                    # html.Img(src='assets/nurse2.svg',  id = 'img3'),
                                    html.A( html.Img(src='assets/nurse2.svg',  id = 'img3'), href='/page3', style={'color': 'yellow'})
                                ],
                        id='c3',
                        className='',
                    ),
                    html.Button
                    (
                        children=[
                                
                                # html.Img(src='assets/nurse3.svg',  id = 'img4'),
                                html.A( html.Img(src='assets/nurse3.svg',  id = 'img4'), href='/page4', style={'color': 'yellow'})
                            ],
                        id='c4',
                        className='',
                    )

                ],  
      
            )
        ]
    )

# ************************** Experiment  **************************

@callback(
    Output('c1', 'className'),
    Output('c2', 'className'),
    Output('c3', 'className'),
    Output('c4', 'className'),

    Input('c1', 'n_clicks'),
    Input('c2', 'n_clicks'),
    Input('c3', 'n_clicks'),
    Input('c4', 'n_clicks'),

    prevent_initial_call=True
)

def toggle_class(n_clicks1, n_clicks2, n_clicks3, n_clicks4):
    # Urči stavy pro jednotlivá tlačítka
    classes = ['', '', '', '']
    
    # Změna tříd na základě počtu kliknutí
    if n_clicks1 is not None and n_clicks1 % 2 == 1:
        classes[0] = 'active-btn'
    if n_clicks2 is not None and n_clicks2 % 2 == 1:
        classes[1] = 'active-btn2'
    if n_clicks3 is not None and n_clicks3 % 2 == 1:
        classes[2] = 'active-btn3'
    if n_clicks4 is not None and n_clicks4 % 2 == 1:
        classes[3] = 'active-btn4'
    
    return classes

# ************************ Změna obrázků v kontejneru *************************************


@callback(
    Output('img1', 'className'),
    Output('img2', 'className'),
    Output('img3', 'className'),
    Output('img4', 'className'),
    Input('c1', 'n_clicks'),
    Input('c2', 'n_clicks'),
    Input('c3', 'n_clicks'),
    Input('c4', 'n_clicks'),
    prevent_initial_call=True
)

def toggle_image_class(n_clicks1, n_clicks2, n_clicks3, n_clicks4):
    classes = ['', '', '', '']

    if n_clicks1 is not None and n_clicks1 % 2 == 1:
        classes[0] = 'active-img'
    if n_clicks2 is not None and n_clicks2 % 2 == 1:
        classes[1] = 'active-img2'
    if n_clicks3 is not None and n_clicks3 % 2 == 1:
        classes[2] = 'active-img3'
    if n_clicks4 is not None and n_clicks4 % 2 == 1:
        classes[3] = 'active-img4'

    return classes