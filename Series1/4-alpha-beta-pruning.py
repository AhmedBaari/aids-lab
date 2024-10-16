def alphabeta(node, graph, ismax, alpha=-float('inf'), beta=float('inf')):
    if isinstance(node, int):
        return node
    if ismax:
        opti = -float('inf')
        for child in graph[node]:
            val = alphabeta(child, graph, False, alpha, beta)
            opti = max(opti, val)
            alpha = max(alpha, opti)
            if alpha >= beta:
                break
    else:
        opti = float('inf')
        for child in graph[node]:
            val = alphabeta(child, graph, True, alpha, beta)
            opti = min(opti, val)
            beta = min(beta, opti)
            if alpha >= beta:
                break
    return opti
graph = {'A': ['B', 'C', 'D'], 'B': ['E', 'F'], 'C': ['G', 'H', 'I'], 'D': ['J', 'K'], 'E': [4, 3], 'F': [6, 2], 'G': [2, 1], 'H': [9, 5], 'I': [3, 1], 'J': [5, 4], 'K': [7, 5] }
print(alphabeta('A', graph, True))