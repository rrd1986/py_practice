class Graph:
    def __init__(self, v: int ):  # v is no of vertices
        self.v = v
        self.adj_matrix = [[0 for i in range(v) ] for j in range(v)]


    def add_edge(self, s, e):
        self.adj_matrix[s][e] = 1
        self.adj_matrix[e][s] = 1

    def DFS(self, start, visited):

        print(f"{start} \n")
        visited[start] = True
        
        for i in range(self.v):
            if self.adj_matrix[start][i] == 1 and not visited[i]:
                self.DFS(i, visited)
            

if __name__ == "__main__":
    G = Graph(5)
    print(G.adj_matrix)
    G.add_edge(0, 1)
    G.add_edge(0, 2)
    G.add_edge(0, 3)
    G.add_edge(0, 4)
    
    # Visited vector to so that a vertex
    # is not visited more than once
    # Initializing the vector to false as no
    # vertex is visited at the beginning
    visited = [False] * 5
    
    # Perform DFS
    G.DFS(0, visited);