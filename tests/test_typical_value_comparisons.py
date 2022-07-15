import numpy as np
from diagnostic import typical_value_comparison

# IEC typical value tests
def test_iec_typical_values_nan():
    assert typical_value_comparison.iec_typical_calculation(np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan) == ['-', '-', '-', '-', '-', '-', '-']

def test_iec_typical_values_all_exceeded_with_com_OLTC():
    assert typical_value_comparison.iec_typical_calculation(151, 131, 91, 281, 281, 601, 14001) == ['Typical values exceeded!', 'Typical values exceeded!', 'Typical values exceeded!', 'Typical values exceeded!', 'Communicating OLTC typical values exceeded!', 'Typical values exceeded!', 'Typical values exceeded!']

def test_iec_typical_values_all_exceeded_without_com_OLTC():
    assert typical_value_comparison.iec_typical_calculation(151, 131, 91, 281, 280, 601, 14001) == ['Typical values exceeded!', 'Typical values exceeded!', 'Typical values exceeded!', 'Typical values exceeded!', 'Typical values exceeded unless communicating OLTC!', 'Typical values exceeded!', 'Typical values exceeded!']

def test_iec_typical_values_all_normal():
    assert typical_value_comparison.iec_typical_calculation(10, 10, 10, 10, 10, 10, 10) == ['Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal']

def test_iec_typical_values_all_zero():
    assert typical_value_comparison.iec_typical_calculation(0, 0, 0, 0, 0, 0, 0) == ['Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal']


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

