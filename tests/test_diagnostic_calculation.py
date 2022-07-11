import numpy as np
from diagnostic import diagnostic_calculation
from diagnostic import duval_triangle_1
from diagnostic import duval_triangle_4
from diagnostic import duval_triangle_5

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

def test_duval_1_result_calculation_DT_T2_T3_cross():
    assert duval_triangle_1.calculate_duval_1_result(46, 4, 50) == 'T3'

def test_duval_1_result_calculation_T2_T3_edge_1():
    assert duval_triangle_1.calculate_duval_1_result(48, 2, 50) == 'T3'

def test_duval_1_result_calculation_T3_middle():
    assert duval_triangle_1.calculate_duval_1_result(16, 8, 76) == 'T3'

def test_duval_1_result_calculation_T2_DT_between():
    assert duval_triangle_1.calculate_duval_1_result(61, 4, 35) == 'T3'

def test_duval_1_result_calculation_DT_T1_T2_cross():
    assert duval_triangle_1.calculate_duval_1_result(76, 4, 20) == 'T1'

def test_duval_1_result_calculation_T1_T2_edge():
    assert duval_triangle_1.calculate_duval_1_result(78, 2, 20) == 'T2'

def test_duval_1_result_calculation_T2_middle():
    assert duval_triangle_1.calculate_duval_1_result(64, 2, 34) == 'T2'

def test_duval_1_result_calculation_T1_DT_between():
    assert duval_triangle_1.calculate_duval_1_result(86, 4, 10) == 'T1'

def test_duval_1_result_calculation_T1_middle():
    assert duval_triangle_1.calculate_duval_1_result(88, 2, 10) == 'T1'

def test_duval_1_result_calculation_PD_T1_right_edge():
    assert duval_triangle_1.calculate_duval_1_result(98, 0, 2) == 'PD'

def test_duval_1_result_calculation_PD_T1_left_edge():
    assert duval_triangle_1.calculate_duval_1_result(98, 2, 0) == 'PD'

def test_duval_1_result_calculation_PD_middle():
    assert duval_triangle_1.calculate_duval_1_result(99, 1, 1) == 'PD'

def test_duval_1_result_calculation_PD_T1_DT_cross():
    assert duval_triangle_1.calculate_duval_1_result(96, 4, 0) == 'T1'

def test_duval_1_result_calculation_DT_middle():
    assert duval_triangle_1.calculate_duval_1_result(40, 15, 45) == 'DT'

def test_duval_1_result_calculation_D1_middle():
    assert duval_triangle_1.calculate_duval_1_result(42, 46, 12) == 'D1'

def test_duval_1_result_calculation_D1_DT_edge():
    assert duval_triangle_1.calculate_duval_1_result(87, 13, 0) == 'D1'

def test_duval_1_result_calculation_D1_DT_between():
    assert duval_triangle_1.calculate_duval_1_result(77, 13, 10) == 'D1'

def test_duval_1_result_calculation_D1_D2_DT_cross():
    assert duval_triangle_1.calculate_duval_1_result(64, 13, 23) == 'D1'

def test_duval_1_result_calculation_D2_middle():
    assert duval_triangle_1.calculate_duval_1_result(25, 40, 35) == 'D2'

def test_duval_1_result_calculation_D2_DT_between():
    assert duval_triangle_1.calculate_duval_1_result(57, 13, 30) == 'D2'

def test_duval_1_result_calculation_D2_DT_edge():
    assert duval_triangle_1.calculate_duval_1_result(47, 13, 40) == 'D2'

def test_duval_1_result_calculation_D2_DT_edge_2():
    assert duval_triangle_1.calculate_duval_1_result(31, 29, 40) == 'D2'

def test_duval_1_result_calculation_D2_DT_edge_3():
    assert duval_triangle_1.calculate_duval_1_result(15, 29, 56) == 'D2'

def test_duval_1_result_calculation_D2_DT_edge_4():
    assert duval_triangle_1.calculate_duval_1_result(0, 29, 71) == 'D2'

def test_duval_1_result_calculation_D1_D2_edge():
    assert duval_triangle_1.calculate_duval_1_result(37, 40, 23) == 'D1'

def test_duval_1_result_calculation_D1_D2_edge_2():
    assert duval_triangle_1.calculate_duval_1_result(0, 77, 23) == 'D1'

def test_duval_1_result_calculation_DT_T3_edge_2():
    assert duval_triangle_1.calculate_duval_1_result(0, 15, 85) == 'T3'

def test_duval_1_result_calculation_DT_T3_edge_2():
    assert duval_triangle_1.calculate_duval_1_result(20, 15, 65) == 'T3'

def test_duval_1_result_calculation_DT_T3_edge_2():
    assert duval_triangle_1.calculate_duval_1_result(40, 10, 50) == 'T3'

# Duval triangle 4 tests
# TODO add tests for all cases and edge events
def test_duval_4_result_calculation_triangle_tip():
    assert duval_triangle_4.calculate_duval_4_result(100, 0, 0) == 'S'

def test_duval_4_result_calculation_S_middle():
    assert duval_triangle_4.calculate_duval_4_result(50, 23, 27) == 'S'

def test_duval_4_result_calculation_S_ND_edge():
    assert duval_triangle_4.calculate_duval_4_result(54, 46, 0) == 'N/D'

def test_duval_4_result_calculation_S_ND_edge_2():
    assert duval_triangle_4.calculate_duval_4_result(30, 46, 24) == 'N/D'

def test_duval_4_result_calculation_O_ND_edge():
    assert duval_triangle_4.calculate_duval_4_result(9, 91, 0) == 'N/D'

def test_duval_4_result_calculation_O_ND_edge_2():
    assert duval_triangle_4.calculate_duval_4_result(9, 70, 21) == 'N/D'

def test_duval_4_result_calculation_O_S_ND_cross():
    assert duval_triangle_4.calculate_duval_4_result(9, 46, 45) == 'N/D'

def test_duval_4_result_calculation_ND_middle():
    assert duval_triangle_4.calculate_duval_4_result(25, 60, 15) == 'N/D'

def test_duval_4_result_calculation_O_S_edge():
    assert duval_triangle_4.calculate_duval_4_result(9, 40, 51) == 'O'

def test_duval_4_result_calculation_O_middle():
    assert duval_triangle_4.calculate_duval_4_result(5, 60, 35) == 'O'

def test_duval_4_result_calculation_O_S_C_cross():
    assert duval_triangle_4.calculate_duval_4_result(9, 30, 61) == 'C'

def test_duval_4_result_calculation_O_C_edge():
    assert duval_triangle_4.calculate_duval_4_result(0, 30, 70) == 'C'

def test_duval_4_result_calculation_S_C_edge():
    assert duval_triangle_4.calculate_duval_4_result(15, 30, 55) == 'C'

def test_duval_4_result_calculation_S_C_edge_2():
    assert duval_triangle_4.calculate_duval_4_result(15, 24, 61) == 'C'

def test_duval_4_result_calculation_S_C_edge_3():
    assert duval_triangle_4.calculate_duval_4_result(26, 24, 50) == 'C'

def test_duval_4_result_calculation_S_C_edge_4():
    assert duval_triangle_4.calculate_duval_4_result(40, 24, 36) == 'C'

def test_duval_4_result_calculation_S_C_edge_5():
    assert duval_triangle_4.calculate_duval_4_result(54, 10, 36) == 'C'

def test_duval_4_result_calculation_S_C_edge_6():
    assert duval_triangle_4.calculate_duval_4_result(64, 0, 36) == 'C'

def test_duval_4_result_calculation_C_middle():
    assert duval_triangle_4.calculate_duval_4_result(25, 15, 60) == 'C'

def test_duval_4_result_calculation_S_PD_edge():
    assert duval_triangle_4.calculate_duval_4_result(85, 0, 15) == 'PD'

def test_duval_4_result_calculation_S_PD_edge_2():
    assert duval_triangle_4.calculate_duval_4_result(84, 1, 15) == 'PD'

def test_duval_4_result_calculation_S_PD_edge_3():
    assert duval_triangle_4.calculate_duval_4_result(91, 1, 8) == 'PD'

def test_duval_4_result_calculation_S_PD_edge_4():
    assert duval_triangle_4.calculate_duval_4_result(97, 1, 2) == 'PD'

def test_duval_4_result_calculation_S_PD_edge_5():
    assert duval_triangle_4.calculate_duval_4_result(98, 0, 2) == 'PD'

def test_duval_4_result_calculation_PD_middle():
    assert duval_triangle_4.calculate_duval_4_result(91, 0.5, 8.5) == 'PD'

# Duval triangle 5 tests
# TODO add tests for all cases and edge events
def test_duval_5_result_calculation_O_1_middle():
    assert duval_triangle_5.calculate_duval_5_result(90, 5, 5) == 'O'

def test_duval_5_result_calculation_O_T2_edge_1():
    assert duval_triangle_5.calculate_duval_5_result(90, 0, 10) == 'T2'

def test_duval_5_result_calculation_O_T2_edge_2():
    assert duval_triangle_5.calculate_duval_5_result(85, 5, 10) == 'T2'

def test_duval_5_result_calculation_O_T2_C_cross():
    assert duval_triangle_5.calculate_duval_5_result(78, 12, 10) == 'T2'

def test_duval_5_result_calculation_C_T2_edge_1():
    assert duval_triangle_5.calculate_duval_5_result(63, 12, 25) == 'T2'

def test_duval_5_result_calculation_C_T2_T3_cross():
    assert duval_triangle_5.calculate_duval_5_result(53, 12, 35) == 'T2'

def test_duval_5_result_calculation_T2_T3_edge_1():
    assert duval_triangle_5.calculate_duval_5_result(59, 6, 35) == 'T2'

def test_duval_5_result_calculation_T2_T3_edge_2():
    assert duval_triangle_5.calculate_duval_5_result(65, 0, 35) == 'T2'

def test_duval_5_result_calculation_T2_middle():
    assert duval_triangle_5.calculate_duval_5_result(69, 6, 25) == 'T2'

def test_duval_5_result_calculation_C_T3_edge_1():
    assert duval_triangle_5.calculate_duval_5_result(43, 12, 45) == 'T3'

def test_duval_5_result_calculation_C_T3_edge_2():
    assert duval_triangle_5.calculate_duval_5_result(38, 12, 50) == 'T3'

def test_duval_5_result_calculation_C_T3_edge_3():
    assert duval_triangle_5.calculate_duval_5_result(37, 13, 50) == 'T3'

def test_duval_5_result_calculation_C_T3_edge_4():
    assert duval_triangle_5.calculate_duval_5_result(37, 14, 49) == 'T3'

def test_duval_5_result_calculation_C_T3_edge_5():
    assert duval_triangle_5.calculate_duval_5_result(36, 14, 50) == 'T3'

def test_duval_5_result_calculation_C_T3_edge_6():
    assert duval_triangle_5.calculate_duval_5_result(21, 14, 65) == 'T3'

def test_duval_5_result_calculation_C_T3_edge_7():
    assert duval_triangle_5.calculate_duval_5_result(16, 14, 70) == 'T3'

def test_duval_5_result_calculation_T3_R_middle():
    assert duval_triangle_5.calculate_duval_5_result(10, 10, 80) == 'T3'

def test_duval_5_result_calculation_C_middle():
    assert duval_triangle_5.calculate_duval_5_result(45, 20, 35) == 'C'

def test_duval_5_result_calculation_C_T3_edge_8():
    assert duval_triangle_5.calculate_duval_5_result(10, 20, 70) == 'C'

def test_duval_5_result_calculation_C_T3_edge_9():
    assert duval_triangle_5.calculate_duval_5_result(0, 30, 70) == 'T3'

def test_duval_5_result_calculation_T3_C_edge_10():
    assert duval_triangle_5.calculate_duval_5_result(15, 30, 55) == 'T3'

def test_duval_5_result_calculation_T3_C_ND_cross():
    assert duval_triangle_5.calculate_duval_5_result(35, 30, 35) == 'T3'

def test_duval_5_result_calculation_ND_T3_edge_1():
    assert duval_triangle_5.calculate_duval_5_result(20, 45, 35) == 'T3'

def test_duval_5_result_calculation_ND_T3_edge_2():
    assert duval_triangle_5.calculate_duval_5_result(0, 65, 35) == 'T3'

def test_duval_5_result_calculation_T3_L_middle():
    assert duval_triangle_5.calculate_duval_5_result(15, 40, 45) == 'T3'

def test_duval_5_result_calculation_O_ND_edge_1():
    assert duval_triangle_5.calculate_duval_5_result(0, 90, 10) == 'N/D'

def test_duval_5_result_calculation_O_ND_edge_2():
    assert duval_triangle_5.calculate_duval_5_result(20, 70, 10) == 'N/D'

def test_duval_5_result_calculation_O_ND_S_cross():
    assert duval_triangle_5.calculate_duval_5_result(36, 54, 10) == 'N/D'

def test_duval_5_result_calculation_ND_middle():
    assert duval_triangle_5.calculate_duval_5_result(25, 55, 20) == 'N/D'

def test_duval_5_result_calculation_O_S_edge_1():
    assert duval_triangle_5.calculate_duval_5_result(41, 54, 5) == 'O'

def test_duval_5_result_calculation_O_2_middle():
    assert duval_triangle_5.calculate_duval_5_result(25, 70, 5) == 'O'

def test_duval_5_result_calculation_S_ND_edge_1():
    assert duval_triangle_5.calculate_duval_5_result(36, 54, 10) == 'N/D'

def test_duval_5_result_calculation_S_ND_edge_1():
    assert duval_triangle_5.calculate_duval_5_result(36, 54, 10) == 'N/D'

def test_duval_5_result_calculation_ND_C_edge():
    assert duval_triangle_5.calculate_duval_5_result(50, 30, 20) == 'N/D'

def test_duval_5_result_calculation_S_ND_C_cross():
    assert duval_triangle_5.calculate_duval_5_result(60, 30, 10) == 'N/D'

def test_duval_5_result_calculation_S_middle():
    assert duval_triangle_5.calculate_duval_5_result(65, 30, 5) == 'S'

def test_duval_5_result_calculation_S_C_edge_1():
    assert duval_triangle_5.calculate_duval_5_result(70, 20, 10) == 'C'
    
def test_duval_5_result_calculation_S_C_edge_1():
    assert duval_triangle_5.calculate_duval_5_result(70, 20, 10) == 'C'

def test_duval_5_result_calculation_S_O_C_cross():
    assert duval_triangle_5.calculate_duval_5_result(76, 14, 10) == 'C'

def test_duval_5_result_calculation_S_O_edge_1():
    assert duval_triangle_5.calculate_duval_5_result(81, 14, 5) == 'O'

def test_duval_5_result_calculation_S_O_PD_cross():
    assert duval_triangle_5.calculate_duval_5_result(85, 14, 1) == 'PD'

def test_duval_5_result_calculation_S_PD_edge():
    assert duval_triangle_5.calculate_duval_5_result(86, 14, 0) == 'PD'

def test_duval_5_result_calculation_PD_O_edge_1():
    assert duval_triangle_5.calculate_duval_5_result(97, 2, 1) == 'PD'

def test_duval_5_result_calculation_PD_O_edge_2():
    assert duval_triangle_5.calculate_duval_5_result(98, 2, 0) == 'PD'

def test_duval_5_result_calculation_PD_middle():
    assert duval_triangle_5.calculate_duval_5_result(95, 9.5, 0.5) == 'PD'
