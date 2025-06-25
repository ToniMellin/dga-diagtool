# %%
# -*- coding: utf-8 -*-
"""trend_analysis.py

This module makes the calculations of rate-of-change (ROC) for gas readings.

@Author: https://github.com/ToniMellin

* Copyright (C) 2023-2025 Toni Mellin - All Rights Reserved
* You may use, distribute and modify this code under the
* terms of the MIT license.
*
* See file LICENSE or go to 
* https://github.com/ToniMellin/dga-diagtool/blob/master/LICENSE 
* for full license details.
"""

import numpy as np
import pandas as pd
import pymannkendall

# https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html
def fit_least_squares_line(x, y):
    # convert into numpy arrays
    x = np.array(list(x))
    y = np.array(list(y))

    # convert into matrix
    A = np.vstack([x, np.ones(len(x))]).T 
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]

    return m, c

def round_half_up(n, decimals=0):
    # rounding values
    multiplier = 10 ** decimals
    return np.floor(n*multiplier + 0.5) / multiplier

def mann_kendall_method(gas_data, x_series, iii_a_rule=False, timeseries=None, sampling_window=None):
    """
    Mann-Kendall DGA trend detection based heavily on following article
    
     
    @article{herath2024development,
    title={Development of Trend Detection Technique for Dissolved Gas Analysis of Transmission Power Transformers},
    author={Herath, T and Wang, ZD and Liu, Q and Wilson, G and Hooton, R and Raymond, T},
    journal={IEEE Transactions on Power Delivery},
    year={2024},
    publisher={IEEE}
    }

    Exceptions:
    - III-A 6-month median filtering rule ignored for purposes of monitoring data

    Utilizing pymanendall python package reference as follows

    @article{Hussain2019pyMannKendall,
	journal = {Journal of Open Source Software},
	doi = {10.21105/joss.01556},
	issn = {2475-9066},
	number = {39},
	publisher = {The Open Journal},
	title = {pyMannKendall: a python package for non parametric Mann Kendall family of trend tests.},
	url = {http://dx.doi.org/10.21105/joss.01556},
	volume = {4},
	author = {Hussain, Md. and Mahmud, Ishtiak},
	pages = {1556},
	date = {2019-07-25},
	year = {2019},
	month = {7},
	day = {25},
    }

    


    """
    if iii_a_rule is True:
        if timeseries is None:
            raise Exception('Time series data not included!')
        elif len(timeseries) != len(gas_data):
            raise Exception('Time series data and gas data lengths do not match!')
        
        if sampling_window != None:
            if type(sampling_window) == str:
                #TODO implement sampling window with pandas str format
                raise Exception('Data sampling not implemented!')

            elif type(sampling_window) == int:
                #TODO implement sampling window with strict window size
                raise Exception('Data sampling not implemented!')
        else:
            #TODO implement 6 month median sampling
            raise Exception('Data sampling not implemented!')
        
    else:
        if sampling_window != None:
            if (type(sampling_window) == str) and (timeseries is None):
                #TODO implement sampling window with pandas str format
                raise Exception('Time series data missing')
            elif type(sampling_window) == int:
                #TODO implement sampling window with strict window size
                raise Exception('Data sampling not implemented!')
            else:
                #TODO implement sampling window with pandas str format
                raise Exception('Data sampling not implemented!')



    if len(gas_data) < 4:
        return None, None
    
    # segmentation loop
    segment_list = []
    i = 0
    j = 0
    m = 4
    minimum_exists = False
    maximum_exists = False

    while i <= (len(gas_data)-3):

        for n in range(i+4, len(gas_data)-1):

            forward_gas_data = gas_data[i:n]
            forward_gas_data_1 = gas_data[i:n+1]
            forward_gas_data_2 = gas_data[i:n+2]

            trend,h,p,z,tau,s,var_s,slope,intercept = pymannkendall.original_test(forward_gas_data)
            trend_1,h_1,p_1,z_1,tau_1,s_1,var_s_1,slope_1,intercept_1 = pymannkendall.original_test(forward_gas_data_1)
            trend_2,h_2,p_2,z_2,tau_2,s_2,var_s_2,slope_2,intercept_2 = pymannkendall.original_test(forward_gas_data_2)
            
            if (p < 0.05) and (p < p_1) and (p < p_2):
                minimum_exists = True
                m=n-1
                break

        if minimum_exists is False:
            m=len(gas_data)


        for j in range(m-3, i+1, -1):

            backward_gas_data = gas_data[j:m][::-1]
            backward_gas_data_1 = gas_data[j-1:m][::-1]
            backward_gas_data_2 = gas_data[j-2:m][::-1]

            trend_b,h_b,p_b,z_b,tau_b,s_b,var_s_b,slope_b,intercept_b = pymannkendall.original_test(backward_gas_data)
            trend_b1,h_b1,p_b1,z_b1,tau_b1,s_b1,var_s_b1,slope_b1,intercept_b1 = pymannkendall.original_test(backward_gas_data_1)
            trend_b2,h_b2,p_b2,z_b2,tau_b2,s_b2,var_s_b2,slope_b2,intercept_b2 = pymannkendall.original_test(backward_gas_data_2)

            if (p_b < 0.05) and (p_b < p_b1) and (p_b < p_b2):

                segment_list.append(gas_data[i:j])
                segment_list.append(gas_data[j:m])
                maximum_exists = True
                i = m
                break

        if maximum_exists is False:

            segment_list.append(gas_data[i:m])
            j = i
            i = m
            

        minimum_exists = False
        maximum_exists = False

    segment_start = 0
    segment_confidences = []
    segment_trends = []
    segment_trend_lines_y = []
    segment_trend_lines_x = []

    for segment in segment_list:
        segment_size = len(segment)

        seg_trend,seg_h,seg_p,seg_z,seg_tau,seg_s,seg_var_s,seg_slope,seg_intercept = pymannkendall.original_test(segment)        
        seg_confidence_percentage = round_half_up((1 - seg_p)*100, 2) 
        
        segment_confidences.append(seg_confidence_percentage)

        if timeseries != None:
            #TODO add trend analysis with ppm/year estimation based on timestamps
            raise Exception('Trend analysis does not support timeseries estimation yet!')
        
        else:
            x_segment = x_series[segment_start:segment_start+segment_size]
            seg_m, seg_c = fit_least_squares_line(x_segment, segment)
            y_segment = seg_m * x_segment + seg_c

            segment_trends.append([seg_m, seg_c, seg_trend, seg_h, seg_slope])
            segment_trend_lines_x.append(x_segment)
            segment_trend_lines_y.append(y_segment)
            
            segment_start = segment_start + segment_size

    return segment_list, segment_confidences, segment_trends, segment_trend_lines_x, segment_trend_lines_y

# %%
if __name__ == '__main__':
    import plotly.graph_objects as go
    import plotly.io as pio
    import plotly.colors as pcolors
    import plotly.express as px
    from plotly.subplots import make_subplots

    # plotly default theme
    pio.templates['custom_theme'] = pio.templates['plotly_white']
    pio.templates['custom_theme'].layout.colorway = pcolors.qualitative.D3
    pio.templates.default = 'custom_theme'

    df_sample3 = pd.DataFrame({'Timestamp': [pd.to_datetime('2021-05-11'), pd.to_datetime('2021-06-02'), pd.to_datetime('2022-05-02 15:02'), pd.to_datetime('2022-05-24 06:02'), pd.to_datetime('2022-06-01 06:02'), pd.to_datetime('2022-06-01 23:34')],  
                    'H2': [0, 10, 50, 100, 160, 250], 
                    'CH4': [0, 20, 41, 60, 66, 80], 
                    'C2H6': [0, 60, 121, 172, 200, 207], 
                    'C2H4': [0, 5, 50, 60, 66, 67], 
                    'C2H2': [0, 1, 2, 5, 6, 10], 
                    'CO': [0, 150, 200, 400, 500, 600], 
                    'CO2': [0, 2211, 4200, 4500, 4561, 4603], 
                    'O2': [0, 19000, 20005, 20100, 21000, 21010], 
                    'N2': [0, 51000, 52500, 53780, 54900, 55620]}, index=[0, 1, 2, 3, 4, 5])

    seg_list, seg_confs, seg_trends, seg_x_lines, seg_y_lines = mann_kendall_method(df_sample3['H2'], df_sample3.index)

    print(seg_list)
    print(seg_trends)
    print(seg_y_lines)

    # %%
    fig_test = go.Figure()
    fig_test.add_trace(go.Scatter(
                        x=df_sample3.index,
                        y=df_sample3['H2'],
                        mode='markers',
                        name='test data'))
    fig_test.add_trace(go.Scatter(
                        x=seg_x_lines[0],
                        y=seg_y_lines[0],
                        mode='lines',
                        line=go.scatter.Line(color=px.colors.qualitative.D3[1]),
                        text=f'Confidence: {seg_confs[0]}%<br>Trend: {seg_trends[0][2]}<br>Slope: {seg_trends[0][4]}<br>m: {seg_trends[0][0]}',
                        name='trendline'))
    fig_test.update_layout(title='Mann-Kendall fit test')
    fig_test.show()

    # %%
    test_saw = np.append(np.arange(1, 11), np.arange(9 , 0, -1))
    x_saw = np.arange(1, 20)

    seg_saw_list, seg_saw_confs, seg_saw_trends, seg_saw_x_lines, seg_saw_y_lines = mann_kendall_method(test_saw, x_saw)

    fig_saw = go.Figure()
    fig_saw.add_trace(go.Scatter(
                        x=x_saw,
                        y=test_saw,
                        mode='markers',
                        name='test data'))

    for s, trend_line_xy in enumerate(zip(seg_saw_x_lines, seg_saw_y_lines)):
        fig_saw.add_trace(go.Scatter(
                            x=trend_line_xy[0],
                            y=trend_line_xy[1],
                            mode='lines',
                            line=go.scatter.Line(color=px.colors.qualitative.D3[1]),
                            text=f'Confidence: {seg_saw_confs[s]}%<br>Trend: {seg_saw_trends[s][2]}<br>Slope: {seg_saw_trends[s][4]}<br>m: {seg_saw_trends[s][0]}',
                            name=f'trendline {s}'))


    fig_saw.update_layout(title='Mann-Kendall fit test for triangle edge')
    fig_saw.show()


    # %%
    test_saw_pattern = np.append(test_saw, np.repeat(1, 10))
    test_saw_r = np.tile(test_saw_pattern, 2)
    x_saw_r = np.arange(1, len(test_saw_r)+1)

    seg_saw_r_list, seg_saw_r_confs, seg_saw_r_trends, seg_saw_r_x_lines, seg_saw_r_y_lines = mann_kendall_method(test_saw_r, x_saw_r)

    fig_saw_r = go.Figure()
    fig_saw_r.add_trace(go.Scatter(
                        x=x_saw_r,
                        y=test_saw_r,
                        mode='markers',
                        name='test data'))

    for s, trend_line_xy in enumerate(zip(seg_saw_r_x_lines, seg_saw_r_y_lines)):
        fig_saw_r.add_trace(go.Scatter(
                            x=trend_line_xy[0],
                            y=trend_line_xy[1],
                            mode='lines',
                            line=go.scatter.Line(color=px.colors.qualitative.D3[1]),
                            text=f'Confidence: {seg_saw_r_confs[s]}%<br>Trend: {seg_saw_r_trends[s][2]}<br>Slope: {seg_saw_r_trends[s][4]}<br>m: {seg_saw_r_trends[s][0]}',
                            name=f'trendline {s}'))


    fig_saw_r.update_layout(title='Mann-Kendall fit test for sawtooth edge')
    fig_saw_r.show()

    # %%
    a = np.append(np.arange(5, 66, 4), np.arange(64, 30, -2))
    b = np.append(a, np.repeat(30, 10))
    c = np.append(b, np.arange(33, 66, 2))

    y_saw_ext = np.tile(np.array([10, 15, 5]), 20) + c
    print(y_saw_ext)
    x_saw_ext = np.arange(1, len(y_saw_ext)+1)

    seg_saw_ext_list, seg_saw_ext_confs, seg_saw_ext_trends, seg_saw_ext_x_lines, seg_saw_ext_y_lines = mann_kendall_method(y_saw_ext, x_saw_ext)

    fig_saw_ext = go.Figure()
    fig_saw_ext.add_trace(go.Scatter(
                        x=x_saw_ext,
                        y=y_saw_ext,
                        mode='markers',
                        name='test data'))

    for s, trend_line_xy in enumerate(zip(seg_saw_ext_x_lines, seg_saw_ext_y_lines)):
        fig_saw_ext.add_trace(go.Scatter(
                            x=trend_line_xy[0],
                            y=trend_line_xy[1],
                            mode='lines',
                            line=go.scatter.Line(color=px.colors.qualitative.D3[1]),
                            text=f'Confidence: {seg_saw_ext_confs[s]}%<br>Trend: {seg_saw_ext_trends[s][2]}<br>Slope: {seg_saw_ext_trends[s][4]}<br>m: {seg_saw_ext_trends[s][0]}',
                            name=f'trendline {s}'))


    fig_saw_ext.update_layout(title='Mann-Kendall fit test for simulated trending with data variance')
    fig_saw_ext.show()
# %%
