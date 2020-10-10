from data_structures_and_algorithms.data_structures.graphs.graph import Graph


def depthFirstSearch(self,graph,node):

    visited=[]
    def _walk(graph,node):
        visited.append(node)
        for node in graph.adjacency_list[node]:
            if node not in visited:
                _walk(graph,node)
    
    _walk(graph,node)
    return visited

Graph.dfs=depthFirstSearch


if __name__ == "__main__":
    pass