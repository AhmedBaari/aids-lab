from collections import defaultdict

class Graph:
    def __init__(self):
        self.graphlist = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graphlist[u].append(v)
    
    def DLS(self, s, t, depth):
        if s == t:
            return True
        if depth <= 0:
            return False
        for neighbor in self.graphlist[s]:
            if self.DLS(neighbor, t, depth - 1):
                return True
        return False
    
    def IDDFS(self, s, t, max_depth):
        for depth in range(max_depth + 1):
            if self.DLS(s, t, depth):
                return True
        return False

# Hardcoded graph
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)

# Define start, target, and maximum depth
start = 0
target = 5
max_depth = 3

if g.IDDFS(start, target, max_depth):
    print("Target is reachable")
else:
    print("Target is not reachable")
