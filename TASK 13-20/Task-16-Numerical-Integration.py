
import numpy as np
from scipy.integrate import simpson

# Smart-meter readings taken every two hours
# Time is measured in hours
time_hours = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)

# Power consumption in kilowatts
power_kw = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9])

# Calculate energy using the Trapezoidal Rule
energy_trapezoid = np.trapezoid(power_kw, time_hours)

# Calculate energy using Simpson's Rule
energy_simpson = simpson(power_kw, x=time_hours)

# Calculate the difference between the two estimates
difference = abs(energy_simpson - energy_trapezoid)

# Display results
print("NUMERICAL INTEGRATION: ELECTRICITY CONSUMPTION")
print("----------------------------------------------")

print(
    f"Energy using Trapezoidal Rule: "
    f"{energy_trapezoid:.3f} kWh"
)

print(
    f"Energy using Simpson's Rule: "
    f"{energy_simpson:.3f} kWh"
)

print(
    f"Difference between estimates: "
    f"{difference:.3f} kWh"
)
