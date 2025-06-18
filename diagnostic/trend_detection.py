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



def mann_kendall_method(gas_data, ignore_iii_a, sampling_window):
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

    if gas_data.shape[0] < 4:
        return 'N/A'
    
    # forward sequential
    forward_sement_data_list = []
    for i, gas_value in enumerate(gas_data):
        forward_sement_data_list.append(gas_value)
        if i < 4:
            continue

        trend,h,p,z,tau,s,var_s,slope,intercept = pymannkendall.original_test(forward_sement_data_list, 0.05)
        
        # TODO checkp value to segment data 

    # backward sequential
    # TODO backward sequential with check p value for segmenting

    # TODO combine segments

    # TODO linear fitting for segments + calculate trends

    # TODO confidence levels

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
    
