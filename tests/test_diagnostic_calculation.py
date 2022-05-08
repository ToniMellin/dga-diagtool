from diagnostic import diagnostic_calculation
from diagnostic import duval_triangle_1
from diagnostic import duval_triangle_4
import numpy as np

def test_ratio_calculation_nan():
    diagnostic_calculation.calculate_ratios(np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan) == [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]

def test_ratio_calculation_even_set():
    diagnostic_calculation.calculate_ratios(20, 40, 10, 10, 20, 50, 500, 40000, 80000) == [2, 2, 1, 0.5, 1, 10, 0.5]

def test_iec_ratio_nan():
    assert diagnostic_calculation.iec_ratio_calculation(np.nan, np.nan, np.nan) == 'N/A'

def test_duval_4_result_calculation_1():
    assert duval_triangle_4.calculate_duval_4_result(10, 26, 64) == 'C'
    