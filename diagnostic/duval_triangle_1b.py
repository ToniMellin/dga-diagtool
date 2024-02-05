# -*- coding: utf-8 -*-
"""duval_triangle_1b.py

This module calculates duval triangle 1b related diagnostics and generates duval triangle visualizations using plotly library.

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

def create_duval_1b_colorized():
    # https://community.plotly.com/t/shapes-in-ternary-plot/38566/10
    # https://plotly.com/python/reference/layout/ternary/
    fig = go.Figure(layout=dict(ternary_sum=100))
    '''
    #D1
    fig.add_trace(go.Scatterternary(a= [0, 0, 64, 87, 0],
                                    b= [100, 77, 13, 13, 100],
                                    c= [0, 23, 23, 0, 0],
                                    name='D1',
                                    showlegend=True,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(178,244,255, 0.5)'
                                    ))
    #D2
    fig.add_trace(go.Scatterternary(a= [64, 0, 0, 31, 47, 64],
                                    b= [13, 77, 29, 29, 13, 13],
                                    c= [23, 23, 71, 40, 40, 23],
                                    name='D2',
                                    showlegend=True,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(178,205,255, 0.5)'
                                    ))
    '''
    #D1-P
    fig.add_trace(go.Scatterternary(a= [13, 17, 39, 39, 13],
                                    b= [64, 63, 41, 38, 64],
                                    c= [23, 20, 20, 23, 23],
                                    name='D1-P',
                                    showlegend=True,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(0, 217, 255, 0.5)'
                                    ))
    #D1-H
    fig.add_trace(go.Scatterternary(a= [0, 87, 64, 13, 17, 39, 39, 0, 0],
                                    b= [100, 13, 13, 64, 63, 41, 38, 77, 100],
                                    c= [0, 0, 23, 23, 20, 20, 23, 23, 0],
                                    name='D1-H',
                                    showlegend=True,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(178,244,255, 0.5)'
                                    ))

    #D2-P
    fig.add_trace(go.Scatterternary(a= [43, 41, 16, 13, 43],
                                    b= [34, 26, 49, 64, 34],
                                    c= [23, 33, 35, 23, 23],
                                    name='D2-P',
                                    showlegend=True,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(0, 89, 255, 0.5)'
                                    ))
    #D2-H
    fig.add_trace(go.Scatterternary(a= [0, 13, 16, 41, 43, 64, 47, 31, 0, 0],
                                    b= [77, 64, 49, 26, 34, 13, 13, 29, 29, 77],
                                    c= [23, 23, 35, 33, 23, 23, 40, 40, 71, 23],
                                    name='D2-H',
                                    showlegend=True,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(178,205,255, 0.5)'
                                    ))
    #DT
    fig.add_trace(go.Scatterternary(a= [87, 47, 31, 0, 0, 35, 46, 96, 87],
                                    b= [13, 13, 29, 29, 15, 15, 4, 4, 13],
                                    c= [0, 40, 40, 71, 85, 50, 50, 0, 0],
                                    name='DT',
                                    showlegend=True,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(228,178,255, 0.5)'
                                    ))
    #PD
    fig.add_trace(go.Scatterternary(a= [100, 98, 98],
                                    b= [0, 2, 0],
                                    c= [0, 0, 2],
                                    name='PD',
                                    showlegend=True,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(178,255,228, 0.5)'
                                    ))
    #T1
    fig.add_trace(go.Scatterternary(a= [96, 76, 80, 98, 98, 96],
                                    b= [4, 4, 0, 0, 2, 4],
                                    c= [0, 20, 20, 2, 0, 0],
                                    name='T1',
                                    showlegend=True,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(245, 243, 39, 0.5)'
                                    ))
    #T2
    fig.add_trace(go.Scatterternary(a= [80, 76, 46, 50, 80],
                                    b= [0, 4, 4, 0, 0],
                                    c= [20, 20, 50, 50, 20],
                                    name='T2',
                                    showlegend=True,
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
                                    showlegend=True,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(245, 54, 39, 0.5)'
                                    ))
    fig.add_scatterternary(a=[20, 28, 28, 20, 20, 20], b=[68.5, 50.5, 43.5, 38, 22, 7.5], c=[11.5, 21.5, 28.5, 42, 58, 72.5],
                            mode='text', text=['D1-H', 'D1-P', 'D2-P', 'D2-H', 'DT', 'T3'], hoverinfo='none', showlegend=True)
    fig.add_scatterternary(a=[99, 88, 63], b=[0.5, 2, 2], c=[0.5, 10, 35],
                            mode='text', text=['PD', 'T1', 'T2'], hoverinfo='none',
                            showlegend=True)
    
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

def create_duval_1b_nocolor():
    # https://community.plotly.com/t/shapes-in-ternary-plot/38566/10
    # https://plotly.com/python/reference/layout/ternary/
    fig = go.Figure(layout=dict(ternary_sum=100))
    '''
    #D1
    fig.add_trace(go.Scatterternary(a= [0, 0, 64, 87, 0],
                                    b= [100, 77, 13, 13, 100],
                                    c= [0, 23, 23, 0, 0],
                                    name='D1',
                                    showlegend=True,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #D2
    fig.add_trace(go.Scatterternary(a= [64, 0, 0, 31, 47, 64],
                                    b= [13, 77, 29, 29, 13, 13],
                                    c= [23, 23, 71, 40, 40, 23],
                                    name='D2',
                                    showlegend=True,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    '''
    #D1-P
    fig.add_trace(go.Scatterternary(a= [13, 17, 39, 39, 13],
                                    b= [64, 63, 41, 38, 64],
                                    c= [23, 20, 20, 23, 23],
                                    name='D1-P',
                                    showlegend=True,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #D1-H
    fig.add_trace(go.Scatterternary(a= [0, 87, 64, 13, 17, 39, 39, 0, 0],
                                    b= [100, 13, 13, 64, 63, 41, 38, 77, 100],
                                    c= [0, 0, 23, 23, 20, 20, 23, 23, 0],
                                    name='D1-H',
                                    showlegend=True,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))

    #D2-P
    fig.add_trace(go.Scatterternary(a= [43, 41, 16, 13, 43],
                                    b= [34, 26, 49, 64, 34],
                                    c= [23, 33, 35, 23, 23],
                                    name='D2-P',
                                    showlegend=True,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #D2-H
    fig.add_trace(go.Scatterternary(a= [0, 13, 16, 41, 43, 64, 47, 31, 0, 0],
                                    b= [77, 64, 49, 26, 34, 13, 13, 29, 29, 77],
                                    c= [23, 23, 35, 33, 23, 23, 40, 40, 71, 23],
                                    name='D2-H',
                                    showlegend=True,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #DT
    fig.add_trace(go.Scatterternary(a= [87, 47, 31, 0, 0, 35, 46, 96, 87],
                                    b= [13, 13, 29, 29, 15, 15, 4, 4, 13],
                                    c= [0, 40, 40, 71, 85, 50, 50, 0, 0],
                                    name='DT',
                                    showlegend=True,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #PD
    fig.add_trace(go.Scatterternary(a= [100, 98, 98],
                                    b= [0, 2, 0],
                                    c= [0, 0, 2],
                                    name='PD',
                                    showlegend=True,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #T1
    fig.add_trace(go.Scatterternary(a= [96, 76, 80, 98, 98, 96],
                                    b= [4, 4, 0, 0, 2, 4],
                                    c= [0, 20, 20, 2, 0, 0],
                                    name='T1',
                                    showlegend=True,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #T2
    fig.add_trace(go.Scatterternary(a= [80, 76, 46, 50, 80],
                                    b= [0, 4, 4, 0, 0],
                                    c= [20, 20, 50, 50, 20],
                                    name='T2',
                                    showlegend=True,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #T3
    fig.add_trace(go.Scatterternary(a= [50, 35, 0, 0, 50],
                                    b= [0, 15, 15, 0, 0],
                                    c= [50, 50, 85, 100, 50],
                                    name='T3',
                                    showlegend=True,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    fig.add_scatterternary(a=[20, 28, 28, 20, 20, 20], b=[68.5, 50.5, 43.5, 38, 22, 7.5], c=[11.5, 21.5, 28.5, 42, 58, 72.5],
                            mode='text', text=['D1-H', 'D1-P', 'D2-P', 'D2-H', 'DT', 'T3'], hoverinfo='none', showlegend=True)
    fig.add_scatterternary(a=[99, 88, 63], b=[0.5, 2, 2], c=[0.5, 10, 35],
                            mode='text', text=['PD', 'T1', 'T2'], hoverinfo='none',
                            showlegend=True)
    
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

def calculate_duval_1b_coordinates(ch4, c2h2, c2h4):

    i = ch4
    j = c2h2
    k = c2h4

    if (i == 0) and (j == 0) and (k == 0):
        return [0, 0, 0]

    x = (i / (i + j + k))*100
    y = (j / (i + j + k))*100
    z = (k / (i + j + k))*100
    coordinates = round_half_up(np.array([x, y, z]), 2)

    return coordinates

def calculate_duval_1b_result(ch4, c2h2, c2h4):
    try:
        if (isna(ch4) is True) or (isna(c2h2) is True) or (isna(c2h4) is True):
            return 'N/A'
        if (ch4 == 0) and (c2h2 == 0) and (c2h4 == 0):
            return 'N/A'
        else:
            x, y, z = calculate_duval_1b_coordinates(ch4, c2h2, c2h4)
            if x >= 98:
                return 'PD'
            elif z <= 23 and y >= 13:
                return 'D1'
            elif (z <= 40 and z > 23 and y >= 13) or (z >= 40 and y >= 29):
                return 'D2'
            elif x < 98 and z <= 20 and y <= 4:
                return 'T1'
            elif  z > 20 and z < 50 and y <= 4:
                return 'T2'
            elif y <= 15 and z >= 50:
                return 'T3'
            elif (z <= 40 and y > 4 and y < 13 ) or (z > 40 and z < 50 and y > 4 and y < 29) or (z >= 50 and y > 15 and y < 29):
                return 'DT'
            else:
                return 'ND'
    except TypeError:
        print('Duval result calculation error!')
        print('{ch4}, {c2h2}, {c2h4}')
        return 'N/A'
 
def create_duval_1b_marker(ch4, c2h2, c2h4, marker_name, **kwargs):
    marker_coordinates = calculate_duval_1b_coordinates(ch4, c2h2, c2h4)

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

def create_duval_1b_result_graph(ch4, c2h2, c2h4):
    fig = create_duval_1b_colorized()

    try:
        result_name = calculate_duval_1b_result(ch4, c2h2, c2h4)
        fig.add_trace(create_duval_1b_marker(ch4, c2h2, c2h4, result_name))
        return fig
    except:
        return fig

def create_duval_1b_multi_results_graph(samples_df):
    fig = create_duval_1b_colorized()

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
                duval_result = calculate_duval_1b_result(ch4, c2h2, c2h4)
                mark_name = f'{duval_result} {time}'
                fig.add_trace(create_duval_1b_marker(ch4, c2h2, c2h4, mark_name, timestamp=time, result=duval_result, marker_color=rowcolor))
        return fig
    except Exception as e:
        print(e)
        return fig
    
def create_duval_1b_group_graph(ch4_groups, c2h2_groups, c2h4_groups, group_names, colorized=True, **kwargs):
    # https://plotly.com/python/marker-style/
    marker_symbol_list = ['circle', 'diamond', 'square', 'x-thin', 'cross-thin', 
                          'asterisk', 'y-up', 'star-triangle-up', 'star-triangle-down', 
                          'circle-open', 'diamond-open', 'square-open', 'star-triangle-up-open', 
                          'star-triangle-down-open']
    try:
        assert len(ch4_groups) == len(c2h2_groups)
        assert len(c2h2_groups) == len(c2h4_groups)
        assert len(ch4_groups) == len(c2h4_groups)
        assert len(ch4_groups) == len(group_names)
    except Exception as e:
        print(e)

    if colorized is True:
        fig = create_duval_1b_colorized()
    else:
        fig = create_duval_1b_nocolor()

    if 'group_colors' in kwargs:
        color_list = kwargs['group_colors']
    else:
        color_list = pcolors.qualitative.Plotly + pcolors.qualitative.Light24_r
    
    try:
        for i, group_name in enumerate(group_names):
            coord_list = []

            for ch4_value, c2h2_value, c2h4_value in zip(ch4_groups[i], c2h2_groups[i], ch4_groups[i]):
                if (ch4_value == 0) and (c2h2_value == 0) and (c2h4_value == 0):
                    continue
                coord_list.append(calculate_duval_1b_coordinates(ch4_value, c2h2_value, c2h4_value))

            
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
                                            hovertemplate="%{meta[0]}<br>CH4:  %{a:.2f}%<br>C2H2: %{b:.2f}%<br>C2H4: %{c:.2f}%<extra></extra>"))
    except Exception as e:
        print(e)

    return fig

# %%
if __name__ == "__main__":
    '''
    fig = create_duval_1b_nocolor()
    marker_name = calculate_duval_1b_result(10, 26, 64)
    fig.add_trace(create_duval_1b_marker(10, 26, 64, marker_name))
    fig.show()
    '''
    fig2 = create_duval_1b_colorized()
    marker_name2 = calculate_duval_1b_result(10, 26, 64)
    fig2.add_trace(create_duval_1b_marker(10, 26, 64, marker_name2))
    fig2.show()
    
    '''

    #fig3 = create_duval_1b_result_graph(55, 8, 55)
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

    #print(df_sample)

    #fig4 = create_duval_1b_multi_results_graph(df_sample)
    #fig4.show()

    ch4_list= [[200, 50, 100, 200], [0, 20, 41, 60, 66, 80], [15, 60, 160]]
    c2h2_list= [[10, 20, 30, 40], [0, 1, 2, 5, 6, 10], [100, 200, 500]]
    c2h4_list= [[400, 500, 600, 1000], [0, 5, 50, 60, 66, 67], [60, 80, 110]]
    groups_list= ['Group1', 'Group2', 'Group3']

    fig5 = create_duval_1b_group_graph(ch4_list, c2h2_list, c2h4_list, groups_list, colorized=False, group_colors=['rgb(136, 204, 238)', 'rgb(204, 102, 119)', 'rgb(221, 204, 119)', 'rgb(17, 119, 51)'])
    fig5.show()
    '''