graph = {
    's': [('A', 2), ('B', 3), ('D', 5)],
    'A': [('C', 4)],
    'B': [('D', 4)],
    'C': [('D', 1), ('G', 2)],
    'D': [('G', 5)]
}

def path_cost(path):
    return sum(cost for node, cost in path), path[-1][0]

def ucs(graph, start, goal):
    visited = set()
    queue = [[(start, 0)]]
    
    while queue:
        queue.sort(key=path_cost)
        path = queue.pop(0)
        node = path[-1][0]
        
        if node in visited:
            continue
        
        visited.add(node)
        
        if node == goal:
            return path
        
        for node2, cost in graph.get(node, []):
            new_path = path + [(node2, cost)]
            queue.append(new_path)

solution = ucs(graph, 's', 'G')
print("The solution is:", solution)
print("Cost of the solution is:", path_cost(solution)[0])
