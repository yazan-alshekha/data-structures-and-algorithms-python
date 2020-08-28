from data_structures_and_algorithms.data_structures.linked_list.linked_list import (
    LinkedList,
)
from data_structures_and_algorithms.data_structures.linked_list.zip_linked_lists import zip

def test_instance():
    ll = LinkedList()
    assert isinstance(ll, LinkedList)

def test_empty_linked_list():
    li=LinkedList()
    assert li.head==None

def test_insert_into_linked_list():
    li=LinkedList()
    li.insert(2)
    assert li.head.value==2

def test_includes_exist_value():
    li=LinkedList()
    li.append(5)
    li.append(2)
    li.append(10)
    result=li.includes(2)
    assert result==1

def test_includes_not_exist_value():
    li=LinkedList()
    li.append(2)
    li.append(5)
    result=li.includes(10)
    assert result==-1


def test_insertAfter():
    li=LinkedList()
    li.append('orange')
    li.append('apple')
    li.insertAfter('apple','grap')
    actual=li.head.next.next.value
    expected='grap'
    assert expected==actual

def test_insertAfter_first_node():
    li=LinkedList()
    li.append('orange')
    li.append('apple')
    li.insertAfter('orange','grap')
    actual=li.head.next.value
    expected='grap'
    assert expected==actual

def test_insertAfter_last_index():
    li=LinkedList()
    li.append('orange')
    li.append('apple')
    li.insertAfter('apple','grap')
    actual=li.head.next.next.value
    expected='grap'
    assert expected==actual    


def test_insertBefore():
    li=LinkedList()
    li.append('orange')
    li.append('apple')
    li.insertBefore('apple','grap')
    actual=li.head.next.value
    expected='grap'
    assert expected==actual

def test_insertBefore_first_node():
    li=LinkedList()
    li.append('orange')
    li.append('apple')
    li.insertBefore('orange','grap')
    actual=li.head.value
    expected='grap'
    assert expected==actual


def test_zip_empty_linked_list():
     fruits = LinkedList()
     people=LinkedList()
     actual= zip(fruits,people)
     expexted="Null"
     assert actual==expexted

def test_zip_linked_list():
    fruits = LinkedList()
    fruits.append('apple')
    fruits.append('orange')
    fruits.append('grap')

    people=LinkedList()
    people.append('yazan')
    people.append('rami')
    people.append('hamza')
    
    actual= zip(fruits,people)
    expexted="apple->yazan->orange->rami->grap->hamza-> NULL"
    assert actual==expexted

def test_zip_first_linked_list_isEmpty():
    fruits = LinkedList()

    people=LinkedList()
    people.append('yazan')
    people.append('rami')
    people.append('hamza')
    
    actual= zip(fruits,people)
    expexted="yazan->rami->hamza-> NULL"
    assert actual==expexted

def test_zip_second_linked_list_isEmpty():
    fruits = LinkedList()
    fruits.append('apple')
    fruits.append('orange')
    fruits.append('grap')

    people=LinkedList()

    actual= zip(fruits,people)
    expexted="apple->orange->grap-> NULL"
    assert actual==expexted

def test_kthFromEnd_value_greater_than_length_of_list():
    li=LinkedList()
    li.append('orange')
    li.append('apple')
    li.append('grap')
    actual=li.kthFromEnd(10)
    expected='invalid reverse index \n  reverse index should be => length of list'      
    assert actual==expected


def test_kthFromEnd_last_reverse_index():
    li=LinkedList()
    li.append('orange')
    li.append('apple')
    li.append('grap')
    actual=li.kthFromEnd(0)
    expected='grap'     
    assert actual==expected

def test_kthFromEnd_Not_positive_value():
    li=LinkedList()
    li.append('orange')
    li.append('apple')
    li.append('grap')
    actual=li.kthFromEnd(-1)
    expected='you should enter positive value'     
    assert actual==expected    

def test_kthFromEnd_have_1_item():
    li=LinkedList()
    li.append('orange')
    actual=li.kthFromEnd(0)
    expected='orange'     
    assert actual==expected 


def test_kthFromEnd_value_from_the_middle():
    li=LinkedList()
    li.append('orange')
    li.append('apple')
    li.append('grap')
    li.append('banana')
    li.append('pear')
    actual=li.kthFromEnd(2)
    expected='grap'     
    assert actual==expected     