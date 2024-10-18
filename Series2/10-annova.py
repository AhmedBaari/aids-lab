# Original code by Ahmed Baari

col1 = [1,2,3]
col2 = [4,5,6]
col3 = [7,8,9]

# T^2 is the square of sum of all the values in the column, for each column added together
t2 = sum(col1)**2 + sum(col2)**2 + sum(col3)**2

# G^2 is the square of the grand total
g2 = (sum(col1) + sum(col2) + sum(col3))**2

n = len(col1) # Number of samples in each column
N = len(col1) + len(col2) + len(col3)   # Total number of samples

SS_between = (t2 / n) - (g2 / N)

S_x2 = sum([x**2 for x in col1]) + sum([x**2 for x in col2]) + sum([x**2 for x in col3])

SS_within = S_x2 - t2 / N

k = 3 # Number of columns
df_between = k - 1
df_within = N - k

MS_between = SS_between / df_between
MS_within = SS_within / df_within

F = MS_between / MS_within

print(f'F-statistic: {F}')

# Hypothesis Test
critical_value = 3.885  # 2 tail
if F <= critical_value:
    print("Accept the Null Hypothesis")

else:
    print("Reject the Null Hypothesis")
