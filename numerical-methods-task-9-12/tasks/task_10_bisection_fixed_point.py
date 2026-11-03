from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

AMBIENT_TEMPERATURE = 22.0
HEAT_GAIN = 14.0
TEMPERATURE_SCALE = 25.0


def heat_balance(temperature, heat_gain=HEAT_GAIN):

    return (
        temperature
        - AMBIENT_TEMPERATURE
        - heat_gain * np.exp(-temperature / TEMPERATURE_SCALE)
    )


def fixed_point(
    initial_guess=30.0,
    heat_gain=HEAT_GAIN,
    tolerance=1e-10,
    max_iterations=500
):

    def g(temp):
        return (
            AMBIENT_TEMPERATURE
            + heat_gain * np.exp(-temp / TEMPERATURE_SCALE)
        )

    current = float(initial_guess)

    history = [current]

    for _ in range(max_iterations):

        updated = float(g(current))

        history.append(updated)

        if abs(updated - current) < tolerance:
            return updated, history

        current = updated

    raise RuntimeError("Fixed-point iteration did not converge.")


def main():

    bracket = (20.0, 50.0)

    # Bisection method
    bisection = root_scalar(
        heat_balance,
        bracket=bracket,
        method="bisect",
        xtol=1e-10
    )

    # Fixed-point method
    fixed_temperature, history = fixed_point()

    # Change heat gain from 14 to 18
    changed_gain = 18.0

    changed = root_scalar(
        lambda t: heat_balance(t, changed_gain),
        bracket=bracket,
        method="bisect",
        xtol=1e-10
    )

    print("TASK 10 - GREENHOUSE TEMPERATURE EQUILIBRIUM")

    print("Ambient temperature:", AMBIENT_TEMPERATURE)

    print("Heat gain:", HEAT_GAIN)

    print(
        f"Bisection equilibrium: {bisection.root:.6f} °C"
    )

    print(
        f"Fixed-point equilibrium: {fixed_temperature:.6f} °C"
    )

    print(
        f"Bisection iterations: {bisection.iterations}"
    )

    print(
        f"Fixed-point iterations: {len(history) - 1}"
    )

    print(
        f"Residual: {heat_balance(bisection.root):.3e}"
    )

    print(
        f"Equilibrium with heat gain 18: {changed.root:.6f} °C"
    )

    # Plot heat balance
    temperatures = np.linspace(*bracket, 400)

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(
        temperatures,
        heat_balance(temperatures),
        label="Heat-balance residual"
    )

    ax.axhline(0, color="black", linewidth=0.8)

    ax.axvline(
        bisection.root,
        linestyle="--",
        label=f"Equilibrium: {bisection.root:.2f} °C"
    )

    ax.set_xlabel("Greenhouse Temperature (°C)")
    ax.set_ylabel("Heat-balance residual")

    ax.set_title("Greenhouse Heat-Balance Equilibrium")

    ax.legend()
    ax.grid(True, alpha=0.3)

    fig.tight_layout()

    fig.savefig(
        OUTPUT_DIR / "task_10_heat_balance.png",
        dpi=160
    )

    plt.close(fig)

    # Plot fixed-point convergence
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(
        range(len(history)),
        history,
        marker="o",
        markersize=3
    )

    ax.set_xlabel("Iteration")
    ax.set_ylabel("Temperature Estimate (°C)")

    ax.set_title("Fixed-Point Iteration Convergence")

    ax.grid(True, alpha=0.3)

    fig.tight_layout()

    fig.savefig(
        OUTPUT_DIR / "task_10_fixed_point_convergence.png",
        dpi=160
    )

    plt.close(fig)


if __name__ == "__main__":
    main()
