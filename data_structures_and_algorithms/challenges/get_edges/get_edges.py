from data_structures_and_algorithms.data_structures.graphs.graph import Graph

def getEdge(self,graph,arr):
    keys=list(graph.adjacency_list.keys())

    cost=0
    for x,i in enumerate(arr):
        if x+1 == len(arr):
            break
        if arr[x+1] in graph.adjacency_list[i] :
            # print("YEs")
            cost +=graph.getweight(i,arr[x+1])

        else:
            return 'False, $0'
    cost = '$'+ str(cost)
    print(cost)
    return f'True, {cost}'


# Assign getEdge function to be a class method for Graph
Graph.getEdge=getEdge




if __name__ == "__main__":
    pass