
import numpy as np
import matplotlib.pyplot as plt

# GPS samples: time in seconds and position in metres
time = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)

position = np.array([
    0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0
])

# Create an array to store estimated speeds
speed = np.zeros_like(position)

# Forward difference at the beginning
speed[0] = (
    (position[1] - position[0]) /
    (time[1] - time[0])
)

# Central differences for interior points
for i in range(1, len(time) - 1):
    speed[i] = (
        (position[i + 1] - position[i - 1]) /
        (time[i + 1] - time[i - 1])
    )

# Backward difference at the end
speed[-1] = (
    (position[-1] - position[-2]) /
    (time[-1] - time[-2])
)

# Display the results
print("NUMERICAL DIFFERENTIATION: GPS VEHICLE SPEED")
print("--------------------------------------------")

for t, x, v in zip(time, position, speed):
    print(
        f"Time: {t:.0f}s | "
        f"Position: {x:.1f}m | "
        f"Estimated speed: {v:.2f}m/s"
    )

# Plot estimated speed against time
plt.plot(time, speed, marker="o")

plt.xlabel("Time (seconds)")
plt.ylabel("Estimated speed (m/s)")
plt.title("Vehicle Speed Estimated from GPS Position Data")

plt.grid(True)
plt.show()
