from math import sqrt


def find_a_path(graph, start, path=None):
    if path is None:
        path = []
    path = path + [start]
    if len(graph) == len(path):
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            new_path = find_a_path(graph, node, path)
            if new_path:
                return new_path
    return None


i = 1
connections = {}
while True:
    connections[i] = []
    for j in range(1, i):
        if sqrt(i + j).is_integer():
            connections[i] += [j]
            connections[j] += [i]
    found = None
    for start_point in range(1, i + 1):
        found = found or find_a_path(connections, start_point)
        if found:
            break
    print(i, ":", found)
    i += 1
