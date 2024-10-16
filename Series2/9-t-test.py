import numpy as np
import seaborn as sns
df = sns.load_dataset("tips")
population = df["total_bill"]
n = int(input("Enter No. of Samples:"))
sample = np.random.choice(population, size = n, replace = True)
sample_mean = sample.mean()
population_mean = population.mean()
standard_deviation = sample.std()
t = (sample_mean - population_mean) / (standard_deviation/np.sqrt(n))
print(f'Sample Mean: {sample_mean}')
print(f'Population Mean: {population_mean}')
print(f'Standard Deviation: {standard_deviation}')
print(f'T-statistic: {t}')
alpha = 0.05
if(abs(t) <= 1.96):
    print("Accept the Null Hypothesis")
else:
    print("Reject the Null Hypothesis")