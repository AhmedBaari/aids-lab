import numpy as np
import seaborn as sns

# Load the dataset and extract the "total_bill" column as the population data
df = sns.load_dataset("tips")
population = df["total_bill"]

# Get the number of samples from user input
n = int(input("Enter No. of Samples:"))

# Draw a random sample with replacement from the population
sample = np.random.choice(population, size=n, replace=True)

# Calculate the sample mean and population mean
sample_mean = sample.mean()
population_mean = population.mean()

# Use population standard deviation since z-test assumes known population std dev
standard_deviation = population.std() 

# Calculate the z-statistic
z = (sample_mean - population_mean) / (standard_deviation / np.sqrt(n))

# Print results
print(f'Sample Mean: {sample_mean}')
print(f'Population Mean: {population_mean}')
print(f'Standard Deviation (Population): {standard_deviation}')
print(f'Z-statistic: {z}')

# Perform the hypothesis test (alpha = 0.05, two-tailed test, critical value = ±1.96)
critical_value = 1.96  # Z-critical value for 95% confidence
if abs(z) <= critical_value:
    print("Accept the Null Hypothesis")
else:
    print("Reject the Null Hypothesis")
