# from data_structures_and_algorithms.challenges.array-shift.array-shift import array_shift
from data_structures_and_algorithms.challenges.array_shift.array_shift_basics import array_shift


def test_array_shift():
    expected=[0,1,2,3,7,8]
    arr=[0,1,3,7,8]
    actual=array_shift(arr,2)
    assert expected==actual