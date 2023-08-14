# -*- coding: utf-8 -*-
"""duval_triangle_4.py

This module calculates duval triangle 4 related diagnostics and generates duval triangle visualizations using plotly library.

@Author: https://github.com/ToniMellin
"""

# %%
import numpy as np
from pandas import isna
import pandas as pd
import plotly.graph_objects as go   # plotly is an interactive plotting library
import plotly.colors as pcolors

def create_duval_4_colorized():
    # https://community.plotly.com/t/shapes-in-ternary-plot/38566/10
    # https://plotly.com/python/reference/layout/ternary/
    fig = go.Figure(layout=dict(ternary_sum=100))
    #O
    fig.add_trace(go.Scatterternary(a= [0, 0, 9, 9, 0],
                                    b= [100, 30, 30, 91, 100],
                                    c= [0, 70, 61, 0, 0],
                                    name='O',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(255,211,37, 0.5)'
                                    ))
    #C
    fig.add_trace(go.Scatterternary(a= [0, 0, 64, 40, 15, 15, 0],
                                    b= [30, 0, 0, 24, 24, 30, 30],
                                    c= [70, 100, 36, 36, 61, 55, 70],
                                    name='C',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(92,81,75, 0.6)'
                                    ))
    #PD
    fig.add_trace(go.Scatterternary(a= [98, 97, 84, 85, 98],
                                    b= [0, 1, 1, 0, 0],
                                    c= [2, 2, 15, 15, 2],
                                    name='PD',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(178,255,228, 0.5)'
                                    ))
    #S
    fig.add_trace(go.Scatterternary(a= [9, 9, 15, 15, 40, 64, 85, 84, 97, 98, 100, 56, 9],
                                    b= [44, 30, 30, 24, 24, 0, 0, 1, 1, 0, 0, 44, 44],
                                    c= [47, 61, 55, 61,  36, 36, 15, 15, 2, 2, 0, 0, 47],
                                    name='S',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(170,156,192, 0.5)'
                                    ))
    fig.add_scatterternary(a=[4.5, 64, 28], b=[62, 18, 12], c=[33.5, 18, 60],
                            mode='text', text=['O', 'S', 'C'], hoverinfo='none', showlegend=False)
    fig.add_scatterternary(a=[91], b=[0.5], c=[8.5],
                            mode='text', text=['PD'], hoverinfo='none',
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
                        aaxis=dict(linecolor='#000000', hoverformat='H2=%%{a}<br>C2H6=%%{b}<br>CH4=%%{b}<extra></extra>'), 
                        baxis=dict(linecolor='#000000', hoverformat='H2=%%{a}<br>C2H6=%%{b}<br>CH4=%%{b}<extra></extra>'), 
                        caxis=dict(linecolor='#000000', hoverformat='H2=%%{a}<br>C2H6=%%{b}<br>CH4=%%{b}<extra></extra>'),
                        aaxis_title_text='H2',
                        baxis_title_text='C2H6',
                        caxis_title_text='CH4')
    #fig.update_traces(hovertemplate='H2: %{a}<br>C2H6: %{b}<br>CH4: %{c}<extra></extra>')
    
    return fig

def create_duval_4_nocolor():
    # https://community.plotly.com/t/shapes-in-ternary-plot/38566/10
    # https://plotly.com/python/reference/layout/ternary/
    fig = go.Figure(layout=dict(ternary_sum=100))
    #O
    fig.add_trace(go.Scatterternary(a= [0, 0, 9, 9, 0],
                                    b= [100, 30, 30, 91, 100],
                                    c= [0, 70, 61, 0, 0],
                                    name='O',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #C
    fig.add_trace(go.Scatterternary(a= [0, 0, 64, 40, 15, 15, 0],
                                    b= [30, 0, 0, 24, 24, 30, 30],
                                    c= [70, 100, 36, 36, 61, 55, 70],
                                    name='C',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #PD
    fig.add_trace(go.Scatterternary(a= [98, 97, 84, 85, 98],
                                    b= [0, 1, 1, 0, 0],
                                    c= [2, 2, 15, 15, 2],
                                    name='PD',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #S
    fig.add_trace(go.Scatterternary(a= [9, 9, 15, 15, 40, 64, 85, 84, 97, 98, 100, 56, 9],
                                    b= [44, 30, 30, 24, 24, 0, 0, 1, 1, 0, 0, 44, 44],
                                    c= [47, 61, 55, 61,  36, 36, 15, 15, 2, 2, 0, 0, 47],
                                    name='S',
                                    showlegend=False,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))

    fig.add_scatterternary(a=[4.5, 64, 28], b=[62, 18, 12], c=[33.5, 18, 60],
                            mode='text', text=['O', 'S', 'C'], hoverinfo='skip',
                            showlegend=False)
    fig.add_scatterternary(a=[91], b=[0.5], c=[8.5],
                            mode='text', text=['PD'], hoverinfo='skip',
                            showlegend=False)
    
    """
    # https://plotly.com/python/text-and-annotations/
    # arrow annotations
    fig.add_annotation(x=0.54, y=0.85,
                text="PD",
                showarrow=True,
                ax=40,
                ay=-10,
                arrowhead=1)
    """
    fig.update_ternaries(bgcolor='#FFFFFF', 
                        aaxis=dict(linecolor='#000000', hoverformat='H2=%%{a}<br>C2H6=%%{b}<br>CH4=%%{b}<extra></extra>'), 
                        baxis=dict(linecolor='#000000', hoverformat='H2=%%{a}<br>C2H6=%%{b}<br>CH4=%%{b}<extra></extra>'), 
                        caxis=dict(linecolor='#000000', hoverformat='H2=%%{a}<br>C2H6=%%{b}<br>CH4=%%{b}<extra></extra>'),
                        aaxis_title_text='H2',
                        baxis_title_text='C2H6',
                        caxis_title_text='CH4')
    #fig.update_traces(hovertemplate='CH4: %{a:.2f}<br>C2H2: %{b:.2f}<br>C2H4: %{c:.2f}<extra></extra>')
    
    return fig

def round_half_up(n, decimals=0):
    # rounding values
    multiplier = 10 ** decimals
    return np.floor(n*multiplier + 0.5) / multiplier

def calculate_duval_4_coordinates(h2, c2h6, ch4):

    i = h2
    j = c2h6
    k = ch4

    x = (i / (i + j + k))*100
    y = (j / (i + j + k))*100
    z = (k / (i + j + k))*100
    coordinates = round_half_up(np.array([x, y, z]), 2)

    return coordinates

def calculate_duval_4_result(h2, c2h6, ch4):
    try:
        if (isna(h2) is True) or (isna(c2h6) is True) or (isna(ch4) is True):
            return 'N/A'
        else:
            x, y, z = calculate_duval_4_coordinates(h2, c2h6, ch4)
            if z >= 2 and z <= 15 and y <= 1:
                return 'PD'
            elif (x > 9 and y > 30 and y < 46) or (x > 15 and y > 24 and y < 30) or (z < 36 and y >= 1 and y < 24) or (z < 36 and z > 15 and y < 1) or (z < 2 and y < 1):
                return 'S'
            elif (z >= 36 and y <= 24) or (x <= 15 and y >= 24 and y <= 30):
                return 'C'
            elif x <= 9 and y >= 30:
                return 'O'
            elif (x >= 9 and y >= 46):
                return 'ND'
            else:
                return 'ND'
    except TypeError:
        print('Duval result calculation error!')
        print('{h2}, {c2h6}, {ch4}')
        return 'N/A'
    
def create_duval_4_marker(h2, c2h6, ch4, marker_name, **kwargs):
    marker_coordinates = calculate_duval_4_coordinates(h2, c2h6, ch4)
    if 'timestamp' in kwargs and 'result' in kwargs and 'marker_color' in kwargs:
        try:
            timestamp = kwargs['timestamp']
            result = kwargs['result']
            set_color = kwargs['marker_color']
            return go.Scatterternary(   a= [marker_coordinates[0]],
                                        b= [marker_coordinates[1]],
                                        c= [marker_coordinates[2]],
                                        name= marker_name,
                                        mode='markers',
                                        marker_color=set_color,
                                        marker_size=10,
                                        meta= [result, timestamp],
                                        hovertemplate='Diagnosis: %{meta[0]}<br>H2: %{a:.2f}<br>C2H6: %{b:.2f}<br>CH4: %{c:.2f}%<br>%{meta[1]}<extra></extra>'
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
                                            meta= marker_name,
                                            hovertemplate='Diagnosis: %{meta}<br>H2: %{a:.2f}<br>C2H6: %{b:.2f}<br>CH4: %{c:.2f}<extra></extra>'
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
                                        meta= marker_name,
                                        hovertemplate='Diagnosis: %{meta}<br>H2: %{a:.2f}<br>C2H6: %{b:.2f}<br>CH4: %{c:.2f}<extra></extra>'
                                        )

def create_duval_4_result_graph(h2, c2h6, ch4):
    fig = create_duval_4_colorized()

    try:
        result_name = calculate_duval_4_result(h2, c2h6, ch4)
        fig.add_trace(create_duval_4_marker(h2, c2h6, ch4, result_name))
        return fig
    except:
        return fig

def create_duval_4_multi_results_graph(samples_df):
    fig = create_duval_4_colorized()
    sample_count = len(samples_df)
    colorscale = pcolors.sample_colorscale('Bluered', sample_count, low=0.0, high=1.0, colortype='rgb')

    try:
        sample_num = 0
        for row in samples_df.itertuples(name=None):
            time, h2, c2h6, ch4, rowcolor = row[1], row[2], row[4], row[3], colorscale[sample_num]
            sample_num+=1
            if (h2 == 0) and (c2h6 == 0) and (ch4 == 0):
                continue
            else:
                duval_result = calculate_duval_4_result(h2, c2h6, ch4)
                mark_name = f'{duval_result} {time}'
                fig.add_trace(create_duval_4_marker(h2, c2h6, ch4, mark_name, timestamp=time, result=duval_result, marker_color=rowcolor))
        return fig
    except Exception as e:
        print(e)
        return fig

# %%
if __name__ == "__main__":
    '''
    fig = create_duval_4_nocolor()
    marker_name = calculate_duval_4_result(10, 26, 64)
    fig.add_trace(create_duval_4_marker(10, 26, 64, marker_name))
    fig.show()

    fig2 = create_duval_4_colorized()
    marker_name2 = calculate_duval_4_result(10, 26, 64)
    fig2.add_trace(create_duval_4_marker(10, 26, 64, marker_name2))
    fig2.show()
    '''

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

    fig4 = create_duval_4_multi_results_graph(df_sample)
    fig4.show()
