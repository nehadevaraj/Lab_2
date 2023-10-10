import pandas as pd
import matplotlib as plt

file = pd.read_csv('linear_data.csv')
x_axis = file ['X']
y_axis = file ['Y']

plt.plot(x_axis, y_axis)
plt.xlabel("X-Axis")
plt.yaxis("Y-Axis")
plt.show()