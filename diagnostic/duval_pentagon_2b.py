# -*- coding: utf-8 -*-
"""duval_pentagon_2b.py

This module calculates duval pentagon 2b (Pentagon 2 draft) related diagnostics and generates duval pentagon visualizations using plotly library.

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

## Defining Duval pentagon 2 coordinates and areas

# D2-H - Discharges of high energy in oil
D2Hx = [0, 0, 24, 32, 11, 10.1, 1, 0]
D2Hy = [1.5, -3, -30, -6, 10.6, 7.2, 5, 1.5]

D2H_poly = [(D2Hx[i], D2Hy[i]) for i in range(0, len(D2Hx)-1)]
D2H_polygon = Polygon(D2H_poly)

# D2-P - Discharges of high energy in paper
D2Px = [1, 4, 11, 10.1, 1]
D2Py = [5, 16, 10.5, 7.2, 5]

D2P_poly = [(D2Px[i], D2Py[i]) for i in range(0, len(D2Px)-1)]
D2P_polygon = Polygon(D2P_poly)

# D1-H - Discharges of low energy in oil
D1Hx = [0, 38, 32, 11, 10.2, 0, 0]
D1Hy = [40, 12.4, -6, 10.5, 17, 20, 40]

D1H_poly = [(D1Hx[i], D1Hy[i]) for i in range(0, len(D1Hx)-1)]
D1H_polygon = Polygon(D1H_poly)

# D1-P (original, draft) - Discharges of low energy in paper
D1P_origx = [0, 0, 19.2, 11, 4, 0] # 19.2 probably should be 10.2
D1P_origy = [1.5, 20, 17, 10.5, 16, 1.5]

D1P_orig_poly = [(D1P_origx[i], D1P_origy[i]) for i in range(0, len(D1P_origx)-1)]
D1P_orig_polygon = Polygon(D1P_orig_poly)

# D1-P - Discharges of low energy in paper
D1Px = [0, 0, 10.2, 11, 4, 0]
D1Py = [1.5, 20, 17, 10.5, 16, 1.5]

D1P_poly = [(D1Px[i], D1Py[i]) for i in range(0, len(D1Px)-1)]
D1P_polygon = Polygon(D1P_poly)

# C (original, draft) - Carbonization of paper
C_origx = [0, -3.5, -11, -21.5, 2.5, 0] #(0, -3) is unnecessary overlap
C_origy = [-3, -3, -8, -32.4, -32.4, -3]

C_orig_poly = [(C_origx[i], C_origy[i]) for i in range(0, len(C_origx)-1)]
C_orig_polygon = Polygon(C_orig_poly)

# C - Carbonization of paper
Cx = [-3.5, 2.5, -21.5, -11, -3.5]
Cy = [-3, -32.4, -32.4, -8, -3]

C_poly = [(Cx[i], Cy[i]) for i in range(0, len(Cx)-1)]
C_polygon = Polygon(C_poly)

# T3-H - Thermal fault T3 in oil only
T3Hx = [0, -3.5, 2.5, 23.5, 24, 0]
T3Hy = [-3, -3, -32.4, -32.4, -30, -3]

T3H_poly = [(T3Hx[i], T3Hy[i]) for i in range(0, len(T3Hx)-1)]
T3H_polygon = Polygon(T3H_poly)

# O - Overheating
Ox = [0, -35, -23.5, -21.5, -11, -3.5, 0, 0] 
Oy = [1.5, 3, -32.4, -32.4, -8, -3, -3, 1.5]

O_poly = [(Ox[i], Oy[i]) for i in range(0, len(Ox)-1)]
O_polygon = Polygon(O_poly)

# S (original, draft) - Stray gassing
S_origx = [0, -38, -35, 0, 0] # does not create a slot for PD, should be similar to P2
S_origy = [40, 12.4, 3, 1.5, 40]

S_orig_poly = [(S_origx[i], S_origy[i]) for i in range(0, len(S_origx)-1)]
S_orig_polygon = Polygon(S_orig_poly)

# S - Stray gassing
Sx = [0, -35, -38, 0, 0, -1, -1, 0, 0]
Sy = [1.5, 3.1, 12.4, 40, 33, 33, 24.5, 24.5, 1.5]

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

def create_duval_p2b_colorized():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=S_origx, y=S_origy, 
                             name='S (original draft)',
                            showlegend=True,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(170,156,192, 0.5)'
                            ))
    fig.add_trace(go.Scatter(x=Sx, y=Sy, 
                             name='S',
                            showlegend=True,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(170,156,192, 0.5)'
                            ))
    fig.add_trace(go.Scatter(x=PDx, y=PDy, 
                             name='PD',
                            showlegend=True,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(178,255,228, 0.5)'
                            ))
    fig.add_trace(go.Scatter(x=Ox, y=Oy, 
                             name='O',
                            showlegend=True,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(255,211,37, 0.5)'
                            ))
    fig.add_trace(go.Scatter(x=C_origx, y=C_origy, 
                             name='C (original draft)',
                            showlegend=True,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(92,81,75, 0.6)'
                            ))
    fig.add_trace(go.Scatter(x=Cx, y=Cy, 
                             name='C',
                            showlegend=True,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(92,81,75, 0.6)'
                            ))
    fig.add_trace(go.Scatter(x=T3Hx, y=T3Hy, 
                             name='T3-H',
                            showlegend=True,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(245, 54, 39, 0.5)'
                            ))
    fig.add_trace(go.Scatter(x=D2Px, y=D2Py, 
                             name='D2-P',
                            showlegend=True,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(0, 89, 255, 0.5)'
                            ))
    fig.add_trace(go.Scatter(x=D2Hx, y=D2Hy, 
                             name='D2-H',
                            showlegend=True,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(178,205,255, 0.5)'
                            ))
    fig.add_trace(go.Scatter(x=D1P_origx, y=D1P_origy, 
                             name='D1-P (original draft)',
                            showlegend=True,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(0, 217, 255, 0.5)'
                            ))
    fig.add_trace(go.Scatter(x=D1Px, y=D1Py, 
                             name='D1-P',
                            showlegend=True,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(0, 217, 255, 0.5)'
                            ))
    fig.add_trace(go.Scatter(x=D1Hx, y=D1Hy, 
                             name='D1-H',
                            showlegend=True,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(178,244,255, 0.5)'
                            ))
    fig.add_scatter(x=[0, -24.5, -40, 25, 40], y=[41, -34, 12.5, -34, 12.5],
                    mode='text', text=['H2', 'CH4', 'C2H6', 'C2H4', 'C2H2'], 
                    hoverinfo='skip', showlegend=True)
    fig.add_scatter(x=[-16, -0.5, 1.8, 16, 6, 14, 7, -8, -20], y=[16, 28.75, 15, 18, 10, -5, -20, -20, -8],
                    mode='text', text=['S', 'PD', 'D1-P', 'D1-H', 'D2-P', 'D2-H', 'T3-H', 'C', 'O'], 
                    hoverinfo='skip', showlegend=True)
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

def create_duval_p2b_nocolor():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=Sx, y=Sy, 
                             name='S',
                            showlegend=True,
                            mode='lines',
                            line_color='black',
                            line_width=0.5
                            ))
    fig.add_trace(go.Scatter(x=PDx, y=PDy, 
                             name='PD',
                            showlegend=True,
                            mode='lines',
                            line_color='black',
                            line_width=0.5
                            ))
    fig.add_trace(go.Scatter(x=Ox, y=Oy, 
                             name='O',
                            showlegend=True,
                            mode='lines',
                            line_color='black',
                            line_width=0.5
                            ))
    fig.add_trace(go.Scatter(x=Cx, y=Cy, 
                             name='C',
                            showlegend=True,
                            mode='lines',
                            line_color='black',
                            line_width=0.5
                            ))
    fig.add_trace(go.Scatter(x=T3Hx, y=T3Hy, 
                             name='T3-H',
                            showlegend=True,
                            mode='lines',
                            line_color='black',
                            line_width=0.5
                            ))
    fig.add_trace(go.Scatter(x=D2Px, y=D2Py, 
                             name='D2-P',
                            showlegend=True,
                            mode='lines',
                            line_color='black',
                            line_width=0.5
                            ))
    fig.add_trace(go.Scatter(x=D2Hx, y=D2Hy, 
                             name='D2-H',
                            showlegend=True,
                            mode='lines',
                            line_color='black',
                            line_width=0.5
                            ))
    fig.add_trace(go.Scatter(x=D1Px, y=D1Py, 
                             name='D1-P',
                            showlegend=True,
                            mode='lines',
                            line_color='black',
                            line_width=0.5
                            ))
    fig.add_trace(go.Scatter(x=D1Hx, y=D1Hy, 
                             name='D1-H',
                            showlegend=True,
                            mode='lines',
                            line_color='black',
                            line_width=0.5
                            ))
    fig.add_scatter(x=[0, -24.5, -40, 25, 40], y=[41, -34, 12.5, -34, 12.5],
                    mode='text', text=['H2', 'CH4', 'C2H6', 'C2H4', 'C2H2'], 
                    hoverinfo='skip', showlegend=True)
    fig.add_scatter(x=[-16, -0.5, 16, 14, 7, -8, -20], y=[16, 28.75, 16 ,-5, -20, -20, -8],
                    mode='text', text=['S', 'PD', 'D1', 'D2', 'T3-H', 'C', 'O'], 
                    hoverinfo='skip', showlegend=True)
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

def calculate_duval_p2b_coordinates(h2, c2h6, ch4, c2h4, c2h2):

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


def calculate_duval_p2b_result(h2, c2h6, ch4, c2h4, c2h2):

    try:
        if (isna(h2) or isna(ch4) or isna(c2h6) or isna(c2h4) or isna(c2h2)) is True:
            return 'N/A'
        if ((h2 == 0) and (ch4 == 0) and (c2h6 == 0) and (c2h4 == 0) and (c2h2 == 0)) is True:
            return 'N/A'
        else:
            centroid_list, summit_list = calculate_duval_p2b_coordinates(h2, c2h6, ch4, c2h4, c2h2)
            point = Point(centroid_list[0], centroid_list[1])
            if (D2P_polygon.contains(point) or (point.distance(D2P_polygon) < epsilon)) is True:
                return 'D2-P'
            if (D2H_polygon.contains(point) or (point.distance(D2H_polygon) < epsilon)) is True:
                return 'D2-H'
            if (D1P_polygon.contains(point) or (point.distance(D1P_polygon) < epsilon)) is True:
                return 'D1-P'
            if (D1H_polygon.contains(point) or (point.distance(D1H_polygon) < epsilon)) is True:
                return 'D1-H'
            if (C_polygon.contains(point) or (point.distance(C_polygon) < epsilon)) is True:
                return 'C'
            if (T3H_polygon.contains(point) or (point.distance(T3H_polygon) < epsilon)) is True:
                return 'T3H'
            if (O_polygon.contains(point) or (point.distance(O_polygon) < epsilon)) is True:
                return 'O'
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

def create_duval_p2b_marker(h2, c2h6, ch4, c2h4, c2h2, marker_name, **kwargs):
    marker_coord, summit_list = calculate_duval_p2b_coordinates(h2, c2h6, ch4, c2h4, c2h2)

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
                                hovertemplate="Diagnosis: %{meta[0]}<br>X: %{x:.2f}<br>Y: %{y:.2f}<br><extra></extra>")
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
                                    hovertemplate="Diagnosis: %{meta}<br>X: %{x:.2f}<br>Y: %{y:.2f}<br><extra></extra>")
        except Exception as e:
            print(e)
            pass

def draw_duval_p2b_summits(h2, c2h6, ch4, c2h4, c2h2):
    marker_coord, summit_list = calculate_duval_p2b_coordinates(h2, c2h6, ch4, c2h4, c2h2)

    summit_x = [summit[0] for summit in summit_list]
    summit_x.append(summit_list[0][0])

    summit_y = [summit[1] for summit in summit_list]
    summit_y.append(summit_list[0][1])

    return go.Scatter(x=summit_x, y=summit_y, 
                             name='summits',
                            showlegend=True,
                            mode='lines',
                            line_color='blue',
                            line_width=0.8
                            )

def create_duval_p2b_result_graph(h2, c2h6, ch4, c2h4, c2h2, include_summit=False):
    fig = create_duval_p2b_colorized()

    try:
        result_name = calculate_duval_p2b_result(h2, c2h6, ch4, c2h4, c2h2)
        fig.add_trace(create_duval_p2b_marker(h2, c2h6, ch4, c2h4, c2h2, result_name))
        if include_summit is True:
            fig.add_trace(draw_duval_p2b_summits(h2, c2h6, ch4, c2h4, c2h2))
        return fig
    except:
        return fig

def create_duval_p2_multi_results_graph(samples_df):
    fig = create_duval_p2b_colorized()

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
                duval_result = calculate_duval_p2b_result(h2, c2h6, ch4, c2h4, c2h2)
                mark_name = f'{duval_result} {time}'
                fig.add_trace(create_duval_p2b_marker(h2, c2h6, ch4, c2h4, c2h2, mark_name, timestamp=time, result=duval_result, marker_color=rowcolor))
        return fig
    except Exception as e:
        print(e)
        return fig
        

# %%
if __name__ == "__main__":
    
    # H2 = 31 ppm, C2H6 = 130 ppm, CH4 = 192 ppm, C2H4 = 31 ppm, and C2H2 = 0 ppm -> (−17.3, −9.1) [O]
    dp2_coord, dp2_summits = calculate_duval_p2b_coordinates(31, 130, 192, 31, 0)
    print(f'centroid_XY:\n{dp2_coord}\nsummit_coordsXY:\n{dp2_summits}')
    print(dp2_coord, dp2_summits)
    
    poly1 = Polygon(dp2_summits)
    print(f'shapely_XY:\n{list(poly1.centroid.coords)}')

    dp2_result = calculate_duval_p2b_result(31, 130, 192, 31, 0)
    print(dp2_result)

    duvp2_fig = create_duval_p2b_result_graph(31, 130, 192, 31, 0)
    duvp2_fig.show()

    '''
    # H2 = 50 ppm, C2H6 = 80 ppm, CH4 = 120 ppm, C2H4 = 60 ppm and C2H2 = 30 ppm  -> xo = -7.35, and yo = -5.79 (C)
    # 50, 120, 80, 60, 30
    dp2_coord2, dp2_summits2 = calculate_duval_p2_coordinates(50, 80, 120, 60, 30)
    print(f'centroid_XY:{dp2_coord2}\nsummit_coordsXY:{dp2_summits2}')

    poly2 = Polygon(dp2_summits2)
    print(f'shapely_XY:{list(poly2.centroid.coords)}')

    dp2_result2 = calculate_duval_p2_result(50, 80, 120, 60, 30)
    print(dp2_result2)

    duvp2_2_fig = create_duval_p2_result_graph(50, 80, 120, 60, 30, include_summit=True)
    duvp2_2_fig = create_duval_p2_colorized()
    duvp2_2_fig.add_trace(create_duval_p2_marker(50, 80, 120, 60, 30, dp2_result2, timestamp='2021-05-11', result=dp2_result2, marker_color='blue'))
    duvp2_2_fig.add_trace(draw_duval_p2_summits(50, 80, 120, 60, 30))
    duvp2_2_fig.show()

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

    #duvp2_multi_fig = create_duval_p2_multi_results_graph(df_sample)
    #duvp2_multi_fig.show()
    '''
