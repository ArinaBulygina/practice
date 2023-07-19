def find_paths(graph, start, end, path):
    path = path + [start]
    paths = []
    if start == end:
        return [path]
    if not graph.get(start):
        return []
    for neighbor in graph[start]:
        new_paths = find_paths(graph, neighbor, end, path)
        paths.extend(new_paths)
    return paths


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start = 'A'
end = 'F'
path = []

paths = find_paths(graph, start, end, path)
print(*paths)
