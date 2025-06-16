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

import duval_triangle_1b
import duval_triangle_4
import duval_triangle_5

import numpy as np
import pandas as pd

# Requires Duval triangle 1b
D1_P_C2H2_L1 = 3
D1_P_C2H2_L2 = 18

# Requires Duval triangle 1b
D2_P_C2H2_L1 = 3
D2_P_C2H2_L2 = 12

# Requires Duval triangle 1b
D1_H_C2H2_L1 = 28
D1_H_C2H2_L2 = 249

# Requires Duval triangle 1b
D2_H_C2H2_L1 = 21
D2_H_C2H2_L2 = 84

C_C2H4_L1 = 15
C_C2H4_L2 = 49

# Requires Duval triangle 5b
C1_CH4_L1 = 6
C1_CH4_L2 = 24

# Requires Duval triangle 5b
C2_C2H4_L1 = 9
C2_C2H4_L2 = 42

# Requires Duval triangle 5b
C3_C2H4_L1 = 25
C3_C2H4_L2 = 338

T3_H_C2H4_L1 = 205
T3_H_C2H4_L2 = 762

S_H2_L1 = 140
S_H2_L2 = 484

O_C2H6_L1 = 165
O_C2H6_L2 = 1030

# Requires Duval triangle 5b
O_P_C2H6_L1 = 475
O_P_C2H6_L2 = 688

PD_H2_L1 = 78
PD_H2_L2 = 1234


def duval_limit_condition(fault_type, h2_ppm, ch4_ppm, c2h6_ppm, c2h4_ppm, c2h2_ppm):
    if (fault_type == 'N/A') or (fault_type == 'N/D'):
        return '-'
    
    elif fault_type == 'D1-P':
        if c2h2_ppm >= D1_P_C2H2_L2:
            return 'C2H2 >= L2'
        elif c2h2_ppm >= D1_P_C2H2_L1:
            return 'C2H2 >= L1'
        else:
            return '-'
        
    elif fault_type == 'D2-P':
        if c2h2_ppm >= D2_P_C2H2_L2:
            return 'C2H2 >= L2'
        elif c2h2_ppm >= D2_P_C2H2_L1:
            return 'C2H2 >= L1'
        else:
            return '-'
        
    elif fault_type == 'D1-H':
        if c2h2_ppm >= D1_H_C2H2_L2:
            return 'C2H2 >= L2'
        elif c2h2_ppm >= D1_H_C2H2_L1:
            return 'C2H2 >= L1'
        else:
            return '-'
        
    elif fault_type == 'D2-H':
        if c2h2_ppm >= D2_H_C2H2_L2:
            return 'C2H2 >= L2'
        elif c2h2_ppm >= D2_H_C2H2_L1:
            return 'C2H2 >= L1'
        else:
            return '-'
        
    elif fault_type == 'C':
        if c2h4_ppm >= C_C2H4_L2:
            return 'C2H4 >= L2'
        elif c2h4_ppm >= C_C2H4_L1:
            return 'C2H4 >= L1'
        else:
            return '-'
        
    elif fault_type == 'T3-H':
        if c2h4_ppm >= T3_H_C2H4_L2:
            return 'C2H4 >= L2'
        elif c2h4_ppm >= T3_H_C2H4_L1:
            return 'C2H4 >= L1'
        else:
            return '-'
        
    elif fault_type == 'S':
        if h2_ppm >= S_H2_L2:
            return 'H2 >= L2'
        elif h2_ppm >= S_H2_L1:
            return 'H2 >= L1'
        else:
            return '-'
        
    elif fault_type == 'O':
        if c2h6_ppm >= O_C2H6_L2:
            return 'C2H6 >= L2'
        elif c2h6_ppm >= O_C2H6_L1:
            return 'C2H6 >= L1'
        else:
            return '-'
        
    elif fault_type == 'PD':
        if h2_ppm >= PD_H2_L2:
            return 'H2 >= L2'
        elif h2_ppm >= PD_H2_L1:
            return 'H2 >= L1'
        else:
            return '-'
        
    else:
        return '-'
    
def duval_limit_condition_series(h2_s, ch4_s, c2h6_s, c2h4_s, c2h2_s):

    #TODO add triangle 1, 4 & 5 workflow
    #TODO loop over all data and return series of results
    if (h2_s is None) or (c2h6_s is None) or (c2h4_s is None) or (c2h2_s is None):
        result_series = None

    

    return result_series


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
                    'N2': [0, 51000, 52500, 53780, 54900, 55620], 
                    'Transformer age': [9, 10, 10, 10, 10, 10]}, index=[0, 1, 2, 3, 4, 5])