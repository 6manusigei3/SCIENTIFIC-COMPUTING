
import numpy as np
import matplotlib.pyplot as plt

# TASK 13: INTERPOLATION
# Estimating temperature using Linear Interpolation

# 1. Known data points
# Time in hours
x = np.array([10, 14])

# Temperature in degrees Celsius
y = np.array([20, 28])

# 2. Point where temperature is to be estimated
target_time = 12

# 3. Linear interpolation formula
estimated_temperature = y[0] + (
    (target_time - x[0]) / (x[1] - x[0])
) * (y[1] - y[0])

# 4. Display the results
print("TASK 13: LINEAR INTERPOLATION")
print("--------------------------------")
print(f"Known time values: {x}")
print(f"Known temperatures: {y}")
print(f"Estimated time: {target_time}:00")
print(f"Estimated temperature: {estimated_temperature:.2f} °C")

# 5. Plot the known points and interpolation line
plt.scatter(x, y, color="blue", label="Known temperatures")

plt.plot(
    x,
    y,
    linestyle="--",
    color="green",
    label="Interpolation line"
)

plt.scatter(
    target_time,
    estimated_temperature,
    color="red",
    label="Estimated temperature",
    zorder=3
)

plt.annotate(
    f"{estimated_temperature:.2f} °C",
    (target_time, estimated_temperature),
    xytext=(8, 8),
    textcoords="offset points"
)

plt.title("Temperature Estimation Using Linear Interpolation")
plt.xlabel("Time (Hours)")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)

plt.show()

# 6. Parameter change experiment
# Change target_time from 12 to 11 and run again.
