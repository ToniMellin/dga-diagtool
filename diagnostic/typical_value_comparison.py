# -*- coding: utf-8 -*-
"""typical_value_comparison.py

This module makes the comparisons againts typical gas values and returns the results based on defined standards.

@Author: https://github.com/ToniMellin
"""

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

def cigre_771_typical_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val):
    """
    Checks given gas concentration values (ppm) againt Cigre Technical Brochure 771 typical values and indicates if they are exceeded

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
    #Cigre TB 771 C.5.2 typical values
    #TODO include the option of comparing with table F1 using oxygen/nitrogen ratio based typical values
    h2_typ = 118
    h2_int1 = 200
    h2_int2 = 280
    h2_pf = 725

    ch4_typ = 85
    ch4_int1 = 135
    ch4_int2 = 180
    ch4_pf = 400

    c2h6_typ = 111
    c2h6_int1 = 210
    c2h6_int2 = 300
    c2h6_pf = 900

    c2h4_typ = 56
    c2h4_int1 = 120
    c2h4_int2 = 200
    c2h4_pf = 800

    c2h2_typ = 5
    c2h2_int1 = 19
    c2h2_int2 = 40
    c2h2_pf = 450

    co_typ = 700
    co_int1 = 970
    co_int2 = 1180
    co_pf = 2100

    co2_typ = 6300
    co2_int1 = 11600
    co2_int2 = 16700
    co2_pf = 50000


    cigre_771_typical_results = []
    #TODO add Cigre TB 771 based typical value comparison

    try:
        if pd.isna(h2_val) is True:
            cigre_771_typical_results.append('-')
        elif h2_val > h2_pf:
            cigre_771_typical_results.append('Typical values and pre-failure levels exceeded!')
        elif h2_val > h2_int2:
            cigre_771_typical_results.append('Typical values and intermediate 2 levels exceeded!')
        elif h2_val > h2_int1:
            cigre_771_typical_results.append('Typical values and intermediate 1 levels exceeded!')
        elif h2_val > h2_typ:
            cigre_771_typical_results.append('Typical values exceeded!')
        else:
            cigre_771_typical_results.append('Normal')

        if pd.isna(ch4_val) is True:
            cigre_771_typical_results.append('-')
        elif ch4_val > ch4_pf:
            cigre_771_typical_results.append('Typical values and pre-failure levels exceeded!')
        elif ch4_val > ch4_int2:
            cigre_771_typical_results.append('Typical values and intermediate 2 levels exceeded!')
        elif ch4_val > ch4_int1:
            cigre_771_typical_results.append('Typical values and intermediate 1 levels exceeded!')
        elif ch4_val > ch4_typ:
            cigre_771_typical_results.append('Typical values exceeded!')
        else:
            cigre_771_typical_results.append('Normal')

        if pd.isna(c2h6_val) is True:
            cigre_771_typical_results.append('-')
        elif c2h6_val > c2h6_pf:
            cigre_771_typical_results.append('Typical values and pre-failure levels exceeded!')
        elif c2h6_val > c2h6_int2:
            cigre_771_typical_results.append('Typical values and intermediate 2 levels exceeded!')
        elif c2h6_val > c2h6_int1:
            cigre_771_typical_results.append('Typical values and intermediate 1 levels exceeded!')
        elif c2h6_val > c2h6_typ:
            cigre_771_typical_results.append('Typical values exceeded!')
        else:
            cigre_771_typical_results.append('Normal')

        if pd.isna(c2h4_val) is True:
            cigre_771_typical_results.append('-')
        elif c2h4_val > c2h4_pf:
            cigre_771_typical_results.append('Typical values and pre-failure levels exceeded!')
        elif c2h4_val > c2h4_int2:
            cigre_771_typical_results.append('Typical values and intermediate 2 levels exceeded!')
        elif c2h4_val > c2h4_int1:
            cigre_771_typical_results.append('Typical values and intermediate 1 levels exceeded!')
        elif c2h4_val > c2h4_typ:
            cigre_771_typical_results.append('Typical values exceeded!')
        else:
            cigre_771_typical_results.append('Normal')

        if pd.isna(c2h2_val) is True:
            cigre_771_typical_results.append('-')
        elif c2h2_val > c2h2_pf:
            cigre_771_typical_results.append('Typical values and pre-failure levels exceeded!')
        elif c2h2_val > c2h2_int2:
            cigre_771_typical_results.append('Typical values and intermediate 2 levels exceeded!')
        elif c2h2_val > c2h2_int1:
            cigre_771_typical_results.append('Typical values and intermediate 1 levels exceeded!')
        elif c2h2_val > c2h2_typ:
            cigre_771_typical_results.append('Typical values exceeded!')
        else:
            cigre_771_typical_results.append('Normal')

        if pd.isna(co_val) is True:
            cigre_771_typical_results.append('-')
        elif co_val > co_pf:
            cigre_771_typical_results.append('Typical values and pre-failure levels exceeded!')
        elif co_val > co_int2:
            cigre_771_typical_results.append('Typical values and intermediate 2 levels exceeded!')
        elif co_val > co_int1:
            cigre_771_typical_results.append('Typical values and intermediate 1 levels exceeded!')
        elif co_val > co_int1:
            cigre_771_typical_results.append('Typical values exceeded!')
        else:
            cigre_771_typical_results.append('Normal')

        if pd.isna(co2_val) is True:
            cigre_771_typical_results.append('-')
        elif co2_val > co2_pf:
            cigre_771_typical_results.append('Typical values and pre-failure levels exceeded!')
        elif co2_val > co2_int2:
            cigre_771_typical_results.append('Typical values and intermediate 2 levels exceeded!')
        elif co2_val > co2_int1:
            cigre_771_typical_results.append('Typical values and intermediate 1 levels exceeded!')
        elif co2_val > co2_int1:
            cigre_771_typical_results.append('Typical values exceeded!')
        else:
            cigre_771_typical_results.append('Normal')
        
    except Exception as e:
        print(f'Cigre TB 771 typical values comparison issue!!\n{e}')
        cigre_771_typical_results = ['-', '-', '-', '-', '-', '-', '-']

    return cigre_771_typical_results


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

        #ieee_2008_typical_list = ieee_2008_typical_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val)
        #typical_result_list.append(ieee_2008_typical_list)

        ieee_2019_typical_list = ieee_2019_typical_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val, o2_val, n2_val, trafo_age_val)
        typical_result_list.append(ieee_2019_typical_list)

        cigre_tb771_typical_list = cigre_771_typical_calculation(h2_val, ch4_val, c2h6_val, c2h4_val, c2h2_val, co_val, co2_val)
        typical_result_list.append(cigre_tb771_typical_list)

    except Exception as e:
        print(f'Typical value comparison issue!!\n{e}')

    return typical_result_list

def typical_value_combined_result_check(results_list):
    unique = list(dict.fromkeys(results_list))

    if len(unique) == 0 or unique == ['-']:
        return '-'
    if len(unique) == 1 and unique == ['Normal']:
        return 'Normal'
    if unique == ['-', 'Normal'] or unique == ['Normal', '-']:
        return 'Normal / -'
    if any('exceeded' in s for s in unique):
        return 'Typical values exceeded!'

def combine_typical_results_to_dataframe(input_df):

    gas_names_list = ['h2', 'ch4', 'c2h6', 'c2h4', 'c2h2', 'co', 'co2']
    combined_col = ['Timestamp', 'IEC typical values', 'IEEE typical values', 'Cigre typical values']

    iec_col = ['Timestamp']
    iec_col.extend([f'iec_typ_{gas}' for gas in gas_names_list])

    ieee_col = ['Timestamp']
    ieee_col.extend([f'ieee_typ_{gas}' for gas in gas_names_list])

    cigre_col = ['Timestamp']
    cigre_col.extend([f'cigre_typ_{gas}' for gas in gas_names_list])

    df_combined = pd.DataFrame(columns=combined_col)
    df_iec = pd.DataFrame(columns=iec_col)
    df_ieee = pd.DataFrame(columns=ieee_col)
    df_cigre = pd.DataFrame(columns=cigre_col)


    for row in input_df.itertuples():
        results = calculate_typical_results(row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])

        df_combined_new = pd.DataFrame([[row[1], typical_value_combined_result_check(results[0]), typical_value_combined_result_check(results[1]), typical_value_combined_result_check(results[2])]], columns=combined_col)
        df_combined = pd.concat([df_combined, df_combined_new], ignore_index=True)

        df_iec_new = pd.DataFrame([[row[1], results[0][0], results[0][1], results[0][2], results[0][3], results[0][4], results[0][5], results[0][6]]], columns=iec_col)
        df_iec = pd.concat([df_iec, df_iec_new], ignore_index=True)
        
        df_ieee_new = pd.DataFrame([[row[1], results[1][0], results[1][1], results[1][2], results[1][3], results[1][4], results[1][5], results[1][6]]], columns=ieee_col)
        df_ieee = pd.concat([df_ieee, df_ieee_new], ignore_index=True)
        
        df_cigre_new = pd.DataFrame([[row[1], results[2][0], results[2][1], results[2][2], results[2][3], results[2][4], results[2][5], results[2][6]]], columns=cigre_col)
        df_cigre = pd.concat([df_cigre, df_cigre_new], ignore_index=True)

    df_typical_matrix = df_combined.merge(df_iec, how='inner').merge(df_ieee, how='inner').merge(df_cigre, how='inner')
    
    return df_typical_matrix

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

    df_combined = combine_typical_results_to_dataframe(df_sample3)
    print(df_combined)
    
