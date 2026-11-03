from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

RADIUS = 5.0
CURVATURE = 0.20
OFFSET = 2.0


def residuals(
    point,
    radius=RADIUS,
    curvature=CURVATURE,
    offset=OFFSET
):

    x, y = point

    return np.array([
        x**2 + y**2 - radius**2,
        y - (curvature * x**2 - offset)
    ])


def find_intersections(
    radius=RADIUS,
    curvature=CURVATURE,
    offset=OFFSET
):

    guesses = [
        [4.0, 2.0],
        [-4.0, 2.0]
    ]

    solutions = []

    for guess in guesses:

        result = root(
            lambda point: residuals(
                point,
                radius,
                curvature,
                offset
            ),
            guess,
            method="hybr",
            tol=1e-10
        )

        if (
            not result.success
            or np.linalg.norm(result.fun) > 1e-7
        ):

            raise RuntimeError(
                f"Solver failed: {result.message}"
            )

        solutions.append(result.x)

    # Remove duplicate solutions
    unique = []

    for point in solutions:

        if not any(
            np.linalg.norm(point - other) < 1e-6
            for other in unique
        ):

            unique.append(point)

    return unique


def main():

    intersections = find_intersections()

    # Increase radius from 5 to 5.5 metres
    changed_intersections = find_intersections(radius=5.5)

    print("TASK 12 - RESERVOIR AND EMBANKMENT INTERSECTIONS")

    print(f"Circle radius: {RADIUS:.2f} metres")

    print(
        f"Parabola: y = {CURVATURE:.2f}x² - {OFFSET:.2f}"
    )

    for index, point in enumerate(intersections, start=1):

        print(
            f"\nIntersection {index}: "
            f"x={point[0]:.6f}, y={point[1]:.6f}"
        )

        print("Residuals:", residuals(point))

    print("\nRadius increased to 5.5 metres")

    for index, point in enumerate(
        changed_intersections,
        start=1
    ):

        print(
            f"Changed intersection {index}: "
            f"x={point[0]:.6f}, y={point[1]:.6f}"
        )

    # Plot the circle and parabola
    x = np.linspace(-5.8, 5.8, 500)

    circle_y = np.sqrt(
        np.maximum(RADIUS**2 - x**2, 0)
    )

    parabola_y = CURVATURE * x**2 - OFFSET

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.plot(
        x,
        circle_y,
        label="Upper half of reservoir circle"
    )

    ax.plot(
        x,
        -circle_y,
        label="Lower half of reservoir circle"
    )

    ax.plot(
        x,
        parabola_y,
        label="Parabolic embankment"
    )

    points = np.array(intersections)

    ax.scatter(
        points[:, 0],
        points[:, 1],
        color="red",
        label="Intersection points",
        zorder=3
    )

    ax.set_xlabel("Horizontal Position x (m)")
    ax.set_ylabel("Vertical Position y (m)")

    ax.set_title(
        "Reservoir Boundary and Embankment Intersections"
    )

    ax.set_xlim(-5.8, 5.8)
    ax.set_ylim(-5.8, 5.8)

    ax.set_aspect("equal", adjustable="box")

    ax.legend()
    ax.grid(True, alpha=0.3)

    fig.tight_layout()

    fig.savefig(
        OUTPUT_DIR / "task_12_intersections.png",
        dpi=160
    )

    plt.close(fig)


if __name__ == "__main__":
    main()
