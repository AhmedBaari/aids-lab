import numpy as np
import seaborn as sns
df = sns.load_dataset("tips")
a = df["total_bill"].to_numpy()
b = df["tip"].to_numpy()
pop = np.array([*a, *b])
mean_x = a.mean()
mean_y = b.mean()
vbg = 0
for x in [mean_x, mean_y]:
    vbg+=len(a)*(x - mean_x)**2
def var(a, mean_x):
    vari = 0
    for x in a:
        vari+=(x - mean_x)**2
    return vari 
if(round(vbg, 2) / round(var(a, mean_x), 2) + round(var(b, mean_y), 2) < 1):
    print("Acept Ho")
else:
    print("Reject No")