import pandas as pd
import numpy as np

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

    # typical values for condition 1
    h2_typ1 = 100
    ch4_typ1 = 120
    c2h6_typ1 = 65
    c2h4_typ1 = 50
    c2h2_typ1 = 1
    co_typ1 = 350
    co2_typ1 = 2500
    tdcg_typ1 = 720

    # typical values for condition 2

    #TODO add condition 2 and condition 3 typical values and result calculations

    #TODO individual typical value comparison handling
    ieee_typical_results = []

    try:
        if pd.isna(h2_val) is True:
            ieee_typical_results.append('-')
        elif h2_val > h2_typ1:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')

        if pd.isna(ch4_val) is True:
            ieee_typical_results.append('-')
        elif ch4_val > ch4_typ1:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')

        if pd.isna(c2h6_val) is True:
            ieee_typical_results.append('-')
        elif c2h6_val > c2h6_typ1:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')

        if pd.isna(c2h4_val) is True:
            ieee_typical_results.append('-')
        elif c2h4_val > c2h4_typ1:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')

        if pd.isna(c2h2_val) is True:
            ieee_typical_results.append('-')
        elif c2h2_val > c2h2_typ1:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')

        if pd.isna(co_val) is True:
            ieee_typical_results.append('-')
        elif co_val > co_typ1:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')

        if pd.isna(co2_val) is True:
            ieee_typical_results.append('-')
        elif co2_val > co2_typ1:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')

        if pd.isna(tdcg_val) is True:
            ieee_typical_results.append('-')
        elif tdcg_val > tdcg_typ1:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')
        
    except Exception as e:
        print(f'IEEE-2008 typical value comparison issue!!\n{e}')
        ieee_typical_results = ['-', '-', '-', '-', '-', '-', '-', '-']

    return ieee_typical_results

#TODO add IEEE C57.104-2019 typical values, requires O2/N2 ratio and optional transformer age

def ieee_2019_typical_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, o2_val, n2_val, trafo_age_val):
    ieee_2019_typical_results = []

    if (pd.isna(o2_val) == True) or (pd.isna(n2_val) == True):
        o2_n2_ratio = 1
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
            elif trafo_age_val > 10:
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
            elif trafo_age_val > 10:
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