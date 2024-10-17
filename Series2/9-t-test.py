import numpy as np
import seaborn as sns

# Load the dataset and extract the "total_bill" column as population data
df = sns.load_dataset("tips")
population = df["total_bill"]

# Get the number of samples from user input
n = int(input("Enter No. of Samples:"))

# Draw a random sample with replacement from the population
sample = np.random.choice(population, size=n, replace=True)
# replace=True is to put back after selection

# Calculate the sample mean, population mean, and sample standard deviation
sample_mean = sample.mean() # X_bar
population_mean = population.mean() # U
# STD of SAMPLE
standard_deviation = sample.std() 

# Calculate the t-statistic
t = (sample_mean - population_mean) / \
    (standard_deviation / np.sqrt(n))

# Print results
print(f'Sample Mean: {sample_mean}')
print(f'Population Mean: {population_mean}')
print(f'Standard Deviation: {standard_deviation}')
print(f'T-statistic: {t}')

# Perform the hypothesis test (assuming alpha = 0.05, two-tailed test, critical value = ±1.96)
alpha = 0.05
critical_value = 1.96  # Critical value for 95% confidence level (two-tailed)
if abs(t) <= critical_value:
    print("Accept the Null Hypothesis")
else:
    print("Reject the Null Hypothesis")
