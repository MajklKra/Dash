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


# Získejte počáteční čas
aktualni_cas = datetime.now()
datum = aktualni_cas.strftime("%d.%m.%Y")
cas = aktualni_cas.strftime("%H:%M")

# Získání dne v týdnu
den_v_tydnu = aktualni_cas.weekday()
dny = ["Pondělí", "Úterý", "Středa", "Čtvrtek", "Pátek", "Sobota", "Neděle"]
nazev_dne = dny[den_v_tydnu]

# ----------------------   Experiment ----------------------------------------------------------


# Callback pro aktualizaci času
@callback(
    Output('sp2', 'children'),  # Aktualizujeme sp2
    Input('interval-component', 'n_intervals')
)

def update_time(n):
    aktualni_cas = datetime.now()
    cas = aktualni_cas.strftime("%H:%M")
    return cas

# --------------------------------------------------------------------------------------------

def layout():  

    return html.Div(

id = 'hc1',

children = [

        # html.Div([
        #     html.Span("KF1", style={"font-weight": "bold", "color": "White", "font-size": "22px", "margin-right": "20px"}),
        #     "Oddělení Kufr HCC-20"],
        #     id = 'p1'),

        # html.Div([

        #                 html.Span(f"{nazev_dne} {datum}", id = "sp1"),
        #                 html.Br(),
        #                 html.Span(f"{cas}", id = "sp2"),
        #                 html.Br(),
        #                 html.Span('Místnost sester 2', id = "sp3")
        #             ],
        #             id = 'p2',
        # ),


        html.Div([
                html.Span("KF1", style={"font-weight": "bold", "color": "White", "font-size": "22px", "margin-right": "20px"}),
                "Oddělení Kufr HCC-20"],
                id='p1'),
            html.Div([
                html.Span(f"{nazev_dne} {datum}", id="sp1"),
                html.Br(),
                html.Span(id="sp2"),  # Změna id na sp2, kde se bude aktualizovat čas
                html.Br(),
                html.Span('Místnost sester 2', id="sp3")
            ], id='p2'),
            # Přidání komponenty Interval pro pravidelnou aktualizaci
            dcc.Interval(
                id='interval-component',
                interval=1*1000,  # 1 sekunda v milisekundách
                n_intervals=0,  # Počáteční počet intervalů
            ),

            dcc.Interval(
                id='interval-component2',
                interval=1*750,  # 1 sekunda v milisekundách
                n_intervals=0,  # Počáteční počet intervalů
                # disabled=True
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
                                    # html.A(html.Img(src='assets/nurse.svg', id = 'img1',), href='/page1', style={'color': 'yellow'})
                                    html.A(html.Img(src='assets/nurse.svg', id = 'img1',))
                                ],
                      
                        id='c1',
                        className='',
                        style={'backgroundColor': 'transparent', 'border': 'none'}
                    ),
                    html.Button
                    (
                        children=[
                                    # html.Img(src='assets/caduceus.svg', id = 'img2')
                                    html.A( html.Img(src='assets/caduceus.svg', id = 'img2'), href='/page2')
                                ],
                        id='c2',
                        className='',
                    ),
                    html.Button
                    (
                        children=[
                                    # html.Img(src='assets/nurse2.svg',  id = 'img3'),
                                    html.A( html.Img(src='assets/nurse2.svg',  id = 'img3'), href='/key')
                                ],
                        id='c3',
                        className='',
                    ),
                    html.Button
                    (
                        children=[
                                
                                # html.Img(src='assets/nurse3.svg',  id = 'img4'),
                                html.A( html.Img(src='assets/nurse3.svg',  id = 'img4'), href='/db')
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


# ************************ Experiment Blikacka *************************************

@callback(
    [Output('c1', 'style'),
     Output('img1', 'style'),
     Input('interval-component2', 'n_intervals')]
)

def update_button(n):

    print(f"Interval count: {n}")

    if n == 0:  # Pokud je n 0, znamená to, že interval je zakázán
        return {'backgroundColor': 'white', 'border': 'none'}, {'filter': ' brightness(0) saturate(100%) invert(27%) sepia(50%) saturate(5281%) hue-rotate(349deg) brightness(88%) contrast(85%)'}

    if n % 2 == 0:  # Změna barvy každé 2 intervaly (tj. každou sekundu)
        button_style = {'backgroundColor':'red', 'border': 'none'}
        img_style = {'filter': 'invert(100%)'}
    else:
        button_style = {'backgroundColor': 'white', 'border': 'none'}
        img_style = {'filter': ' brightness(0) saturate(100%) invert(27%) sepia(50%) saturate(5281%) hue-rotate(349deg) brightness(88%) contrast(85%)'}


    # print(f"Button style: {button_style}, Image style: {img_style}") 

    return button_style, img_style


@callback(
    Output('interval-component2', 'disabled'),
    Input('c1', 'n_clicks'),
    State('interval-component2', 'disabled')
)

def toggle_interval(n_clicks, disabled):
    if n_clicks == 0:
        # Pokud bylo tlačítko nikdy nekliknuto, ponechejte interval zakázaný
        return True
    # Při každém kliknutí přepněte stav disabled
    return not disabled


@callback(
    Output('interval-component2', 'n_intervals'),
    Input('interval-component', 'disabled'),
    State('interval-component2', 'n_intervals')
)
def reset_interval(disabled, n):
    if disabled:
        return 0  # Resetuje n_intervals, pokud je interval zakázaný
    return n  # Jinak vrátí aktuální n_interval
 
