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
        
        # TDCG not included in IEC
        iec_typical_results.append('-')
    except Exception as e:
        print(f'IEC typical value comparison issue!!\n{e}')
        iec_typical_results = ['-', '-', '-', '-', '-', '-', '-', '-']

    return iec_typical_results

def ieee_2008_typical_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val):
    try:
        tdcg_val = h2_val + ch4_val + c2h6_val + c2h4_val + c2h2_val + co_val
    except:
        tdcg_val = 0

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
            ieee_typical_results.append('')
        elif co2_val > co2_typ1:
            ieee_typical_results.append('Typical values exceeded! / Condition 2')
        else:
            ieee_typical_results.append('Normal / Condition 1')

        if pd.isna(tdcg_val) is True:
            ieee_typical_results.append('')
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

    # 90th percentile typical values

def calculate_typical_results(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, o2_val, n2_val, trafo_age_val):
    typical_result_list = []
    
    try:
        iec_typical_list = iec_typical_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val)
        typical_result_list.append(iec_typical_list)

        ieee_2008_typical_list = ieee_2008_typical_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val)
        typical_result_list.append(ieee_2008_typical_list)
    except Exception as e:
        print(f'Typical value comparison issue!!\n{e}')

    return typical_result_list