# Original Code by Shriram Jayakar

def color_graph(assignment, graph, colors):
    # If all nodes are assigned a color, return the assignment
    if all(color != -1 for color in assignment.values()):
        return assignment

    # Pick the next unassigned node
    node = next((n for n in assignment if assignment[n] == -1), None)

    # Try assigning each color
    for color_index in range(len(colors)):
        if all(assignment[neighbor] != color_index for neighbor in graph[node]):
            assignment[node] = color_index
            if result := color_graph(assignment, graph, colors):
                return result
            assignment[node] = -1  # backtrack

    return None

# Graph structure and available colors
graph = {'a': ['b', 'c'], 'b': ['a', 'c', 'd', 'e'], 'c': ['b', 'e'], 'd': ['a', 'b', 'e'], 'e': ['b', 'c', 'd']}
colors = ["Red", "Green", "Blue"]

# Initialize assignment (-1 means no color assigned)
solution = color_graph({node: -1 for node in graph}, graph, colors)

# Print solution if found, else indicate no solution
if solution:
    for node in solution:
        print(f"Node: {node}\tColor: {colors[solution[node]]}")
else:
    print("No solution exists")
