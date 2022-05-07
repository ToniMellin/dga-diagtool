from diagnostic import typical_value_comparison
import numpy as np

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
