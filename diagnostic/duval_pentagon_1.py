# -*- coding: utf-8 -*-
"""duval_pentagon_1.py

This module calculates duval pentagon 1 related diagnostics and generates duval pentagon visualizations using plotly library.

@Author: https://github.com/ToniMellin
"""

# %%
import numpy as np
from pandas import isna
import pandas as pd
import plotly.graph_objects as go   # plotly is an interactive plotting library
import plotly.colors as pcolors

def round_half_up(n, decimals=0):
    # rounding values
    multiplier = 10 ** decimals
    return np.floor(n*multiplier + 0.5) / multiplier

def create_duval_p1_colorized():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, -35, -38, 0, 0, -1, -1, 0, 0], y=[1.5, 3.1, 12.4, 40, 33, 33, 24.5, 24.5, 1.5], 
                             name='S',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(170,156,192, 0.5)'
                            ))
    fig.add_trace(go.Scatter(x=[0, -1, -1, 0, 0], y=[33, 33, 24.5, 24.5, 33], 
                             name='PD',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(178,255,228, 0.5)'
                            ))
    fig.add_trace(go.Scatter(x=[-6, -22.5, -23.5, -35, 0, 0, -6], y=[-4, -32.4, -32.4, 3, 1.5, -3, -4], 
                             name='T1',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(245, 243, 39, 0.5)'
                            ))
    fig.add_trace(go.Scatter(x=[-6, 1, -22.5, -6], y=[-4, -32.4, -32.4, -4], 
                             name='T2',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(245, 148, 39, 0.5)'
                            ))
    fig.add_trace(go.Scatter(x=[0, 24.3, 23.5, 1, -6, 0], y=[-3, -30, -32.4, -32.4, -4, -3], #-32 as per TB 771 & C57.143-2019 would leave a gap
                             name='T3',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(245, 54, 39, 0.5)'
                            ))
    fig.add_trace(go.Scatter(x=[4, 32, 24.3, 0, 0, 4], y=[16, -6.1, -30, -3, 1.5, 16], 
                             name='D2',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5,
                            fill="toself",
                            fillcolor='rgba(178,205,255, 0.5)'
                            ))
    fig.add_trace(go.Scatter(x=[0, 38, 32, 4, 0, 0], y=[40, 12, -6.1, 16, 1.5, 40], 
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

def create_duval_p1_nocolor():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, -35, -38, 0, 0, -1, -1, 0, 0], y=[1.5, 3.1, 12.4, 40, 33, 33, 24.5, 24.5, 1.5], 
                             name='S',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5
                            ))
    fig.add_trace(go.Scatter(x=[0, -1, -1, 0, 0], y=[33, 33, 24.5, 24.5, 33], 
                             name='PD',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5
                            ))
    fig.add_trace(go.Scatter(x=[-6, -22.5, -23.5, -35, 0, 0, -6], y=[-4, -32.4, -32.4, 3, 1.5, -3, -4], 
                             name='T1',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5
                            ))
    fig.add_trace(go.Scatter(x=[-6, 1, -22.5, -6], y=[-4, -32.4, -32.4, -4], 
                             name='T2',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5
                            ))
    fig.add_trace(go.Scatter(x=[0, 24.3, 23.5, 1, -6, 0], y=[-3, -30, -32.4, -32.4, -4, -3], 
                             name='T3',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5
                            ))
    fig.add_trace(go.Scatter(x=[4, 32, 24.3, 0, 0, 4], y=[16, -6.1, -30, -3, 1.5, 16], 
                             name='D2',
                            showlegend=False,
                            mode='lines',
                            line_color='black',
                            line_width=0.5
                            ))
    fig.add_trace(go.Scatter(x=[0, 38, 32, 4, 0, 0], y=[40, 12, -6.1, 16, 1.5, 40], 
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

def calculate_duval_p1_result():

    return

def create_duval_p1_marker():

    return


# %%
if __name__ == "__main__":
    '''
    fig = create_duval_p1_colorized()
    marker_name = calculate_duval_p1_result(10, 26, 64)
    fig.add_trace(create_duval_p1_marker(10, 26, 64, marker_name))
    fig.show()
    '''
    fig = create_duval_p1_colorized()
    #fig = create_duval_p1_nocolor()
    fig.show()