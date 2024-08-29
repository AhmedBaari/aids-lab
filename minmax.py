import math

# Minimax algorithm implementation
def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    # Base case: leaf node is reached
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = -math.inf

        # Recur for left and right children
        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        # Recur for left and right children
        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best

# Driver code
if __name__ == "__main__":
    # Values at the leaf nodes
    values = [3, 5, 6, 9, 1, 2, 0, -1]

    print("The optimal value is:", minimax(0, 0, True, values, -math.inf, math.inf))
