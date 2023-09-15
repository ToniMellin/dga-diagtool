# -*- coding: utf-8 -*-
"""duval_triangle_2.py

This module calculates duval triangle 2 (LTC) related diagnostics and generates duval triangle visualizations using plotly library.

@Author: https://github.com/ToniMellin

* Copyright (C) 2023 Toni Mellin - All Rights Reserved
* You may use, distribute and modify this code under the
* terms of the MIT license.
*
* See file LICENSE or go to 
* https://github.com/ToniMellin/dga-diagtool/blob/master/LICENSE 
* for full license details.
"""

# %%
import numpy as np
from pandas import isna
import pandas as pd
import plotly.graph_objects as go   # plotly is an interactive plotting library
import plotly.colors as pcolors

def create_duval_2_colorized():
    # https://community.plotly.com/t/shapes-in-ternary-plot/38566/10
    # https://plotly.com/python/reference/layout/ternary/
    fig = go.Figure(layout=dict(ternary_sum=100))
    #D1
    fig.add_trace(go.Scatterternary(a= [0, 19, 19, 2, 2, 0, 0],
                                    b= [100, 81, 75, 92, 75, 77, 100],
                                    c= [0, 0, 6, 6, 23, 23, 0],
                                    name='D1',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(228,178,255, 0.5)'
                                    ))
    #N
    fig.add_trace(go.Scatterternary(a= [19, 19, 2, 2, 19],
                                    b= [58, 75, 92, 75, 58],
                                    c= [23, 6, 6, 23, 23],
                                    name='N',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(178,255,228, 0.5)'
                                    ))


    #X1
    fig.add_trace(go.Scatterternary(a= [77, 19, 19, 100, 77],
                                    b= [0, 58, 81, 0, 0],
                                    c= [23, 23, 0, 0, 23],
                                    name='X1',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(178,205,255, 0.5)'
                                    ))
    
    #X3
    fig.add_trace(go.Scatterternary(a= [0, 0, 62],
                                    b= [15, 77, 15],
                                    c= [85, 23, 23],
                                    name='X3',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(178,244,255, 0.5)'
                                    ))
    
    #T2
    fig.add_trace(go.Scatterternary(a= [77, 62, 35, 50, 77],
                                    b= [0, 15, 15, 0, 0],
                                    c= [23, 23, 50, 50, 23],
                                    name='T2',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(245, 148, 39, 0.5)'
                                    ))
    #T3
    fig.add_trace(go.Scatterternary(a= [50, 35, 0, 0, 50],
                                    b= [0, 15, 15, 0, 0],
                                    c= [50, 50, 85, 100, 50],
                                    name='T3',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(245, 54, 39, 0.5)'
                                    ))
    fig.add_scatterternary(a=[10, 11], b=[87, 73], c=[3, 14],
                            mode='text', text=['D1', 'N'], hoverinfo='none', showlegend=False)
    fig.add_scatterternary(a=[50, 30, 55, 20], b=[38, 30, 8, 7.5], c=[12, 40, 37, 72.5],
                            mode='text', text=['X1', 'X3', 'T2', 'T3'], hoverinfo='none',
                            showlegend=False)
    
    """
    # https://plotly.com/python/text-and-annotations/
    # arrow annotations
    fig.add_annotation(x=0.50, y=0.85,
                text="PD",
                showarrow=True,
                xref='paper',
                yref='paper',
                xanchor='center',
                yanchor='middle',
                ax=40,
                ay=-10,
                arrowhead=1)
    fig.add_annotation(x=0.535, y=0.78,
                text="T1",
                showarrow=True,
                xref='paper',
                yref='paper',
                xanchor='center',
                yanchor='middle',
                ax=40,
                ay=-10,
                arrowhead=1)
    fig.add_annotation(x=0.665, y=0.60,
                text="T2",
                showarrow=True,
                xref='paper',
                yref='paper',
                xanchor='center',
                yanchor='middle',
                ax=40,
                ay=-10,
                arrowhead=1)
    """
    fig.update_ternaries(bgcolor='#FFFFFF', 
                        aaxis=dict(linecolor='#000000', hoverformat='CH4=%%{a}<br>C2H2=%%{b}<br>C2H4=%%{b}<extra></extra>'), 
                        baxis=dict(linecolor='#000000', hoverformat='CH4=%%{a}<br>C2H2=%%{b}<br>C2H4=%%{b}<extra></extra>'), 
                        caxis=dict(linecolor='#000000', hoverformat='CH4=%%{a}<br>C2H2=%%{b}<br>C2H4=%%{b}<extra></extra>'),
                        aaxis_title_text='CH4',
                        baxis_title_text='C2H2',
                        caxis_title_text='C2H4')
    #fig.update_traces(hovertemplate='CH4: %{a}<br>C2H2: %{b}<br>C2H4: %{c}<extra></extra>')
    
    return fig

def create_duval_2_nocolor():
    # https://community.plotly.com/t/shapes-in-ternary-plot/38566/10
    # https://plotly.com/python/reference/layout/ternary/
    # a = CH4%, b = C2H2%, c = C2H4%
    fig = go.Figure(layout=dict(ternary_sum=100))
    #D1
    fig.add_trace(go.Scatterternary(a= [0, 19, 19, 2, 2, 0, 0],
                                    b= [100, 81, 75, 92, 75, 77, 100],
                                    c= [0, 0, 6, 6, 23, 23, 0],
                                    name='D1',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #N
    fig.add_trace(go.Scatterternary(a= [19, 19, 2, 2, 19],
                                    b= [58, 75, 92, 75, 58],
                                    c= [23, 6, 6, 23, 23],
                                    name='N',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))


    #X1
    fig.add_trace(go.Scatterternary(a= [77, 19, 19, 100, 77],
                                    b= [0, 58, 81, 0, 0],
                                    c= [23, 23, 0, 0, 23],
                                    name='X1',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    
    #X3
    fig.add_trace(go.Scatterternary(a= [0, 0, 62, 0],
                                    b= [15, 77, 15, 15],
                                    c= [85, 23, 23, 85],
                                    name='X3',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    
    #T2
    fig.add_trace(go.Scatterternary(a= [77, 62, 35, 50, 77],
                                    b= [0, 15, 15, 0, 0],
                                    c= [23, 23, 50, 50, 23],
                                    name='T2',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #T3
    fig.add_trace(go.Scatterternary(a= [50, 35, 0, 0, 50],
                                    b= [0, 15, 15, 0, 0],
                                    c= [50, 50, 85, 100, 50],
                                    name='T3',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    fig.add_scatterternary(a=[10, 11], b=[87, 73], c=[3, 14],
                            mode='text', text=['D1', 'N'], hoverinfo='skip',
                            showlegend=False)
    fig.add_scatterternary(a=[50, 30, 55, 20], b=[38, 30, 8, 7.5], c=[12, 40, 37, 72.5],
                            mode='text', text=['X1', 'X3', 'T2', 'T3'], hoverinfo='skip',
                            showlegend=False)
    
    """
    # https://plotly.com/python/text-and-annotations/
    # arrow annotations
    fig.add_annotation(x=0.50, y=0.99,
                text="PD",
                showarrow=True,
                ax=40,
                ay=-10,
                arrowhead=1)
    fig.add_annotation(x=0.525, y=0.90,
                text="T1",
                showarrow=True,
                ax=40,
                ay=-10,
                arrowhead=1)
    fig.add_annotation(x=0.643, y=0.65,
                text="T2",
                showarrow=True,
                ax=40,
                ay=-10,
                arrowhead=1)
    """
    fig.update_ternaries(bgcolor='#FFFFFF', 
                        aaxis=dict(linecolor='#000000', hoverformat='CH4=%%{a}<br>C2H2=%%{b}<br>C2H4=%%{b}<extra></extra>'), 
                        baxis=dict(linecolor='#000000', hoverformat='CH4=%%{a}<br>C2H2=%%{b}<br>C2H4=%%{b}<extra></extra>'), 
                        caxis=dict(linecolor='#000000', hoverformat='CH4=%%{a}<br>C2H2=%%{b}<br>C2H4=%%{b}<extra></extra>'),
                        aaxis_title_text='CH4',
                        baxis_title_text='C2H2',
                        caxis_title_text='C2H4')
    #fig.update_traces(hovertemplate='CH4: %{a:.2f}<br>C2H2: %{b:.2f}<br>C2H4: %{c:.2f}<extra></extra>')
    
    return fig

def round_half_up(n, decimals=0):
    # rounding values
    multiplier = 10 ** decimals
    return np.floor(n*multiplier + 0.5) / multiplier

def calculate_duval_2_coordinates(ch4, c2h2, c2h4):

    i = ch4
    j = c2h2
    k = c2h4

    x = (i / (i + j + k))*100
    y = (j / (i + j + k))*100
    z = (k / (i + j + k))*100
    coordinates = round_half_up(np.array([x, y, z]), 2)

    return coordinates

def calculate_duval_2_result(ch4, c2h2, c2h4):
    try:
        if (isna(ch4) is True) or (isna(c2h2) is True) or (isna(c2h4) is True):
            return 'N/A'
        if (ch4 == 0) and (c2h2 == 0) and (c2h4 == 0):
            return 'N/A'
        else:
            x, y, z = calculate_duval_2_coordinates(ch4, c2h2, c2h4)
            if x <= 19 and x >= 2 and z <= 23 and z >= 6:
                return 'N'
            elif (x <= 19 and z <6) or (x < 2 and z <= 23):
                return 'D1'
            elif x > 19 and z <=23:
                return 'X1'
            elif y > 15 and z > 23:
                return 'X3'
            elif  z > 23 and z < 50 and y <=15:
                return 'T2'
            elif z >= 50 and y <= 15:
                return 'T3'
            else:
                return 'ND'
    except TypeError:
        print('Duval result calculation error!')
        print('{ch4}, {c2h2}, {c2h4}')
        return 'N/A'
 
def create_duval_2_marker(ch4, c2h2, c2h4, marker_name, **kwargs):
    marker_coordinates = calculate_duval_2_coordinates(ch4, c2h2, c2h4)

    if 'timestamp' in kwargs and 'result' in kwargs and 'marker_color' in kwargs:
        try:
            timestamp = kwargs['timestamp']
            result = kwargs['result']
            set_color = kwargs['marker_color']
            return go.Scatterternary(       a= [marker_coordinates[0]],
                                            b= [marker_coordinates[1]],
                                            c= [marker_coordinates[2]],
                                            name= marker_name,
                                            mode='markers',
                                            marker_color=set_color,
                                            marker_size=10,
                                            meta= [result, ch4, c2h2, c2h4, timestamp],
                                            hovertemplate="Diagnosis: %{meta[0]}<br>CH4:  %{meta[1]} ppm (%{a:.2f}%)<br>C2H2: %{meta[2]} ppm (%{b:.2f}%)<br>C2H4: %{meta[3]} ppm (%{c:.2f}%)<br>%{meta[4]}<extra></extra>"
                                            )
        except Exception as e:
            print(e)
            pass
    elif 'timestamp' not in kwargs and 'result' not in kwargs and 'marker_color' in kwargs:
        try:
            set_color = kwargs['marker_color']
            return go.Scatterternary(       a= [marker_coordinates[0]],
                                            b= [marker_coordinates[1]],
                                            c= [marker_coordinates[2]],
                                            name= marker_name,
                                            mode='markers',
                                            marker_color=set_color,
                                            marker_size=10,
                                            meta= [marker_name, ch4, c2h2, c2h4],
                                            hovertemplate="Diagnosis: %{meta[0]}<br>CH4:  %{meta[1]} ppm (%{a:.2f}%)<br>C2H2: %{meta[2]} ppm (%{b:.2f}%)<br>C2H4: %{meta[3]} ppm (%{c:.2f}%)<extra></extra>"
                                            )
        except Exception as e:
            print(e)
            pass
    else:  
        return go.Scatterternary(       a= [marker_coordinates[0]],
                                        b= [marker_coordinates[1]],
                                        c= [marker_coordinates[2]],
                                        name= marker_name,
                                        mode='markers',
                                        marker_color='red',
                                        marker_size=10,
                                        meta= [marker_name, ch4, c2h2, c2h4],
                                        hovertemplate="Diagnosis: %{meta[0]}<br>CH4:  %{meta[1]} ppm (%{a:.2f}%)<br>C2H2: %{meta[2]} ppm (%{b:.2f}%)<br>C2H4: %{meta[3]} ppm (%{c:.2f}%)<extra></extra>"
                                        )

def create_duval_2_result_graph(ch4, c2h2, c2h4):
    fig = create_duval_2_colorized()

    try:
        result_name = calculate_duval_2_result(ch4, c2h2, c2h4)
        fig.add_trace(create_duval_2_marker(ch4, c2h2, c2h4, result_name))
        return fig
    except:
        return fig

def create_duval_2_multi_results_graph(samples_df):
    fig = create_duval_2_colorized()

    sample_count = len(samples_df)
    if sample_count == 1:
        colorscale = ['blue']
    else:
        colorscale = pcolors.sample_colorscale('Bluered', sample_count, low=0.0, high=1.0, colortype='rgb')

    try:
        sample_num = 0
        for row in samples_df.itertuples(name=None):
            time, ch4, c2h4, c2h2, rowcolor = row[1], row[3], row[5], row[6], colorscale[sample_num]
            sample_num+=1
            if (ch4 == 0) and (c2h2 == 0) and (c2h4 == 0):
                continue
            else:
                duval_result = calculate_duval_2_result(ch4, c2h2, c2h4)
                mark_name = f'{duval_result} {time}'
                fig.add_trace(create_duval_2_marker(ch4, c2h2, c2h4, mark_name, timestamp=time, result=duval_result, marker_color=rowcolor))
        return fig
    except Exception as e:
        print(e)
        return fig

# %%
if __name__ == "__main__":
    '''
    fig = create_duval_2_nocolor()
    marker_name = calculate_duval_2_result(10, 26, 64)
    fig.add_trace(create_duval_2_marker(10, 26, 64, marker_name))
    fig.show()

    fig2 = create_duval_2_colorized()
    marker_name2 = calculate_duval_2_result(10, 26, 64)
    fig2.add_trace(create_duval_2_marker(10, 26, 64, marker_name2))
    fig2.show()

    '''

    fig2 = create_duval_2_colorized()
    marker_name2 = calculate_duval_2_result(10, 85, 5)
    fig2.add_trace(create_duval_2_marker(10, 85, 5, marker_name2))
    fig2.show()

    #fig3 = create_duval_2_result_graph(55, 8, 55)
    #fig3.show()

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

    print(df_sample)

    #fig4 = create_duval_2_multi_results_graph(df_sample)
    #fig4.show()
