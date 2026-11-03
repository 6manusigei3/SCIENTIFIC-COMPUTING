
import numpy as np
from scipy.optimize import minimize

# x = number/capacity units of Type A server
# y = number/capacity units of Type B server
#
# Cost per unit: A = 12, B = 18
# Capacity per unit: A = 100, B = 170
# Required total capacity: at least 1000

# Objective function: minimize total operating cost
def cost(z):
    x, y = z
    return 12 * x + 18 * y

# Constraint: total capacity must be at least 1000
def capacity_constraint(z):
    x, y = z
    return 100 * x + 170 * y - 1000

constraints = {
    "type": "ineq",
    "fun": capacity_constraint
}

# Server allocations cannot be negative
bounds = [(0, None), (0, None)]

# Perform numerical optimization
solution = minimize(
    cost,
    x0=[5, 3],
    method="SLSQP",
    bounds=bounds,
    constraints=constraints
)

x, y = solution.x

# Display continuous optimization results
print("NUMERICAL OPTIMIZATION: CLOUD SERVER ALLOCATION")
print("------------------------------------------------")
print("Optimization success:", solution.success)
print(f"Type A allocation: {x:.3f}")
print(f"Type B allocation: {y:.3f}")
print(f"Total capacity: {100*x + 170*y:.2f}")
print(f"Minimum planning cost: {solution.fun:.2f}")

# If whole servers are required, test integer combinations
best_integer = None

for a in range(0, 20):
    for b in range(0, 20):
        capacity = 100 * a + 170 * b

        if capacity >= 1000:
            total_cost = 12 * a + 18 * b

            if best_integer is None or total_cost < best_integer[0]:
                best_integer = (total_cost, a, b, capacity)

print("\nBEST WHOLE-SERVER ALLOCATION")
print("----------------------------")
print("Cost, Type A, Type B, Capacity:", best_integer)
