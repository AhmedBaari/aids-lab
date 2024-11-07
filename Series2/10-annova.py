import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Load the dataset
data = pd.read_csv('acquiredDataset.csv')

# Set the significance level
alpha = 0.05

# Calculate the grand mean
grand_mean = data['attention'].mean()

# Group data by 'classification'
grouped_data = data.groupby('classification')

# Calculate SS Between (SSB) and MSB
ss_between = sum(len(group) * (group['attention'].mean() - grand_mean) ** 2 for _, group in grouped_data)
df_between = len(grouped_data) - 1
ms_between = ss_between / df_between

# Calculate SS Within (SSW) and MSW
ss_within = sum(((group['attention'] - group['attention'].mean()) ** 2).sum() for _, group in grouped_data)
df_within = len(data) - len(grouped_data)
ms_within = ss_within / df_within

# Calculate F-statistic
F_statistic = ms_between / ms_within

# Determine the critical value
critical_value = stats.f.ppf(1 - alpha, df_between, df_within)

# Print ANOVA results
print("ANOVA Results:")
print(f"F Statistic: {F_statistic:.2f}")
print(f"Critical Value: {critical_value:.2f}")

# Decision
if F_statistic > critical_value:
    print("Reject the null hypothesis. There is a significant difference between the group means.")
else:
    print("Fail to reject the null hypothesis. No significant difference between group means.")

# Plot the F-distribution
x = np.linspace(0, F_statistic + 2, 500)
y = stats.f.pdf(x, df_between, df_within)

plt.plot(x, y, label='F-distribution')
plt.axvline(F_statistic, color='red', label=f'F-statistic = {F_statistic:.2f}')
plt.axvline(critical_value, color='green', linestyle='--', label=f'Critical F-value = {critical_value:.2f}')
plt.xlabel('F-value')
plt.ylabel('Probability Density')
plt.title('F-distribution with F-statistic and Critical Value')
plt.legend()
plt.show()
