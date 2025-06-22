# -*- coding: utf-8 -*-
"""roc_calculation.py

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
    x = x.to_numpy()
    y = y.to_numpy()

    # convert into matrix
    A = np.vstack([x, np.ones(len(x))]).T 
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]

    return m, c

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
    - III-A 6-month rule ignore option for monitoring data


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
    
    # forward sequential
    segment_list = []
    i = 0
    k = 0
    m = 4
    while m < (len(gas_data)):

        if m+2 == (len(gas_data)-1):
            m=(len(gas_data)-1)
            j = i
            while j <= (m-3):
                backward_gas_data = gas_data[i:j]
                backward_gas_data_1 = gas_data[i:j-1]
                backward_gas_data_2 = gas_data[i:j-2]

                trend_b,h_b,p_b,z_b,tau_b,s_b,var_s_b,slope_b,intercept_b = pymannkendall.original_test(backward_gas_data)
                trend_b1,h_b1,p_b1,z_b1,tau_b1,s_b1,var_s_b1,slope_b1,intercept_b1 = pymannkendall.original_test(backward_gas_data_1)
                trend_b2,h_b2,p_b2,z_b2,tau_b2,s_b2,var_s_b2,slope_b2,intercept_b2 = pymannkendall.original_test(backward_gas_data_2)

                if (p_b < 0.05) and (p_b < p_b1) and (p_b1 < p_b2):
                    segment_list.append(gas_data[i:j-1])
                    segment_list.append(gas_data[j:m])

                    i = i + 1
                    k = k + 2
                    break

                if j == (m-3):
                    j = i
                    i = i + 1
                    k = k + 1
                    segment_list.append(gas_data[i:m])

                j+=1

            break

        forward_gas_data = gas_data[i:m]
        forward_gas_data_1 = gas_data[i:m+1]
        forward_gas_data_2 = gas_data[i:m+2]

        trend,h,p,z,tau,s,var_s,slope,intercept = pymannkendall.original_test(forward_gas_data)
        trend_1,h_1,p_1,z_1,tau_1,s_1,var_s_1,slope_1,intercept_1 = pymannkendall.original_test(forward_gas_data_1)
        trend_2,h_2,p_2,z_2,tau_2,s_2,var_s_2,slope_2,intercept_2 = pymannkendall.original_test(forward_gas_data_2)
        
        if (p < 0.05) and (p < p_1) and (p_1 < p_2):
            j = i

        else:
            continue

        while j <= (m-3):
            backward_gas_data = gas_data[i:j]
            backward_gas_data_1 = gas_data[i:j-1]
            backward_gas_data_2 = gas_data[i:j-2]

            trend_b,h_b,p_b,z_b,tau_b,s_b,var_s_b,slope_b,intercept_b = pymannkendall.original_test(backward_gas_data)
            trend_b1,h_b1,p_b1,z_b1,tau_b1,s_b1,var_s_b1,slope_b1,intercept_b1 = pymannkendall.original_test(backward_gas_data_1)
            trend_b2,h_b2,p_b2,z_b2,tau_b2,s_b2,var_s_b2,slope_b2,intercept_b2 = pymannkendall.original_test(backward_gas_data_2)

            if (p_b < 0.05) and (p_b < p_b1) and (p_b1 < p_b2):
                segment_list.append(gas_data[i:j-1])
                segment_list.append(gas_data[j:m])

                i = i + 1
                k = k + 2
                break
            if j == (m-3):
                j = i
                i = i + 1
                k = k + 1
                segment_list.append(gas_data[i:m])

            j+=1

        m+=1

    segment_start = 0
    segment_trends = []
    for segment in segment_list:
        segment_size = len(segment)
        if timeseries != None:
            #TODO add trend analysis with ppm/year estimation
            raise Exception('Trend analysis does not support timeseries estimation yet!')
        else:
            x_segment = x_series[segment_start:segment_size]
            seg_m, seg_c = fit_least_squares_line(x_segment, segment)
            y_segment = seg_m * x_segment + seg_c
            segment_trends.append(seg_m)

    # TODO check linear fitting for segments + calculate trends

    # TODO check confidence levels

    return segment_list, segment_trends




if __name__ == '__main__':
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
    
