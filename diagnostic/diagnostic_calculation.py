import sys
import pathlib

import numpy as np
import pandas as pd

sys.path.insert(0, str(pathlib.Path(__file__).parent)) # path change to allow importing in upper level for diagnostic sub-modules
import duval_triangle_1
import duval_triangle_4
import duval_triangle_5

def round_half_up(n, decimals=0):
    # rounding values
    multiplier = 10 ** decimals
    return np.floor(n*multiplier + 0.5) / multiplier

def calculate_ratios(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, o2_val, n2_val):
    '''
    R1: CH4/H2
    R2: C2H2/C2H4
    R3: C2H2/CH4
    R4: C2H6/C2H2
    R5: C2H4/C2H6
    R6: CO2/CO
    R7: O2/N2
    '''

    # Ratio 1: CH4/H2
    try:
        if h2_val == 0:
            r1_val = 0
        elif (pd.isna(ch4_val) is True) or (pd.isna(h2_val) is True):
            r1_val = np.nan
        else:
            r1_val = round_half_up(ch4_val / h2_val, 2)
    except TypeError as e:
        print(f'Ratio TypeError: {e}')
        r1_val = np.nan
    
    # Ratio 2: C2H2/C2H4
    try:
        if c2h4_val == 0:
            r2_val = 0
        elif (pd.isna(c2h2_val) is True) or (pd.isna(c2h4_val) is True):
            r2_val = np.nan
        else:
            r2_val = round_half_up(c2h2_val / c2h4_val, 2)
    except TypeError as e:
        print(f'Ratio TypeError: {e}')
        r2_val = np.nan

    # Ratio 3: C2H2/CH4
    try:
        if ch4_val == 0:
            r3_val = 0
        elif (pd.isna(c2h2_val) is True) or (pd.isna(ch4_val) is True):
            r3_val = np.nan
        else:
            r3_val = round_half_up(c2h2_val / ch4_val, 2)
    except TypeError as e:
        print(f'Ratio TypeError: {e}')
        r3_val = np.nan

    # Ratio 4: C2H6/C2H2
    try:
        if c2h2_val == 0:
            r4_val = 0
        elif (pd.isna(c2h6_val) is True) or (pd.isna(c2h2_val) is True):
            r4_val = np.nan
        else:
            r4_val = round_half_up(c2h6_val / c2h2_val, 2)
    except TypeError as e:
        print(f'Ratio TypeError: {e}')
        r4_val = np.nan

    # Ratio 5: C2H4/C2H6
    try:
        if c2h6_val == 0:
            r5_val = 0
        elif (pd.isna(c2h4_val) is True) or (pd.isna(c2h6_val) is True):
            r5_val = np.nan
        else:
            r5_val = round_half_up(c2h4_val / c2h6_val, 2)
    except TypeError as e:
        print(f'Ratio TypeError: {e}')
        r5_val = np.nan

    # Ratio 6: CO2/CO
    try:
        if co_val == 0:
            r6_val = 0
        elif (pd.isna(co2_val) is True) or (pd.isna(co_val) is True):
            r6_val = np.nan
        else:
            r6_val =  round_half_up(co2_val / co_val, 2)
    except TypeError as e:
        print(f'Ratio TypeError: {e}')
        r6_val = np.nan

    # Ratio 7: O2/N2
    try:
        if n2_val == 0:
            r7_val = 0
        elif (pd.isna(o2_val) is True) or (pd.isna(n2_val) is True):
            r7_val = np.nan
        else:
            r7_val = round_half_up(o2_val / n2_val, 2)
    except TypeError as e:
        print(f'Ratio TypeError: {e}')
        r7_val = np.nan

    ratio_list = [r1_val, r2_val, r3_val, r4_val, r5_val, r6_val, r7_val]
    
    return ratio_list

def rogers_ratio_calculation(ratio2, ratio1, ratio5):
    try:
        if (pd.isna(ratio2) is True) or (pd.isna(ratio1) is True) or (pd.isna(ratio5) is True):
            return 'N/A'
        elif ratio2 < 0.1 and ratio1 > 0.1 and ratio1 < 1 and ratio5 < 1:
            return 'Normal'
        elif ratio2 < 0.1 and ratio1 < 0.1 and ratio5 < 1:
            return 'PD'
        elif ratio2 > 0.1 and ratio2 < 3 and ratio1 > 0.1 and ratio1 < 1 and ratio5 > 3:
            return 'D1/D2'
        elif ratio2 < 0.1 and ratio1  > 0.1 and ratio1 < 1 and ratio5 >= 1 and ratio5 <= 3:
            return 'T1'
        elif ratio2 < 0.1 and ratio1 > 1 and ratio5 >= 1 and ratio5 <= 3:
            return 'T2'
        elif ratio2 < 0.1 and ratio1 > 1 and ratio5 > 3:
            return 'T3'
        else:
            return 'ND'
    except:
        print('Rogers ratio calculation error!')
        print(f'{ratio2}, {ratio1}, {ratio5}')
        return '-'

def doernenburg_ratio_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val):
    ratio_list = calculate_ratios(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, np.nan, np.nan)
    ratio1 = ratio_list[0]
    ratio2 = ratio_list[1]
    ratio3 = ratio_list[2]
    ratio4 = ratio_list[3]

    h2_l1 = 100
    h2_2l1 = 100 * 2
    ch4_l1 = 120
    ch4_2l1 = 120 * 2
    c2h2_l1 = 1
    c2h2_2l1 = 1 * 2
    c2h4_l1 =50
    c2h4_2l1 = 50 * 2
    c2h6_l1 = 65
    co_l1 = 350

    try:
        if (pd.isna(ratio1) is True) or (pd.isna(ratio2) is True) or (pd.isna(ratio3) is True) or (pd.isna(ratio4) is True):
            return 'N/A'
        elif (h2_val > h2_2l1 or ch4_val > ch4_2l1 or c2h2_val > c2h2_2l1 or c2h4_val > c2h4_2l1) and (c2h6_val > c2h6_l1 or co_val > co_l1):
            if (ch4_val > ch4_l1 or h2_val > h2_l1) and (c2h2_val > c2h2_l1 or c2h4_val > c2h4_l1) and (c2h2_val > c2h2_l1 or ch4_val > ch4_l1) and (c2h6_val > c2h6_l1 or c2h2_val > c2h2_l1):
                if ratio1 > 1 and ratio2 < 0.75 and ratio3 < 0.3 and ratio4 > 0.4:
                    return 'T'
                elif ratio1 < 0.1 and ratio3 < 0.3 and ratio4 > 0.4:
                    return 'PD'
                elif ratio1 > 0.1 and ratio1 < 1 and ratio2 > 0.75 and ratio3 > 0.3 and ratio4 < 0.4:
                    return  'D1/D2'
                else:
                    return 'ND'
            else:
                return 'N/A'
        else:
            return 'No fault'
    except:
        print('Doernenburg ratio calculation error!')
        print(f'{h2_val}, {ch4_val}, {c2h6_val}, {c2h4_val}, {c2h2_val}, {co_val}, {co2_val}')
        return '-'

def iec_ratio_calculation(ratio2, ratio1, ratio5):
    try:
        if (pd.isna(ratio2) is True) or (pd.isna(ratio1) is True) or (pd.isna(ratio5) is True):
            return 'N/A'
        if ratio2 < 0.1 and ratio5 < 0.2:
            return 'PD'
        elif ratio2 > 1 and ratio1 >= 0.1 and ratio1 <= 0.5 and ratio5 >1:
            return 'D1'
        elif ratio2 >= 0.6 and ratio2 <= 2.5 and ratio1 >= 0.1 and ratio1 <= 1 and ratio5 >2:
            return 'D2'
        elif ratio1 >1 and ratio5 <1:
            return 'T1'
        elif ratio2 < 0.1 and ratio1 > 1 and ratio5 >= 1 and ratio5 <= 4:
            return 'T2'
        elif ratio2 < 0.2 and ratio1 > 1 and ratio5 > 4:
            return 'T3'
        else:
            return "ND"
    except:
        print('IEC ratio calculation error!')
        print(f'{ratio2}, {ratio1}, {ratio5}')
        return '-'

def calculate_diagnostic_results(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val):
    ratio_list = calculate_ratios(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, np.nan, np.nan)

    diag_result_list = []

    try:
        if pd.isna([ratio_list[0], ratio_list[1], ratio_list[4]]).any() is True:
            diag_result_list.append('N/A')
        else:
            rogers_result = rogers_ratio_calculation(ratio_list[1], ratio_list[0], ratio_list[4])
            diag_result_list.append(rogers_result)

        if pd.isna([ratio_list[0], ratio_list[1], ratio_list[2], ratio_list[3]]).any() is True:
            diag_result_list.append('N/A')
        else:
            doernenburg_result = doernenburg_ratio_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val)
            diag_result_list.append(doernenburg_result)

        if pd.isna([ratio_list[0], ratio_list[1], ratio_list[4]]).any() is True:
            diag_result_list.append('N/A')
        else:
            iec_result = iec_ratio_calculation(ratio_list[1], ratio_list[0], ratio_list[4])
            diag_result_list.append(iec_result)

        if pd.isna([ch4_val, c2h2_val, c2h4_val]).any() is True:
            diag_result_list.append('N/A')
            duval1_result = 'N/A'
        else:
            duval1_result = duval_triangle_1.calculate_duval_1_result(ch4_val, c2h2_val, c2h4_val)
            diag_result_list.append(duval1_result)

        if pd.isna([h2_val, c2h6_val, ch4_val]).any() is True:
            diag_result_list.append('N/A')
        elif duval1_result in ['PD', 'T1', 'T2']:
            duval4_result = duval_triangle_4.calculate_duval_4_result(h2_val, c2h6_val, ch4_val)
            diag_result_list.append(duval4_result)
        else:
            diag_result_list.append('N/A')

        if pd.isna([ch4_val, c2h6_val, c2h4_val]).any() is True:
            diag_result_list.append('N/A')
        elif duval1_result in ['T2', 'T3']:
            duval5_result = duval_triangle_5.calculate_duval_5_result(ch4_val, c2h6_val, c2h4_val)
            diag_result_list.append(duval5_result)
        else:
            diag_result_list.append('N/A')
        
    except Exception as e:
        print(f'diag result calculation error!!:\n{e}')
        print(f'Input: {h2_val}, {ch4_val}, {c2h6_val}, {c2h4_val}, {c2h2_val}, {co_val}, {co2_val}')
        print(f'Ratios isna: {pd.isna(ratio_list)}')
        print(diag_result_list)

        diag_result_list = ['-', '-', '-', '-', '-', '-']

    return diag_result_list
    