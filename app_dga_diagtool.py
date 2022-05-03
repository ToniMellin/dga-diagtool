# -*- coding: utf-8 -*-
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import numpy as np
import pandas as pd
import duval_triangle_1
import webbrowser # autobrowser opening
from threading import Timer # autobrowser opening
import os # autobrowser opening

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

def open_browser():
    # function to open browser if not already running
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new('http://127.0.0.1:8050/')

def calculate_ratios(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, o2_val, n2_val):
    '''
    R1: CH4/H2
    R2: C2H2/C2H4
    R3: C2H2/CH4
    R4: C2H6/C2H2
    R5: C2H4/C2H6
    R6: CO2/CO
    R7: O2/N2
    '''

    # Ratio 1: CH4/H2
    try:
        if h2_val == 0:
            r1_val = 0
        elif (pd.isna(ch4_val) is True) or (pd.isna(h2_val) is True):
            r1_val = np.nan
        else:
            r1_val = ch4_val / h2_val
    except TypeError as e:
        print(f'Ratio TypeError: {e}')
        r1_val = np.nan
    
    # Ratio 2: C2H2/C2H4
    try:
        if c2h4_val == 0:
            r2_val = 0
        elif (pd.isna(c2h2_val) is True) or (pd.isna(c2h4_val) is True):
            r2_val = np.nan
        else:
            r2_val = c2h2_val / c2h4_val
    except TypeError as e:
        print(f'Ratio TypeError: {e}')
        r2_val = np.nan

    # Ratio 3: C2H2/CH4
    try:
        if ch4_val == 0:
            r3_val = 0
        elif (pd.isna(c2h2_val) is True) or (pd.isna(ch4_val) is True):
            r3_val = np.nan
        else:
            r3_val = c2h2_val / ch4_val
    except TypeError as e:
        print(f'Ratio TypeError: {e}')
        r3_val = np.nan

    # Ratio 4: C2H6/C2H2
    try:
        if c2h2_val == 0:
            r4_val = 0
        elif (pd.isna(c2h6_val) is True) or (pd.isna(c2h2_val) is True):
            r4_val = np.nan
        else:
            r4_val = c2h6_val / c2h2_val
    except TypeError as e:
        print(f'Ratio TypeError: {e}')
        r4_val = np.nan

    # Ratio 5: C2H4/C2H6
    try:
        if c2h6_val == 0:
            r5_val = 0
        elif (pd.isna(c2h4_val) is True) or (pd.isna(c2h6_val) is True):
            r5_val = np.nan
        else:
            r5_val = c2h4_val / c2h6_val
    except TypeError as e:
        print(f'Ratio TypeError: {e}')
        r5_val = np.nan

    # Ratio 6: CO2/CO
    try:
        if co_val == 0:
            r6_val = 0
        elif (pd.isna(co2_val) is True) or (pd.isna(co_val) is True):
            r6_val = np.nan
        else:
            r6_val =  co2_val / co_val
    except TypeError as e:
        print(f'Ratio TypeError: {e}')
        r6_val = np.nan

    # Ratio 7: O2/N2
    try:
        if n2_val == 0:
            r7_val = 0
        elif (pd.isna(o2_val) is True) or (pd.isna(n2_val) is True):
            r7_val = np.nan
        else:
            r7_val = o2_val / n2_val
    except TypeError as e:
        print(f'Ratio TypeError: {e}')
        r7_val = np.nan

    ratio_list = [r1_val, r2_val, r3_val, r4_val, r5_val, r6_val, r7_val]
    
    return ratio_list

def rogers_ratio_calculation(ratio2, ratio1, ratio5):
    try:
        if (pd.isna(ratio2) is True) or (pd.isna(ratio1) is True) or (pd.isna(ratio5) is True):
            return 'N/A'
        elif ratio2 < 0.1 and ratio1 > 0.1 and ratio1 < 1 and ratio5 < 1:
            return 'Normal'
        elif ratio2 < 0.1 and ratio1 < 0.1 and ratio5 < 1:
            return 'PD'
        elif ratio2 > 0.1 and ratio2 < 3 and ratio1 > 0.1 and ratio1 < 1 and ratio5 > 3:
            return 'D1/D2'
        elif ratio2 < 0.1 and ratio1  > 0.1 and ratio1 < 1 and ratio5 >= 1 and ratio5 <= 3:
            return 'T1'
        elif ratio2 < 0.1 and ratio1 > 1 and ratio5 >= 1 and ratio5 <= 3:
            return 'T2'
        elif ratio2 < 0.1 and ratio1 > 1 and ratio5 > 3:
            return 'T3'
        else:
            return 'ND'
    except:
        print('Rogers ratio calculation error!')
        print(f'{ratio2}, {ratio1}, {ratio5}')
        return 'N/A'

def doernenburg_ratio_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val):
    ratio_list = calculate_ratios(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, np.nan, np.nan)
    ratio1 = ratio_list[0]
    ratio2 = ratio_list[1]
    ratio3 = ratio_list[2]
    ratio4 = ratio_list[3]

    h2_l1 = 100
    h2_2l1 = 100 * 2
    ch4_l1 = 120
    ch4_2l1 = 120 * 2
    c2h2_l1 = 1
    c2h2_2l1 = 1 * 2
    c2h4_l1 =50
    c2h4_2l1 = 50 * 2
    c2h6_l1 = 65
    co_l1 = 350

    try:
        if (pd.isna(ratio1) is True) or (pd.isna(ratio2) is True) or (pd.isna(ratio3) is True) or (pd.isna(ratio4) is True):
            return 'N/A'
        elif (h2_val > h2_2l1 or ch4_val > ch4_2l1 or c2h2_val > c2h2_2l1 or c2h4_val > c2h4_2l1) and (c2h6_val > c2h6_l1 or co_val > co_l1):
            if (ch4_val > ch4_l1 or h2_val > h2_l1) and (c2h2_val > c2h2_l1 or c2h4_val > c2h4_l1) and (c2h2_val > c2h2_l1 or ch4_val > ch4_l1) and (c2h6_val > c2h6_l1 or c2h2_val > c2h2_l1):
                if ratio1 > 1 and ratio2 < 0.75 and ratio3 < 0.3 and ratio4 > 0.4:
                    return 'T'
                elif ratio1 < 0.1 and ratio3 < 0.3 and ratio4 > 0.4:
                    return 'PD'
                elif ratio1 > 0.1 and ratio1 < 1 and ratio2 > 0.75 and ratio3 > 0.3 and ratio4 < 0.4:
                    return  'D1/D2'
                else:
                    return 'ND'
            else:
                return 'N/A'
        else:
            return 'No fault'
    except:
        print('Doernenburg ratio calculation error!')
        print(f'{h2_val}, {ch4_val}, {c2h6_val}, {c2h4_val}, {c2h2_val}, {co_val}, {co2_val}')
        return 'N/A'

def iec_ratio_calculation(ratio2, ratio1, ratio5):
    try:
        if ratio2 < 0.1 and ratio5 < 0.2:
            return 'PD'
        elif ratio2 > 1 and ratio1 >= 0.1 and ratio1 <= 0.5 and ratio5 >1:
            return 'D1'
        elif ratio2 >= 0.6 and ratio2 <= 2.5 and ratio1 >= 0.1 and ratio1 <= 1 and ratio5 >2:
            return 'D2'
        elif ratio1 >1 and ratio5 <1:
            return 'T1'
        elif ratio2 < 0.1 and ratio1 > 1 and ratio5 >= 1 and ratio5 <= 4:
            return 'T2'
        elif ratio2 < 0.2 and ratio1 > 1 and ratio5 > 4:
            return 'T3'
        else:
            return "ND"
    except:
        print('IEC ratio calculation error!')
        print(f'{ratio2}, {ratio1}, {ratio5}')
        return 'N/A'

def calculate_diagnostic_results(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val):
    ratio_list = calculate_ratios(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, np.nan, np.nan)

    diag_result_list = []

    try:
        if pd.isna([ratio_list[0], ratio_list[1], ratio_list[4]]).any() is True:
            diag_result_list.append('N/A')
        else:
            rogers_result = rogers_ratio_calculation(ratio_list[1], ratio_list[0], ratio_list[4])
            diag_result_list.append(rogers_result)

        if pd.isna([ratio_list[0], ratio_list[1], ratio_list[2], ratio_list[3]]).any() is True:
            diag_result_list.append('N/A')
        else:
            doernenburg_result = doernenburg_ratio_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val)
            diag_result_list.append(doernenburg_result)

        if pd.isna([ratio_list[0], ratio_list[1], ratio_list[4]]).any() is True:
            diag_result_list.append('N/A')
        else:
            iec_result = iec_ratio_calculation(ratio_list[1], ratio_list[0], ratio_list[4])
            diag_result_list.append(iec_result)

        if pd.isna([ch4_val, c2h2_val, c2h4_val]).any() is True:
            diag_result_list.append('N/A')
        else:
            duval1_result = duval_triangle_1.calculate_duval1_result(ch4_val, c2h2_val, c2h4_val)
            diag_result_list.append(duval1_result)
        
    except Exception as e:
        print(f'diag result calculation error!!:\n {e}')
        print(f'Input: {h2_val}, {ch4_val}, {c2h6_val}, {c2h4_val}, {c2h2_val}, {co_val}, {co2_val}')
        print(f'Ratios isna: {pd.isna(ratio_list)}')
        print(diag_result_list)

        diag_result_list = ['-', '-', '-', '-']

    return diag_result_list

def iec_typical_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val):
    
    # iec 90th percentile typical values
    h2_typ = 132
    ch4_typ = 120
    c2h6_typ = 90
    c2h4_typ = 146
    c2h2_typ = 4
    c2h2_oltc_typ = 37
    co_typ = 1060
    co2_typ = 10000

    iec_typical_results = []
    try:
        if h2_val > h2_typ:
            iec_typical_results.append('Typical values exceeded!')
        else:
            iec_typical_results.append('Normal')

        if ch4_val > ch4_typ:
            iec_typical_results.append('Typical values exceeded!')
        else:
            iec_typical_results.append('Normal')

        if c2h6_val > c2h6_typ:
            iec_typical_results.append('Typical values exceeded!')
        else:
            iec_typical_results.append('Normal')

        if c2h4_val > c2h4_typ:
            iec_typical_results.append('Typical values exceeded!')
        else:
            iec_typical_results.append('Normal')

        if c2h2_val > c2h2_typ:
            if c2h2_val > c2h2_oltc_typ:
                iec_typical_results.append('Communicating OLTC typical values exceeded!')
            else:
                iec_typical_results.append('Typical values exceeded unless communicating OLTC!')
        else:
            iec_typical_results.append('Normal')

        if co_val > co_typ:
            iec_typical_results.append('Typical values exceeded!')
        else:
            iec_typical_results.append('Normal')

        if co2_val > co2_typ:
            iec_typical_results.append('Typical values exceeded!')
        else:
            iec_typical_results.append('Normal')
        
        # TDCG not included in IEC
        iec_typical_results.append('-')
    except:
        iec_typical_results = ['-', '-', '-', '-', '-', '-', '-', '-']

    return iec_typical_results

def ieee_2008_typical_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val):
    try:
        tdcg_val = h2_val + ch4_val + c2h6_val + c2h4_val + c2h2_val + co_val
    except:
        tdcg_val = 0

    # typical values for condition 1
    h2_typ1 = 100
    ch4_typ1 = 120
    c2h6_typ1 = 65
    c2h4_typ1 = 50
    c2h2_typ1 = 1
    co_typ1 = 350
    co2_typ1 = 2500
    tdcg_typ1 = 720

    # typical values for condition 2

    #TODO add condition 2 and condition 3 typical values and result calculations

    
    try:
        ieee_typical_results = []
        if h2_val > h2_typ1:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')

        if ch4_val > ch4_typ1:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')

        if c2h6_val > c2h6_typ1:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')

        if c2h4_val > c2h4_typ1:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')

        if c2h2_val > c2h2_typ1:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')

        if co_val > co_typ1:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')

        if co2_val > co2_typ1:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')
        
        if co2_val > co2_typ1:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')

        if tdcg_val > tdcg_typ1:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')
        
    except:
        ieee_typical_results = ['-', '-', '-', '-', '-', '-', '-', '-']

    return ieee_typical_results

#TODO add IEEE C57.104-2019 typical values, requires O2/N2 ratio and optional transformer age

#TODO add duval 4 and conditions to use

#TODO add duval 5 and conditions to use

def calculate_typical_results(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, o2_val, n2_val, trafo_age_val):
    typical_result_list = []
    
    iec_typical_list = iec_typical_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val)
    typical_result_list.append(iec_typical_list)

    ieee_2008_typical_list = ieee_2008_typical_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val)
    typical_result_list.append(ieee_2008_typical_list)

    return typical_result_list

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
    r_list = calculate_ratios(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, o2_val, n2_val)
    df_ratio = pd.DataFrame({'Ratio': ['Ratio 1 (CH4/H2):', 'Ratio 2 (C2H2/C2H4):', 'Ratio 3 (C2H2/CH4):', 'Ratio 4 (C2H6/C2H2):', 'Ratio 5 (C2H4/C2H6):', 'Ratio 6 (CO2/CO):', 'Ratio 7 (O2/N2):'],
                            'Value': r_list}).round(2)
    try:
        diag_results = calculate_diagnostic_results(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val)
    except TypeError:
        print('diag TypeERROR')
        diag_results = ['N/A', 'N/A', 'N/A', 'N/A']
    df_diag = pd.DataFrame({'Diagnostic method': ['Rogers ratio:', 'Doernenburg ratio:', 'IEC 60599:', 'Duval triangle 1:'], 'Result': diag_results})
    
    typical_results = calculate_typical_results(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, o2_val, n2_val, trafo_age_val)
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

                    html.Div([
                    dcc.Graph(figure=duval_triangle_1.create_duval1_result_graph(ch4_val, c2h2_val, c2h4_val))
                    ])
                    ])



if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run_server(debug=True)