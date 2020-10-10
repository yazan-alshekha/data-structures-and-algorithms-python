
from data_structures_and_algorithms.data_structures.graphs.graph import Graph,Node
import pytest

def test_conn():
    pass

def test_add_1():
    g1=Graph()
    expected = "A node with a and another node with b was added to the graph"
    actual = g1.AddNode("a","b")
    assert expected == actual

def test_add_2():
    g1=Graph()
    expected = "A node with yazan and another node with alshekha was added to the graph"
    actual = g1.AddNode("yazan","alshekha")
    assert expected == actual



def test_retrive_graph(pre):
    expected = {
        'a': ['b', 'c', 'd'],
        'b': ['a', 'c', 'd'],
        'c': ['a', 'b', 'd'],
        'd': ['a', 'b', 'c', 'f'],
        'f': ['d']
            }
    actual = pre.adjacency_list
    assert expected ==actual

    


def test_getNeighbor():
    g=Graph()
    g.AddNode("a","b")
    g.AddNode("a","c")
    g.AddNode("a","d")  
    g.AddEdge("a","b",800)
    g.AddEdge("a","c",100)
    g.AddEdge("a","d",50)
    actual=g.GetNeighbors("a")
    expected = [('b', 800), ('c', 100), ('d', 50)]
    assert expected ==actual

   

def test_sizer():
    g=Graph()
    g.AddNode("a","b")
    g.AddNode("a","c")
    g.AddNode("a","d")  
    g.AddEdge("a","b",800)
    g.AddEdge("a","c",100)
    g.AddEdge("a","d",50)
    actual=g.Size()
    expected = 4
    assert expected ==actual


@pytest.fixture
def pre():
    g=Graph()
    
    g.AddNode("a","b")
    g.AddNode("a","c")
    g.AddNode("a","d")    
    g.AddNode("b","c")
    g.AddNode("b","d")  
    g.AddNode("c","d") 
    g.AddNode("d","f")     

    g.AddEdge("a","b",800)
    g.AddEdge("a","c",100)
    g.AddEdge("a","d",50)
    g.AddEdge("b","c",25)
    g.AddEdge("b","d",10)
    g.AddEdge("c","d",16)
    g.AddEdge("d","f",17)

    return g