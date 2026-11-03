
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# RC charging circuit:
# dV/dt = (Vs - V)/(R*C)

Vs = 5.0          # Supply voltage (V)
R = 1000.0        # Resistance (ohms)
C = 0.001         # Capacitance (farads)
V0 = 0.0          # Initial capacitor voltage

# Define the differential equation
def rc_circuit(t, V):
    return [(Vs - V[0]) / (R * C)]

# Time values for the solution
t_eval = np.linspace(0, 5, 200)

# Solve the differential equation using SciPy
solution = solve_ivp(
    rc_circuit,
    (0, 5),
    [V0],
    t_eval=t_eval,
    rtol=1e-9,
    atol=1e-11
)

# Exact RC charging curve for comparison
exact = Vs * (1 - np.exp(-solution.t / (R * C)))

# Display results
print("NUMERICAL SOLUTION OF ODEs USING SCIPY")
print("--------------------------------------")
print("Solver success:", solution.success)

print(
    f"Capacitor voltage at 5 seconds: "
    f"{solution.y[0, -1]:.4f} V"
)

print(
    f"Maximum error against exact solution: "
    f"{np.max(np.abs(solution.y[0] - exact)):.3e} V"
)

# Plot numerical and exact solutions
plt.plot(solution.t, solution.y[0], label="solve_ivp")
plt.plot(solution.t, exact, linestyle="--", label="Exact solution")

plt.xlabel("Time (seconds)")
plt.ylabel("Capacitor voltage (V)")
plt.title("RC Circuit Charging Using SciPy")
plt.legend()
plt.grid(True)
plt.show()
