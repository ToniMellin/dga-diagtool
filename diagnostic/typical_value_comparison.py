import numpy as np
import pandas as pd

def iec_typical_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val):
    """
    Checks given gas concentration values (ppm) againt IEC 60599 typical values and indicates if they are exceeded

    Parameters
    ----------
    h2_val : float
        hydrogen (H2) gas concentration in ppm
    ch4_val : float
        methane (CH4) gas concentration in ppm
    c2h6_val : float
        ethane (C2H6) gas concentration in ppm
    c2h4_val : float
        ethylene (C2H4) gas concentration in ppm
    c2h2_val : float
        acetylene (C2H2) gas concentration in ppm
    co_val : float
        carbon monoxide (CO) gas concentration in ppm
    co2_val : float
        carbon dioxide (CO2) gas concentration in ppm
    
    Returns
    -------
    list
        list of str values that are results from checking the gas concentrations against typical values if nothing is given or comparison impossible dashes '-' are returned
    """
    
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
            iec_typical_results.append('90% typical values exceeded!')
        else:
            iec_typical_results.append('Normal')

        if pd.isna(ch4_val) is True:
            iec_typical_results.append('-')
        elif ch4_val > ch4_typ:
            iec_typical_results.append('90% typical values exceeded!')
        else:
            iec_typical_results.append('Normal')

        if pd.isna(c2h6_val) is True:
            iec_typical_results.append('-')
        elif c2h6_val > c2h6_typ:
            iec_typical_results.append('90% typical values exceeded!')
        else:
            iec_typical_results.append('Normal')

        if pd.isna(c2h4_val) is True:
            iec_typical_results.append('-')
        elif c2h4_val > c2h4_typ:
            iec_typical_results.append('90% typical values exceeded!')
        else:
            iec_typical_results.append('Normal')

        if pd.isna(c2h2_val) is True:
            iec_typical_results.append('-')
        elif c2h2_val > c2h2_typ:
            if c2h2_val > c2h2_oltc_typ:
                iec_typical_results.append('Communicating OLTC 90% typical values exceeded!')
            else:
                iec_typical_results.append('90% typical values exceeded unless communicating OLTC!')
        else:
            iec_typical_results.append('Normal')

        if pd.isna(co_val) is True:
            iec_typical_results.append('-')
        elif co_val > co_typ:
            iec_typical_results.append('90% typical values exceeded!')
        else:
            iec_typical_results.append('Normal')

        if pd.isna(co2_val) is True:
            iec_typical_results.append('-')
        elif co2_val > co2_typ:
            iec_typical_results.append('90% typical values exceeded!')
        else:
            iec_typical_results.append('Normal')
        
    except Exception as e:
        print(f'IEC typical value comparison issue!!\n{e}')
        iec_typical_results = ['-', '-', '-', '-', '-', '-', '-']

    return iec_typical_results

def ieee_2008_typical_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val):
    """
    Checks given gas concentration values (ppm) againt IEEE C57.104-2008 typical values and indicates if they are exceeded

    Parameters
    ----------
    h2_val : float
        hydrogen (H2) gas concentration in ppm
    ch4_val : float
        methane (CH4) gas concentration in ppm
    c2h6_val : float
        ethane (C2H6) gas concentration in ppm
    c2h4_val : float
        ethylene (C2H4) gas concentration in ppm
    c2h2_val : float
        acetylene (C2H2) gas concentration in ppm
    co_val : float
        carbon monoxide (CO) gas concentration in ppm
    co2_val : float
        carbon dioxide (CO2) gas concentration in ppm
    
    Returns
    -------
    list
        list of str values that are results from checking the gas concentrations against typical values if nothing is given or comparison impossible dashes '-' are returned
    """

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

def ieee_2019_typical_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, o2_val, n2_val, trafo_age_val):
    """
    Checks given gas concentration values (ppm) againt IEEE C57.104-2019 typical values and indicates if they are exceeded

    Parameters
    ----------
    h2_val : float
        hydrogen (H2) gas concentration in ppm
    ch4_val : float
        methane (CH4) gas concentration in ppm
    c2h6_val : float
        ethane (C2H6) gas concentration in ppm
    c2h4_val : float
        ethylene (C2H4) gas concentration in ppm
    c2h2_val : float
        acetylene (C2H2) gas concentration in ppm
    co_val : float
        carbon monoxide (CO) gas concentration in ppm
    co2_val : float
        carbon dioxide (CO2) gas concentration in ppm
    o2_val : float
        oxygen (O2) gas concentration in ppm
    n2_val : float
        nitrogen (N2) gas concentration in ppm
    trafo_age_val : int
        transformer age in years

    Returns
    -------
    list
        list of str values that are results from checking the gas concentrations against typical values if nothing is given or comparison impossible dashes '-' are returned
    """
    
    ieee_2019_typical_results = []

    if (pd.isna(o2_val) == True) or (pd.isna(n2_val) == True):
        o2_n2_ratio = 1
    elif (o2_val == 0 or n2_val == 0) is True:
        o2_n2_ratio = 0
    else:
        o2_n2_ratio = o2_val/n2_val

    # 90th percentile typical values o2/n2 <= 0.2 (sealed)
    h2_typ_sealed_unknown = 80
    h2_typ_sealed_under_30 = 75
    h2_typ_sealed_over_30 = 100

    ch4_typ_sealed_unknown = 90
    ch4_typ_sealed_under_10 = 45
    ch4_typ_sealed_over_10 = 90
    ch4_typ_sealed_over_30 = 110

    c2h6_typ_sealed_unknown = 90
    c2h6_typ_sealed_under_10 = 30
    c2h6_typ_sealed_over_10 = 90
    c2h6_typ_sealed_over_30 = 150

    c2h4_typ_sealed_unknown = 50
    c2h4_typ_sealed_under_10 = 20
    c2h4_typ_sealed_over_10 = 50
    c2h4_typ_sealed_over_30 = 90

    c2h2_typ_sealed = 1
    
    co_typ_sealed = 900

    co2_typ_sealed_unknown = 9000
    co2_typ_sealed_under_10 = 5000
    co2_typ_sealed_over_10 = 10000    

    # 90th percentile typical values o2/n2 > 0.2 (open / free-breathing)
    h2_typ_open = 40

    ch4_typ_open = 20

    c2h6_typ_open = 15

    c2h4_typ_open_unknown = 50
    c2h4_typ_open_under_10 = 25
    c2h4_typ_open_over_10 = 60

    c2h2_typ_open = 2
    
    co_typ_open = 500

    co2_typ_open_unknown = 5000
    co2_typ_open_under_10 = 3500
    co2_typ_open_over_10 = 5500

    # 95th percentile typical values o2/n2 <= 0.2 (sealed)
    h2_typ95_sealed = 200

    ch4_typ95_sealed_unknown = 150
    ch4_typ95_sealed_under_10 = 100
    ch4_typ95_sealed_over_10 = 150
    ch4_typ95_sealed_over_30 = 200

    c2h6_typ95_sealed_unknown = 175 
    c2h6_typ95_sealed_under_10 = 70
    c2h6_typ95_sealed_over_10 = 175
    c2h6_typ95_sealed_over_30 = 250

    c2h4_typ95_sealed_unknown = 100
    c2h4_typ95_sealed_under_10 = 40
    c2h4_typ95_sealed_over_10 = 95
    c2h4_typ95_sealed_over_30 = 175

    c2h2_typ95_sealed = 2
    c2h2_typ95_sealed_over_30 = 4

    co_typ95_sealed = 1100

    co2_typ95_sealed_unknown = 12500
    co2_typ95_sealed_under_10 = 7000
    co2_typ95_sealed_over_10 = 14000

    # 95th percentile typical values o2/n2 > 0.2 (open / free-breathing)
    h2_typ95_open = 90

    ch4_typ95_open_unknown = 50
    ch4_typ95_open_under_30 = 60
    ch4_typ95_open_over_30 = 30

    c2h6_typ95_open_unknown = 40
    c2h6_typ95_open_under_10 = 30
    c2h6_typ95_open_over_10 = 40

    c2h4_typ95_open_unknown = 100
    c2h4_typ95_open_under_10 = 80
    c2h4_typ95_open_over_10 = 125

    c2h2_typ95_open = 7

    co_typ95_open = 600

    co2_typ95_open_unknown = 7000
    co2_typ95_open_under_10 = 5000
    co2_typ95_open_over_10 = 8000

    try:
        # Sealed transformer tank, o2/n2 <= 0.2
        if o2_n2_ratio <= 0.2:
            if pd.isna(h2_val) is True:
                ieee_2019_typical_results.append('-')
            elif pd.isna(trafo_age_val) is True:
                if h2_val > h2_typ95_sealed:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif h2_val > h2_typ_sealed_unknown:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val <= 30:
                if h2_val > h2_typ95_sealed:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif h2_val > h2_typ_sealed_under_30:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val > 30:
                if h2_val > h2_typ95_sealed:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif h2_val > h2_typ_sealed_over_30:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')

            if pd.isna(ch4_val) is True:
                ieee_2019_typical_results.append('-')
            elif pd.isna(trafo_age_val) is True:
                if ch4_val > ch4_typ95_sealed_unknown:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif ch4_val > ch4_typ_sealed_unknown:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val < 10:
                if ch4_val > ch4_typ95_sealed_under_10:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif ch4_val > ch4_typ_sealed_under_10:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif (trafo_age_val >= 10) and (trafo_age_val <= 30):
                if ch4_val > ch4_typ95_sealed_over_10:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif ch4_val > ch4_typ_sealed_over_10:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val > 30:
                if ch4_val > ch4_typ95_sealed_over_30:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif ch4_val > ch4_typ_sealed_over_30:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')

            if pd.isna(c2h6_val) is True:
                ieee_2019_typical_results.append('-')
            elif pd.isna(trafo_age_val) is True:
                if c2h6_val > c2h6_typ95_sealed_unknown:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif c2h6_val > c2h6_typ_sealed_unknown:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val < 10:
                if c2h6_val > c2h6_typ95_sealed_under_10:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif c2h6_val > c2h6_typ_sealed_under_10:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif (trafo_age_val >= 10) and (trafo_age_val <= 30):
                if c2h6_val > c2h6_typ95_sealed_over_10:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif c2h6_val > c2h6_typ_sealed_over_10:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val > 30:
                if c2h6_val > c2h6_typ95_sealed_over_30:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif c2h6_val > c2h6_typ_sealed_over_30:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')

            if pd.isna(c2h4_val) is True:
                ieee_2019_typical_results.append('-')
            elif pd.isna(trafo_age_val) is True:
                if c2h4_val > c2h4_typ95_sealed_unknown:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif c2h4_val > c2h4_typ_sealed_unknown:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val < 10:
                if c2h4_val > c2h4_typ95_sealed_under_10:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif c2h4_val > c2h4_typ_sealed_under_10:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif (trafo_age_val >= 10) and (trafo_age_val <= 30):
                if c2h4_val > c2h4_typ95_sealed_over_10:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif c2h4_val > c2h4_typ_sealed_over_10:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val > 30:
                if c2h4_val > c2h4_typ95_sealed_over_30:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif c2h4_val > c2h4_typ_sealed_over_30:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')

            if pd.isna(c2h2_val) is True:
                ieee_2019_typical_results.append('-')
            elif pd.isna(trafo_age_val) is True:
                if c2h2_val > c2h2_typ95_sealed:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif c2h2_val > c2h2_typ_sealed:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val <= 30:
                if c2h2_val > c2h2_typ95_sealed:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif c2h2_val > c2h2_typ_sealed:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val > 30:
                if c2h2_val > c2h2_typ95_sealed_over_30:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif c2h2_val > c2h2_typ_sealed:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            
            if pd.isna(co_val) is True:
                ieee_2019_typical_results.append('-')
            else:
                if co_val > co_typ95_sealed:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif co_val > co_typ_sealed:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')

            if pd.isna(co2_val) is True:
                ieee_2019_typical_results.append('-')
            elif pd.isna(trafo_age_val) is True:
                if co2_val > co2_typ95_sealed_unknown:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif co2_val > co2_typ_sealed_unknown:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val < 10:
                if co2_val > co2_typ95_sealed_under_10:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif co2_val > co2_typ_sealed_under_10:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val >= 10:
                if co2_val > co2_typ95_sealed_over_10:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif co2_val > co2_typ_sealed_over_10:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')

        # Open / free-breathing transformer tank, o2/n2 > 0.2
        else:
            if pd.isna(h2_val) is True:
                ieee_2019_typical_results.append('-')
            else:
                if h2_val > h2_typ95_open:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif h2_val > h2_typ_open:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')

            if pd.isna(ch4_val) is True:
                ieee_2019_typical_results.append('-')
            elif pd.isna(trafo_age_val) is True:
                if ch4_val > ch4_typ95_open_unknown:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif ch4_val > ch4_typ_open:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val <= 30:
                if ch4_val > ch4_typ95_open_under_30:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif ch4_val > ch4_typ_open:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val > 30:
                if ch4_val > ch4_typ95_open_over_30:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif ch4_val > ch4_typ_open:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')

            if pd.isna(c2h6_val) is True:
                ieee_2019_typical_results.append('-')
            elif pd.isna(trafo_age_val) is True:
                if c2h6_val > c2h6_typ95_open_unknown:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif c2h6_val > c2h6_typ_open:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val < 10:
                if c2h6_val > c2h6_typ95_open_under_10:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif c2h6_val > c2h6_typ_open:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val >= 10:
                if c2h6_val > c2h6_typ95_open_over_10:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif c2h6_val > c2h6_typ_open:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            
            if pd.isna(c2h4_val) is True:
                ieee_2019_typical_results.append('-')
            elif pd.isna(trafo_age_val) is True:
                if c2h4_val > c2h4_typ95_open_unknown:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif c2h4_val > c2h4_typ_open_unknown:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val < 10:
                if c2h4_val > c2h4_typ95_open_under_10:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif c2h4_val > c2h4_typ_open_under_10:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val >= 10:
                if c2h4_val > c2h4_typ95_open_over_10:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif c2h4_val > c2h4_typ_open_over_10:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')

            if pd.isna(c2h2_val) is True:
                ieee_2019_typical_results.append('-')
            else:
                if c2h2_val > c2h2_typ95_open:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif c2h2_val > c2h2_typ_open:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')

            if pd.isna(co_val) is True:
                ieee_2019_typical_results.append('-')
            else:
                if co_val > co_typ95_open:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif co_val > co_typ_open:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')

            if pd.isna(co2_val) is True:
                ieee_2019_typical_results.append('-')
            elif pd.isna(trafo_age_val) is True:
                if co2_val > co2_typ95_open_unknown:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif co2_val > co2_typ_open_unknown:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val < 10:
                if co2_val > co2_typ95_open_under_10:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif co2_val > co2_typ_open_under_10:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')
            elif trafo_age_val >= 10:
                if co2_val > co2_typ95_open_over_10:
                    ieee_2019_typical_results.append('95% typical values exceeded!')
                elif co2_val > co2_typ_open_over_10:
                    ieee_2019_typical_results.append('90% typical values exceeded!')
                else:
                    ieee_2019_typical_results.append('Normal')

    except Exception as e:
        print(f'IEEE-2019 typical value comparison issue!!\n{e}')
        ieee_2019_typical_results = ['-', '-', '-', '-', '-', '-', '-']

    return ieee_2019_typical_results
    

def calculate_typical_results(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, o2_val, n2_val, trafo_age_val):
    """
    Combines the multiple checks of given gas concentration values (ppm) againt different standards typical values and indicates if they are exceeded

    Parameters
    ----------
    h2_val : float
        hydrogen (H2) gas concentration in ppm
    ch4_val : float
        methane (CH4) gas concentration in ppm
    c2h6_val : float
        ethane (C2H6) gas concentration in ppm
    c2h4_val : float
        ethylene (C2H4) gas concentration in ppm
    c2h2_val : float
        acetylene (C2H2) gas concentration in ppm
    co_val : float
        carbon monoxide (CO) gas concentration in ppm
    co2_val : float
        carbon dioxide (CO2) gas concentration in ppm
    o2_val : float
        oxygen (O2) gas concentration in ppm
    n2_val : float
        nitrogen (N2) gas concentration in ppm
    trafo_age_val : int
        transformer age in years

    Returns
    -------
    list
        nested list of str values that combines results from checking the gas concentrations against different standards typical values if nothing is given or comparison impossible dashes '-' are returned
    """
    
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
    #ieee2008_list = ieee_2008_typical_calculation(109.99, 120.99, 65.99, 50.99, 1.99, 350.99, 2500)
    #print(ieee2008_list, len(ieee2008_list))

    ieee2019_0_list = ieee_2019_typical_calculation(40, 20, 15, 50, 2, 500, 5000, 21000, 56000, np.nan)
    print(ieee2019_0_list, len(ieee2019_0_list))
