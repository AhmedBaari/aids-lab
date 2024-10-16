def check(assign, loc):
    if (assign['c'] != -1 and assign['d'] != -1 and assign['c'] < assign['d']) or \
       (assign['d'] != -1 and assign['a'] != -1 and assign['a'] - assign['d'] != 1) or \
       (assign['d'] != -1 and assign['b'] != -1 and assign['d'] - assign['b'] == 1) or \
       (assign['c'] == 3) or (assign['b'] == 1) or (loc in assign.values()):
        return False
    return True
def fun(assign, locs):
    if check(assign ,-1):
        return assign
    i = next((i for i in assign if assign[i] == -1), None)
    for loc in locs:
        if check(assign, loc):
            assign[i] = loc
            if res := fun(assign, locs):
                return res
            assign[i] = -1
    return None
assign = {'a': -1, 'b': -1, 'c': -1, 'd': -1}
sol = fun(assign, [1, 2, 3, 4])
if sol:
    for node in sol:
        print(f"House: {node}\tlocation: {sol[node]}")
else:
    print("No Solution Exists!")