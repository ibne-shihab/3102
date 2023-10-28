from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, node, visited):
        visited[node] = True
        print(node, end=' ')

        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

# Create a graph
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 3)
graph.add_edge(1, 2)
graph.add_edge(1, 5)
graph.add_edge(2, 4)
graph.add_edge(2, 6)
graph.add_edge(2, 7)
graph.add_edge(3, 5)
graph.add_edge(4, 1)
graph.add_edge(4, 5)
graph.add_edge(5, 0)
graph.add_edge(6, 4)
graph.add_edge(6, 7)
graph.add_edge(7, 0)

# Starting from node 7
visited = [False] * len(graph.graph)
print("Depth-First Search:")
graph.dfs(7, visited)
