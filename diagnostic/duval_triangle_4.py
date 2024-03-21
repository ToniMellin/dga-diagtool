# -*- coding: utf-8 -*-
"""duval_triangle_4.py

This module calculates duval triangle 4 related diagnostics and generates duval triangle visualizations using plotly library.

@Author: https://github.com/ToniMellin

* Copyright (C) 2023-2024 Toni Mellin - All Rights Reserved
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

# * Triangle 4 fault area ternary coordinate constants (plotly: a, b, c) *

TRIANGLE4_PD_A = [98, 97, 84, 85, 98]
TRIANGLE4_PD_B = [0, 1, 1, 0, 0]
TRIANGLE4_PD_C = [2, 2, 15, 15, 2]

TRIANGLE4_S_A = [100, 54, 9, 9, 15, 15, 40, 64, 85, 84, 97, 98, 100]
TRIANGLE4_S_B = [0, 46, 46, 30, 30, 24, 24, 0, 0, 1, 1, 0, 0]
TRIANGLE4_S_C = [0, 0, 45, 61, 55, 61,  36, 36, 15, 15, 2, 2, 0]

TRIANGLE4_O_A = [0, 0, 9, 9, 0]
TRIANGLE4_O_B = [100, 30, 30, 91, 100]
TRIANGLE4_O_C = [0, 70, 61, 0, 0]

TRIANGLE4_C_A = [0, 0, 64, 40, 15, 15, 0]
TRIANGLE4_C_B = [30, 0, 0, 24, 24, 30, 30]
TRIANGLE4_C_C = [70, 100, 36, 36, 61, 55, 70]

TRIANGLE4_ND_A = [54, 9, 9, 54]
TRIANGLE4_ND_B = [46, 91, 46, 46]
TRIANGLE4_ND_C = [0, 0, 45, 0]


def create_duval_4_colorized(legend_show=False):
    # https://community.plotly.com/t/shapes-in-ternary-plot/38566/10
    # https://plotly.com/python/reference/layout/ternary/
    fig = go.Figure(layout=dict(ternary_sum=100))

    #PD
    fig.add_trace(go.Scatterternary(a= TRIANGLE4_PD_A,
                                    b= TRIANGLE4_PD_B,
                                    c= TRIANGLE4_PD_C,
                                    name='PD',
                                    showlegend=legend_show,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(178,255,228, 0.5)'
                                    ))
    #S
    fig.add_trace(go.Scatterternary(a= TRIANGLE4_S_A,
                                    b= TRIANGLE4_S_B,
                                    c= TRIANGLE4_S_C,
                                    name='S',
                                    showlegend=legend_show,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(170,156,192, 0.5)'
                                    ))
    #O
    fig.add_trace(go.Scatterternary(a= TRIANGLE4_O_A,
                                    b= TRIANGLE4_O_B,
                                    c= TRIANGLE4_O_C,
                                    name='O',
                                    showlegend=legend_show,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(255,211,37, 0.5)'
                                    ))
    #C
    fig.add_trace(go.Scatterternary(a= TRIANGLE4_C_A,
                                    b= TRIANGLE4_C_B,
                                    c= TRIANGLE4_C_C,
                                    name='C',
                                    showlegend=legend_show,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(92,81,75, 0.6)'
                                    ))
    #ND
    fig.add_trace(go.Scatterternary(a= TRIANGLE4_ND_A,
                                    b= TRIANGLE4_ND_B,
                                    c= TRIANGLE4_ND_C,
                                    name='ND',
                                    showlegend=legend_show,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))

    # Annotations
    fig.add_scatterternary(a=[26, 4.5, 64, 28], b=[62, 62, 18, 12], c=[14, 33.5, 18, 60],
                            mode='text', text=['ND', 'O', 'S', 'C'], hoverinfo='none', showlegend=legend_show)
    fig.add_scatterternary(a=[91], b=[0.5], c=[8.5],
                            mode='text', text=['PD'], hoverinfo='none',
                            showlegend=legend_show)
    
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

def create_duval_4_nocolor(legend_show=False):
    # https://community.plotly.com/t/shapes-in-ternary-plot/38566/10
    # https://plotly.com/python/reference/layout/ternary/
    fig = go.Figure(layout=dict(ternary_sum=100))

    #PD
    fig.add_trace(go.Scatterternary(a= TRIANGLE4_PD_A,
                                    b= TRIANGLE4_PD_B,
                                    c= TRIANGLE4_PD_C,
                                    name='PD',
                                    showlegend=legend_show,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #S
    fig.add_trace(go.Scatterternary(a= TRIANGLE4_S_A,
                                    b= TRIANGLE4_S_B,
                                    c= TRIANGLE4_S_C,
                                    name='S',
                                    showlegend=legend_show,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #O
    fig.add_trace(go.Scatterternary(a= TRIANGLE4_O_A,
                                    b= TRIANGLE4_O_B,
                                    c= TRIANGLE4_O_C,
                                    name='O',
                                    showlegend=legend_show,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #C
    fig.add_trace(go.Scatterternary(a= TRIANGLE4_C_A,
                                    b= TRIANGLE4_C_B,
                                    c= TRIANGLE4_C_C,
                                    name='C',
                                    showlegend=legend_show,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #ND
    fig.add_trace(go.Scatterternary(a= TRIANGLE4_ND_A,
                                    b= TRIANGLE4_ND_B,
                                    c= TRIANGLE4_ND_C,
                                    name='ND',
                                    showlegend=legend_show,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))

    # Annotations
    fig.add_scatterternary(a=[26, 4.5, 64, 28], b=[62, 62, 18, 12], c=[14, 33.5, 18, 60],
                            mode='text', text=['ND', 'O', 'S', 'C'], hoverinfo='skip',
                            showlegend=legend_show)
    fig.add_scatterternary(a=[91], b=[0.5], c=[8.5],
                            mode='text', text=['PD'], hoverinfo='skip',
                            showlegend=legend_show)
    
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

def calculate_duval_4_coordinates(h2, c2h6, ch4, rounding=False):

    i = h2
    j = c2h6
    k = ch4

    if (i == 0) and (j == 0) and (k == 0):
        return [100/3, 100/3, 100/3]

    x = (i / (i + j + k))*100
    y = (j / (i + j + k))*100
    z = (k / (i + j + k))*100

    if rounding is False:
       coordinates = np.array([x, y, z])
    elif type(rounding) is int:
        coordinates = round_half_up(np.array([x, y, z]), rounding)
    else:
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
            elif (x > 9 and y > 30 and y < 46) or (x > 15 and y > 24 and y < 30) or (z < 36 and y >= 1 and y <= 24) or (z < 36 and z > 15 and y < 1) or (z < 2 and y < 1):
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
    
def create_duval_4_marker(h2, c2h6, ch4, **kwargs):
    marker_coordinates = calculate_duval_4_coordinates(h2, c2h6, ch4)
    result = calculate_duval_4_result(h2, c2h6, ch4)

    # check for timestamp
    if  'timestamp' in kwargs:
        timestamp = kwargs['timestamp']
        metalist = [result, h2, c2h6, ch4, timestamp]
    else:
        timestamp = None
        metalist = [result, h2, c2h6, ch4]

    # formulate a name for the marker if not given
    if 'marker_name' in kwargs:
        marker_name = kwargs['marker_name']
    elif (timestamp is not None) and ('marker_name' not in kwargs):
        marker_name = f'{result} {timestamp}'
    else:
        marker_name = result


    if (timestamp is not None) and 'marker_color' in kwargs:
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
                                        meta= metalist,
                                        hovertemplate="Diagnosis: %{meta[0]}<br>H2:   %{meta[1]} ppm (%{a:.2f}%)<br>C2H6: %{meta[2]} ppm (%{b:.2f}%)<br>CH4:  %{meta[3]} ppm (%{c:.2f}%)<br>%{meta[4]}<extra></extra>"
                                            )
        except Exception as e:
            print(e)
            pass
    elif (timestamp is None) and 'marker_color' in kwargs:
        try:
            set_color = kwargs['marker_color']
            return go.Scatterternary(       a= [marker_coordinates[0]],
                                            b= [marker_coordinates[1]],
                                            c= [marker_coordinates[2]],
                                            name= marker_name,
                                            mode='markers',
                                            marker_color=set_color,
                                            marker_size=10,
                                            meta= metalist,
                                            hovertemplate="Diagnosis: %{meta[0]}<br>H2:   %{meta[1]} ppm (%{a:.2f}%)<br>C2H6: %{meta[2]} ppm (%{b:.2f}%)<br>CH4:  %{meta[3]} ppm (%{c:.2f}%)<extra></extra>"
                                            )
        except Exception as e:
            print(e)
            pass
    elif (timestamp is not None) and 'marker_color' not in kwargs:
        try:
            set_color = kwargs['marker_color']
            return go.Scatterternary(       a= [marker_coordinates[0]],
                                            b= [marker_coordinates[1]],
                                            c= [marker_coordinates[2]],
                                            name= marker_name,
                                            mode='markers',
                                            marker_color=set_color,
                                            marker_size=10,
                                            meta= metalist,
                                            hovertemplate="Diagnosis: %{meta[0]}<br>H2:   %{meta[1]} ppm (%{a:.2f}%)<br>C2H6: %{meta[2]} ppm (%{b:.2f}%)<br>CH4:  %{meta[3]} ppm (%{c:.2f}%)<br>%{meta[4]}<extra></extra>"
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
                                        meta= [result, h2, c2h6, ch4],
                                        hovertemplate="Diagnosis: %{meta[0]}<br>H2:   %{meta[1]} ppm (%{a:.2f}%)<br>C2H6: %{meta[2]} ppm (%{b:.2f}%)<br>CH4:  %{meta[3]} ppm (%{c:.2f}%)<extra></extra>"
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
    if sample_count == 1:
        colorscale = ['blue']
    else:
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
                fig.add_trace(create_duval_4_marker(h2, c2h6, ch4, marker_name=mark_name, timestamp=time, marker_color=rowcolor))
        return fig
    except Exception as e:
        print(e)
        return fig
    
def create_duval_4_group_graph(h2_groups, c2h6_groups, ch4_groups, group_names, colorized=True, **kwargs):
    # https://plotly.com/python/marker-style/
    marker_symbol_list = ['circle', 'diamond', 'square', 'x-thin', 'cross-thin', 
                          'asterisk', 'y-up', 'star-triangle-up', 'star-triangle-down', 
                          'circle-open', 'diamond-open', 'square-open', 'star-triangle-up-open', 
                          'star-triangle-down-open']
    try:
        assert len(h2_groups) == len(c2h6_groups)
        assert len(c2h6_groups) == len(ch4_groups)
        assert len(h2_groups) == len(ch4_groups)
        assert len(h2_groups) == len(group_names)
    except Exception as e:
        print(e)

    if colorized is True:
        fig = create_duval_4_colorized()
    else:
        fig = create_duval_4_nocolor()

    if 'group_colors' in kwargs:
        color_list = kwargs['group_colors']
    else:
        color_list = pcolors.qualitative.Plotly + pcolors.qualitative.Light24_r
    
    try:
        for i, group_name in enumerate(group_names):
            coord_list = []

            for h2_value, c2h6_value, ch4_value in zip(h2_groups[i], c2h6_groups[i], ch4_groups[i]):
                if (h2_value == 0) and (c2h6_value == 0) and (ch4_value == 0):
                    continue
                coord_list.append(calculate_duval_4_coordinates(h2_value, c2h6_value, ch4_value))

            
            coord_list_t = np.transpose(coord_list)
            print(coord_list_t)
            fig.add_trace(go.Scatterternary(a= coord_list_t[0],
                                            b= coord_list_t[1],
                                            c= coord_list_t[2],
                                            name= group_name,
                                            mode='markers',
                                            marker_symbol=marker_symbol_list[i],
                                            marker_color=color_list[i],
                                            marker_size=10,
                                            meta= [group_name],
                                            hovertemplate="%{meta[0]}<br>H2:  %{a:.2f}%<br>C2H6: %{b:.2f}%<br>CH4: %{c:.2f}%<extra></extra>"))
    except Exception as e:
        print(e)

    return fig

# %%
if __name__ == "__main__":
    
    fig = create_duval_4_nocolor()
    fig.add_trace(create_duval_4_marker(56, 24, 20))
    fig.show()

    fig2 = create_duval_4_colorized()
    fig2.add_trace(create_duval_4_marker(9, 46, 45, marker_name='test'))
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

    #h2_list= [[200, 300, 400, 500], [0, 10, 50, 100, 160, 250], [1000, 1100, 1200]]
    #c2h6_list= [[10, 20, 30, 40], [0, 60, 121, 172, 200, 207], [100, 200, 500]]
    #ch4_list= [[400, 500, 600, 1000], [0, 20, 41, 60, 66, 80], [60, 80, 110]]
    #groups_list= ['Group1', 'Group2', 'Group3']

    #fig5 = create_duval_4_group_graph(h2_list, c2h6_list, ch4_list, groups_list, colorized=False, group_colors=['rgb(136, 204, 238)', 'rgb(204, 102, 119)', 'rgb(221, 204, 119)', 'rgb(17, 119, 51)'])
    #fig5.show()
    '''
