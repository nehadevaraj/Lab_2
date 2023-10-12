import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv('linear_data.csv')
x_axis = file ['X']
y_axis = file ['Y']

plt.scatter(x_axis, y_axis)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()

#find correlation coefficient
# unit testing after (separate file)