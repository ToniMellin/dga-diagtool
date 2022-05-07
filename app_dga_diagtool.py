# -*- coding: utf-8 -*-
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import numpy as np
import pandas as pd
from diagnostic import duval_triangle_1
from diagnostic import diagnostic_calculation
from diagnostic import typical_value_comparison
import webbrowser # autobrowser opening
from threading import Timer # autobrowser opening
import os # autobrowser opening

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

def open_browser():
    # function to open browser if not already running
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new('http://127.0.0.1:8050/')

def generate_table(dataframe):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), len(dataframe.index)))
        ])
    ])

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    
    html.H2('DGA diagtool\n'), #, style={'color': 'white', 'backgroundColor':'#003366'}
    

    html.Div([
    html.Br(),
    html.Label('Hydrogen (H2)'),    
    dcc.Input(id='h2-state', type='number'),

    html.Br(),
    html.Label('Methane (CH4)'),    
    dcc.Input(id='ch4-state', type='number'),

    html.Br(),
    html.Label('Ethane (C2H6)'),    
    dcc.Input(id='c2h6-state', type='number'),

    html.Br(),
    html.Label('Ethylene (C2H4)'),    
    dcc.Input(id='c2h4-state', type='number'),

    html.Br(),
    html.Label('Acetylene (C2H2)'),    
    dcc.Input(id='c2h2-state', type='number'),

    html.Div([
    html.Br(),
    html.Button(id='submit-button-state', n_clicks=0, children='Calculate')
    ], style={'padding': 10}),

    ], style={
            'display': 'inline-block',
            'vertical-align': 'top',
            'padding': 20
        }),

    html.Div([
    html.Br(),
    html.Label('Carbon monoxide (CO)'),
    dcc.Input(id='co-state', type='number'),

    html.Br(),
    html.Label('Carbon dioxide (CO2)'),
    dcc.Input(id='co2-state', type='number'),

    html.Br(),
    html.Label('Oxygen (O2) - Optional'), 
    dcc.Input(id='o2-state', type='number'),

    html.Br(),
    html.Label('Nitrogen (N2) - Optional'), 
    dcc.Input(id='n2-state', type='number'),

    html.Br(),
    html.Label('Transformer age (years) - Optional'), 
    dcc.Input(id='trafo-age-state', type='number')
    ], style={
            'display': 'inline-block',
            'vertical-align': 'top',
            'margin-left': '50px',
            'padding': 20
        }),

    html.Br(),
    html.Div(id='output-state')
    ], style={
            'display': 'inline-block',
            'vertical-align': 'top'
        })

@app.callback(Output('output-state', 'children'),
              [Input('submit-button-state', 'n_clicks')],
              [State('h2-state', 'value'),
               State('ch4-state', 'value'),
               State('c2h6-state', 'value'),
               State('c2h4-state', 'value'),
               State('c2h2-state', 'value'),
               State('co-state', 'value'),
               State('co2-state', 'value'),
               State('o2-state', 'value'),
               State('n2-state', 'value'),
               State('trafo-age-state', 'value')]
               )


def update_output(n_clicks, h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, o2_val, n2_val, trafo_age_val):
    r_list = diagnostic_calculation.calculate_ratios(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, o2_val, n2_val)
    df_ratio = pd.DataFrame({'Ratio': ['Ratio 1 (CH4/H2):', 'Ratio 2 (C2H2/C2H4):', 'Ratio 3 (C2H2/CH4):', 'Ratio 4 (C2H6/C2H2):', 'Ratio 5 (C2H4/C2H6):', 'Ratio 6 (CO2/CO):', 'Ratio 7 (O2/N2):'],
                            'Value': r_list}).round(2)
    try:
        diag_results = diagnostic_calculation.calculate_diagnostic_results(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val)
    except TypeError:
        print('diag TypeERROR')
        diag_results = ['-', '-', '-', '-']
    df_diag = pd.DataFrame({'Diagnostic method': ['Rogers ratio:', 'Doernenburg ratio:', 'IEC 60599:', 'Duval triangle 1:'], 'Result': diag_results})
    
    typical_results = typical_value_comparison.calculate_typical_results(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, o2_val, n2_val, trafo_age_val)
    df_typicals = pd.DataFrame({'Typical Values': ['IEC 60599, 90% typical values', 'IEEE C57.104-2008, typical values'], 
                                'H2': [typical_results[0][0], typical_results[1][0]], 
                                'CH4': [typical_results[0][1], typical_results[1][1]], 
                                'C2H6': [typical_results[0][2], typical_results[1][2]], 
                                'C2H4': [typical_results[0][3], typical_results[1][3]], 
                                'C2H2': [typical_results[0][4], typical_results[1][4]], 
                                'CO': [typical_results[0][5], typical_results[1][5]], 
                                'CO2': [typical_results[0][6], typical_results[1][6]],
                                'TDCG': [typical_results[0][7], typical_results[1][7]]
                                })


    return html.Div([
                    html.Div([
                        generate_table(df_ratio)], style={
                                                        'display': 'inline-block',
                                                        'vertical-align': 'top',
                                                        'padding': 20
                                                        }),
                    html.Div([
                        generate_table(df_diag)], style={
                                                        'display': 'inline-block',
                                                        'vertical-align': 'top',
                                                        'margin-left': '100px',
                                                        'padding': 20
                                                        }),

                    html.Br(),
                    html.Div([
                    generate_table(df_typicals)], style={'padding': 20}),

                    #TODO triangle 4 & 5 +styling for parallel triangles
                    html.Div([
                    dcc.Graph(figure=duval_triangle_1.create_duval1_result_graph(ch4_val, c2h2_val, c2h4_val))
                    ])
                    ])


if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run_server(debug=True)
