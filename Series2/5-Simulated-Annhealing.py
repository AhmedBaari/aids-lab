import math
import random

def simulated_annealing(arr, temp, a, n):
    cur = sum(x ** 2 for x in arr) # sum of squares
    res = arr # best solution so far
    cost = cur # cost of best solution found so far

    # Perform siman
    for _ in range(n):
        tempres = [x + random.uniform(-1, 1) for x in arr] # adds rand bet -1 and 1 (rand nums)
        tempcost = sum(x ** 2 for x in tempres) # sum of squares. Cost of new solution

        """This line checks if the new solution is better than the current solution (tempcost - cur < 0) or if a random number is less than the acceptance probability calculated using the simulated annealing formula. If either condition is true, the new solution is accepted."""
        if tempcost - cur < 0 or random.random() < math.exp(-(tempcost - cur) / temp):
            arr = tempres 
            cur = tempcost
            if cur < cost: # is cost of newsol lesser than bestsol
                res = arr  
                cost = cur 
        temp *= a # temp * cooling factor

    return res, cost

res, cost = simulated_annealing([300.0, 400.0], 1000.0, 0.95, 500)
print("Best solution:", res)
print("Cost of the best solution:", cost)