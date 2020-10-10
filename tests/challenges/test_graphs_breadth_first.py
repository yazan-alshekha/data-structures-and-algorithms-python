from data_structures_and_algorithms.data_structures.graphs.graph import Graph
from data_structures_and_algorithms.challenges.graph_breadth_first.graph_breadth_first import breadth_first
import pytest


def test_conn():
    pass

def test_new_method_appendded():
    """
    To test if breadth_first method was appended correctly. I didnt create a new graph to create one new method (waste of time)
    """
    expected = True
    actual = "breadth_first" in dir(Graph)
    assert expected ==actual


def test_breadth_first_method(pre):
    """
    Test breadth_first method at start node : 'a'
    """
    expected = ['a', 'b', 'c', 'd', 'f']
    actual = pre.breadth_first("a")
    assert expected ==actual

def test_different_startNode(pre):
    """
    Test breadth_first method at start node : 'a'
    """
    expected = ['b', 'a', 'c', 'd', 'f']
    actual = pre.breadth_first("b")
    assert expected ==actual

def test_different_startNode_lastNode(pre):
    
    """
    Test breadth_first method at start node : 'a'
    """
    expected = ['f', 'd', 'a', 'b', 'c']
    actual = pre.breadth_first("f")
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