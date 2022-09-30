# -*- coding: utf-8 -*-
"""roc_calculation.py

This module makes the calculations of rate-of-change (ROC) for gas readings.

@Author: https://github.com/ToniMellin
"""

import sys
import pathlib

import numpy as np
import pandas as pd

sys.path.insert(0, str(pathlib.Path(__file__).parent)) # path change to allow importing in upper level for diagnostic sub-modules


def round_half_up(n, decimals=0):
    """Function for rounding values up according to given decimal count, returns the rounded float value"""
    multiplier = 10 ** decimals
    return np.floor(n*multiplier + 0.5) / multiplier

#TODO add sequential ROC calculation
#TODO add linear fit ROC calculation option
def calculate_rates_of_change(df, time_name):
    df_sorted = df.sort_values(by=[time_name])

    # calculate from first to last point timedeltas
    first_to_last_timedelta = df_sorted[time_name][-1:].values[0] - df_sorted[time_name][:1].values[0]
    first_to_last_timedelta_in_years = (first_to_last_timedelta / np.timedelta64(365, 'D')).astype('float')
    first_to_last_timedelta_in_months = (first_to_last_timedelta / np.timedelta64(30, 'D')).astype('float')
    first_to_last_timedelta_in_weeks = (first_to_last_timedelta / np.timedelta64(7, 'D')).astype('float')
    first_to_last_timedelta_in_days = (first_to_last_timedelta / np.timedelta64(1, 'D')).astype('float')
    first_to_last_timedelta_in_hours = (first_to_last_timedelta / np.timedelta64(1, 'h')).astype('float')

    # calculate first to last rates of changes for the gases
    df_filtered = df_sorted.filter(['H2', 'CH4', 'C2H6', 'C2H4', 'C2H2', 'CO', 'CO2'])
    df_ftl_roc = df_filtered.iloc[len(df_filtered)-1] - df_filtered.iloc[0]

    df_ftl_roc_per_year = df_ftl_roc / first_to_last_timedelta_in_years
    df_ftl_roc_per_month = df_ftl_roc / first_to_last_timedelta_in_months
    df_ftl_roc_per_week = df_ftl_roc / first_to_last_timedelta_in_weeks
    df_ftl_roc_per_day = df_ftl_roc / first_to_last_timedelta_in_days
    df_ftl_roc_per_hour = df_ftl_roc / first_to_last_timedelta_in_hours

    # combine first to last rate of change results to a dataframe
    df_ftl_roc_summary_without_name = pd.concat([df_ftl_roc, df_ftl_roc_per_year, df_ftl_roc_per_month, df_ftl_roc_per_week, df_ftl_roc_per_day, df_ftl_roc_per_hour], axis=1).T
    df_ftl_roc_naming = pd.DataFrame({'Rate-of-Change category': ['ROC absolute', 'ROC per year', 'ROC per 30 days', 'ROC per 7 days', 'ROC per 1 day', 'ROC per 1 hour']})
    df_ftl_roc_summary = pd.concat([df_ftl_roc_naming, df_ftl_roc_summary_without_name], axis=1)

    # calculate last time periods rates of changes
    last_roc_title_list = []
    last_roc_summary_list = []

    if first_to_last_timedelta_in_years >= 1:
        roc_y_start_time = df_sorted[time_name][-1:].values[0] - np.timedelta64(365, 'D')
        df_y = df_sorted[df_sorted[time_name] >= roc_y_start_time]

        if len(df_y) >= 2: 
            y_timedelta = ((df_y[time_name][-1:].values[0] - df_y[time_name][:1].values[0]) / np.timedelta64(365, 'D')).astype('float')
            df_y_filtered = df_y.filter(['H2', 'CH4', 'C2H6', 'C2H4', 'C2H2', 'CO', 'CO2'])

            df_roc_y = (df_y_filtered.iloc[len(df_y) -1] - df_y_filtered.iloc[0]) / y_timedelta

            last_roc_summary_list.append(df_roc_y)
            last_roc_title_list.append('ROC last year')
            
    if first_to_last_timedelta_in_months >= 1:
        roc_m_start_time = df_sorted[time_name][-1:].values[0] - np.timedelta64(30, 'D')
        df_m = df_sorted[df_sorted[time_name] >= roc_m_start_time]

        if len(df_m) >= 2: 
            m_timedelta = ((df_m[time_name][-1:].values[0] - df_m[time_name][:1].values[0]) / np.timedelta64(30, 'D')).astype('float')
            df_m_filtered = df_m.filter(['H2', 'CH4', 'C2H6', 'C2H4', 'C2H2', 'CO', 'CO2'])

            df_roc_m = (df_m_filtered.iloc[len(df_m) -1] - df_m_filtered.iloc[0]) / m_timedelta

            last_roc_summary_list.append(df_roc_m)
            last_roc_title_list.append('ROC last 30 days')

    if first_to_last_timedelta_in_weeks >= 1:
        roc_w_start_time = df_sorted[time_name][-1:].values[0] - np.timedelta64(7, 'D')
        df_w = df_sorted[df_sorted[time_name] >= roc_w_start_time]

        if len(df_w) >= 2: 
            w_timedelta = ((df_w[time_name][-1:].values[0] - df_w[time_name][:1].values[0]) / np.timedelta64(7, 'D')).astype('float')
            df_w_filtered = df_w.filter(['H2', 'CH4', 'C2H6', 'C2H4', 'C2H2', 'CO', 'CO2'])

            df_roc_w = (df_w_filtered.iloc[len(df_w) -1] - df_w_filtered.iloc[0]) / w_timedelta

            last_roc_summary_list.append(df_roc_w)
            last_roc_title_list.append('ROC last 7 days')

    if first_to_last_timedelta_in_days >= 1:
        roc_d_start_time = df_sorted[time_name][-1:].values[0] - np.timedelta64(1, 'D')
        df_d = df_sorted[df_sorted[time_name] >= roc_d_start_time]

        if len(df_d) >= 2: 
            d_timedelta = ((df_d[time_name][-1:].values[0] - df_d[time_name][:1].values[0]) / np.timedelta64(1, 'D')).astype('float')
            df_d_filtered = df_d.filter(['H2', 'CH4', 'C2H6', 'C2H4', 'C2H2', 'CO', 'CO2'])

            df_roc_d = (df_d_filtered.iloc[len(df_d) -1] - df_d_filtered.iloc[0]) / d_timedelta

            last_roc_summary_list.append(df_roc_d)
            last_roc_title_list.append('ROC last 1 day')

    # combine last time periods rates of changes to summary dataframe
    df_last_roc_summary_without_name = pd.concat(last_roc_summary_list, axis=1).T
    df_last_roc_naming = pd.DataFrame({'Rate-of-Change category': last_roc_title_list})
    df_last_roc_summary = pd.concat([df_last_roc_naming, df_last_roc_summary_without_name], axis=1)

    return df_ftl_roc_summary, df_last_roc_summary

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
    
    ftl_roc, last_roc = calculate_rates_of_change(df_sample3, 'Timestamp')

    print(ftl_roc)
    print(last_roc)
