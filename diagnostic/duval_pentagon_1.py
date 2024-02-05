# -*- coding: utf-8 -*-
"""duval_pentagon_1.py

This module calculates duval pentagon 1 related diagnostics and generates duval pentagon visualizations using plotly library.

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
from math import cos, pi, sin

import numpy as np
from pandas import isna
import pandas as pd
import plotly.graph_objects as go   # plotly is an interactive plotting library
import plotly.colors as pcolors
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

## Defining Duval pentagon 1 coordinates and areas

# D2 - Discharges of high energy
D2x = [4, 32, 24.3, 0, 0, 4]
D2y = [16, -6.1, -30, -3, 1.5, 16]

D2_poly = [(D2x[i], D2y[i]) for i in range(0, len(D2x)-1)]
D2_polygon = Polygon(D2_poly)

# D1 - Discharges of lowenergy
D1x = [0, 38, 32, 4, 0, 0]
D1y = [40, 12, -6.1, 16, 1.5, 40]

D1_poly = [(D1x[i], D1y[i]) for i in range(0, len(D1x)-1)]
D1_polygon = Polygon(D1_poly)

# T3 - Thermal fault T3 >700C
T3x = [0, 24.3, 23.5, 1, -6, 0]
T3y = [-3, -30, -32.4, -32.4, -4, -3] #-32 as per TB 771 & C57.143-2019 would leave a gap

T3_poly = [(T3x[i], T3y[i]) for i in range(0, len(T3x)-1)]
T3_polygon = Polygon(T3_poly)

# T2 - Thermal fault T2 300C < T < 700C
T2x = [-6, 1, -22.5, -6]
T2y = [-4, -32.4, -32.4, -4]

T2_poly = [(T2x[i], T2y[i]) for i in range(0, len(T2x)-1)]
T2_polygon = Polygon(T2_poly)

# T1 - Thermal fault T1 > 300C
T1x = [-6, -22.5, -23.5, -35, 0, 0, -6] 
T1y = [-4, -32.4, -32.4, 3, 1.5, -3, -4]

T1_poly = [(T1x[i], T1y[i]) for i in range(0, len(T1x)-1)]
T1_polygon = Polygon(T1_poly)

# S - Stray gassing
Sx = [0, -35, -38, 0, 0, -1, -1, 0, 0]
Sy = [1.5, 3.0, 12.4, 40, 33, 33, 24.5, 24.5, 1.5]

S_poly = [(Sx[i], Sy[i]) for i in range(0, len(Sx)-1)]
S_polygon = Polygon(S_poly)
    
# PD - Partial discharges
PDx = [0, -1, -1, 0, 0]
PDy = [33, 33, 24.5, 24.5, 33]

PD_poly = [(PDx[i], PDy[i]) for i in range(0, len(PDx)-1)]
PD_polygon = Polygon(PD_poly)

# point & polygon comparison accuracy
epsilon = 1e-15

def round_half_up(n, decimals=0):
    # rounding values
    multiplier = 10 ** decimals
    return np.floor(n*multiplier + 0.5) / multiplier

def create_duval_p1_colorized():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=Sx, y=Sy, 
                             name='S',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(170,156,192, 0.5)'
                            ))
    fig.add_trace(go.Scatter(x=PDx, y=PDy, 
                             name='PD',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(178,255,228, 0.5)'
                            ))
    fig.add_trace(go.Scatter(x=T1x, y=T1y, 
                             name='T1',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(245, 243, 39, 0.5)'
                            ))
    fig.add_trace(go.Scatter(x=T2x, y=T2y, 
                             name='T2',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(245, 148, 39, 0.5)'
                            ))
    fig.add_trace(go.Scatter(x=T3x, y=T3y,
                             name='T3',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(245, 54, 39, 0.5)'
                            ))
    fig.add_trace(go.Scatter(x=D2x, y=D2y, 
                             name='D2',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(178,205,255, 0.5)'
                            ))
    fig.add_trace(go.Scatter(x=D1x, y=D1y, 
                             name='D1',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(178,244,255, 0.5)'
                            ))
    fig.add_scatter(x=[0, -24.5, -40, 25, 40], y=[41, -34, 12.5, -34, 12.5],
                    mode='text', text=['H2', 'CH4', 'C2H6', 'C2H4', 'C2H2'], 
                    hoverinfo='skip', showlegend=False)
    fig.add_scatter(x=[-16, -0.5, 16, 14, 7, -8, -20], y=[16, 28.75, 16 ,-5, -20, -20, -8],
                    mode='text', text=['S', 'PD', 'D1', 'D2', 'T3', 'T2', 'T1'], 
                    hoverinfo='skip', showlegend=False)
    fig.update_layout(
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        xaxis=dict(visible= False, showticklabels= False),
                        yaxis=dict(visible= False, showticklabels= False),
                        showlegend=True,
  						modebar_add = ['v1hovermode', 'drawline', 'eraseshape'],
                        )
    # fixed aspect ratio prevents distortion of the pentagon
    fig.update_yaxes(
        scaleanchor = "x",
        scaleratio = 1,
    )
    
    return fig

def create_duval_p1_nocolor():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=Sx, y=Sy, 
                             name='S',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5
                            ))
    fig.add_trace(go.Scatter(x=PDx, y=PDy, 
                             name='PD',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5
                            ))
    fig.add_trace(go.Scatter(x=T1x, y=T1y, 
                             name='T1',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5
                            ))
    fig.add_trace(go.Scatter(x=T2x, y=T2y, 
                             name='T2',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5
                            ))
    fig.add_trace(go.Scatter(x=T3x, y=T3y, 
                             name='T3',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5
                            ))
    fig.add_trace(go.Scatter(x=D2x, y=D2y, 
                             name='D2',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5
                            ))
    fig.add_trace(go.Scatter(x=D1x, y=D1y, 
                             name='D1',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5
                            ))
    fig.add_scatter(x=[0, -24.5, -40, 25, 40], y=[41, -34, 12.5, -34, 12.5],
                    mode='text', text=['H2', 'CH4', 'C2H6', 'C2H4', 'C2H2'], 
                    hoverinfo='skip', showlegend=False)
    fig.add_scatter(x=[-16, -0.5, 16, 14, 7, -8, -20], y=[16, 28.75, 16 ,-5, -20, -20, -8],
                    mode='text', text=['S', 'PD', 'D1', 'D2', 'T3', 'T2', 'T1'], 
                    hoverinfo='skip', showlegend=False)
    fig.update_layout(
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        xaxis=dict(visible= False, showticklabels= False),
                        yaxis=dict(visible= False, showticklabels= False),
                        showlegend=True,
  						modebar_add = ['v1hovermode', 'drawline', 'eraseshape'],
                        )
    # fixed aspect ratio prevents distortion of the pentagon
    fig.update_yaxes(
        scaleanchor = "x",
        scaleratio = 1,
    )

    return fig

def calculate_duval_p1_coordinates(h2, c2h6, ch4, c2h4, c2h2):

    gas_sum = h2 + c2h6 + ch4 + c2h4 + c2h2

    h2_perc = (h2 / gas_sum)*100
    c2h6_perc = (c2h6 / gas_sum)*100
    ch4_perc = (ch4 / gas_sum)*100
    c2h4_perc = (c2h4 / gas_sum)*100
    c2h2_perc = (c2h2 / gas_sum)*100

    x0 = 0 # cos(90) = 0
    y0 = h2_perc # sin(90) = 1

    x1 = c2h6_perc * cos( ((180 - 18) / 180 ) * pi)
    y1 = c2h6_perc * sin( ((180 - 18) / 180 ) * pi)

    x2 = ch4_perc * cos( ((180 + 54) / 180 ) * pi)
    y2 = ch4_perc * sin( ((180 + 54) / 180 ) * pi)
    
    x3 = c2h4_perc * cos( ((180 + 54 + 72) / 180 ) * pi)
    y3 = c2h4_perc * sin( ((180 + 54 + 72) / 180 ) * pi)

    x4 = c2h2_perc * cos( ((18) / 180 ) * pi)
    y4 = c2h2_perc * sin( ((18) / 180 ) * pi)

    x_list = [x0, x1, x2, x3, x4]
    y_list = [y0, y1, y2, y3, y4]
    summit_list = [(x_list[i], y_list[i]) for i in range(0, len(x_list))]

    # https://en.wikipedia.org/wiki/Centroid#Of_a_polygon
    # calculate denominator sum
    denominator_xy = 0
    for i in range(0, 5):
        if i == 4:
            denominator_xy += (3*(x_list[i] * y_list[0] - x_list[0] * y_list[i]))
        else:
            denominator_xy += (3*(x_list[i] * y_list[i+1] - x_list[i+1] * y_list[i]))

    # x coordinate numerator sum
    numerator_x = 0
    for i in range(0, 5):
        if i == 4:
            numerator_x += ((x_list[i] + x_list[0]) * (x_list[i] * y_list[0] - x_list[0] * y_list[i]))
        else:
            numerator_x += ((x_list[i] + x_list[i+1]) * (x_list[i] * y_list[i+1] - x_list[i+1] * y_list[i]))

    # y coordinate numerator sum
    numerator_y = 0
    for i in range(0, 5):
        if i == 4:
            numerator_y += ((y_list[i] + y_list[0]) * (x_list[i] * y_list[0] - x_list[0] * y_list[i]))
        else:
            numerator_y += ((y_list[i] + y_list[i+1]) * (x_list[i] * y_list[i+1] - x_list[i+1] * y_list[i]))

    centroid_x = round_half_up((numerator_x / denominator_xy), 2)

    centroid_y = round_half_up((numerator_y / denominator_xy), 2)

    centroid_list = [centroid_x, centroid_y]

    return centroid_list, summit_list

def calculate_duval_p1_result(h2, c2h6, ch4, c2h4, c2h2):

    try:
        if (isna(h2) or isna(c2h6) or isna(ch4) or isna(c2h4) or isna(c2h2)) is True:
            return 'N/A'
        if ((h2 == 0) and (c2h6 == 0) and (ch4 == 0) and (c2h4 == 0) and (c2h2 == 0)) is True:
            return 'N/A'
        else:
            centroid_list, summit_list = calculate_duval_p1_coordinates(h2, ch4, c2h6, c2h4, c2h2)
            point = Point(centroid_list[0], centroid_list[1])
            if (D2_polygon.contains(point) or (point.distance(D2_polygon) < epsilon)) is True:
                return 'D2'
            if (D1_polygon.contains(point) or (point.distance(D1_polygon) < epsilon)) is True:
                return 'D1'
            if (T3_polygon.contains(point) or (point.distance(T3_polygon) < epsilon)) is True:
                return 'T3'
            if (T2_polygon.contains(point) or (point.distance(T2_polygon) < epsilon)) is True:
                return 'T2'
            if (T1_polygon.contains(point) or (point.distance(T1_polygon) < epsilon)) is True:
                return 'T1'
            if (S_polygon.contains(point) or (point.distance(S_polygon) < epsilon)) is True:
                return 'S'
            if (PD_polygon.contains(point) or (point.distance(PD_polygon) < epsilon)) is True:
                return 'PD'
            else:
                return 'ND'

    except TypeError:
        print('Duval result calculation error!')
        print('{h2}, {ch4}, {c2h6}, {c2h4}, {c2h2}')
        return 'N/A'

def create_duval_p1_marker(h2, c2h6, ch4, c2h4, c2h2, marker_name, **kwargs):
    marker_coord, summit_list = calculate_duval_p1_coordinates(h2, c2h6, ch4, c2h4, c2h2)

    if 'timestamp' in kwargs and 'result' in kwargs and 'marker_color' in kwargs:
         try:
            timestamp = kwargs['timestamp']
            result = kwargs['result']
            set_color = kwargs['marker_color']
            return go.Scatter(x=[marker_coord[0]], y=[marker_coord[1]],
                                name= marker_name,
                                mode='markers',
                                marker_color=set_color,
                                marker_size=10,
                                meta= [result, h2, c2h6, ch4, c2h4, c2h2, timestamp],
                                hovertemplate="Diagnosis: %{meta[0]}<br>X: %{x:.2f}<br>Y: %{y:.2f}<br>%{meta[6]}<extra></extra>")
         except Exception as e:
            print(e)
            pass
    elif 'timestamp' not in kwargs and 'result' not in kwargs and 'marker_color' in kwargs:
        try:
            set_color = kwargs['marker_color']
            return go.Scatter(x=[marker_coord[0]], y=[marker_coord[1]],
                                name= marker_name,
                                mode='markers',
                                marker_color=set_color,
                                marker_size=10,
                                meta= [marker_name, h2, c2h6, ch4, c2h4, c2h2],
                                hovertemplate="Diagnosis: %{meta[0]}<br>X: %{x:.2f}<br>Y: %{y:.2f}<extra></extra>")
        except Exception as e:
            print(e)
            pass
    else:
        try:  
            return go.Scatter(x=[marker_coord[0]], y=[marker_coord[1]],
                                    name= marker_name,
                                    marker_color='red',
                                    marker_size=10,
                                    meta= marker_name,
                                    hovertemplate="Diagnosis: %{meta}<br>X: %{x:.2f}<br>Y: %{y:.2f}<extra></extra>")
        except Exception as e:
            print(e)
            pass

def draw_duval_p1_summits(h2, c2h6, ch4, c2h4, c2h2):
    marker_coord, summit_list = calculate_duval_p1_coordinates(h2, c2h6, ch4, c2h4, c2h2)

    summit_x = [summit[0] for summit in summit_list]
    summit_x.append(summit_list[0][0])

    summit_y = [summit[1] for summit in summit_list]
    summit_y.append(summit_list[0][1])

    return go.Scatter(x=summit_x, y=summit_y, 
                             name='summits',
                            showlegend=False,
                            mode='lines',
                            line_color='blue',
                            line_width=0.8
                            )

def create_duval_p1_result_graph(h2, c2h6, ch4, c2h4, c2h2, include_summit=False):
    fig = create_duval_p1_colorized()

    try:
        result_name = calculate_duval_p1_result(h2, c2h6, ch4, c2h4, c2h2)
        fig.add_trace(create_duval_p1_marker(h2, c2h6, ch4, c2h4, c2h2, result_name))
        if include_summit is True:
            fig.add_trace(draw_duval_p1_summits(h2, c2h6, ch4, c2h4, c2h2))
        return fig
    except:
        return fig
    
def create_duval_p1_multi_results_graph(samples_df):
    fig = create_duval_p1_colorized()

    sample_count = len(samples_df)
    colorscale = pcolors.sample_colorscale('Bluered', sample_count, low=0.0, high=1.0, colortype='rgb')

    try:
        sample_num = 0
        for row in samples_df.itertuples(name=None):
            time, h2, ch4, c2h6, c2h4, c2h2, rowcolor = row[1], row[2], row[3], row[4], row[5], row[6], colorscale[sample_num]
            sample_num+=1
            if ((h2 == 0) and (ch4 == 0) and (c2h6 == 0) and (c2h4 == 0) and (c2h2 == 0)) is True:
                continue
            else:
                duval_result = calculate_duval_p1_result(h2, c2h6, ch4, c2h4, c2h2)
                mark_name = f'{duval_result} {time}'
                fig.add_trace(create_duval_p1_marker(h2, c2h6, ch4, c2h4, c2h2, mark_name, timestamp=time, result=duval_result, marker_color=rowcolor))
        return fig
    except Exception as e:
        print(e)
        return fig

# %%
if __name__ == "__main__":
    
    # H2 = 31 ppm, C2H6 = 130 ppm, CH4 = 192 ppm, C2H4 = 31 ppm, and C2H2 = 0 ppm -> (−17.3, −9.1) [T1]
    dp1_coord, dp1_summits = calculate_duval_p1_coordinates(31, 130, 192, 31, 0)
    print(f'centroid_XY:\n{dp1_coord}\nsummit_coordsXY:\n{dp1_summits}')

    poly1 = Polygon(dp1_summits)
    print(f'shapely_XY:\n{list(poly1.centroid.coords)}')

    dp1_result = calculate_duval_p1_result(31, 130, 192, 31, 0)
    print(dp1_result)

    duvp1_fig = create_duval_p1_result_graph(31, 130, 192, 31, 0, include_summit=True)
    duvp1_fig.show()
    
    # H2 = 50 ppm, C2H6 = 80 ppm, CH4 = 120 ppm, C2H4 = 60 ppm and C2H2 = 30 ppm  -> xo = -7.35, and yo = -5.79 (T1)
    # 50, 120, 80, 60, 30
    dp1_coord2, dp1_summits2 = calculate_duval_p1_coordinates(50, 80, 120, 60, 30)
    print(f'centroid_XY:{dp1_coord2}\nsummit_coordsXY:{dp1_summits2}')

    poly2 = Polygon(dp1_summits2)
    print(f'shapely_XY:{list(poly2.centroid.coords)}')

    dp1_result2 = calculate_duval_p1_result(50, 80, 120, 60, 30)
    print(dp1_result2)

    duvp1_2_fig = create_duval_p1_result_graph(50, 80, 120, 60, 30, include_summit=True)
    duvp1_2_fig = create_duval_p1_colorized()
    duvp1_2_fig.add_trace(create_duval_p1_marker(50, 80, 120, 60, 30, dp1_result2, timestamp='2021-05-11', result=dp1_result2, marker_color='blue'))
    duvp1_2_fig.add_trace(draw_duval_p1_summits(50, 80, 120, 60, 30))
    duvp1_2_fig.show()

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

    #duvp1_multi_fig = create_duval_p1_multi_results_graph(df_sample)
    #duvp1_multi_fig.show()
