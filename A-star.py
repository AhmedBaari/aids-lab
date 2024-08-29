from queue import PriorityQueue

def a_star(graph, start, goal, heuristic):
    open_set = PriorityQueue()
    open_set.put((0, start))
    g_costs = {start: 0}
    parents = {start: None}
    
    while not open_set.empty():
        _, current = open_set.get()
        
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1]
        
        for neighbor, weight in graph.get(current, []):
            g = g_costs[current] + weight
            if g < g_costs.get(neighbor, float('inf')):
                g_costs[neighbor] = g
                f = g + heuristic[neighbor]
                open_set.put((f, neighbor))
                parents[neighbor] = current
    
    return None

# Heuristic function and graph definition
heuristic = {
    'A': 11,
    'B': 6,
    'C': 99,
    'D': 1,
    'E': 7,
    'G': 0
}

graph = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'E': [('D', 6)],
    'D': [('G', 1)],
}

# Running the A* algorithm
path = a_star(graph, 'A', 'G', heuristic)
print(f"Path found: {path}")
