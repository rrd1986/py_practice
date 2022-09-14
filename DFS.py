from typing import Dict


class Graph:
    def __init__(self, nodes: int, vertices: int) -> None:
        self.nodes = nodes
        self.vertices = vertices
        self.adj_matrix = [[0 for j in range(nodes)] for i in range(nodes)]

    def add_edge(self, start_node_no, end_node_no):
        self.adj_matrix[start_node_no][end_node_no] = 1
        self.adj_matrix[end_node_no][start_node_no] = 1

   
    def DFS(self, start_node: int, visited: Dict[int, bool]):
        # mark start_node as visited
        visited[start_node] = True
        print(f'{start_node} \n')
        for i in range(self.nodes):
            if self.adj_matrix[start_node][i] == 1 and visited[i] != True:
                self.DFS(i, visited)

if __name__ == "__main__":
    G = Graph(5, 4)

    print(G.adj_matrix)
    G.add_edge(0, 1)
    G.add_edge(0, 2)
    G.add_edge(0, 3)
    G.add_edge(0, 4)

    # visited = [False] * 5

    # visited = {k:v for k,v in zip([i for i in range(5)], [False for i in range(5)])}
    
    visited = {k:False for k in range(5)}

    G.DFS(0, visited)
