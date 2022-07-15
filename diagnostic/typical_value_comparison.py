import numpy as np
import pandas as pd

def iec_typical_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val):
    
    # IEC 90th percentile typical values
    h2_typ = 150
    ch4_typ = 130
    c2h6_typ = 90
    c2h4_typ = 280
    c2h2_typ = 20
    c2h2_oltc_typ = 280
    co_typ = 600
    co2_typ = 14000

    iec_typical_results = []
    try:
        if pd.isna(h2_val) is True:
            iec_typical_results.append('-')
        elif h2_val > h2_typ:
            iec_typical_results.append('Typical values exceeded!')
        else:
            iec_typical_results.append('Normal')

        if pd.isna(ch4_val) is True:
            iec_typical_results.append('-')
        elif ch4_val > ch4_typ:
            iec_typical_results.append('Typical values exceeded!')
        else:
            iec_typical_results.append('Normal')

        if pd.isna(c2h6_val) is True:
            iec_typical_results.append('-')
        elif c2h6_val > c2h6_typ:
            iec_typical_results.append('Typical values exceeded!')
        else:
            iec_typical_results.append('Normal')

        if pd.isna(c2h4_val) is True:
            iec_typical_results.append('-')
        elif c2h4_val > c2h4_typ:
            iec_typical_results.append('Typical values exceeded!')
        else:
            iec_typical_results.append('Normal')

        if pd.isna(c2h2_val) is True:
            iec_typical_results.append('-')
        elif c2h2_val > c2h2_typ:
            if c2h2_val > c2h2_oltc_typ:
                iec_typical_results.append('Communicating OLTC typical values exceeded!')
            else:
                iec_typical_results.append('Typical values exceeded unless communicating OLTC!')
        else:
            iec_typical_results.append('Normal')

        if pd.isna(co_val) is True:
            iec_typical_results.append('-')
        elif co_val > co_typ:
            iec_typical_results.append('Typical values exceeded!')
        else:
            iec_typical_results.append('Normal')

        if pd.isna(co2_val) is True:
            iec_typical_results.append('-')
        elif co2_val > co2_typ:
            iec_typical_results.append('Typical values exceeded!')
        else:
            iec_typical_results.append('Normal')
        
    except Exception as e:
        print(f'IEC typical value comparison issue!!\n{e}')
        iec_typical_results = ['-', '-', '-', '-', '-', '-', '-']

    return iec_typical_results

def ieee_2008_typical_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val):
    try:
        tdcg_val = h2_val + ch4_val + c2h6_val + c2h4_val + c2h2_val + co_val
    except:
        tdcg_val = np.nan

    # breakpoint of typical values for condition 2
    h2_typ2 = 101
    ch4_typ2 = 121
    c2h6_typ2 = 66
    c2h4_typ2 = 51
    c2h2_typ2 = 2
    co_typ2 = 351
    co2_typ2 = 2500
    tdcg_typ2 = 721

    # breakpoint of typical values for condition 3
    h2_typ3 = 701
    ch4_typ3 = 401
    c2h6_typ3 = 101
    c2h4_typ3 = 101
    c2h2_typ3 = 10
    co_typ3 = 571
    co2_typ3 = 4001
    tdcg_typ3 = 1921

    # breakpoint of typical values for condition 4
    h2_typ4 = 1800
    ch4_typ4 = 1000
    c2h6_typ4 = 150
    c2h4_typ4 = 200
    c2h2_typ4 = 35
    co_typ4 = 1400
    co2_typ4 = 10000
    tdcg_typ4 = 4630
    #TODO add condition 2 and condition 3 typical values and result calculations

    #TODO individual typical value comparison handling
    ieee_typical_results = []

    try:
        if pd.isna(h2_val) is True:
            ieee_typical_results.append('-')
        elif h2_val > h2_typ4:
            ieee_typical_results.append('Typical values exceeded! / Condition 4')
        elif h2_val >= h2_typ3:
            ieee_typical_results.append('Typical values exceeded! / Condition 3')
        elif h2_val >= h2_typ2:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')

        if pd.isna(ch4_val) is True:
            ieee_typical_results.append('-')
        elif ch4_val > ch4_typ4:
            ieee_typical_results.append('Typical values exceeded! / Condition 4')
        elif ch4_val >= ch4_typ3:
            ieee_typical_results.append('Typical values exceeded! / Condition 3')
        elif ch4_val >= ch4_typ2:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')

        if pd.isna(c2h6_val) is True:
            ieee_typical_results.append('-')
        elif c2h6_val > c2h6_typ4:
            ieee_typical_results.append('Typical values exceeded! / Condition 4')
        elif c2h6_val >= c2h6_typ3:
            ieee_typical_results.append('Typical values exceeded! / Condition 3')
        elif c2h6_val >= c2h6_typ2:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')

        if pd.isna(c2h4_val) is True:
            ieee_typical_results.append('-')
        elif c2h4_val > c2h4_typ4:
            ieee_typical_results.append('Typical values exceeded! / Condition 4')
        elif c2h4_val >= c2h4_typ3:
            ieee_typical_results.append('Typical values exceeded! / Condition 3')
        elif c2h4_val >= c2h4_typ2:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')

        if pd.isna(c2h2_val) is True:
            ieee_typical_results.append('-')
        elif c2h2_val > c2h2_typ4:
            ieee_typical_results.append('Typical values exceeded! / Condition 4')
        elif c2h2_val >= c2h2_typ3:
            ieee_typical_results.append('Typical values exceeded! / Condition 3')
        elif c2h2_val >= c2h2_typ2:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')

        if pd.isna(co_val) is True:
            ieee_typical_results.append('-')
        elif co_val > co_typ4:
            ieee_typical_results.append('Typical values exceeded! / Condition 4')
        elif co_val >= co_typ3:
            ieee_typical_results.append('Typical values exceeded! / Condition 3')
        elif co_val >= co_typ2:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')

        if pd.isna(co2_val) is True:
            ieee_typical_results.append('-')
        elif co2_val > co2_typ4:
            ieee_typical_results.append('Typical values exceeded! / Condition 4')
        elif co2_val >= co2_typ3:
            ieee_typical_results.append('Typical values exceeded! / Condition 3')
        elif co2_val > co2_typ2:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')

        if pd.isna(tdcg_val) is True:
            ieee_typical_results.append('-')
        elif tdcg_val > tdcg_typ4:
            ieee_typical_results.append('Typical values exceeded! / Condition 4')
        elif tdcg_val >= tdcg_typ3:
            ieee_typical_results.append('Typical values exceeded! / Condition 3')
        elif tdcg_val >= tdcg_typ2:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')
        
    except Exception as e:
        print(f'IEEE-2008 typical value comparison issue!!\n{e}')
        ieee_typical_results = ['-', '-', '-', '-', '-', '-', '-', '-']

    return ieee_typical_results

# TODO add IEEE C57.104-2019 95% typical values
# TODO add 0-value handling for O2/N2 ratio and optional transformer age

def ieee_2019_typical_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, o2_val, n2_val, trafo_age_val):
    ieee_2019_typical_results = []

    if (pd.isna(o2_val) == True) or (pd.isna(n2_val) == True):
        o2_n2_ratio = 1
    elif (o2_val == 0 or n2_val == 0) is True:
        o2_n2_ratio = 0
    else:
        o2_n2_ratio = o2_val/n2_val

    # 90th percentile typical values o2/n2 <= 0.2
    h2_typ_sealed_unknown = 80
    h2_typ_sealed_under_30 = 75
    h2_typ_sealed_over_30 = 100

    ch4_typ_sealed_unknown = 90
    ch4_typ_sealed_under_9 = 45
    ch4_typ_sealed_under_30 = 90
    ch4_typ_sealed_over_30 = 110

    c2h6_typ_sealed_unknown = 90
    c2h6_typ_sealed_under_9 = 30
    c2h6_typ_sealed_under_30 = 90
    c2h6_typ_sealed_over_30 = 150

    c2h4_typ_sealed_unknown = 50
    c2h4_typ_sealed_under_9 = 20
    c2h4_typ_sealed_under_30 = 50
    c2h4_typ_sealed_over_30 = 90

    c2h2_typ_sealed = 1
    
    co_typ_sealed = 900

    co2_typ_sealed_unknown = 9000
    co2_typ_sealed_under_9 = 5000
    co2_typ_sealed_over_10 = 10000    

    # 90th percentile typical values o2/n2 > 0.2
    h2_typ_open = 40

    ch4_typ_open = 20

    c2h6_typ_open = 15

    c2h4_typ_open_unknown = 50
    c2h4_typ_open_under_9 = 25
    c2h4_typ_open_over_10 = 60

    c2h2_typ_open = 2
    
    co_typ_open = 500

    co2_typ_open_unknown = 5000
    co2_typ_open_under_9 = 3500
    co2_typ_open_over_10 = 5500

    try:
        if o2_n2_ratio <= 0.2:
            if pd.isna(h2_val) is True:
                ieee_2019_typical_results.append('-')
            elif pd.isna(trafo_age_val) is True:
                if h2_val > h2_typ_sealed_unknown:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val <= 30:
                if h2_val > h2_typ_sealed_under_30:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val > 30:
                if h2_val > h2_typ_sealed_over_30:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')

            if pd.isna(ch4_val) is True:
                ieee_2019_typical_results.append('-')
            elif pd.isna(trafo_age_val) is True:
                if ch4_val > ch4_typ_sealed_unknown:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val <= 9:
                if ch4_val > ch4_typ_sealed_under_9:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif (trafo_age_val >= 10) and (trafo_age_val <= 30):
                if ch4_val > ch4_typ_sealed_under_30:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val > 30:
                if ch4_val > ch4_typ_sealed_over_30:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')

            if pd.isna(c2h6_val) is True:
                ieee_2019_typical_results.append('-')
            elif pd.isna(trafo_age_val) is True:
                if c2h6_val > c2h6_typ_sealed_unknown:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val <= 9:
                if c2h6_val > c2h6_typ_sealed_under_9:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif (trafo_age_val >= 10) and (trafo_age_val <= 30):
                if c2h6_val > c2h6_typ_sealed_under_30:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val > 30:
                if c2h6_val > c2h6_typ_sealed_over_30:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')

            if pd.isna(c2h4_val) is True:
                ieee_2019_typical_results.append('-')
            elif pd.isna(trafo_age_val) is True:
                if c2h4_val > c2h4_typ_sealed_unknown:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val <= 9:
                if c2h4_val > c2h4_typ_sealed_under_9:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif (trafo_age_val >= 10) and (trafo_age_val <= 30):
                if c2h4_val > c2h4_typ_sealed_under_30:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val > 30:
                if c2h4_val > c2h4_typ_sealed_over_30:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')

            if pd.isna(c2h2_val) is True:
                ieee_2019_typical_results.append('-')
            else:
                if c2h2_val > c2h2_typ_sealed:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            
            if pd.isna(co_val) is True:
                ieee_2019_typical_results.append('-')
            else:
                if co_val > co_typ_sealed:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')

            if pd.isna(co2_val) is True:
                ieee_2019_typical_results.append('-')
            elif pd.isna(trafo_age_val) is True:
                if co2_val > co2_typ_sealed_unknown:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val <= 9:
                if co2_val > co2_typ_sealed_under_9:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val >= 10:
                if co2_val > co2_typ_sealed_over_10:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')

        else:
            if pd.isna(h2_val) is True:
                ieee_2019_typical_results.append('-')
            else:
                if h2_val > h2_typ_open:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')

            if pd.isna(ch4_val) is True:
                ieee_2019_typical_results.append('-')
            else:
                if ch4_val > ch4_typ_open:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')

            if pd.isna(c2h6_val) is True:
                ieee_2019_typical_results.append('-')
            else:
                if c2h6_val > c2h6_typ_open:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            
            if pd.isna(c2h4_val) is True:
                ieee_2019_typical_results.append('-')
            elif pd.isna(trafo_age_val) is True:
                if c2h4_val > c2h4_typ_open_unknown:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val <= 9:
                if c2h4_val > c2h4_typ_open_under_9:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val >= 10:
                if c2h4_val > c2h4_typ_open_over_10:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')

            if pd.isna(c2h2_val) is True:
                ieee_2019_typical_results.append('-')
            else:
                if c2h2_val > c2h2_typ_open:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')

            if pd.isna(co_val) is True:
                ieee_2019_typical_results.append('-')
            else:
                if co_val > co_typ_open:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')

            if pd.isna(co2_val) is True:
                ieee_2019_typical_results.append('-')
            elif pd.isna(trafo_age_val) is True:
                if co2_val > co2_typ_open_unknown:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val <= 9:
                if co2_val > co2_typ_open_under_9:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val >= 10:
                if co2_val > co2_typ_open_over_10:
                    ieee_2019_typical_results.append('Typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')

    except Exception as e:
        print(f'IEEE-2019 typical value comparison issue!!\n{e}')
        ieee_2019_typical_results = ['-', '-', '-', '-', '-', '-', '-']

    return ieee_2019_typical_results
    

def calculate_typical_results(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, o2_val, n2_val, trafo_age_val):
    typical_result_list = []
    
    try:
        iec_typical_list = iec_typical_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val)
        typical_result_list.append(iec_typical_list)

        ieee_2008_typical_list = ieee_2008_typical_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val)
        typical_result_list.append(ieee_2008_typical_list)

        ieee_2019_typical_list = ieee_2019_typical_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, o2_val, n2_val, trafo_age_val)
        typical_result_list.append(ieee_2019_typical_list)
    except Exception as e:
        print(f'Typical value comparison issue!!\n{e}')

    return typical_result_list

if __name__ == '__main__':
    '''
    typical_list = calculate_typical_results(50, 60, 100, 80, 10, 500, 2000, 15600, 56000, 10)
    for r in typical_list:
        print(r, len(r))
    '''
    ieee2008_list = ieee_2008_typical_calculation(109.99, 120.99, 65.99, 50.99, 1.99, 350.99, 2500)
    print(ieee2008_list, len(ieee2008_list))

    #ieee2019_0_list = ieee_2019_typical_calculation(50, 60, 100, 80, 10, 500, 2000, 15600, 56000, 10)
    #print(ieee2019_0_list, len(ieee2019_0_list))
