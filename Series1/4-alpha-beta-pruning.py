def alphabeta(node, graph, ismax, alpha=-float('inf'), beta=float('inf')):
    # Base case: if the node is a leaf (integer value), return it
    if isinstance(node, int):
        return node

    # Maximizing player's turn
    if ismax:
        for child in graph[node]:
            value = alphabeta(child, graph, False, alpha, beta)
            alpha = max(alpha, value)

            if alpha >= beta:
                break
        return alpha

    # Minimizing player's turn
    else:
        for child in graph[node]:
            value = alphabeta(child, graph, True, alpha, beta)
            beta = min(beta,value)

            if alpha >= beta:
                break
        return beta

# Example game tree
graph = {
    'A': ['B', 'C', 'D'], 
    'B': ['E', 'F'], 
    'C': ['G', 'H', 'I'], 
    'D': ['J', 'K'], 
    'E': [4, 3], 
    'F': [6, 2], 
    'G': [2, 1], 
    'H': [9, 5], 
    'I': [3, 1], 
    'J': [5, 4], 
    'K': [7, 5] 
}

# Run the alphabeta pruning starting from the root node
print(alphabeta('A', graph, True))
