# from data_structures_and_algorithms.challenges.array_binary_search import BinarySearch 
from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import BinarySearch


arr=[2,3,4,10,40] 
x=10
def test_BinarySearch():
    expected=3
    actual=BinarySearch(arr, arr[0],len(arr)-1, x)
    assert actual==expected