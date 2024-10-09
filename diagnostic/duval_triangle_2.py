# -*- coding: utf-8 -*-
"""duval_triangle_2.py

This module calculates duval triangle 2 (LTC) related diagnostics and generates duval triangle visualizations using plotly library.

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

from graphical_distributions import create_ternary_group_distribution_data as ternary_distribution_data

# * Triangle 2 fault area ternary coordinate constants (plotly: a, b, c) *
TRIANGLE2_N_A = [19, 19, 2, 2, 19]
TRIANGLE2_N_B = [58, 75, 92, 75, 58]
TRIANGLE2_N_C = [23, 6, 6, 23, 23]

TRIANGLE2_T2_A = [77, 62, 35, 50, 77]
TRIANGLE2_T2_B = [0, 15, 15, 0, 0]
TRIANGLE2_T2_C = [23, 23, 50, 50, 23]

TRIANGLE2_T3_A = [50, 35, 0, 0, 50]
TRIANGLE2_T3_B = [0, 15, 15, 0, 0]
TRIANGLE2_T3_C = [50, 50, 85, 100, 50]

TRIANGLE2_X1_A = [77, 19, 19, 100, 77]
TRIANGLE2_X1_B = [0, 58, 81, 0, 0]
TRIANGLE2_X1_C = [23, 23, 0, 0, 23]

TRIANGLE2_D1_A = [0, 19, 19, 2, 2, 0, 0]
TRIANGLE2_D1_B = [100, 81, 75, 92, 75, 77, 100]
TRIANGLE2_D1_C = [0, 0, 6, 6, 23, 23, 0]

TRIANGLE2_X3_A = [0, 0, 62, 0]
TRIANGLE2_X3_B = [15, 77, 15, 15]
TRIANGLE2_X3_C = [85, 23, 23, 85]

def create_duval_2_colorized(legend_show=False):
    # https://community.plotly.com/t/shapes-in-ternary-plot/38566/10
    # https://plotly.com/python/reference/layout/ternary/
    fig = go.Figure(layout=dict(ternary_sum=100))

    #N
    fig.add_trace(go.Scatterternary(a= TRIANGLE2_N_A,
                                    b= TRIANGLE2_N_B,
                                    c= TRIANGLE2_N_C,
                                    name='N',
                                    showlegend=legend_show,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(178,255,228, 0.5)'
                                    ))
    #T2
    fig.add_trace(go.Scatterternary(a= TRIANGLE2_T2_A,
                                    b= TRIANGLE2_T2_B,
                                    c= TRIANGLE2_T2_C,
                                    name='T2',
                                    showlegend=legend_show,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(245, 148, 39, 0.5)'
                                    ))
    #T3
    fig.add_trace(go.Scatterternary(a= TRIANGLE2_T3_A,
                                    b= TRIANGLE2_T3_B,
                                    c= TRIANGLE2_T3_C,
                                    name='T3',
                                    showlegend=legend_show,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(245, 54, 39, 0.5)'
                                    ))
    #X1
    fig.add_trace(go.Scatterternary(a= TRIANGLE2_X1_A,
                                    b= TRIANGLE2_X1_B,
                                    c= TRIANGLE2_X1_C,
                                    name='X1',
                                    showlegend=legend_show,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(178,205,255, 0.5)'
                                    ))
    #D1
    fig.add_trace(go.Scatterternary(a= TRIANGLE2_D1_A,
                                    b= TRIANGLE2_D1_B,
                                    c= TRIANGLE2_D1_C,
                                    name='D1',
                                    showlegend=legend_show,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(228,178,255, 0.5)'
                                    ))    
    #X3
    fig.add_trace(go.Scatterternary(a= TRIANGLE2_X3_A,
                                    b= TRIANGLE2_X3_B,
                                    c= TRIANGLE2_X3_C,
                                    name='X3',
                                    showlegend=legend_show,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5,
                                    fill='toself',
                                    fillcolor='rgba(178,244,255, 0.5)'
                                    ))
    
    # Annotations
    fig.add_scatterternary(a=[10, 11], b=[87, 73], c=[3, 14],
                            mode='text', text=['D1', 'N'], hoverinfo='none', showlegend=legend_show)
    fig.add_scatterternary(a=[50, 30, 55, 20], b=[38, 30, 8, 7.5], c=[12, 40, 37, 72.5],
                            mode='text', text=['X1', 'X3', 'T2', 'T3'], hoverinfo='none',
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
                        aaxis=dict(linecolor='#000000', hoverformat='CH4=%%{a}<br>C2H2=%%{b}<br>C2H4=%%{b}<extra></extra>'), 
                        baxis=dict(linecolor='#000000', hoverformat='CH4=%%{a}<br>C2H2=%%{b}<br>C2H4=%%{b}<extra></extra>'), 
                        caxis=dict(linecolor='#000000', hoverformat='CH4=%%{a}<br>C2H2=%%{b}<br>C2H4=%%{b}<extra></extra>'),
                        aaxis_title_text='CH4',
                        baxis_title_text='C2H2',
                        caxis_title_text='C2H4')
    #fig.update_traces(hovertemplate='CH4: %{a}<br>C2H2: %{b}<br>C2H4: %{c}<extra></extra>')
    
    return fig

def create_duval_2_nocolor(legend_show=False):
    # https://community.plotly.com/t/shapes-in-ternary-plot/38566/10
    # https://plotly.com/python/reference/layout/ternary/
    # a = CH4%, b = C2H2%, c = C2H4%
    fig = go.Figure(layout=dict(ternary_sum=100))

    #N
    fig.add_trace(go.Scatterternary(a= TRIANGLE2_N_A,
                                    b= TRIANGLE2_N_B,
                                    c= TRIANGLE2_N_C,
                                    name='N',
                                    showlegend=legend_show,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #T2
    fig.add_trace(go.Scatterternary(a= TRIANGLE2_T2_A,
                                    b= TRIANGLE2_T2_B,
                                    c= TRIANGLE2_T2_C,
                                    name='T2',
                                    showlegend=legend_show,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #T3
    fig.add_trace(go.Scatterternary(a= TRIANGLE2_T3_A,
                                    b= TRIANGLE2_T3_B,
                                    c= TRIANGLE2_T3_C,
                                    name='T3',
                                    showlegend=legend_show,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))

    #X1
    fig.add_trace(go.Scatterternary(a= TRIANGLE2_X1_A,
                                    b= TRIANGLE2_X1_B,
                                    c= TRIANGLE2_X1_C,
                                    name='X1',
                                    showlegend=legend_show,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #D1
    fig.add_trace(go.Scatterternary(a= TRIANGLE2_D1_A,
                                    b= TRIANGLE2_D1_B,
                                    c= TRIANGLE2_D1_C,
                                    name='D1',
                                    showlegend=legend_show,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    #X3
    fig.add_trace(go.Scatterternary(a= TRIANGLE2_X3_A,
                                    b= TRIANGLE2_X3_B,
                                    c= TRIANGLE2_X3_C,
                                    name='X3',
                                    showlegend=legend_show,
                                    mode='lines',
                                    line_color='black',
                                    line_width=0.5
                                    ))
    
    # Annotations
    fig.add_scatterternary(a=[10, 11], b=[87, 73], c=[3, 14],
                            mode='text', text=['D1', 'N'], hoverinfo='skip',
                            showlegend=legend_show)
    fig.add_scatterternary(a=[50, 30, 55, 20], b=[38, 30, 8, 7.5], c=[12, 40, 37, 72.5],
                            mode='text', text=['X1', 'X3', 'T2', 'T3'], hoverinfo='skip',
                            showlegend=legend_show)
    
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

def calculate_duval_2_coordinates(ch4, c2h2, c2h4, rounding=False):

    i = ch4
    j = c2h2
    k = c2h4

    if (i == 0) and (j == 0) and (k == 0):
        x = 100/3
        y = 100/3
        z = 100/3
    else:
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
    

def calculate_duval_2_result(ch4, c2h2, c2h4, cutoff=False):
    try:
        if (isna(ch4) is True) or (isna(c2h2) is True) or (isna(c2h4) is True):
            return 'N/A'
        if (cutoff != False) and (ch4 < cutoff[0]) and (c2h2 < cutoff[1]) and (c2h4 < cutoff[2]):
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
        print(f'{ch4}, {c2h2}, {c2h4}')
        return 'N/A'
 
def create_duval_2_marker(ch4, c2h2, c2h4, **kwargs):
    marker_coordinates = calculate_duval_2_coordinates(ch4, c2h2, c2h4)
    result = calculate_duval_2_result(ch4, c2h2, c2h4)

    # check for timestamp
    if  'timestamp' in kwargs:
        timestamp = kwargs['timestamp']
        metalist = [result, ch4, c2h2, c2h4, timestamp]
    else:
        timestamp = None
        metalist = [result, ch4, c2h2, c2h4]

    # formulate a name for the marker if not given
    if 'marker_name' in kwargs:
        marker_name = kwargs['marker_name']
    elif (timestamp is not None) and ('marker_name' not in kwargs):
        marker_name = f'{result} {timestamp}'
    else:
        marker_name = result

    if (timestamp is not None) and 'marker_color' in kwargs:
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
                                            hovertemplate="Diagnosis: %{meta[0]}<br>CH4:  %{meta[1]} ppm (%{a:.2f}%)<br>C2H2: %{meta[2]} ppm (%{b:.2f}%)<br>C2H4: %{meta[3]} ppm (%{c:.2f}%)<br>%{meta[4]}<extra></extra>"
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
                                            hovertemplate="Diagnosis: %{meta[0]}<br>CH4:  %{meta[1]} ppm (%{a:.2f}%)<br>C2H2: %{meta[2]} ppm (%{b:.2f}%)<br>C2H4: %{meta[3]} ppm (%{c:.2f}%)<extra></extra>"
                                            )
        except Exception as e:
            print(e)
            pass
    elif (timestamp is not None) and 'marker_color' not in kwargs:
        try:
            return go.Scatterternary(       a= [marker_coordinates[0]],
                                            b= [marker_coordinates[1]],
                                            c= [marker_coordinates[2]],
                                            name= marker_name,
                                            mode='markers',
                                            marker_size=10,
                                            meta= metalist,
                                            hovertemplate="Diagnosis: %{meta[0]}<br>CH4:  %{meta[1]} ppm (%{a:.2f}%)<br>C2H2: %{meta[2]} ppm (%{b:.2f}%)<br>C2H4: %{meta[3]} ppm (%{c:.2f}%)<br>%{meta[4]}<extra></extra>"
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
                                        meta= [result, ch4, c2h2, c2h4],
                                        hovertemplate="Diagnosis: %{meta[0]}<br>CH4:  %{meta[1]} ppm (%{a:.2f}%)<br>C2H2: %{meta[2]} ppm (%{b:.2f}%)<br>C2H4: %{meta[3]} ppm (%{c:.2f}%)<extra></extra>"
                                        )

def create_duval_2_result_graph(ch4, c2h2, c2h4, colorized=True):
    if colorized is True:
        fig = create_duval_2_colorized()
    else:
        fig = create_duval_2_nocolor()

    try:
        result_name = calculate_duval_2_result(ch4, c2h2, c2h4)
        fig.add_trace(create_duval_2_marker(ch4, c2h2, c2h4, result_name))
        return fig
    except:
        return fig

def create_duval_2_multi_results_graph(samples_df, colorized=True):
    if colorized is True:
        fig = create_duval_2_colorized()
    else:
        fig = create_duval_2_nocolor()

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
                fig.add_trace(create_duval_2_marker(ch4, c2h2, c2h4, marker_name=mark_name, timestamp=time, marker_color=rowcolor))
        return fig
    except Exception as e:
        print(e)
        return fig
    
def create_duval_2_group_graph(ch4_groups, c2h2_groups, c2h4_groups, group_names, colorized=False, **kwargs):
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

    # TODO handle usage of lists not list of groups

    if colorized is True:
        fig = create_duval_2_colorized()
    else:
        fig = create_duval_2_nocolor()

    if 'group_colors' in kwargs:
        color_list = kwargs['group_colors']
    else:
        color_list = pcolors.qualitative.Plotly + pcolors.qualitative.Light24_r

    if 'cutoff' in kwargs:
        cutoff = kwargs['cutoff']
    else:
        cutoff = False
    
    try:
        for i, group_name in enumerate(group_names):
            coord_list = []

            for ch4_value, c2h2_value, c2h4_value in zip(ch4_groups[i], c2h2_groups[i], c2h4_groups[i]):
                if ('discard_zeros' in kwargs) and (ch4_value == 0) and (c2h2_value == 0) and (c2h4_value == 0):
                    continue
                elif (cutoff != False) and (ch4_value < cutoff[0]) and (c2h2_value < cutoff[1]) and (c2h4_value < cutoff[2]):
                    continue
                coord_list.append(calculate_duval_2_coordinates(ch4_value, c2h2_value, c2h4_value))

            
            coord_list_t = np.transpose(coord_list)
            print(f'\nDuval triangle {group_name} graph coordinates')
            print(coord_list)
            print(coord_list_t)
            fig.add_trace(go.Scatterternary(a= coord_list_t[0],
                                            b= coord_list_t[1],
                                            c= coord_list_t[2],
                                            name= group_name,
                                            mode='markers',
                                            marker_symbol=marker_symbol_list[i%13],
                                            marker_color=color_list[i],
                                            marker_size=10,
                                            meta= [group_name],
                                            hovertemplate="%{meta[0]}<br>CH4:  %{a:.2f}%<br>C2H2: %{b:.2f}%<br>C2H4: %{c:.2f}%<extra></extra>"))
    except Exception as e:
        print(e)

    return fig

def create_duval_2_group_distribution_graph(ch4_groups, c2h2_groups, c2h4_groups, group_names, colorized=False, **kwargs):

    center_marker_symbol_list = ['diamond', 'square', 'x-thin', 'cross-thin', 
                          'asterisk', 'y-up', 'star-triangle-up', 'star-triangle-down', 
                          'circle-open', 'diamond-open', 'square-open', 'star-triangle-up-open', 
                          'star-triangle-down-open']
    
    dash_type = ["solid", "longdash", "longdashdot", "dash", "dashdot", "dot"]
    
    colorscale_list = ['Teal', 'Peach', 'algae', 'turbid', 'Mint', 'Magenta']
    cscale_len = len(colorscale_list)
 
    if 'dash_mode' in kwargs:
        dash_mode = kwargs['dash_mode']
    else:
        dash_mode = False

    if colorized is True:
        fig = create_duval_2_colorized()
    else:
        fig = create_duval_2_nocolor()

    if 'invertered_percentiles' in kwargs:
        dist_perc = kwargs['invertered_percentiles']
    else:
        dist_perc = [100, 75, 50, 25, 0]

    sample_count=len(dist_perc)
    
    if 'ternary_rounding' in kwargs:
        ter_rnd = kwargs['ternary_rounding']
    else:
        ter_rnd = 2

    if 'discard_zeros' in kwargs:
        discard_zeros = kwargs['discard_zeros']
    else:
        discard_zeros = False

    if 'cutoff' in kwargs:
        cutoff = kwargs['cutoff']
    else:
        cutoff = False

    if 'cutoff_direction' in kwargs:
        cutoff_direction = kwargs['cutoff_direction']
    else:
        cutoff_direction = '>'

    # TODO implement plotting of points as per percentile grouping
    # TODO fix ternary rounding
    try:
        if cutoff != False:
            center, ternary_edge, cartesian_edge = ternary_distribution_data(ch4_groups, c2h2_groups, c2h4_groups, dist_perc, ter_rnd, cutoff=cutoff, cutoff_direction=cutoff_direction)
        elif discard_zeros != False:
            center, ternary_edge, cartesian_edge = ternary_distribution_data(ch4_groups, c2h2_groups, c2h4_groups, dist_perc, ter_rnd, discard_zeros=discard_zeros)
        else:
            center, ternary_edge, cartesian_edge = ternary_distribution_data(ch4_groups, c2h2_groups, c2h4_groups, dist_perc, ter_rnd)

        g = 0
        for cent, ter_edge, grp_name in zip(center, ternary_edge, group_names):

            colorscale = pcolors.sample_colorscale(colorscale_list[g%cscale_len], sample_count, low=1.0, high=0.0, colortype='rgb')
        
            # centerpoint
            fig.add_trace(go.Scatterternary(a= [cent[0]],
                                            b= [cent[1]],
                                            c= [cent[2]],
                                            name= f'{grp_name} - center',
                                            mode='markers',
                                            marker_symbol=center_marker_symbol_list[g%13],
                                            marker_color=colorscale[0],
                                            marker_size=10,
                                            meta= [f'{grp_name} - center'],
                                            hovertemplate="%{meta[0]}<br>CH4:  %{a:.2f}%<br>C2H2: %{b:.2f}%<br>C2H4: %{c:.2f}%<extra></extra>"))

            c = sample_count - 1
            for arr_edge, perc in zip(ter_edge, dist_perc):

                if dash_mode is True:

                    # contour/distribution lines
                    fig.add_trace(go.Scatterternary(a= arr_edge[:, 0],
                                                    b= arr_edge[:, 1],
                                                    c= arr_edge[:, 2],
                                                    name= f'{grp_name} - {perc}%',
                                                    mode='lines',
                                                    marker_color=colorscale[c],
                                                    marker_size=10,
                                                    line=dict(dash=dash_type[(c+1)%6]), # %6 for the 6 different dash types
                                                    meta= [f'{grp_name} - {perc}%'],
                                                    hovertemplate="%{meta[0]}<br>CH4:  %{a:.2f}%<br>C2H2: %{b:.2f}%<br>C2H4: %{c:.2f}%<extra></extra>"))
                    
                else:
                                    # contour/distribution lines
                    fig.add_trace(go.Scatterternary(a= arr_edge[:, 0],
                                                    b= arr_edge[:, 1],
                                                    c= arr_edge[:, 2],
                                                    name= f'{grp_name} - {perc}%',
                                                    mode='lines',
                                                    marker_color=colorscale[c],
                                                    marker_size=10,
                                                    meta= [f'{grp_name} - {perc}%'],
                                                    hovertemplate="%{meta[0]}<br>CH4:  %{a:.2f}%<br>C2H2: %{b:.2f}%<br>C2H4: %{c:.2f}%<extra></extra>"))
                

                c-=1

            g+=1
    except Exception as e:
        print(e)

    return fig

# %%
if __name__ == "__main__":
    '''
    fig = create_duval_2_nocolor()
    fig.add_trace(create_duval_2_marker(10, 26, 64))
    fig.show()

    fig2 = create_duval_2_colorized()
    fig2.add_trace(create_duval_2_marker(10, 26, 64))
    fig2.show()

    '''

    fig2 = create_duval_2_colorized()
    fig2.add_trace(create_duval_2_marker(10, 85, 5))
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

    fig4 = create_duval_2_multi_results_graph(df_sample)
    fig4.show()

    ch4_list= [[200, 50, 100, 200], [0, 20, 41, 60, 66, 80], [15, 60, 160]]
    c2h2_list= [[10, 20, 30, 40], [0, 1, 2, 5, 6, 10], [100, 200, 500]]
    c2h4_list= [[400, 500, 600, 1000], [0, 5, 50, 60, 66, 67], [60, 80, 110]]
    groups_list= ['Group1', 'Group2', 'Group3']

    fig5 = create_duval_2_group_graph(ch4_list, c2h2_list, c2h4_list, groups_list, colorized=False, group_colors=['rgb(136, 204, 238)', 'rgb(204, 102, 119)', 'rgb(221, 204, 119)', 'rgb(17, 119, 51)'])
    fig5.show()


    ch4_long = [11.55, 46.19, 57.74, 69.28, 11.55, 23.09, 17.32, 11.55, 23.09, 23.09, 17.32, 
                23.09, 34.64, 30.02, 34.64, 46.19, 57.74, 58.89, 48.5, 46.19, 43.88, 42.72, 
                40.41, 43.88, 31.18, 17.32, 13.86, 28.87, 23.09, 13.86]
    
    c2h2_long = [84.22, 16.9, 31.13, 15.36, 44.22, 48.46, 56.34, 64.22, 63.46, 68.46, 71.34, 
                 58.46, 52.68, 37.99, 52.68, 36.9, 26.13, 23.55, 20.75, 20.9, 35.06, 28.64, 
                 34.8, 43.06, 44.41, 45.34, 68.07, 35.56, 55.46, 78.07]
    
    c2h4_long = [4.23, 36.91, 11.13, 15.36, 44.23, 28.45, 26.34, 24.23, 13.45, 8.45, 11.34, 
                 18.45, 12.68, 31.99, 12.68, 16.91, 16.13, 17.56, 30.75, 32.91, 21.06, 28.64, 
                 24.79, 13.06, 24.41, 37.34, 18.07, 35.57, 21.45, 8.07]
    
    ch4_long2 = (np.random.random_sample(size = 100)*100).tolist()

    c2h2_long2 = (np.random.random_sample(size = 100)*100).tolist()

    c2h4_long2 = (np.random.random_sample(size = 100)*100).tolist()
    
    figD = create_duval_2_group_distribution_graph([ch4_long, ch4_long2], [c2h2_long, c2h2_long2], [c2h4_long, c2h4_long2], ['grp1', 'grp2'])
    figD.show()

    figD = create_duval_2_group_distribution_graph([ch4_long, ch4_long2], [c2h2_long, c2h2_long2], [c2h4_long, c2h4_long2], ['grp1', 'grp2'], dash_mode = True)
    figD.show()

# %%
