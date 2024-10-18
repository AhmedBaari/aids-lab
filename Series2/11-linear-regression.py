
# `AHMEDBAARI/AIDS-LAB/SERIES2/LINEAR-REGRESSION`
# 1. Import the dataset and libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

# Let's import the dataset and see what it looks like.
df = sns.load_dataset('tips')
df.head()

# 2. Data Analysis
plt.plot(df['total_bill'], df['tip'], 'o')

# 3. Features and Targets
X = df[['total_bill']]
y = df['tip']

# 4. Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Test the Model
total_bill = 50
tip = model.predict([[total_bill]])


# Make predictions on the test set
y_pred = model.predict(X_test)

# Plot the data and the model
plt.plot(X_test, y_test, 'o')
plt.plot(X_test, y_pred, 'o')
plt.show()

# 7. Evaluate the Model  
# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)

# **Optional:** Show the line equation
print('Intercept:', model.intercept_)
print('Slope:', model.coef_)
print('LINE EQUATION: y = (', model.coef_[0], ') x +', model.intercept_)

# R-squared
r2 = model.score(X_test, y_test)
r2