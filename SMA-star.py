import heapq

class Node:
    def __init__(self, name, h):
        self.name = name        # Name of the node
        self.h = h              # Heuristic value (estimated cost to goal)
        self.g = float('inf')   # Actual cost from the start node
        self.f = float('inf')   # Estimated total cost (g + h)
        self.parent = None      # Parent node in the path

    def __lt__(self, other):
        return self.f < other.f # Nodes are compared based on their f value for the priority queue

def sma_star(start, goal, memory_limit):
    start.g = 0               # Cost from start to start is 0
    start.f = start.h         # Initial f value is the heuristic
    frontier = [start]        # Priority queue to store frontier nodes
    closed = set()            # Set to store explored nodes

    while frontier:
        if len(frontier) > memory_limit:
            # Remove node with the highest f value when memory limit is exceeded
            max_f_node = max(frontier, key=lambda node: node.f)
            frontier.remove(max_f_node)
            closed.add(max_f_node)

        current = heapq.heappop(frontier)  # Get the node with the lowest f value
        if current.name == goal.name:
            return reconstruct_path(current)  # Goal reached, return the path

        closed.add(current)  # Mark current node as explored

        for neighbor, cost in current.neighbors:
            if neighbor in closed:
                continue  # Skip already explored nodes

            tentative_g = current.g + cost
            if tentative_g < neighbor.g:
                neighbor.g = tentative_g
                neighbor.f = max(neighbor.g + neighbor.h, current.f)
                neighbor.parent = current

                if neighbor not in frontier:
                    heapq.heappush(frontier, neighbor)  # Add new node to the frontier

    return None  # Return None if no path is found

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.name)
        node = node.parent
    return path[::-1]  # Return the path from start to goal

# Example usage:
# Define nodes with their heuristic values (h)
node_a = Node('A', h=4)
node_b = Node('B', h=2)
node_c = Node('C', h=2)
node_d = Node('D', h=0)  # Goal

# Define neighbors with their respective costs
node_a.neighbors = [(node_b, 1), (node_c, 3)]
node_b.neighbors = [(node_d, 1)]
node_c.neighbors = [(node_d, 1)]

# Perform SMA* with a memory limit
path = sma_star(node_a, node_d, memory_limit=3)

print(f"Path: {path}")
