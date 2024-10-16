import heapq

def heuristic(node):
    h = {'A': 10, 'B': 15, 'C': 5, 'D': 5, 'E': 10, 'F': 0}
    return h[node]

def astar(graph, start, goal):
    pq = []
    visited = set()
    heapq.heappush(pq, (heuristic(start), start, None, 0))
    while pq:
        _, current, parent, g_cost = heapq.heappop(pq)
        visited.add(current)
        if current == goal:
            path = []
            while current:
                path.insert(0, current)
                current = None
                if parent:
                    current, parent, _ = parent
            return path
        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                #if neighbor not in (node for _, node, _, _ in pq):
                heapq.heappush(pq, (g_cost + cost + heuristic(neighbor), neighbor, (current, parent, g_cost), g_cost + cost))
    return None

graph = { 'A': [('B', 10), ('D', 5), ('C', 12)], 'B': [('E', 11)], 'C': [('D', 5), ('E', 11), ('F', 8)], 'D': [('F', 14)], 'E': [] }
path = astar(graph, 'A', 'F')
if path:
    print("Path found:", path)
else:
    print("Path not found")