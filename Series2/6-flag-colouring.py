def fun(assign, graph, colors):
    if all(i != -1 for i in assign.values()):
        return assign
    var = next((i for i in assign if assign[i] == -1), None)
    for i in range(len(colors)):
        if all(assign[j] != i for j in graph[var]):
            assign[var] = i
            if result := fun(assign, graph, colors):
                return result
            assign[var] = -1
    return None
graph = {'a': ['b', 'c'], 'b': ['a', 'c', 'd', 'e'], 'c': ['b', 'e'], 'd': ['a', 'b', 'e'], 'e': ['b', 'c', 'd']}
colors = ["Red", "Green", "Blue"]
sol = fun({i: -1 for i in graph}, graph, colors)
if sol:
    for node in sol:
        print("Node:", node, "\tColor:", colors[sol[node]])
else:
    print("No solution exists")