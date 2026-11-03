import numpy as np
from scipy.optimize import root_scalar

CASH_FLOWS = np.array(
    [-120000, 30000, 35000, 40000, 45000, 50000],
    dtype=float
)


def npv(rate, cash_flows=CASH_FLOWS):

    if rate <= -1:
        raise ValueError("Rate must be greater than -1.")

    return sum(
        cf / (1.0 + rate) ** period
        for period, cf in enumerate(cash_flows)
    )


def derivative_npv(rate, cash_flows=CASH_FLOWS):

    if rate <= -1:
        raise ValueError("Rate must be greater than -1.")

    return sum(
        -period * cf / (1.0 + rate) ** (period + 1)
        for period, cf in enumerate(cash_flows)
        if period > 0
    )


def calculate_irr(cash_flows=CASH_FLOWS):

    # Newton-Raphson method
    newton = root_scalar(
        lambda r: npv(r, cash_flows),
        fprime=lambda r: derivative_npv(r, cash_flows),
        x0=0.10,
        method="newton",
        xtol=1e-12,
        maxiter=100
    )

    # Secant method
    secant = root_scalar(
        lambda r: npv(r, cash_flows),
        x0=0.05,
        x1=0.20,
        method="secant",
        xtol=1e-12,
        maxiter=100
    )

    if not newton.converged or not secant.converged:
        raise RuntimeError("An IRR solver did not converge.")

    return newton, secant


def main():

    newton, secant = calculate_irr()

    # Reduce annual cash inflows by 10%
    reduced_flows = CASH_FLOWS.copy()

    reduced_flows[1:] *= 0.90

    reduced_newton, _ = calculate_irr(reduced_flows)

    print("TASK 11 - SOLAR WATER-PUMP PROJECT IRR")

    print("Cash flows:", CASH_FLOWS.tolist())

    print(
        f"Newton-Raphson IRR: {newton.root:.6%}"
    )

    print(
        f"Secant Method IRR: {secant.root:.6%}"
    )

    print(
        f"NPV at Newton solution: {npv(newton.root):.8f}"
    )

    print("\nAnnual inflows reduced by 10%")

    print(
        f"New IRR: {reduced_newton.root:.6%}"
    )

    print(
        f"Change in IRR: "
        f"{(reduced_newton.root - newton.root) * 100:.3f} "
        "percentage points"
    )


if __name__ == "__main__":
    main()
