class Node:
    def __init__(self,data):
        self.data=data


class Graph:

    def __init__(self,made_up_graph={}):
        self.adjacency_list=dict()
        self.edgs={}

    def AddNode(self,data1,data2):
        node = Node(data1)
        neighbors_node=Node(data2)
        
        def node_add(node,neighbors_node):
           
            if node.data in self.adjacency_list.keys():
                print("appended")
                self.adjacency_list[node.data].append(neighbors_node.data)
            else :
                print("new_add")
                
                self.adjacency_list[node.data]=[neighbors_node.data]
            
        node_add(node,neighbors_node)
        node_add(neighbors_node,node)

        return f"A node with {data1} and another node with {data2} was added to the graph"
        
    
    def AddEdge(self,f_node,sec_node,weight=1):

        
        keys=self.adjacency_list.keys()

            
        def add_edg(vertex,linked_node,weight):
            if vertex in self.edgs.keys():
                self.edgs[vertex].append((linked_node,weight))
                
            else:
                self.edgs[vertex]=[(linked_node,weight)]
        if f_node in keys and sec_node in keys :
            """
            To ensure the keys alraedy exist in graph
            """
            if f_node in self.adjacency_list[sec_node]:
                """
                To ensure the two nodes are connected together
                """
                add_edg(f_node,sec_node,weight)
                add_edg(sec_node,f_node,weight)
            return f"Edg was added successfully between {f_node} and {sec_node} with weight = {weight}"

        else:
            return "either nodes are not connected or one of them not exist in the graph"
        

    def GetNodes(self):
       
        return self.adjacency_list.keys()


        

    def GetNeighbors(self,node):
        return self.edgs[node]

        
    def getweight(self,s_node,l_node):
        if l_node in self.edgs.keys():
            print(self.edgs[s_node])
            for i in self.edgs[s_node]:
                if l_node == i[0]:
                    
                    # print(i[1])
                    return i[1]
            pass

    def Size(self):
        return len(self.adjacency_list.keys())
        # pass


if __name__ == "__main__":
    g=Graph()
    g1=Graph()
    g.AddNode("a","b")
    g.AddNode("a","c")
    g.AddNode("a","d")    
    g.AddNode("b","c")
    g.AddNode("b","d")  
    g.AddNode("c","d") 
    g.AddNode("d","f") 
    g1.AddNode("1","2")
    g1.AddNode("1","3")
    g1.AddNode("1","4")
    g1.AddNode("2","3")


    g.AddEdge("a","b",800)
    g.AddEdge("a","c",100)
    g.AddEdge("a","d",50)
    g.AddEdge("b","c",25)
    g.AddEdge("b","d",10)
    g.AddEdge("c","d",16)
    g.AddEdge("d","f",17)
    
    print(g.edgs)
    g.getweight("a","b")