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