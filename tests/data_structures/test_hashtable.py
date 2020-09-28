
from data_structures_and_algorithms.data_structures.hashtable.hashtable import *

def test1():
    expected=('name','ahmad')
    table=Hashtable()
    table.set('name','ahmad')
    actual=table.map[table.hash('name')].head.value
    assert actual==expected