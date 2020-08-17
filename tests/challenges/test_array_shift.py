# from data_structures_and_algorithms.challenges.array-shift.array-shift import array_shift
from data_structures_and_algorithms.challenges.array-shift.array-shift import (
    array-shift,
)

def test_array_shift():
    expected=[0,0,3,7,8]
    arr=[0,2,3,7,8]
    actual=array_shift(arr,0)
    assert expected=actual