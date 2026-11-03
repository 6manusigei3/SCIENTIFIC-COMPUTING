
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Concurrent users and measured server response time (milliseconds)
users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
response_ms = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)

# A quadratic model for increasing server response time
def model(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the model to the measured data
parameters, covariance = curve_fit(model, users, response_ms)

a, b, c = parameters

# Calculate predicted response times
predicted = model(users, a, b, c)

# Calculate Root Mean Square Error (RMSE)
rmse = np.sqrt(np.mean((response_ms - predicted)**2))

# Predict response time for a chosen number of users
prediction_users = 400
future_prediction = model(prediction_users, a, b, c)

# Display results
print("CURVE FITTING: SERVER RESPONSE TIME")
print("-----------------------------------")

print(f"Fitted model: y = {a:.6f}x^2 + {b:.4f}x + {c:.2f}")
print(f"RMSE: {rmse:.2f} ms")

print(
    f"Predicted response time at {prediction_users} users: "
    f"{future_prediction:.2f} ms"
)

# Generate points for drawing the fitted curve
x_plot = np.linspace(users.min(), prediction_users, 300)

# Plot measured data and fitted curve
plt.scatter(users, response_ms, label="Measured response times")
plt.plot(x_plot, model(x_plot, a, b, c), label="Fitted quadratic curve")

plt.xlabel("Number of concurrent users")
plt.ylabel("Server response time (milliseconds)")
plt.title("Server Response-Time Curve Fitting")

plt.legend()
plt.grid(True)
plt.show()
