from data_structures_and_algorithms.challenges.quick_sort.quick_sort import *
import pytest



def test_Quick_sort_1(pre_data):
    sample=pre_data[0]
    n = len(sample)
    expected=[-2,5,8,12,18,20]
    actual=QuickSort(sample,0,n-1)
    assert expected==actual

def test_Quick_sort_2(pre_data):
    sample=pre_data[1]
    n = len(sample)
    expected=[5,5,5,7,7,12]
    actual = QuickSort(sample,0,n-1)
    assert expected==actual

def test_Quick_sort_3(pre_data):
    sample=pre_data[2]
    n = len(sample)
    expected=[2,3,5,7,11,13]
    actual = QuickSort(sample,0,n-1)
    assert expected==actual


def test_Quick_sort_4(pre_data):
    sample=pre_data[3]
    n = len(sample)
    expected=[4,8,15,16,23,42]
    actual = QuickSort(sample,0,n-1)
    assert expected==actual


@pytest.fixture
def pre_data():
    a=[20,18,12,8,5,-2]
    b=[5,12,7,5,5,7]
    c=[2,3,5,7,13,11]
    d=[8,4,23,42,16,15]
    return a,b,c,d