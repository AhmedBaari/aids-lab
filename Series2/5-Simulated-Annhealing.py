# Original code by Shriram Jayakar

import math
import random

def simulated_annealing(arr, temperature, a, n):
    """Simulated Annhealing
    a: cooling factor
    n: no. of iterations
    arr: the array to optimize
    """
    current_cost = sum(x**2 for x in arr) # sum of squares
    best_res = arr # best solution so far
    best_cost = current_cost # cost of best solution found so far

    # Perform siman
    for _ in range(n):
        result = [
            x + random.uniform(-1,1) for x in arr
        ]
        cost = sum(x**2 for x in result)

        # Check if better, or accept by probability
        """Checks if the new solution is better than the current solution (tempcost - cur < 0) or if a random number is less than the acceptance probability calculated using the simulated annealing formula. If either condition is true, the new solution is accepted."""
        if (cost - current_cost) < 0 or \
        (random.random() < math.exp(-(cost - current_cost)/temperature)):
            # Change the current array
            arr = result
            current_cost = cost 

            # If it is better than best sol. as well, then update that
            if current_cost < best_cost:
                best_res = arr
                best_cost = current_cost

        # as always, temperature = temperature * cooling factor
        temp *= a # temp * cooling factor

    return best_res, best_cost

res, cost = simulated_annealing([300.0, 400.0], 1000.0, 0.95, 500)
print("Best solution:", res)
print("Cost of the best solution:", cost)