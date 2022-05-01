# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import numpy as np
import pandas as pd
import duval_triangle_1

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

def calculate_ratios(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val):
    '''
    R1: CH4/H2
    R2: C2H2/C2H4
    R3: C2H2/CH4
    R4: C2H6/C2H2
    R5: C2H4/C2H6
    R6: CO2/CO
    '''
    try:
        r1_val = ch4_val / h2_val
        r2_val = c2h2_val / c2h4_val
        r3_val = c2h2_val / ch4_val
        r4_val = c2h6_val / c2h2_val
        r5_val = c2h4_val / c2h6_val
        r6_val =  co2_val / co_val
    except ZeroDivisionError:
        print('ZeroDivisionError')
        r1_val = np.nan
        r2_val = np.nan
        r3_val = np.nan
        r4_val = np.nan
        r5_val = np.nan
        r6_val = np.nan
    except TypeError:
        print('TypeError')
        r1_val = np.nan
        r2_val = np.nan
        r3_val = np.nan
        r4_val = np.nan
        r5_val = np.nan
        r6_val = np.nan
    
    ratio_list = [r1_val, r2_val, r3_val, r4_val, r5_val, r6_val]
    
    return ratio_list

def rogers_ratio_calculation(ratio2, ratio1, ratio5):
    try:
        if ratio2 < 0.1 and ratio1 > 0.1 and ratio1 < 1 and ratio5 < 1:
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
        return 'N/A'

def doernenburg_ratio_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val):
    ratio_list = calculate_ratios(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val)
    ratio1 = ratio_list[0]
    ratio2 = ratio_list[1]
    ratio3 = ratio_list[2]
    ratio4 = ratio_list[3]
    ratio5 = ratio_list[4]
    ratio6 = ratio_list[5]

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
        if (h2_val > h2_2l1 or ch4_val > ch4_2l1 or c2h2_val > c2h2_2l1 or c2h4_val > c2h4_2l1) and (c2h6_val > c2h6_l1 or co_val > co_l1):
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
                return 'NA'
        else:
            return 'No fault'
    except:
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
        return 'N/A'

def calculate_diagnostic_results(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val):
    ratio_list = calculate_ratios(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val)

    diag_result_list = []

    rogers_result = rogers_ratio_calculation(ratio_list[1], ratio_list[0], ratio_list[4])
    diag_result_list.append(rogers_result)

    doernenburg_result = doernenburg_ratio_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val)
    diag_result_list.append(doernenburg_result)

    iec_result = iec_ratio_calculation(ratio_list[1], ratio_list[0], ratio_list[4])
    diag_result_list.append(iec_result)

    duval1_result = duval_triangle_1.calculate_duval1_result(ch4_val, c2h2_val, c2h4_val)
    diag_result_list.append(duval1_result)

    return diag_result_list

def iec_limit_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val):
    
    h2_lim = 132
    ch4_lim = 120
    c2h6_lim = 90
    c2h4_lim = 146
    c2h2_lim = 4
    c2h2_oltc_lim = 37
    co_lim = 1060
    co2_lim = 10000

    iec_limit_results = []
    try:
        if h2_val > h2_lim:
            iec_limit_results.append('Limit exceeded!')
        else:
            iec_limit_results.append('Normal')

        if ch4_val > ch4_lim:
            iec_limit_results.append('Limit exceeded!')
        else:
            iec_limit_results.append('Normal')

        if c2h6_val > c2h6_lim:
            iec_limit_results.append('Limit exceeded!')
        else:
            iec_limit_results.append('Normal')

        if c2h4_val > c2h4_lim:
            iec_limit_results.append('Limit exceeded!')
        else:
            iec_limit_results.append('Normal')

        if c2h2_val > c2h2_lim:
            if c2h2_val > c2h2_oltc_lim:
                iec_limit_results.append('Communicating OLTC limit exceeded!')
            else:
                iec_limit_results.append('Limit exceeded unless communicating OLTC!')
        else:
            iec_limit_results.append('Normal')

        if co_val > co_lim:
            iec_limit_results.append('Limit exceeded!')
        else:
            iec_limit_results.append('Normal')

        if co2_val > co2_lim:
            iec_limit_results.append('Limit exceeded!')
        else:
            iec_limit_results.append('Normal')
        
        # TDCG not included in IEC
        iec_limit_results.append('-')
    except:
        iec_limit_results = ['-', '-', '-', '-', '-', '-', '-', '-']

    return iec_limit_results

def ieee_2008_limit_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val):
    try:
        tdcg_val = h2_val + ch4_val + c2h6_val + c2h4_val + c2h2_val + co_val
    except:
        tdcg_val = 0

    # limits for condition 1
    h2_lim1 = 100
    ch4_lim1 = 120
    c2h6_lim1 = 65
    c2h4_lim1 = 50
    c2h2_lim1 = 1
    co_lim1 = 350
    co2_lim1 = 2500
    tdcg_lim1 = 720

    #TODO add condition 2 and condition 3 limits and result calculations

    
    try:
        ieee_limit_results = []
        if h2_val > h2_lim1:
            ieee_limit_results.append('Limit exceeded! / Condition 2')
        else:
            ieee_limit_results.append('Normal / Condition 1')

        if ch4_val > ch4_lim1:
            ieee_limit_results.append('Limit exceeded! / Condition 2')
        else:
            ieee_limit_results.append('Normal / Condition 1')

        if c2h6_val > c2h6_lim1:
            ieee_limit_results.append('Limit exceeded! / Condition 2')
        else:
            ieee_limit_results.append('Normal / Condition 1')

        if c2h4_val > c2h4_lim1:
            ieee_limit_results.append('Limit exceeded! / Condition 2')
        else:
            ieee_limit_results.append('Normal / Condition 1')

        if c2h2_val > c2h2_lim1:
            ieee_limit_results.append('Limit exceeded! / Condition 2')
        else:
            ieee_limit_results.append('Normal / Condition 1')

        if co_val > co_lim1:
            ieee_limit_results.append('Limit exceeded! / Condition 2')
        else:
            ieee_limit_results.append('Normal / Condition 1')

        if co2_val > co2_lim1:
            ieee_limit_results.append('Limit exceeded! / Condition 2')
        else:
            ieee_limit_results.append('Normal / Condition 1')
        
        if co2_val > co2_lim1:
            ieee_limit_results.append('Limit exceeded! / Condition 2')
        else:
            ieee_limit_results.append('Normal / Condition 1')

        if tdcg_val > tdcg_lim1:
            ieee_limit_results.append('Limit exceeded! / Condition 2')
        else:
            ieee_limit_results.append('Normal / Condition 1')
        
    except:
        ieee_limit_results = ['-', '-', '-', '-', '-', '-', '-', '-']

    return ieee_limit_results

def calculate_limit_results(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val):
    limit_result_list = []
    
    iec_limit_list = iec_limit_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val)
    limit_result_list.append(iec_limit_list)

    ieee_2008_limit_list = ieee_2008_limit_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val)
    limit_result_list.append(ieee_2008_limit_list)

    return limit_result_list

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
    html.H2('DGA diagnostic dash\n'), #, style={'color': 'white', 'backgroundColor':'#003366'}
    
    html.Div(["H2:  ",    
    dcc.Input(id='h2-state', type='number'),
    ]),

    html.Div(["CH4: ",
    dcc.Input(id='ch4-state', type='number'),
    ]),
    
    html.Div(["C2H6:",    
    dcc.Input(id='c2h6-state', type='number'),
    ]),

    html.Div(["C2H4:",
    dcc.Input(id='c2h4-state', type='number'),
    ]),

    html.Div(["C2H2:",    
    dcc.Input(id='c2h2-state', type='number'),
    ]),

    html.Div(["CO:  ",
    dcc.Input(id='co-state', type='number'),
    ]),

    html.Div(["CO2: ",
    dcc.Input(id='co2-state', type='number'),
    ]),

    html.Div([
    html.Button(id='submit-button-state', n_clicks=0, children='Calculate'),
    ]),
    html.Div(id='output-state')
])


@app.callback(Output('output-state', 'children'),
              [Input('submit-button-state', 'n_clicks')],
              [State('h2-state', 'value'),
               State('ch4-state', 'value'),
               State('c2h6-state', 'value'),
               State('c2h4-state', 'value'),
               State('c2h2-state', 'value'),
               State('co-state', 'value'),
               State('co2-state', 'value')]
               )


def update_output(n_clicks, h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val):
    r_list = calculate_ratios(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val)
    df_ratio = pd.DataFrame({'Ratio': ['Ratio 1 (CH4/H2):', 'Ratio 2 (C2H2/C2H4):', 'Ratio 3 (C2H2/CH4):', 'Ratio 4 (C2H6/C2H2):', 'Ratio 5 (C2H4/C2H6):', 'Ratio 6 (CO2/CO):'],
                            'Value': r_list}).round(2)
    try:
        diag_results = calculate_diagnostic_results(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val)
    except TypeError:
        print('diag TypeERROR')
        diag_results = ['N/A', 'N/A', 'N/A', 'N/A']
    df_diag = pd.DataFrame({'Diagnostic method': ['Rogers ratio:', 'Doernenburg ratio:', 'IEC 60599:', 'Duval triangle 1:'], 'Result': diag_results})
    
    limit_results = calculate_limit_results(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val)
    df_limits = pd.DataFrame({'Value limits': ['IEC 60599 90%', 'IEEE C57.104-2008'], 
                                'H2': [limit_results[0][0], limit_results[1][0]], 
                                'CH4': [limit_results[0][1], limit_results[1][1]], 
                                'C2H6': [limit_results[0][2], limit_results[1][2]], 
                                'C2H4': [limit_results[0][3], limit_results[1][3]], 
                                'C2H2': [limit_results[0][4], limit_results[1][4]], 
                                'CO': [limit_results[0][5], limit_results[1][5]], 
                                'CO2': [limit_results[0][6], limit_results[1][6]],
                                'TDCG': [limit_results[0][7], limit_results[1][7]]
                                })


    return html.Div([generate_table(df_ratio),
                    generate_table(df_diag),
                    generate_table(df_limits),
                    dcc.Graph(figure=duval_triangle_1.create_duval1_result_graph(ch4_val, c2h2_val, c2h4_val))
                    ])



if __name__ == '__main__':
    app.run_server(debug=True)