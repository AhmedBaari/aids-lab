import math, random
def simulated_annealing(arr, temp, a, n):
    cur = sum(x**2 for x in arr)
    res = arr
    cost = cur
    for i in range(n):
        tempres = [x + random.uniform(-1, 1) for x in arr]
        tempcost = sum(x**2 for x in tempres)
        if tempcost - cur < 0 or random.random() < math.exp(-(tempcost - cur) / temp):
            arr = tempres
            cur = tempcost
            if cur < cost:
                res = arr
                cost = cur
        temp *= a
    return res, cost
res, cost = simulated_annealing([300.0, 400.0], 1000.0, 0.95, 500)
print("Best solution:", res,"\n", "Cost of the best solution:", cost)