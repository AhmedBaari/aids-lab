from collections import defaultdict

# Define the graph as a dictionary of lists
graph = {
    0: [1, 2],
    1: [3],
    2: [4],
    3: [5],
    4: [5],
    5: []
}

def DLS(graph, s, t, depth):
    if s == t:
        return True
    if depth <= 0:
        return False
    for neighbor in graph[s]:
        if DLS(graph, neighbor, t, depth - 1):
            return True
    return False

def IDDFS(graph, s, t, max_depth):
    for depth in range(max_depth + 1):
        if DLS(graph, s, t, depth):
            return True
    return False

# Define start, target, and maximum depth
start = 0
target = 5
max_depth = 3

if IDDFS(graph, start, target, max_depth):
    print("Target is reachable")
else:
    print("Target is not reachable")
