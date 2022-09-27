# -*- coding: utf-8 -*-
"""app_dga_diagtool.py

Main program file for the DGA-diagtool, which is a  dash based transformer oil dissolved gas analysis (DGA) diagnostic tool. 

This module contains the functional workings of the user interface.

@Author: https://github.com/ToniMellin
"""

__version__ = 0.1
__author__ = 'ToniMellin'


import os # autobrowser opening
from threading import Timer # autobrowser opening
import webbrowser
from zipfile import is_zipfile # autobrowser opening

import dash
from dash import dash_table
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from diagnostic import duval_triangle_1
from diagnostic import duval_triangle_4
from diagnostic import duval_triangle_5
from diagnostic import diagnostic_calculation
from diagnostic import typical_value_comparison

ctx = dash.callback_context

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




app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css]) # IF needed to not include initial callbacks , prevent_initial_callbacks=True

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

timestamp_tooltip = """Sample timestamp. Used for rate of change analysis and sequantial plotting. Use ISO format \n2022-01-20 15:38 \nOR \n2022-01-20"""

name_tooltip = """Sample reference name (**Optional**). Name is optional, but may help you in handling your samples."""

# TODO multi sample point further descriptions

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
#TODO add toggle for CIgre TB 771 oxygen/nitrogen ratio typical values and selection of over and under 0.05 or 0.2
calculate_button = html.Div([
                    dbc.Button(id='calculate-button-state', n_clicks=0, color="primary", className="d-grid gap-2 col-6 mx-auto", children='Calculate'),
                    ])


timestamp_multi_input = dbc.InputGroup(
    [
        dbc.InputGroupText("Timestamp"),
        dbc.Input(
            id="timestamp-multi-state",
            type="text",
            placeholder="YYYY-MM-DD HH:MM",
        ),
        dbc.Tooltip(timestamp_tooltip, target="timestamp-multi-state"),
    ],
    className="mb-3",
)
h2_multi_input = dbc.InputGroup(
    [
        dbc.InputGroupText("Hydrogen (H2)"),
        dbc.Input(
            id="h2-multi-state",
            type="number",
            min=0,
            max=1000000,
        ),
        dbc.Tooltip(h2_tooltip, target="h2-multi-state"),
    ],
    className="mb-3",
)
ch4_multi_input = dbc.InputGroup(
    [
        dbc.InputGroupText("Methane (CH4)"),
        dbc.Input(
            id="ch4-multi-state",
            type="number",
            min=0,
            max=1000000,
        ),
        dbc.Tooltip(ch4_tooltip, target="ch4-multi-state"),
    ],
    className="mb-3",
)
c2h6_multi_input = dbc.InputGroup(
    [
        dbc.InputGroupText("Ethane (C2H6)"),
        dbc.Input(
            id="c2h6-multi-state",
            type="number",
            min=0,
            max=1000000,
        ),
        dbc.Tooltip(c2h6_tooltip, target="c2h6-multi-state"),
    ],
    className="mb-3",
)
c2h4_multi_input = dbc.InputGroup(
    [
        dbc.InputGroupText("Ethylene (C2H4)"),
        dbc.Input(
            id="c2h4-multi-state",
            type="number",
            min=0,
            max=1000000,
        ),
        dbc.Tooltip(c2h4_tooltip, target="c2h4-multi-state"),
    ],
    className="mb-3",
)
c2h2_multi_input = dbc.InputGroup(
    [
        dbc.InputGroupText("Acetylene (C2H2)"),
        dbc.Input(
            id="c2h2-multi-state",
            type="number",
            min=0,
            max=1000000,
        ),
        dbc.Tooltip(c2h2_tooltip, target="c2h2-multi-state"),
    ],
    className="mb-3",
)
co_multi_input = dbc.InputGroup(
    [
        dbc.InputGroupText("Carbon monoxide (CO)"),
        dbc.Input(
            id="co-multi-state",
            type="number",
            min=0,
            max=1000000,
        ),
        dbc.Tooltip(co_tooltip, target="co-multi-state"),
    ],
    className="mb-3",
)
co2_multi_input = dbc.InputGroup(
    [
        dbc.InputGroupText("Carbon dioxide (CO2)"),
        dbc.Input(
            id="co2-multi-state",
            type="number",
            min=0,
            max=1000000,
        ),
        dbc.Tooltip(co2_tooltip, target="co2-multi-state"),
    ],
    className="mb-3",
)
o2_multi_input = dbc.InputGroup(
    [
        dbc.InputGroupText("Oxygen (O2)"),
        dbc.Input(
            id="o2-multi-state",
            type="number",
            min=0,
            max=1000000,
        ),
        dbc.Tooltip(o2_tooltip, target="o2-multi-state"),
    ],
    className="mb-3",
)
n2_multi_input = dbc.InputGroup(
    [
        dbc.InputGroupText("Nitrogen (N2)"),
        dbc.Input(
            id="n2-multi-state",
            type="number",
            min=0,
            max=1000000,
        ),
        dbc.Tooltip(n2_tooltip, target="n2-multi-state"),
    ],
    className="mb-3",
)
trafo_age_multi_input = dbc.InputGroup(
    [
        dbc.InputGroupText("Transformer age (years)"),
        dbc.Input(
            id="trafo-age-multi-state",
            type="number",
            min=0,
            max=1000000,
        ),
        dbc.Tooltip(trafo_age_tooltip, target="trafo-age-multi-state"),
    ],
    className="mb-3",
)
input_groups_multi = html.Div(
    [timestamp_multi_input, h2_multi_input, ch4_multi_input, c2h6_multi_input, c2h4_multi_input, c2h2_multi_input, co_multi_input, co2_multi_input, o2_multi_input, n2_multi_input, trafo_age_multi_input],
    className="mt-4 p-4",
)
add_sample_button = html.Div([
                    dbc.Button(id='add-sample-button-state', n_clicks=0, color="primary", className="d-grid gap-2 col-8 mx-auto", children='Add sample'),
                    ])
clear_samples_button = html.Div([
                    dbc.Button(id='clear-samples-button-state', n_clicks=0, outline=True, color="danger", className="d-grid gap-2 col-8 mx-auto", children='Clear samples'),
                    ])
update_multi_diagnostic_button = html.Div([
                    dbc.Button(id='update-multi-button-state', n_clicks=0, color="success", className="d-grid gap-2 col-8 mx-auto", children='Update diagnostic'),
                    ])

# TODO add toggle for lineest function usage or absolute values

# ======= Tabs ============================================================

single_sample_data_source_card = dbc.Card(
    [
        dbc.CardHeader("Input sample values:", className="card-title"),
        html.Div([input_groups, calculate_button]),
        html.Br(),
    ],
    className="mt-4",
    )

single_sample_tab = dbc.Container([
    dbc.Row([
            dbc.Col([single_sample_data_source_card], width=12, lg=4, className="mt-4"),
            dbc.Col([html.H4("Ratio calculation:"), 
                    html.Div(id='ratio-output-state'),
                    html.H4("Diagnostic method results:"), 
                    html.Div(id='diagmethod-output-state')], width=12, lg=8, className="mt-4"),

    ]),
    dbc.Row(
            dbc.Col([html.H4("Typical values comparison:"),
                    html.Div(id='typicals-output-state')], className="mt-4"),
    ),
    dbc.Row(
            dbc.Col([html.H4("Duval triangle visualizations:"), 
                    html.Div(id='duval-output-state')], width=12, lg=12, className="mt-4"),
    ),
    ],fluid=True,
    )


multiple_sample_data_source_card = dbc.Card(
    [
        dbc.CardHeader("Input multiple sample values and choose settings:", className="card-title"),
        html.Div([input_groups_multi, add_sample_button, clear_samples_button, html.Br(), update_multi_diagnostic_button]),
        html.Br(),
    ],
    className="mt-4",
    )

multi_sample_data_accordion = html.Div(
    [
        dbc.Accordion(
            [
                dbc.AccordionItem(
                    html.Div(id='samplelist-output-state'),
                    title="Sample data table",
                    item_id="data-table",
                ),
                dbc.AccordionItem(
                    html.Div(dcc.Graph(id='line-chart', figure={})),
                    title="Sample data graph",
                    item_id="data-graph",
                ),
            ],
            id="data-accordion",
            active_item=["data-table", "data-graph"],
            always_open=True,
        ),
        html.Div(id="accordion-contents", className="mt-4"),
    ]
)

multi_sample_diagnostic_accordion = html.Div(
    dbc.Accordion(
        [
            dbc.AccordionItem(
                #TODO add toggle for CIgre TB 771 oxygen/nitrogen ratio typical values and selection of over and under 0.05 or 0.2
                html.Div([
                html.Div(id='multi-typicalvalues-output-state')
                ]),
                title="Typical value results table",
                item_id="multi-1",
            ),
            dbc.AccordionItem(
                html.Div([
                html.Div(id='multi-diagnostic-output-state')
                ]),
                title="Diagnostic results table",
                item_id="multi-2",
            ),
            dbc.AccordionItem(
                html.Div([
                html.Div(id='multi-duvaldiagnostic-output-state')
                ]),
                title="Duval triangles results visualization",
                item_id="multi-3",
            ),
            dbc.AccordionItem(
                "Under development....",
                title="Rate of change summaries",
                item_id="multi-4",
            ),
            dbc.AccordionItem(
                "Under development....",
                title="Rate of change based diagnostics",
                item_id="multi-5",
            ),
            dbc.AccordionItem(
                "Under development....",
                title="Rate of change based duval triangles results",
                item_id="multi-6",
            ),
        ],
        always_open=True,
        active_item=['multi-1', 'multi-2', 'multi-3'],
    )
)

# TODO add accordian for the sample datatable and line-chart
multiple_sample_tab = dbc.Container([
    dbc.Row([ 
        dbc.Col([multiple_sample_data_source_card], width=12, lg=4, className="mt-4"),
        dbc.Col([
                html.Div(multi_sample_data_accordion),
                ], width=12, lg=8, className="mt-4"),
    ]),
    dbc.Row([
        multi_sample_diagnostic_accordion,
    ]),
    ],fluid=True,
    )

# Build tabs
tabs = dbc.Tabs(
    [
        dbc.Tab(single_sample_tab, tab_id="tab-1", label="Single sample diagnostic"),
        dbc.Tab(multiple_sample_tab,
            tab_id="tab-2",
            label="Multiple sample diagnostic",
            className="pb-4",
        ),
    ],
    id="tabs",
    active_tab="tab-1",
    className="mt-2",
)


# ======= Main layout =====================================================

app.layout = dbc.Container(
    [

    dbc.Row(
            dbc.Col(
                html.H2("DGA diagtool", className="text-center bg-secondary text-white p-2"),
            )
    ),
    dbc.Row([
            dbc.Col([tabs], width=12, lg=12, className="mt-4"),
    ]),
    # dcc.Store stores the samples data
    dcc.Store(id='multi-samples-data'),
    ],fluid=True,
    )

# ======= Callbacks =======================================================

@app.callback(Output('ratio-output-state', 'children'),
                Output('diagmethod-output-state', 'children'),
                Output('typicals-output-state', 'children'),
                Output('duval-output-state', 'children'),
                Input('calculate-button-state', 'n_clicks'),
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
def update_single_sample_output(n_clicks, h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, o2_val, n2_val, trafo_age_val):
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

    df_diag = pd.DataFrame({'Diagnostic method': ['Rogers ratio:', 'Doernenburg ratio:', 'IEC 60599 ratio:', 'Duval triangle 1:', 'Duval triangle 4:', 'Duval triangle 5:'], 'Result': diag_results})
    diagresults_table = dbc.Table.from_dataframe(df_diag, striped=True, bordered=True, hover=True)

    typical_results = typical_value_comparison.calculate_typical_results(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, o2_val, n2_val, trafo_age_val)
    df_typicals = pd.DataFrame({'Typical values': ['IEC 60599:2022, typical values:', 'IEEE C57.104-2019, typical values:', 'Cigre TB 771, typical values:'], 
                                'H2': [typical_results[0][0], typical_results[1][0], typical_results[2][0]], 
                                'CH4': [typical_results[0][1], typical_results[1][1], typical_results[2][1]], 
                                'C2H6': [typical_results[0][2], typical_results[1][2], typical_results[2][2]], 
                                'C2H4': [typical_results[0][3], typical_results[1][3], typical_results[2][3]], 
                                'C2H2': [typical_results[0][4], typical_results[1][4], typical_results[2][4]], 
                                'CO': [typical_results[0][5], typical_results[1][5], typical_results[2][5]], 
                                'CO2': [typical_results[0][6], typical_results[1][6], typical_results[2][6]]
                                })
    typicals_table = dbc.Table.from_dataframe(df_typicals, striped=True, bordered=True, hover=True)

    duval1 = dcc.Graph(figure=duval_triangle_1.create_duval_1_result_graph(ch4_val, c2h2_val, c2h4_val))

    if diag_results[3] in ['PD', 'T1', 'T2']:
        duval4 = dcc.Graph(figure=duval_triangle_4.create_duval_4_result_graph(h2_val, c2h6_val, ch4_val))
    else:
        duval4 = dcc.Graph(figure=duval_triangle_4.create_duval_4_colorized())

    if diag_results[3] in ['T2', 'T3']:
        duval5 = dcc.Graph(figure=duval_triangle_5.create_duval_5_result_graph(ch4_val, c2h6_val, c2h4_val))
    else:
        duval5 = dcc.Graph(figure=duval_triangle_5.create_duval_5_colorized())

    duval_triangles = html.Div([
                            html.Div([duval1], style={
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

@app.callback(Output('multi-samples-data', 'data'),
                Input('add-sample-button-state', 'n_clicks'),
                Input('clear-samples-button-state', 'n_clicks'),
                Input('multi-samples-data', 'data'),
                State('timestamp-multi-state', 'value'),
                State('h2-multi-state', 'value'),
                State('ch4-multi-state', 'value'),
                State('c2h6-multi-state', 'value'),
                State('c2h4-multi-state', 'value'),
                State('c2h2-multi-state', 'value'),
                State('co-multi-state', 'value'),
                State('co2-multi-state', 'value'),
                State('o2-multi-state', 'value'),
                State('n2-multi-state', 'value'),
                State('trafo-age-multi-state', 'value')
               )
def add_sample_info(n_clicks, clear_clicks, multi_data, timestamp_val, h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, o2_val, n2_val, trafo_age_val):
    
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if button_id == 'clear-samples-button-state':
        df_no_samples = pd.DataFrame(columns=['Timestamp', 'H2', 'CH4', 'C2H6', 'C2H4', 'C2H2', 'CO', 'CO2', 'O2', 'N2', 'Transformer age'])

        return df_no_samples.to_json(date_format='iso', orient='split')    
    else:
        if n_clicks == 0:
            #df_no_samples = pd.DataFrame(columns=['Timestamp', 'H2', 'CH4', 'C2H6', 'C2H4', 'C2H2', 'CO', 'CO2', 'O2', 'N2', 'Transformer age'])

            df_sample = pd.DataFrame({'Timestamp': [pd.to_datetime('2021-05-11'), pd.to_datetime('2021-06-02'), pd.to_datetime('2022-05-02 15:02'), pd.to_datetime('2022-05-24 06:02'), pd.to_datetime('2022-06-01 06:02'), pd.to_datetime('2022-06-01 23:34')],  
                        'H2': [0, 10, 50, 100, 160, 250], 
                        'CH4': [0, 20, 41, 60, 66, 80], 
                        'C2H6': [0, 60, 121, 172, 200, 207], 
                        'C2H4': [0, 5, 50, 60, 66, 67], 
                        'C2H2': [0, 1, 2, 5, 6, 10], 
                        'CO': [0, 150, 200, 400, 500, 600], 
                        'CO2': [0, 2211, 4200, 4500, 4561, 4603], 
                        'O2': [0, 19000, 20005, 20100, 21000, 21010], 
                        'N2': [0, 51000, 52500, 53780, 54900, 55620], 
                        'Transformer age': [9, 10, 10, 10, 10, 10]}, index=[0, 1, 2, 3, 4, 5])

            #return df_no_samples.to_json(date_format='iso', orient='split')
            return df_sample.to_json(date_format='iso', orient='split')
        else:
            df_sample = pd.DataFrame({'Timestamp': pd.to_datetime(timestamp_val), 'H2': h2_val, 'CH4': ch4_val, 'C2H6': c2h6_val, 'C2H4': c2h4_val, 'C2H2': c2h2_val, 'CO': co_val, 'CO2': co2_val, 'O2': o2_val, 'N2': n2_val, 'Transformer age': trafo_age_val}, index=[n_clicks-1])

            df_multi_samples = pd.read_json(multi_data, orient='split')

            df_multi_samples = pd.concat([df_multi_samples, df_sample])

            return df_multi_samples.to_json(date_format='iso', orient='split')

@app.callback(Output('samplelist-output-state', 'children'),
                Input('multi-samples-data', 'data'),
                Input("data-accordion", "active_item"),
            )
def update_multi_sample_table(multi_data, accordion_active):
    df_multi_samples = pd.read_json(multi_data, orient='split')

    # sorting according to the date column
    df_multi_samples_sorted = df_multi_samples.sort_values(by=['Timestamp'])

    if len(df_multi_samples) == 0:
        return dbc.Alert("No sample data entered", color="info")
    else:
        if accordion_active is None:
            sample_size = 30
        else:
            if 'data-graph' in accordion_active:
                sample_size = 5
            else:
                sample_size = 30
        multi_samples_table = dash_table.DataTable(
            id="multi_samples_table",
            columns=(
                [{"id": "Timestamp", "name": "Timestamp", "type": "datetime"}]
                + [
                    {"id": col, "name": col, "type": "numeric"}
                    for col in df_multi_samples_sorted.columns[1:]
                ]
            ),
            data=df_multi_samples_sorted.to_dict("records"),
            page_size=sample_size,
            style_table={"overflowX": "scroll"},
            #style_as_list_view=True,
            #TODO add a way to delete rows and then update the stored data by removing those rows row_deletable=True, https://community.plotly.com/t/callback-for-deleting-a-row-in-a-data-table/21437
            style_cell={
                        'height': 'auto',
                        # all three widths are needed
                        'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                        'whiteSpace': 'normal'
    }
        )   
        return multi_samples_table

@app.callback(Output('line-chart', 'figure'),
                Input('multi-samples-data', 'data'),
            )
def update_line_chart(multi_data):
    df_multi_samples = pd.read_json(multi_data, orient='split')

    # sorting according to the date column
    df_multi_samples_sorted = df_multi_samples.sort_values(by=['Timestamp'])

    fig = go.Figure()
    for y_gas in df_multi_samples_sorted.filter(['H2', 'CH4', 'C2H6', 'C2H4', 'C2H2']).columns:
        fig.add_trace(go.Scatter(x=df_multi_samples_sorted['Timestamp'], y=df_multi_samples_sorted[y_gas],
                            mode='lines+markers',
                            name=y_gas))
    for y2_gas in df_multi_samples_sorted.filter(['CO', 'CO2', 'O2', 'N2']).columns:
        fig.add_trace(go.Scatter(x=df_multi_samples_sorted['Timestamp'], y=df_multi_samples_sorted[y2_gas],
                            mode='lines+markers',
                            name=f'{y2_gas} (y2)',
                            yaxis="y2"))
    fig.update_layout(
                            showlegend=True,
                            legend=dict(
                                        orientation="h",
                                        yanchor="bottom",
                                        y=1.05,
                                        xanchor="left",
                                        x=0
                                    ),
                            title_x=0.5,
                            height=800,
                            xaxis_title='Time',
                            yaxis_title='Hydrogen & hydrocarbon gases',
                            yaxis_ticksuffix=' ppm',
                            yaxis2=dict(
                                title="Carbon oxides & athmospheric gases",
                                ticksuffix=' ppm',
                                anchor="x",
                                overlaying="y",
                                side="right",
                                ),
                            xaxis=dict(domain=[0, 1],
                                rangeselector=dict(
                                    buttons=list([
                                        dict(count=1,
                                            label="1m",
                                            step="month",
                                            stepmode="backward"),
                                        dict(count=6,
                                            label="6m",
                                            step="month",
                                            stepmode="backward"),
                                        dict(count=1,
                                            label="YTD",
                                            step="year",
                                            stepmode="todate"),
                                        dict(count=1,
                                            label="1y",
                                            step="year",
                                            stepmode="backward"),
                                        dict(step="all")
                                    ])
                                ),
                                rangeslider=dict(
                                    visible=True
                                ),
                                type="date"),
                            modebar_add = ["v1hovermode", 'toggleSpikelines',]
                        )

    

    return fig

@app.callback(Output('multi-typicalvalues-output-state', 'children'),
                Input('multi-samples-data', 'data'),
            )
def update_multi_sample_typical_values_table(multi_data):
    df_multi_samples = pd.read_json(multi_data, orient='split')

    if len(df_multi_samples) == 0:
        return dbc.Alert("No sample data entered", color="info")
    else:
        # sorting according to the date column
        df_multi_samples_sorted = df_multi_samples.sort_values(by=['Timestamp'])

        #combine typical results to dataframe
        df_typicals_combined = typical_value_comparison.combine_typical_results_to_dataframe(df_multi_samples_sorted)

        #TODO colorization of typical value results summary table https://dash.plotly.com/datatable/conditional-formatting
        #TODO add the ppm values in tooltips of each cell

        df_typical_summary = df_typicals_combined.filter(['Timestamp', 'IEC typical values', 'IEEE typical values', 'Cigre typical values'])

        multi_typicals_table = dash_table.DataTable(
            id="multi_samples_table",
            columns=(
                [{"id": "Timestamp", "name": "Timestamp", "type": "datetime"}]
                + [
                    {"id": col, "name": col}
                    for col in df_typical_summary.columns[1:]
                ]
            ),
            data=df_typical_summary.to_dict("records"),
            page_size=5,
            style_table={"overflowX": "scroll"},
            #style_as_list_view=True,
            style_cell={
                        'height': 'auto',
                        # all three widths are needed
                        'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                        'whiteSpace': 'normal'
    }
        )   
        return multi_typicals_table
        
        #return dbc.Alert("Under development...", color='warning')


@app.callback(Output('multi-diagnostic-output-state', 'children'),
                Input('multi-samples-data', 'data'),
            )
def update_multi_sample_diagnostic_table(multi_data):
    df_multi_samples = pd.read_json(multi_data, orient='split')

    

    if len(df_multi_samples) == 0:
        return dbc.Alert("No sample data entered", color="info")
    else:
        # sorting according to the date column
        df_multi_samples_sorted = df_multi_samples.sort_values(by=['Timestamp'])

        df_diagnostics_combined = diagnostic_calculation.combine_diagnostic_result_to_dataframe(df_multi_samples_sorted)

        df_diagnostics_summary = df_diagnostics_combined.filter(['Timestamp', 'Rogers ratio', 'Doernenburg ratio', 'IEC 60599 ratio', 'Duval triangle 1', 'Duval triangle 4', 'Duval triangle 5'])

        #TODO fix ValueError

        #TODO colorization of diagnostics results summary table https://dash.plotly.com/datatable/conditional-formatting
        #TODO add the ppm values in tooltips of columns
        multi_diagnostics_table = dash_table.DataTable(
            id="multi_diagnostics_table",
            columns=(
                [{"id": "Timestamp", "name": "Timestamp", "type": "datetime"}]
                + [
                    {"id": col, "name": col}
                    for col in df_diagnostics_summary.columns[1:]
                ]
            ),
            data=df_diagnostics_summary.to_dict("records"),
            page_size=5,
            style_table={"overflowX": "scroll"},
            #style_as_list_view=True,
            style_cell={
                        'height': 'auto',
                        # all three widths are needed
                        'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                        'whiteSpace': 'normal'
    }
        )   
        #return multi_diagnostics_table
        return dbc.Alert("Under development...", color='warning')

@app.callback(Output('multi-duvaldiagnostic-output-state', 'children'),
                Input('multi-samples-data', 'data'),
            )
def update_multi_duval_diagnostic_output(multi_data):
    df_multi_samples = pd.read_json(multi_data, orient='split')

    # sorting according to the date column
    df_multi_samples_sorted = df_multi_samples.sort_values(by=['Timestamp'])

    if len(df_multi_samples) == 0:
        return dbc.Alert("No sample data entered", color="info")
    else:
        duval1 = dcc.Graph(figure=duval_triangle_1.create_duval_1_multi_results_graph(df_multi_samples_sorted))

        df_multi_samples_sorted['DuvalResult'] = df_multi_samples_sorted.apply(lambda x: duval_triangle_1.calculate_duval_1_result(x['CH4'], x['C2H2'], x['C2H4']), axis=1)
        
        found_PDT1T2 = df_multi_samples_sorted[df_multi_samples_sorted['DuvalResult'].str.contains('PD|T1|T2')]
        found_T2T3 = df_multi_samples_sorted[df_multi_samples_sorted['DuvalResult'].str.contains('T2|T3')]

        if len(found_PDT1T2) > 0:
            duval4 = dcc.Graph(figure=duval_triangle_4.create_duval_4_multi_results_graph(found_PDT1T2))
        else:
            duval4 = dcc.Graph(figure=duval_triangle_4.create_duval_4_colorized())

        if len(found_T2T3) > 0:
            duval5 = dcc.Graph(figure=duval_triangle_5.create_duval_5_multi_results_graph(found_T2T3))
        else:
            duval5 = dcc.Graph(figure=duval_triangle_5.create_duval_5_colorized())

        duval_triangles = html.Div([
                                html.Div([duval1], style={
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
        

        return duval_triangles

def main():
    Timer(1, open_browser).start()
    app.run_server(debug=True)

if __name__ == '__main__':
    main()
