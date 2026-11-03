
import numpy as np
import matplotlib.pyplot as plt

# Generate reproducible random numbers
rng = np.random.default_rng(42)

# Server configuration
capacity = 1000.0
mean_demand = 850.0
std_demand = 120.0
N = 100_000

# Generate random demand scenarios
demand = rng.normal(mean_demand, std_demand, N)

# Identify overloaded scenarios
overloaded = demand > capacity

# Estimate overload probability
overload_probability = overloaded.mean()

# Display results
print("MONTE CARLO SIMULATION: SERVER OVERLOAD RISK")
print("--------------------------------------------")
print(f"Estimated overload probability: {overload_probability:.4%}")
print(f"Number of overload cases: {overloaded.sum()} out of {N}")

# Calculate running probability to show convergence
running_probability = np.cumsum(overloaded) / np.arange(1, N + 1)

# Select points for plotting
indices = np.unique(
    np.logspace(1, np.log10(N), 200).astype(int)
) - 1

# Plot estimated probability as simulations increase
plt.semilogx(
    indices + 1,
    running_probability[indices]
)

plt.xlabel("Number of simulations")
plt.ylabel("Estimated overload probability")
plt.title("Monte Carlo Estimate of Server-Overload Risk")
plt.grid(True)
plt.show()
