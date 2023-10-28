import numpy as np
import matplotlib.pyplot as plt

# Sample data
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
y = np.array([2, 3, 5, 6, 5, 8, 9, 10, 11, 12,13])

# Perform linear regression
slope, intercept = np.polyfit(x, y, 1)

# Predict the y values using the regression line
y_pred = slope * x + intercept

# Plot the data and regression line
plt.scatter(x, y, label='Data Points')
plt.plot(x, y_pred, color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
