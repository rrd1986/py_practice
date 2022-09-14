from typing import List

# import dictionary for graph
from collections import defaultdict


class Graph:
    def __init__(self, nodes: List[str]):
        self.nodes = nodes
        self.adjacency_list = {}
        for n in nodes:
            self.adjacency_list[n]  = []

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)


    def dfs(self, start_node: str) -> List[str]:
        visited = {}
        level = {}
        parent = {}
        dfs_path = []
        from queue import Queue
        q = Queue()

        for node in self.nodes:
            visited[node] = False
            level[node] = -1
            parent[node] = None

        q.put(start_node)
        visited[start_node] = True
        level[start_node] = 0


        while not q.empty():
            node = q.get()
            dfs_path.append(node)
            for n in self.adjacency_list[node]:
                if not visited[n]:
                    visited[n] = True
                    parent[n] = node
                    level[n] = level[u] + 1
                    q.put(n)
        
        return dfs_path

        



if __name__ == "__main__":
    graph = Graph(["A", "B", "C", "D", "E"])
    all_edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("C", "E"), ("D", "E")]
    for u,v in all_edges:
        graph.add_edge(u,v)
    print(graph.adjacency_list)
    dfs_path = graph.dfs("A")
    print(dfs_path)
























'''
# function for adding edge to graph 
graph = defaultdict(list) # this will be {a:[],  }

def addEdge(graph,u,v):
    graph[u].append(v)
  
# definition of function
def generate_edges(graph):
    edges = []
  
    # for each node in graph
    for node in graph:
          
        # for each neighbour node of a single node
        for neighbour in graph[node]:
              
            # if edge exists then append
            edges.append((node, neighbour))
    return edges
  
# declaration of graph as dictionary
addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'b','e')
addEdge(graph,'c','d')
addEdge(graph,'c','e')
addEdge(graph,'c','a')
addEdge(graph,'c','b')
addEdge(graph,'e','b')
addEdge(graph,'d','c')
addEdge(graph,'e','c')
  
# Driver Function call 
# to print generated graph
print(generate_edges(graph))

print(f"adjacency list: {graph}")
'''