
import numpy as np
import pytest

from scipy.optimize import root_scalar

from tasks.task_09_eigenvalues import (
    ADJACENCY,
    eigenvector_centrality,
)

from tasks.task_10_bisection_fixed_point import (
    heat_balance,
    fixed_point,
)

from tasks.task_11_newton_secant import (
    CASH_FLOWS,
    npv,
    derivative_npv,
    calculate_irr,
)

from tasks.task_12_nonlinear_equations import (
    residuals,
    find_intersections,
)


# --------------------------------------------------
# TASK 9: EIGENVALUES AND EIGENVECTORS
# --------------------------------------------------

def test_eigenvector_centrality():

    eigenvalue, scores, eigenvector = eigenvector_centrality(
        ADJACENCY
    )

    assert eigenvalue > 0

    assert len(scores) == 5

    assert np.all(scores >= 0)

    assert np.isclose(np.sum(scores), 1.0)

    assert np.linalg.norm(
        ADJACENCY @ eigenvector
        - eigenvalue * eigenvector
    ) < 1e-8


def test_eigenvector_rejects_non_square_matrix():

    with pytest.raises(ValueError):

        eigenvector_centrality(
            np.array([[1, 2, 3], [4, 5, 6]])
        )


# --------------------------------------------------
# TASK 10: BISECTION AND FIXED-POINT ITERATION
# --------------------------------------------------

def test_bisection_method():

    result = root_scalar(
        heat_balance,
        bracket=(20, 50),
        method="bisect"
    )

    assert result.converged

    assert abs(heat_balance(result.root)) < 1e-7


def test_fixed_point_method():

    temperature, history = fixed_point()

    assert temperature > 22

    assert len(history) > 1

    assert abs(heat_balance(temperature)) < 1e-7


def test_fixed_point_and_bisection_agree():

    bisection = root_scalar(
        heat_balance,
        bracket=(20, 50),
        method="bisect"
    )

    fixed_temperature, _ = fixed_point()

    assert np.isclose(
        bisection.root,
        fixed_temperature,
        atol=1e-7
    )


# --------------------------------------------------
# TASK 11: NEWTON-RAPHSON AND SECANT METHODS
# --------------------------------------------------

def test_newton_and_secant_irr():

    newton, secant = calculate_irr()

    assert newton.converged

    assert secant.converged

    assert np.isclose(
        newton.root,
        secant.root,
        atol=1e-7
    )


def test_npv_at_irr_is_zero():

    newton, _ = calculate_irr()

    assert abs(npv(newton.root)) < 1e-6


def test_derivative_npv():

    rate = 0.15

    numerical_derivative = (
        npv(rate + 1e-6) - npv(rate - 1e-6)
    ) / (2e-6)

    analytical_derivative = derivative_npv(rate)

    assert np.isclose(
        numerical_derivative,
        analytical_derivative,
        rtol=1e-5
    )


# --------------------------------------------------
# TASK 12: NONLINEAR EQUATION SOLVING
# --------------------------------------------------

def test_find_two_intersections():

    intersections = find_intersections()

    assert len(intersections) == 2

    for point in intersections:

        assert np.linalg.norm(residuals(point)) < 1e-7


def test_intersections_are_symmetric():

    intersections = find_intersections()

    x_values = sorted(
        point[0] for point in intersections
    )

    assert np.isclose(
        x_values[0],
        -x_values[1],
        atol=1e-6
    )


def test_larger_radius_changes_intersections():

    original = find_intersections(radius=5.0)

    modified = find_intersections(radius=5.5)

    assert len(original) == 2

    assert len(modified) == 2

    assert abs(modified[0][0]) > abs(original[0][0])
