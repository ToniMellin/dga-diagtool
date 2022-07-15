import numpy as np
from diagnostic import typical_value_comparison

# IEC typical value tests
def test_iec_typical_values_nan():
    assert typical_value_comparison.iec_typical_calculation(np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan) == ['-', '-', '-', '-', '-', '-', '-']

def test_iec_typical_values_all_zero():
    assert typical_value_comparison.iec_typical_calculation(0, 0, 0, 0, 0, 0, 0) == ['Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal']

def test_iec_typical_values_all_exceeded_with_com_OLTC():
    assert typical_value_comparison.iec_typical_calculation(151, 131, 91, 281, 281, 601, 14001) == ['90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', 'Communicating OLTC 90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!']

def test_iec_typical_values_all_exceeded_without_com_OLTC():
    assert typical_value_comparison.iec_typical_calculation(151, 131, 91, 281, 280, 601, 14001) == ['90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded unless communicating OLTC!', '90% typical values exceeded!', '90% typical values exceeded!']

def test_iec_typical_values_all_normal():
    assert typical_value_comparison.iec_typical_calculation(10, 10, 10, 10, 10, 10, 10) == ['Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal']


# IEEE 2008 typical value tests
def test_ieee_2008_typical_values_all_nan():
    assert typical_value_comparison.ieee_2008_typical_calculation(np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan) == ['-', '-', '-', '-', '-', '-', '-', '-']

def test_ieee_2008_typical_values_all_zero():
    assert typical_value_comparison.ieee_2008_typical_calculation(0, 0, 0, 0, 0, 0, 0) == ['Normal / Condition 1', 'Normal / Condition 1', 'Normal / Condition 1', 'Normal / Condition 1', 'Normal / Condition 1', 'Normal / Condition 1', 'Normal / Condition 1', 'Normal / Condition 1']

def test_ieee_2008_typical_values_normal_half():
    assert typical_value_comparison.ieee_2008_typical_calculation(50, 60, 33, 25, 1, 175, 1250) == ['Normal / Condition 1', 'Normal / Condition 1', 'Normal / Condition 1', 'Normal / Condition 1', 'Normal / Condition 1', 'Normal / Condition 1', 'Normal / Condition 1', 'Normal / Condition 1']

def test_ieee_2008_typical_values_normal_under_breakpoint():
    assert typical_value_comparison.ieee_2008_typical_calculation(100.99, 120.99, 65.99, 50.99, 1.99, 350.99, 2500) == ['Normal / Condition 1', 'Normal / Condition 1', 'Normal / Condition 1', 'Normal / Condition 1', 'Normal / Condition 1', 'Normal / Condition 1', 'Normal / Condition 1', 'Normal / Condition 1']

def test_ieee_2008_typical_values_condition2_low_breakpoint():
    assert typical_value_comparison.ieee_2008_typical_calculation(101, 121, 66, 51, 2, 351, 2500.01) == ['Typical values exceeded! / Condition 2', 'Typical values exceeded! / Condition 2', 'Typical values exceeded! / Condition 2', 'Typical values exceeded! / Condition 2', 'Typical values exceeded! / Condition 2', 'Typical values exceeded! / Condition 2', 'Typical values exceeded! / Condition 2', 'Normal / Condition 1']

def test_ieee_2008_typical_values_condition2_low_breakpoint_with_TDCG():
    assert typical_value_comparison.ieee_2008_typical_calculation(130, 121, 66, 51, 2, 351, 2500.01) == ['Typical values exceeded! / Condition 2', 'Typical values exceeded! / Condition 2', 'Typical values exceeded! / Condition 2', 'Typical values exceeded! / Condition 2', 'Typical values exceeded! / Condition 2', 'Typical values exceeded! / Condition 2', 'Typical values exceeded! / Condition 2', 'Typical values exceeded! / Condition 2']

def test_ieee_2008_typical_values_condition2_high_breakpoint():
    assert typical_value_comparison.ieee_2008_typical_calculation(700.99, 400.99, 100.99, 100.99, 9.99, 570.99, 4000.99) == ['Typical values exceeded! / Condition 2', 'Typical values exceeded! / Condition 2', 'Typical values exceeded! / Condition 2', 'Typical values exceeded! / Condition 2', 'Typical values exceeded! / Condition 2', 'Typical values exceeded! / Condition 2', 'Typical values exceeded! / Condition 2', 'Typical values exceeded! / Condition 2']

def test_ieee_2008_typical_values_condition3_low_breakpoint():
    assert typical_value_comparison.ieee_2008_typical_calculation(701, 401, 101, 101, 10, 571, 4001) == ['Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 2']

def test_ieee_2008_typical_values_condition3_low_breakpoint_with_TDCG():
    assert typical_value_comparison.ieee_2008_typical_calculation(701, 437, 101, 101, 10, 571, 4001) == ['Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3']

def test_ieee_2008_typical_values_condition3_high_breakpoint():
    assert typical_value_comparison.ieee_2008_typical_calculation(1800, 1000, 150, 200, 35, 1400, 10000) == ['Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3']

def test_ieee_2008_typical_values_condition3_high_breakpoint():
    assert typical_value_comparison.ieee_2008_typical_calculation(1800, 1000, 150, 200, 35, 1400, 10000) == ['Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 3']

def test_ieee_2008_typical_values_condition4_low_breakpoint():
    assert typical_value_comparison.ieee_2008_typical_calculation(1800.01, 1000.01, 150.01, 200.01, 35.01, 1400.01, 10000.01) == ['Typical values exceeded! / Condition 4', 'Typical values exceeded! / Condition 4', 'Typical values exceeded! / Condition 4', 'Typical values exceeded! / Condition 4', 'Typical values exceeded! / Condition 4', 'Typical values exceeded! / Condition 4', 'Typical values exceeded! / Condition 4', 'Typical values exceeded! / Condition 3']

def test_ieee_2008_typical_values_inverted_pyramid():
    assert typical_value_comparison.ieee_2008_typical_calculation(4000, 800, 78, 20.55, 5.4, 1200, 20000) == ['Typical values exceeded! / Condition 4', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 2', 'Normal / Condition 1', 'Typical values exceeded! / Condition 2', 'Typical values exceeded! / Condition 3', 'Typical values exceeded! / Condition 4', 'Typical values exceeded! / Condition 4']


# TODO add more IEEE 2019 tests
# IEEE 2019 typical value tests
def test_ieee_2019_typical_values_all_zero():
    assert typical_value_comparison.ieee_2019_typical_calculation(0, 0, 0, 0, 0, 0, 0, 0, 0, 0) == ['Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal']

def test_ieee_2019_typical_values_all_nan():
    assert typical_value_comparison.ieee_2019_typical_calculation(np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan) == ['-', '-', '-', '-', '-', '-', '-']


def test_ieee_2019_typical_values_90_under_breakpoint_sealed_age_unknown():
    assert typical_value_comparison.ieee_2019_typical_calculation(80, 90, 90, 50, 1, 900, 9000, 5000, 56000, np.nan) == ['Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal']

def test_ieee_2019_typical_values_90_under_breakpoint_sealed_age_9():
    assert typical_value_comparison.ieee_2019_typical_calculation(75, 45, 30, 20, 1, 900, 5000, 5000, 56000, 9.99) == ['Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal']

def test_ieee_2019_typical_values_90_under_breakpoint_sealed_age_10():
    assert typical_value_comparison.ieee_2019_typical_calculation(75, 90, 90, 50, 1, 900, 10000, 5000, 56000, 10) == ['Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal']

def test_ieee_2019_typical_values_90_under_breakpoint_sealed_age_30():
    assert typical_value_comparison.ieee_2019_typical_calculation(75, 90, 90, 50, 1, 900, 10000, 5000, 56000, 30) == ['Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal']

def test_ieee_2019_typical_values_90_under_breakpoint_sealed_age_40():
    assert typical_value_comparison.ieee_2019_typical_calculation(100, 110, 150, 90, 1, 900, 10000, 5000, 56000, 40) == ['Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal']


def test_ieee_2019_typical_values_90_over_breakpoint_sealed_age_unknown():
    assert typical_value_comparison.ieee_2019_typical_calculation(81, 91, 91, 51, 2, 901, 9001, 5000, 56000, np.nan) == ['90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!']

def test_ieee_2019_typical_values_90_over_breakpoint_sealed_age_9():
    assert typical_value_comparison.ieee_2019_typical_calculation(76, 46, 31, 21, 2, 901, 5001, 5000, 56000, 9.99) == ['90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!']

def test_ieee_2019_typical_values_90_over_breakpoint_sealed_age_10():
    assert typical_value_comparison.ieee_2019_typical_calculation(76, 91, 91, 51, 2, 901, 10001, 5000, 56000, 10) == ['90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!']

def test_ieee_2019_typical_values_90_over_breakpoint_sealed_age_30():
    assert typical_value_comparison.ieee_2019_typical_calculation(76, 91, 91, 51, 2, 901, 10001, 5000, 56000, 30) == ['90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!']

def test_ieee_2019_typical_values_90_over_breakpoint_sealed_age_40():
    assert typical_value_comparison.ieee_2019_typical_calculation(101, 111, 151, 91, 2, 901, 10001, 5000, 56000, 40) == ['90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!']


def test_ieee_2019_typical_values_95_over_breakpoint_sealed_age_unknown():
    assert typical_value_comparison.ieee_2019_typical_calculation(201, 151, 176, 101, 3, 1101, 12501, 5000, 56000, np.nan) == ['95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!']

def test_ieee_2019_typical_values_95_over_breakpoint_sealed_age_9():
    assert typical_value_comparison.ieee_2019_typical_calculation(201, 101, 71, 41, 3, 1101, 7001, 5000, 56000, 9.99) == ['95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!']

def test_ieee_2019_typical_values_95_over_breakpoint_sealed_age_10():
    assert typical_value_comparison.ieee_2019_typical_calculation(201, 151, 176, 96, 3, 1101, 14001, 5000, 56000, 10) == ['95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!']

def test_ieee_2019_typical_values_95_over_breakpoint_sealed_age_30():
    assert typical_value_comparison.ieee_2019_typical_calculation(201, 151, 176, 96, 3, 1101, 14001, 5000, 56000, 30) == ['95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!']

def test_ieee_2019_typical_values_95_over_breakpoint_sealed_age_40():
    assert typical_value_comparison.ieee_2019_typical_calculation(201, 201, 251, 176, 5, 1101, 14001, 5000, 56000, 40) == ['95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!']


def test_ieee_2019_typical_values_90_under_breakpoint_open_age_unknown():
    assert typical_value_comparison.ieee_2019_typical_calculation(40, 20, 15, 50, 2, 500, 5000, 21000, 56000, np.nan) == ['Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal']

def test_ieee_2019_typical_values_90_under_breakpoint_open_age_9():
    assert typical_value_comparison.ieee_2019_typical_calculation(40, 20, 15, 25, 2, 500, 3500, 21000, 56000, 9.99) == ['Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal']

def test_ieee_2019_typical_values_90_under_breakpoint_open_age_10():
    assert typical_value_comparison.ieee_2019_typical_calculation(40, 20, 15, 60, 2, 500, 5500, 21000, 56000, 10) == ['Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal']

def test_ieee_2019_typical_values_90_under_breakpoint_open_age_30():
    assert typical_value_comparison.ieee_2019_typical_calculation(40, 20, 15, 60, 2, 500, 5500, 21000, 56000, 30) == ['Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal']

def test_ieee_2019_typical_values_90_under_breakpoint_open_age_40():
    assert typical_value_comparison.ieee_2019_typical_calculation(40, 20, 15, 60, 2, 500, 5500, 21000, 56000, 40) == ['Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal']


def test_ieee_2019_typical_values_90_over_breakpoint_open_age_unknown():
    assert typical_value_comparison.ieee_2019_typical_calculation(41, 21, 16, 51, 3, 501, 5001, 21000, 56000, np.nan) == ['90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!']

def test_ieee_2019_typical_values_90_over_breakpoint_open_age_9():
    assert typical_value_comparison.ieee_2019_typical_calculation(41, 21, 16, 26, 3, 501, 3501, 21000, 56000, 9.99) == ['90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!']

def test_ieee_2019_typical_values_90_over_breakpoint_open_age_10():
    assert typical_value_comparison.ieee_2019_typical_calculation(41, 21, 16, 61, 3, 501, 5501, 21000, 56000, 10) == ['90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!']

def test_ieee_2019_typical_values_90_over_breakpoint_open_age_30():
    assert typical_value_comparison.ieee_2019_typical_calculation(41, 21, 16, 61, 3, 501, 5501, 21000, 56000, 30) == ['90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!']

def test_ieee_2019_typical_values_90_over_breakpoint_open_age_40():
    assert typical_value_comparison.ieee_2019_typical_calculation(41, 21, 16, 61, 3, 501, 5501, 21000, 56000, 40) == ['90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!', '90% typical values exceeded!']


def test_ieee_2019_typical_values_95_over_breakpoint_open_age_unknown():
    assert typical_value_comparison.ieee_2019_typical_calculation(91, 51, 41, 101, 8, 601, 7001, 21000, 56000, np.nan) == ['95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!']

def test_ieee_2019_typical_values_95_over_breakpoint_open_age_9():
    assert typical_value_comparison.ieee_2019_typical_calculation(91, 61, 31, 81, 8, 601, 5001, 21000, 56000, 9.99) == ['95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!']

def test_ieee_2019_typical_values_95_over_breakpoint_open_age_10():
    assert typical_value_comparison.ieee_2019_typical_calculation(91, 61, 41, 126, 8, 601, 8001, 21000, 56000, 10) == ['95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!']

def test_ieee_2019_typical_values_95_over_breakpoint_open_age_30():
    assert typical_value_comparison.ieee_2019_typical_calculation(91, 61, 41, 126, 8, 601, 8001, 21000, 56000, 30) == ['95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!']

def test_ieee_2019_typical_values_95_over_breakpoint_open_age_40():
    assert typical_value_comparison.ieee_2019_typical_calculation(91, 31, 41, 126, 8, 601, 8001, 21000, 56000, 40) == ['95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!', '95% typical values exceeded!']
