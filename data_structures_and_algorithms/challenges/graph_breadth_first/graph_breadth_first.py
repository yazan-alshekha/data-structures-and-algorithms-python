
from data_structures_and_algorithms.data_structures.graphs.graph import Graph
from data_structures_and_algorithms.data_structures.graphs.queue import Queue

def breadth_first(self,start_node):
    """
    Exteneded method to Graph class
    ______________________________________________
    Method to retreive the graph by breadth_first
    ______________________________________________
    start_node parameter is to decide from where you want to start, Its can be start at  any node
    visited - list to store the visisted nodes
    output  - list to store the nodes that we want to retreive
    q is Queue, its used to traverse over nodes 
    """
    visited = []
    output=[]
    q=Queue()
    visited.append(start_node)
    q.enqueue(start_node)
    graph=self.adjacency_list

    while len(q):
        current = q.dequeue()
        output.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.append(neighbor)
                q.enqueue(neighbor)
    return output



    
    # print("Appending new method was succeeded ")

Graph.breadth_first=breadth_first


if __name__ == "__main__":
    
# obj.new_method()

    g=Graph()
    g1=Graph()
    g.AddNode("a","b")
    g.AddNode("a","c")
    g.AddNode("a","d")    
    g.AddNode("b","c")
    g.AddNode("b","d")  
    g.AddNode("c","d") 
    g.AddNode("d","f")
    print(g.breadth_first("f"))
    print("breadth_first" in dir(Graph))