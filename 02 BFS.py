from collections import deque
def bfs(graph, start_node):
    visited = set()
    queue = deque()

    visited.add(start_node)
    queue.append(start_node)

    while queue:
        current_node = queue.popleft()
        print(current_node, end=' ')

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    0: [1, 3],
    1: [2, 5],
    2: [4, 6],
    3: [5],
    4: [1,5],
    5: [0],
    6: [4]
}
start_node=int(input("Enter the node from where you want to start: "))
print("Breadth First Traversal (starting from node",start_node ,"):", end=' ')
bfs(graph,start_node)
