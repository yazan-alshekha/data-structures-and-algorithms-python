from data_structures_and_algorithms.data_structures.linked_list.linked_list import (
    LinkedList,
)


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



def test_value_not_exists():
    li=LinkedList()
    li.append('orange')
    li.append('apple')
    li.append('grap')
    actual=li.kthFromEnd('banana')
    expected='not exists'      
    assert actual==expected


def test_check_last_value():
    li=LinkedList()
    li.append('orange')
    li.append('apple')
    li.append('grap')
    actual=li.kthFromEnd('grap')
    expected=0      
    assert actual==expected

def test_value_not_positive_integer():
    li=LinkedList()
    li.append('orange')
    li.append('apple')
    li.append('grap')
    actual=li.kthFromEnd(-1)
    expected='not exists'      
    assert actual==expected

 

def test_linked_list_size_1():
    li=LinkedList()
    li.append('orange')
    actual=li.kthFromEnd('orange')
    expected=0     
    assert actual==expected

def test_value_in_the_middle():
    li=LinkedList()
    li.append('orange')
    li.append('apple')
    li.append('grap')
    actual=li.kthFromEnd('apple')
    expected=1      
    assert actual==expected    