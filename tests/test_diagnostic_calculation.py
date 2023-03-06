import numpy as np
from diagnostic import diagnostic_calculation
from diagnostic import duval_triangle_1
from diagnostic import duval_triangle_4
from diagnostic import duval_triangle_5
from diagnostic import duval_pentagon_1
from diagnostic import duval_pentagon_2

# ratio tests
def test_ratio_calculation_nan():
    assert diagnostic_calculation.calculate_ratios(np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan) == [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]

def test_ratio_calculation_even_set():
    assert diagnostic_calculation.calculate_ratios(20, 40, 10, 10, 20, 50, 500, 40000, 80000) == [2, 2, 0.5, 0.5, 1, 10, 0.5]

def test_ratio_calculation_even_and_uneven_set():
    assert diagnostic_calculation.calculate_ratios(10, 60, 20, 10, 20, 100, 2000, 5000, 80000) == [6, 2, 0.33, 1, 0.5, 20, 0.06]

def test_ratio_calculation_even_and_uneven_set():
    assert diagnostic_calculation.calculate_ratios(9, 8, 6, 16, 15, 60, 178, 21100, 80000) == [0.89, 0.94, 1.88, 0.40, 2.67, 2.97, 0.26]

def test_ratio_calculation_set_1():
    assert diagnostic_calculation.calculate_ratios(201, 50, 10, 50, 50, 350, 178, 21100, 80000) == [0.25, 1, 1, 0.20, 5, 0.51, 0.26]

def test_ratio_calculation_set_2():
    assert diagnostic_calculation.calculate_ratios(500, 121, 874, 12, 50, 5000, 1000, 19800, 65000) == [0.24, 4.17, 0.41, 17.48, 0.01, 0.20, 0.30]


# IEC ratio tests
def test_iec_ratio_nan():
    assert diagnostic_calculation.iec_ratio_calculation(np.nan, np.nan, np.nan) == 'N/A'

def test_iec_ratio_all_zero():
    assert diagnostic_calculation.iec_ratio_calculation(0, 0, 0) == 'PD'

def test_iec_ratio_PD_1():
    assert diagnostic_calculation.iec_ratio_calculation(50, 0.01, 0.1) == 'PD'

def test_iec_ratio_D1_1():
    assert diagnostic_calculation.iec_ratio_calculation(2, 0.1, 1.1) == 'D1'

def test_iec_ratio_D1_2():
    assert diagnostic_calculation.iec_ratio_calculation(1.1, 0.5, 2) == 'D1'

def test_iec_ratio_D2_1():
    assert diagnostic_calculation.iec_ratio_calculation(0.6, 0.1, 2.1) == 'D2'

def test_iec_ratio_D2_2():
    assert diagnostic_calculation.iec_ratio_calculation(2.5, 1, 2.1) == 'D2'

def test_iec_ratio_T1_1():
    assert diagnostic_calculation.iec_ratio_calculation(1, 1.1, 0) == 'T1'

def test_iec_ratio_T1_2():
    assert diagnostic_calculation.iec_ratio_calculation(1, 2, 0.9) == 'T1'

def test_iec_ratio_T2_1():
    assert diagnostic_calculation.iec_ratio_calculation(0, 1.1, 1) == 'T2'

def test_iec_ratio_T2_2():
    assert diagnostic_calculation.iec_ratio_calculation(0.01, 1.1, 4) == 'T2'

def test_iec_ratio_T3_1():
    assert diagnostic_calculation.iec_ratio_calculation(0.1, 1.1, 5) == 'T3'


# Rogers ratio tests
def test_rogers_ratio_nan():
    assert diagnostic_calculation.rogers_ratio_calculation(np.nan, np.nan, np.nan) == 'N/A'

def test_rogers_ratio_some_nan():
    assert diagnostic_calculation.rogers_ratio_calculation(np.nan, 2, 1) == 'N/A'

def test_rogers_ratio_all_zero():
    assert diagnostic_calculation.rogers_ratio_calculation(0, 0, 0) == 'PD'

def test_rogers_ratio_PD_1():
    assert diagnostic_calculation.rogers_ratio_calculation(0, 0.01, 0.5) == 'PD'

def test_rogers_ratio_normal_1():
    assert diagnostic_calculation.rogers_ratio_calculation(0, 0.1, 0.5) == 'Normal'

def test_rogers_ratio_normal_2():
    assert diagnostic_calculation.rogers_ratio_calculation(0.01, 1, 0) == 'Normal'

def test_rogers_ratio_D2_1():
    assert diagnostic_calculation.rogers_ratio_calculation(0.1, 0.1, 3.1) == 'D2'

def test_rogers_ratio_D2_2():
    assert diagnostic_calculation.rogers_ratio_calculation(3, 1, 5) == 'D2'

def test_rogers_ratio_T1_1():
    assert diagnostic_calculation.rogers_ratio_calculation(0, 0.1, 1) == 'T1'

def test_rogers_ratio_T1_2():
    assert diagnostic_calculation.rogers_ratio_calculation(0.01, 1, 3) == 'T1'

def test_rogers_ratio_T2_1():
    assert diagnostic_calculation.rogers_ratio_calculation(0, 1.1, 1) == 'T2'

def test_rogers_ratio_T2_2():
    assert diagnostic_calculation.rogers_ratio_calculation(0.01, 2, 3) == 'T2'

def test_rogers_ratio_T3_1():
    assert diagnostic_calculation.rogers_ratio_calculation(0.01, 1.1, 5) == 'T3'

def test_rogers_ratio_ND_1():
    assert diagnostic_calculation.rogers_ratio_calculation(0.1, 1.1, 2) == 'ND'

def test_rogers_ratio_ND_2():
    assert diagnostic_calculation.rogers_ratio_calculation(4, 0.1, 5) == 'ND'

def test_rogers_ratio_ND_3():
    assert diagnostic_calculation.rogers_ratio_calculation(0, 0, 2) == 'ND'

def test_rogers_ratio_ND_4():
    assert diagnostic_calculation.rogers_ratio_calculation(0, 2, 0) == 'ND'

def test_rogers_ratio_ND_5():
    assert diagnostic_calculation.rogers_ratio_calculation(2, 0, 2) == 'ND'


# Doernenburg ratio tests
def test_doernenburg_ratio_all_zero():
    assert diagnostic_calculation.doernenburg_ratio_calculation(0, 0, 0, 0, 0, 0) == 'No fault'

def test_doernenburg_ratio_all_nan():
    assert diagnostic_calculation.doernenburg_ratio_calculation(np.nan, np.nan, np.nan, np.nan, np.nan, np.nan) == 'N/A'

def test_doernenburg_ratio_some_nan():
    assert diagnostic_calculation.doernenburg_ratio_calculation(np.nan, 10, np.nan, 200, 50, 100) == 'N/A'

def test_doernenburg_ratio_no_fault_1():
    assert diagnostic_calculation.doernenburg_ratio_calculation(200, 240, 65, 100, 2, 350) == 'No fault'

def test_doernenburg_ratio_no_fault_2():
    assert diagnostic_calculation.doernenburg_ratio_calculation(201, 240, 65, 100, 2, 350) == 'No fault'

def test_doernenburg_ratio_no_fault_3():
    assert diagnostic_calculation.doernenburg_ratio_calculation(200, 240, 66, 100, 2, 351) == 'No fault'

def test_doernenburg_ratio_no_fault_3():
    assert diagnostic_calculation.doernenburg_ratio_calculation(201, 240, 65, 100, 2, 350) == 'No fault'

def test_doernenburg_ratio_T_1():
    assert diagnostic_calculation.doernenburg_ratio_calculation(201, 240, 66, 100, 2, 350) == 'T'

def test_doernenburg_ratio_PD_1():
    assert diagnostic_calculation.doernenburg_ratio_calculation(201, 0, 66, 100, 2, 350) == 'PD'

def test_doernenburg_ratio_D2_1():
    assert diagnostic_calculation.doernenburg_ratio_calculation(201, 50, 10, 50, 50, 400) == 'D1/D2'

def test_doernenburg_ratio_ND():
    assert diagnostic_calculation.doernenburg_ratio_calculation(201, 121, 66, 51, 0, 351) == 'ND'


# Duval triangle 1 tests
def test_duval_1_coordinates_1():
    assert duval_triangle_1.calculate_duval_1_coordinates(8, 15, 25).tolist() == [16.67, 31.25, 52.08]

def test_duval_1_result_calculation_DT_T3_edge_1():
    assert duval_triangle_1.calculate_duval_1_result(35, 15, 50) == 'T3'

def test_duval_1_result_calculation_DT_T2_T3_cross():
    assert duval_triangle_1.calculate_duval_1_result(46, 4, 50) == 'T3'

def test_duval_1_result_calculation_T2_T3_edge_1():
    assert duval_triangle_1.calculate_duval_1_result(48, 2, 50) == 'T3'

def test_duval_1_result_calculation_T3_middle():
    assert duval_triangle_1.calculate_duval_1_result(16, 8, 76) == 'T3'

def test_duval_1_result_calculation_T2_DT_between():
    assert duval_triangle_1.calculate_duval_1_result(61, 4, 35) == 'T2'

def test_duval_1_result_calculation_DT_T1_T2_cross():
    assert duval_triangle_1.calculate_duval_1_result(76, 4, 20) == 'T1'

def test_duval_1_result_calculation_T1_T2_edge():
    assert duval_triangle_1.calculate_duval_1_result(78, 2, 20) == 'T1'

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

def test_duval_1_result_calculation_DT_upper_zone():
    assert duval_triangle_1.calculate_duval_1_result(57, 8, 35) == 'DT'

def test_duval_1_result_calculation_DT_middle_zone():
    assert duval_triangle_1.calculate_duval_1_result(40, 15, 45) == 'DT'

def test_duval_1_result_calculation_DT_lower_zone():
    assert duval_triangle_1.calculate_duval_1_result(20, 20, 60) == 'DT'

def test_duval_1_result_calculation_D1_middle():
    assert duval_triangle_1.calculate_duval_1_result(42, 46, 12) == 'D1'

def test_duval_1_result_calculation_D1_DT_edge():
    assert duval_triangle_1.calculate_duval_1_result(87, 13, 0) == 'D1'

def test_duval_1_result_calculation_D1_DT_between():
    assert duval_triangle_1.calculate_duval_1_result(77, 13, 10) == 'D1'

def test_duval_1_result_calculation_D1_D2_DT_cross():
    assert duval_triangle_1.calculate_duval_1_result(64, 13, 23) == 'D1'

def test_duval_1_result_calculation_D2_upper_zone():
    assert duval_triangle_1.calculate_duval_1_result(25, 40, 35) == 'D2'

def test_duval_1_result_calculation_D2_lower_zone():
    assert duval_triangle_1.calculate_duval_1_result(10, 40, 50) == 'D2'

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
def test_duval_4_coordinates_1():
    assert duval_triangle_4.calculate_duval_4_coordinates(13, 6, 8).tolist() == [48.15, 22.22, 29.63]

def test_duval_4_result_calculation_triangle_tip():
    assert duval_triangle_4.calculate_duval_4_result(100, 0, 0) == 'S'

def test_duval_4_result_calculation_S_middle():
    assert duval_triangle_4.calculate_duval_4_result(50, 23, 27) == 'S'

def test_duval_4_result_calculation_S_ND_edge():
    assert duval_triangle_4.calculate_duval_4_result(54, 46, 0) == 'ND'

def test_duval_4_result_calculation_S_ND_edge_2():
    assert duval_triangle_4.calculate_duval_4_result(30, 46, 24) == 'ND'

def test_duval_4_result_calculation_O_ND_edge():
    assert duval_triangle_4.calculate_duval_4_result(9, 91, 0) == 'O'

def test_duval_4_result_calculation_O_ND_edge_2():
    assert duval_triangle_4.calculate_duval_4_result(9, 70, 21) == 'O'

def test_duval_4_result_calculation_O_S_ND_cross():
    assert duval_triangle_4.calculate_duval_4_result(9, 46, 45) == 'O'

def test_duval_4_result_calculation_ND_middle():
    assert duval_triangle_4.calculate_duval_4_result(25, 60, 15) == 'ND'

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
def test_duval_5_coordinates_1():
    assert duval_triangle_5.calculate_duval_5_coordinates(8, 6, 16).tolist() == [26.67, 20, 53.33]

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
    assert duval_triangle_5.calculate_duval_5_result(0, 90, 10) == 'ND'

def test_duval_5_result_calculation_O_ND_edge_2():
    assert duval_triangle_5.calculate_duval_5_result(20, 70, 10) == 'ND'

def test_duval_5_result_calculation_O_ND_S_cross():
    assert duval_triangle_5.calculate_duval_5_result(36, 54, 10) == 'ND'

def test_duval_5_result_calculation_ND_middle():
    assert duval_triangle_5.calculate_duval_5_result(25, 55, 20) == 'ND'

def test_duval_5_result_calculation_O_S_edge_1():
    assert duval_triangle_5.calculate_duval_5_result(41, 54, 5) == 'O'

def test_duval_5_result_calculation_O_2_middle():
    assert duval_triangle_5.calculate_duval_5_result(25, 70, 5) == 'O'

def test_duval_5_result_calculation_S_ND_edge_1():
    assert duval_triangle_5.calculate_duval_5_result(36, 54, 10) == 'ND'

def test_duval_5_result_calculation_S_ND_edge_1():
    assert duval_triangle_5.calculate_duval_5_result(36, 54, 10) == 'ND'

def test_duval_5_result_calculation_ND_C_edge():
    assert duval_triangle_5.calculate_duval_5_result(50, 30, 20) == 'ND'

def test_duval_5_result_calculation_S_ND_C_cross():
    assert duval_triangle_5.calculate_duval_5_result(60, 30, 10) == 'ND'

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

#TODO add tests for combined diagnostic results from dataframe

# Duval pentagon 1 tests
#TODO add tests for duval pentagon 1
def test_duval_p1_coordinates_calculation_1():
    assert duval_pentagon_1.calculate_duval_p1_coordinates(31, 192, 130, 31, 0) == (-32.3, 10.5)



# Duval pentagon 2 tests
#TODO add tests for duval pentagon 2
