# -*- coding: utf-8 -*-
import os # autobrowser opening
from threading import Timer # autobrowser opening
import webbrowser
from zipfile import is_zipfile # autobrowser opening

import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import numpy as np
import pandas as pd

from diagnostic import duval_triangle_1
from diagnostic import duval_triangle_4
from diagnostic import duval_triangle_5
from diagnostic import diagnostic_calculation
from diagnostic import typical_value_comparison

# TODO add theme changing https://hellodash.pythonanywhere.com/theme_change_components

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
dbc_css = "bootstrap.min.css"

def open_browser():
    """function to open browser if not already running"""
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new('http://127.0.0.1:8050/')

def generate_table(dataframe):
    """function to generate a Dash html table from given dataframe"""
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




app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css] )

# ======= InputGroup tooltips =============================================

h2_tooltip = """Hydrogen (H2) dissolved gas value in ppm."""

ch4_tooltip = """Methane (CH4) dissolved gas value in ppm."""

c2h6_tooltip = """Ethane (C2H6) dissolved gas value in ppm."""

c2h4_tooltip = """Ethylene (C2H4) dissolved gas value in ppm."""

c2h2_tooltip = """Acetylene (C2H2) dissolved gas value in ppm."""

co_tooltip = """Carbon monoxide (CO) dissolved gas value in ppm."""

co2_tooltip = """Carbon dioxide (CO2) dissolved gas value in ppm. Does not affect included diagnostic method results."""

o2_tooltip = """Oxygen (O2) dissolved gas value in ppm. 
                Oxygen value only affects IEEE C57.104-2019 typical value comparison. 
                If left empty, free breathing transformer design assumed and used as basis for comparison."""

n2_tooltip = """Nitrogen (N2) dissolved gas value in ppm.
                Nitrogen value only affects IEEE C57.104-2019 typical value comparison. 
                If left empty, free breathing transformer design assumed and used as basis for comparison."""

trafo_age_tooltip = """Transformer age (years). 
                    Transformer age only affects IEEE C57.104-2019 typical value comparison.
                    If left empty, \"Unknown\" used as basis for comparison."""

# ======= InputGroup components ===========================================

h2_input = dbc.InputGroup(
    [
        dbc.InputGroupText("Hydrogen (H2)"),
        dbc.Input(
            id="h2-state",
            type="number",
            min=0,
            max=1000000,
        ),
        dbc.Tooltip(h2_tooltip, target="h2-state"),
    ],
    className="mb-3",
)
ch4_input = dbc.InputGroup(
    [
        dbc.InputGroupText("Methane (CH4)"),
        dbc.Input(
            id="ch4-state",
            type="number",
            min=0,
            max=1000000,
        ),
        dbc.Tooltip(ch4_tooltip, target="ch4-state"),
    ],
    className="mb-3",
)
c2h6_input = dbc.InputGroup(
    [
        dbc.InputGroupText("Ethane (C2H6)"),
        dbc.Input(
            id="c2h6-state",
            type="number",
            min=0,
            max=1000000,
        ),
        dbc.Tooltip(c2h6_tooltip, target="c2h6-state"),
    ],
    className="mb-3",
)
c2h4_input = dbc.InputGroup(
    [
        dbc.InputGroupText("Ethylene (C2H4)"),
        dbc.Input(
            id="c2h4-state",
            type="number",
            min=0,
            max=1000000,
        ),
        dbc.Tooltip(c2h4_tooltip, target="c2h4-state"),
    ],
    className="mb-3",
)
c2h2_input = dbc.InputGroup(
    [
        dbc.InputGroupText("Acetylene (C2H2)"),
        dbc.Input(
            id="c2h2-state",
            type="number",
            min=0,
            max=1000000,
        ),
        dbc.Tooltip(c2h2_tooltip, target="c2h2-state"),
    ],
    className="mb-3",
)
co_input = dbc.InputGroup(
    [
        dbc.InputGroupText("Carbon monoxide (CO)"),
        dbc.Input(
            id="co-state",
            type="number",
            min=0,
            max=1000000,
        ),
        dbc.Tooltip(co_tooltip, target="co-state"),
    ],
    className="mb-3",
)
co2_input = dbc.InputGroup(
    [
        dbc.InputGroupText("Carbon dioxide (CO2)"),
        dbc.Input(
            id="co2-state",
            type="number",
            min=0,
            max=1000000,
        ),
        dbc.Tooltip(co2_tooltip, target="co2-state"),
    ],
    className="mb-3",
)
o2_input = dbc.InputGroup(
    [
        dbc.InputGroupText("Oxygen (O2)"),
        dbc.Input(
            id="o2-state",
            type="number",
            min=0,
            max=1000000,
        ),
        dbc.Tooltip(o2_tooltip, target="o2-state"),
    ],
    className="mb-3",
)
n2_input = dbc.InputGroup(
    [
        dbc.InputGroupText("Nitrogen (N2)"),
        dbc.Input(
            id="n2-state",
            type="number",
            min=0,
            max=1000000,
        ),
        dbc.Tooltip(n2_tooltip, target="n2-state"),
    ],
    className="mb-3",
)
trafo_age_input = dbc.InputGroup(
    [
        dbc.InputGroupText("Transformer age (years)"),
        dbc.Input(
            id="trafo-age-state",
            type="number",
            min=0,
            max=1000000,
        ),
        dbc.Tooltip(trafo_age_tooltip, target="trafo-age-state"),
    ],
    className="mb-3",
)
input_groups = html.Div(
    [h2_input, ch4_input, c2h6_input, c2h4_input, c2h2_input, co_input, co2_input, o2_input, n2_input, trafo_age_input],
    className="mt-4 p-4",
)
submit_button = html.Div([
                    html.Button(id='submit-button-state', n_clicks=0, children='Calculate')
                    ], style={'padding': 10})

# ======= Tables ==========================================================
'''
df_ratio = pd.DataFrame({'Ratio': ['Ratio 1 (CH4/H2):', 'Ratio 2 (C2H2/C2H4):', 'Ratio 3 (C2H2/CH4):', 'Ratio 4 (C2H6/C2H2):', 'Ratio 5 (C2H4/C2H6):', 'Ratio 6 (CO2/CO):', 'Ratio 7 (O2/N2):'],
                            'Value': []})

df_ratio_table = dbc.Table.from_dataframe(df_ratio, striped=True, bordered=True, hover=True)
'''
# ======= Main layout

app.layout = dbc.Container(
    [

    dbc.Row(
            dbc.Col(
                html.H2("DGA diagtool", className="text-center bg-secondary text-white p-2"),
            )
    ),
    dbc.Row([
            dbc.Col([input_groups, submit_button], width=12, lg=4, className="mt-4 border"),
            dbc.Col([html.Div(id='ratio-output-state'), html.Div(id='diagmethod-output-state')], width=12, lg=8, className="mt-4 border"),

    ]),
    dbc.Row(
            dbc.Col([html.Div(id='typicals-output-state')], className="mt-4"),
    ),
    dbc.Row(
            dbc.Col([html.Div(id='duval-output-state')], className="mt-4"),
    ),

    ],fluid=True,
    )

# ======= Callbacks =======================================================

@app.callback(Output('ratio-output-state', 'children'),
                Output('diagmethod-output-state', 'children'),
                Output('typicals-output-state', 'children'),
                Output('duval-output-state', 'children'),
                Input('submit-button-state', 'n_clicks'),
                State('h2-state', 'value'),
                State('ch4-state', 'value'),
                State('c2h6-state', 'value'),
                State('c2h4-state', 'value'),
                State('c2h2-state', 'value'),
                State('co-state', 'value'),
                State('co2-state', 'value'),
                State('o2-state', 'value'),
                State('n2-state', 'value'),
                State('trafo-age-state', 'value')
               )
def update_output(n_clicks, h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, o2_val, n2_val, trafo_age_val):
    """Updates the dash app output, including duval triangle graphs, typical value and the diagnostic result tables"""
    r_list = diagnostic_calculation.calculate_ratios(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, o2_val, n2_val)
    df_ratio = pd.DataFrame({'Ratio': ['Ratio 1 (CH4/H2):', 'Ratio 2 (C2H2/C2H4):', 'Ratio 3 (C2H2/CH4):', 'Ratio 4 (C2H6/C2H2):', 'Ratio 5 (C2H4/C2H6):', 'Ratio 6 (CO2/CO):', 'Ratio 7 (O2/N2):'],
                            'Value': r_list})
    ratio_table = dbc.Table.from_dataframe(df_ratio, striped=True, bordered=True, hover=True)
    
    try:
        diag_results = diagnostic_calculation.calculate_diagnostic_results(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val)
    except TypeError:
        print('diag TypeERROR')
        diag_results = ['-', '-', '-', '-', '-', '-']

    df_diag = pd.DataFrame({'Diagnostic method': ['Rogers ratio:', 'Doernenburg ratio:', 'IEC 60599:', 'Duval triangle 1:', 'Duval triangle 4:', 'Duval triangle 5:'], 'Result': diag_results})
    diagresults_table = dbc.Table.from_dataframe(df_diag, striped=True, bordered=True, hover=True)

    typical_results = typical_value_comparison.calculate_typical_results(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, o2_val, n2_val, trafo_age_val)
    df_typicals = pd.DataFrame({'Typical Values': ['IEC 60599, typical values', 'IEEE C57.104-2008, typical values', 'IEEE C57.104-2019, typical values'], 
                                'H2': [typical_results[0][0], typical_results[1][0], typical_results[2][0]], 
                                'CH4': [typical_results[0][1], typical_results[1][1], typical_results[2][1]], 
                                'C2H6': [typical_results[0][2], typical_results[1][2], typical_results[2][2]], 
                                'C2H4': [typical_results[0][3], typical_results[1][3], typical_results[2][3]], 
                                'C2H2': [typical_results[0][4], typical_results[1][4], typical_results[2][4]], 
                                'CO': [typical_results[0][5], typical_results[1][5], typical_results[2][5]], 
                                'CO2': [typical_results[0][6], typical_results[1][6], typical_results[2][6]],
                                'TDCG': ['-', typical_results[1][7], '-']
                                })
    typicals_table = dbc.Table.from_dataframe(df_typicals, striped=True, bordered=True, hover=True)

    if diag_results[3] in ['PD', 'T1', 'T2']:
        duval4 = dcc.Graph(figure=duval_triangle_4.create_duval_4_result_graph(h2_val, c2h6_val, ch4_val))
    else:
        duval4 = dcc.Graph(figure=duval_triangle_4.create_duval_4_colorized())

    if diag_results[3] in ['T2', 'T3']:
        duval5 = dcc.Graph(figure=duval_triangle_5.create_duval_5_result_graph(ch4_val, c2h6_val, c2h4_val))
    else:
        duval5 = dcc.Graph(figure=duval_triangle_5.create_duval_5_colorized())

    duval_triangles = html.Div([
                            html.Div([dcc.Graph(figure=duval_triangle_1.create_duval_1_result_graph(ch4_val, c2h2_val, c2h4_val))], style={
                                                        'display': 'inline-block',
                                                        'vertical-align': 'top',
                                                        'padding': 5
                                                        }),
                            html.Div([duval4], style={
                                                        'display': 'inline-block',
                                                        'vertical-align': 'top',
                                                        'padding': 5
                                                        }),
                            html.Div([duval5], style={
                                                        'display': 'inline-block',
                                                        'vertical-align': 'top',
                                                        'padding': 5
                                                        }), 
                    
                    ])

    return ratio_table, diagresults_table, typicals_table, duval_triangles

def main():
    Timer(1, open_browser).start()
    app.run_server(debug=True)

if __name__ == '__main__':
    main()
