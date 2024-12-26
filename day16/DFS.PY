#Python program to find dfs
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()  
    visited.add(start)
    print(start, end=" ")  


    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [6],
    6: []
}
print("DFS (Recursive) traversal starting from node 1:")
dfs_recursive(graph, 1)
print()
