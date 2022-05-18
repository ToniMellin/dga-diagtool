from diagnostic import diagnostic_calculation
from diagnostic import duval_triangle_1
from diagnostic import duval_triangle_4
from diagnostic import duval_triangle_5
import numpy as np

# ratio tests
# TODO add more ratios
def test_ratio_calculation_nan():
    assert diagnostic_calculation.calculate_ratios(np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan) == [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]

def test_ratio_calculation_even_set():
    assert diagnostic_calculation.calculate_ratios(20, 40, 10, 10, 20, 50, 500, 40000, 80000) == [2, 2, 1, 0.5, 1, 10, 0.5]

# IEC ratio tests
# TODO add tests for all cases and edge events
def test_iec_ratio_nan():
    assert diagnostic_calculation.iec_ratio_calculation(np.nan, np.nan, np.nan) == 'N/A'

# Duval triangle 1 tests
def test_duval_1_result_calculation_DT_T3_edge_1():
    assert duval_triangle_1.calculate_duval_1_result(35, 15, 50) == 'T3'

def test_duval_1_result_calculation_T2_T3_edge_1():
    assert duval_triangle_1.calculate_duval_1_result(48, 2, 50) == 'T3'

def test_duval_1_result_calculation_DT_T2_T3_cross():
    assert duval_triangle_1.calculate_duval_1_result(46, 4, 50) == 'T3'

def test_duval_1_result_calculation_DT_T1_T2_cross():
    assert duval_triangle_1.calculate_duval_1_result(76, 4, 20) == 'T1'

def test_duval_1_result_calculation_D1_D2_DT_cross():
    assert duval_triangle_1.calculate_duval_1_result(63, 31, 24) == 'D2'

def test_duval_1_result_calculation_D1_D2_edge():
    assert duval_triangle_1.calculate_duval_1_result(26, 50, 24) == 'D2'

def test_duval_1_result_calculation_PD_T1_edge():
    assert duval_triangle_1.calculate_duval_1_result(98, 2, 0) == 'PD'

def test_duval_1_result_calculation_D2_DT_edge():
    assert duval_triangle_1.calculate_duval_1_result(47, 13, 40) == 'D2'

def test_duval_1_result_calculation_D2_DT_edge_2():
    assert duval_triangle_1.calculate_duval_1_result(31, 29, 40) == 'D2'

def test_duval_1_result_calculation_D1_D2_edge():
    assert duval_triangle_1.calculate_duval_1_result(64, 13, 23) == 'D1'

# Duval triangle 4 tests
# TODO add tests for all cases and edge events
def test_duval_4_result_calculation_C_edge_1():
    assert duval_triangle_4.calculate_duval_4_result(10, 26, 64) == 'C'

# Duval triangle 5 restes
# TODO add tests for all cases and edge events
def test_duval_5_result_calculation_C_edge_1():
    assert duval_triangle_5.calculate_duval_5_result(35, 15, 50) == 'C'
    