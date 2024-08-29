def depth_limited_search(graph, start, goal, limit):
    queue = [[start]]
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node == goal:
            return path
        
        if len(path) <= limit:
            for neighbor in graph[node]:
                queue.append(path + [neighbor])
                
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

start = 'A'
goal = 'G'
limit = 3

path = depth_limited_search(graph, start, goal, limit)
print(path)
