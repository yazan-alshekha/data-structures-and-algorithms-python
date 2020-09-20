from data_structures_and_algorithms.challenges.insertion_sort.insertion_sort import insertion_sort



def test_sort_list():
    actual=[4,6,2,8] 
    insertion_sort(actual) 
    expected=[2, 4, 6, 8]
    actual=expected

def test2_sort_list():
    actual=[10,5,8,41,62,85] 
    insertion_sort(actual) 
    expected=[5, 8, 10, 41, 62, 85]
    actual=expected