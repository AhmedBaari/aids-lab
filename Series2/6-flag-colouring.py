def color_graph(assignment, graph, colors):
    # If all nodes are assigned a color, return the assignment
    if all(color != -1 for color in assignment.values()):
        return assignment

    # Pick the next unassigned node
    node = None
    for n, color in assignment.items():
        if color == -1:
            node = n
            break

    # Try assigning each color to the node
    for color_index in range(len(colors)):
        # Check if the color can be assigned to the node (no conflicts with neighbors)
        if all(assignment[neighbor] != color_index for neighbor in graph[node]):
            assignment[node] = color_index  # Assign color
            result = color_graph(assignment, graph, colors)  # Recurse with updated assignment
            if result:
                return result  # If a valid assignment is found, return it
            assignment[node] = -1  # Backtrack if no valid result

    return None  # No valid assignment found

# Define the graph and available colors
graph = {'a': ['b', 'c'], 'b': ['a', 'c', 'd', 'e'], 'c': ['b', 'e'], 'd': ['a', 'b', 'e'], 'e': ['b', 'c', 'd']}
colors = ["Red", "Green", "Blue"]

# Initialize the assignment with all nodes uncolored (-1 means no color assigned)
assignment = {node: -1 for node in graph}

# Call the function to find the solution
solution = color_graph(assignment, graph, colors)

# Output the result
if solution:
    for node, color_index in solution.items():
        print(f"Node: {node} -> Color: {colors[color_index]}")
else:
    print("No solution exists")
