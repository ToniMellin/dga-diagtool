# -*- coding: utf-8 -*-
"""duval_pentagon_2.py

This module calculates duval pentagon 2 related diagnostics and generates duval pentagon visualizations using plotly library.

@Author: https://github.com/ToniMellin
"""

# %%
from math import cos, pi

import numpy as np
from pandas import isna
import pandas as pd
import plotly.graph_objects as go   # plotly is an interactive plotting library
import plotly.colors as pcolors
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

## Defining Duval pentagon 2 coordinates and areas

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

# O - Overheating
Ox = [-3.5, -11, -21.5, -23.5, -35, 0, 0, -3.5] 
Oy = [-3, -8, -32.4, -32.4, 3.1, 1.5, -3, -3]

O_poly = [(Ox[i], Oy[i]) for i in range(0, len(Ox)-1)]
O_polygon = Polygon(O_poly)

# C - Carbonization of paper
Cx = [-3.5, 2.5, -21.5, -11, -3.5]
Cy = [-3, -32.4, -32.4, -8, -3]

C_poly = [(Cx[i], Cy[i]) for i in range(0, len(Cx)-1)]
C_polygon = Polygon(C_poly)

# T3-H - Thermal fault T3 in oil only
T3Hx = [0, 24.3, 23.5, 2.5, -3.5, 0]
T3Hy = [-3, -30, -32.4, -32.4, -3, -3]

T3H_poly = [(T3Hx[i], T3Hy[i]) for i in range(0, len(T3Hx)-1)]
T3H_polygon = Polygon(T3H_poly)

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

# point & polygon comparison accuracy
epsilon = 1e-15


def round_half_up(n, decimals=0):
    # rounding values
    multiplier = 10 ** decimals
    return np.floor(n*multiplier + 0.5) / multiplier

def create_duval_p2_colorized():
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
    fig.add_trace(go.Scatter(x=Ox, y=Oy, 
                             name='O',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(255,211,37, 0.5)'
                            ))
    fig.add_trace(go.Scatter(x=Cx, y=Cy, 
                             name='C',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(92,81,75, 0.6)'
                            ))
    fig.add_trace(go.Scatter(x=T3Hx, y=T3Hy, 
                             name='T3-H',
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
    #TODO add labes inside zones
    fig.update_layout(
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        xaxis=dict(visible= False, showticklabels= False),
                        yaxis=dict(visible= False, showticklabels= False),
                        showlegend=True,
  						modebar_add = ["v1hovermode", 'toggleSpikelines',],
                        )
    return fig

def create_duval_p2_nocolor():
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
    fig.add_trace(go.Scatter(x=Ox, y=Oy, 
                             name='O',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5
                            ))
    fig.add_trace(go.Scatter(x=Cx, y=Cy, 
                             name='C',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5
                            ))
    fig.add_trace(go.Scatter(x=T3Hx, y=T3Hy, 
                             name='T3-H',
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
    #TODO add labes inside zones
    fig.update_layout(
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)',
                        xaxis=dict(visible= False, showticklabels= False),
                        yaxis=dict(visible= False, showticklabels= False),
                        showlegend=True,
  						modebar_add = ["v1hovermode", 'toggleSpikelines',],
                        )
    
    return fig

def calculate_duval_p2_coordinates(h2, ch4, c2h6, c2h4, c2h2):

    gas_sum = h2 + ch4 + c2h6 + c2h4 + c2h2

    h2_perc = (h2 / gas_sum)*100
    ch4_perc = (ch4 / gas_sum)*100
    c2h6_perc = (c2h6 / gas_sum)*100
    c2h4_perc = (c2h4 / gas_sum)*100
    c2h2_perc = (c2h2 / gas_sum)*100

    x1 = 0
    y1 = h2_perc

    x2 = ch4_perc * cos( ((180 - 54) / 180 ) * pi)
    y2 = ch4_perc * cos( ((90 + 54) / 180 ) * pi)

    x3 = c2h6_perc * cos( ((180 + 18) / 180 ) * pi)
    y3 = c2h6_perc * cos( ((90 - 18) / 180 ) * pi)

    x4 = c2h4_perc * cos( ((180 - 54) / 180 ) * pi)
    y4 = c2h4_perc * cos( ((90 + 54) / 180 ) * pi)

    x5 = c2h2_perc * cos( ((180 + 18) / 180 ) * pi)
    y5 = c2h2_perc * cos( ((90 - 18) / 180 ) * pi)

    x_list = [x1, x2, x3, x4, x5]
    y_list = [y1, y2, y3, y4, y5]

    # calculate denominator sum
    denominator_xy = 0
    for i in range(0, 4):
        denominator_xy += (3*(x_list[i] * y_list[i+1] - x_list[i+1] * y_list[i]))

    # x coordinate numerator sum
    numerator_x = 0
    for i in range(0, 4):
        numerator_x += ((x_list[i] + x_list[i+1]) * (x_list[i] * y_list[i+1] - x_list[i+1] * y_list[i]))

    # y coordinate numerator sum
    numerator_y = 0
    for i in range(0, 4):
        numerator_y += ((y_list[i] + y_list[i+1]) * (x_list[i] * y_list[i+1] - x_list[i+1] * y_list[i]))

    centroid_x = round_half_up((numerator_x / denominator_xy), 2)

    centroid_y = round_half_up((numerator_y / denominator_xy), 2)

    return centroid_x, centroid_y


def calculate_duval_p2_result(h2, ch4, c2h6, c2h4, c2h2):

    try:
        if (isna(h2) or isna(ch4) or isna(c2h6) or isna(c2h4) or isna(c2h2)) is True:
            return 'N/A'
        if ((h2 == 0) and (ch4 == 0) and (c2h6 == 0) and (c2h4 == 0) and (c2h2 == 0)) is True:
            return 'N/A'
        else:
            centroid_x, centroid_y = calculate_duval_p2_coordinates(h2, ch4, c2h6, c2h4, c2h2)
            point = Point(centroid_x, centroid_y)
            if (S_polygon.contains(point) or (point.distance(S_polygon) < epsilon)) is True:
                return 'S'
            if (PD_polygon.contains(point) or (point.distance(PD_polygon) < epsilon)) is True:
                return 'PD'
            if (O_polygon.contains(point) or (point.distance(O_polygon) < epsilon)) is True:
                return 'O'
            if (C_polygon.contains(point) or (point.distance(C_polygon) < epsilon)) is True:
                return 'C'
            if (T3H_polygon.contains(point) or (point.distance(T3H_polygon) < epsilon)) is True:
                return 'T3H'
            if (D2_polygon.contains(point) or (point.distance(D2_polygon) < epsilon)) is True:
                return 'D2'
            if (D1_polygon.contains(point) or (point.distance(D1_polygon) < epsilon)) is True:
                return 'D1'
            else:
                return 'ND'

    except TypeError:
        print('Duval result calculation error!')
        print('{h2}, {ch4}, {c2h6}, {c2h4}, {c2h2}')
        return 'N/A'

def create_duval_p2_marker(h2, ch4, c2h6, c2h4, c2h2, marker_name, **kwargs):
    marker_x, marker_y = calculate_duval_p2_coordinates(h2, ch4, c2h6, c2h4, c2h2)

    if 'timestamp' in kwargs and 'result' in kwargs and 'marker_color' in kwargs:
         try:
            timestamp = kwargs['timestamp']
            result = kwargs['result']
            set_color = kwargs['marker_color']
            return go.Scatter(x=marker_x, y=marker_y,
                                name= marker_name,
                                mode='markers',
                                marker_color=set_color,
                                marker_size=10,
                                meta= [result, timestamp],
                                hovertemplate="Diagnosis: %{meta[0]}<br>X: %{x:.2f}%<br>Y: %{y:.2f}%<br>%{meta[1]}<extra></extra>")
         except Exception as e:
            print(e)
            pass
    else:  
        return go.Scatter(x=marker_x, y=marker_y,
                                name= marker_name,
                                marker_color=set_color,
                                marker_size=10,
                                meta= marker_name,
                                hovertemplate="Diagnosis: %{meta}<br>X: %{x:.2f}%<br>Y: %{y:.2f}%<br>%<extra></extra>")



# %%
if __name__ == "__main__":
    '''
    fig = create_duval_p2_colorized()
    marker_name = calculate_duval_p2_result(10, 26, 64)
    fig.add_trace(create_duval_p2_marker(10, 26, 64, marker_name))
    fig.show()
    '''
    fig = create_duval_p2_colorized()
    #fig = create_duval_p2_nocolor()
    fig.show()

    # H2 = 31 ppm, C2H6 = 130 ppm, CH4 = 192 ppm, C2H4 = 31 ppm, and C2H2 = 0 ppm -> O
    dp2_result = calculate_duval_p2_result(31, 192, 130, 31, 0)
    print(dp2_result)
