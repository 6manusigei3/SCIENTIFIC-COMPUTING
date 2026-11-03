# BIT2118 – Numerical Methods: Tasks 9–12

## Overview

This project contains Python implementations of numerical methods covered in BIT2118. It focuses on applying numerical techniques to practical, real-world-inspired problems.

The work covers Tasks 9, 10, 11, and 12, including eigenvalues and eigenvectors, root-finding algorithms, and nonlinear equation solving.

## Tasks Completed

### Task 9: Eigenvalues and Eigenvectors

**Application:** Campus network analysis.

This task applies eigenvalues and eigenvectors to analyse connections between locations on a university campus.

- Represents campus locations as a network.
- Uses an adjacency matrix to represent connections.
- Calculates eigenvalues and eigenvectors.
- Uses the dominant eigenvector to estimate the relative importance of each location.
- Compares the network before and after adding a connection.

**Main file:** `tasks/task_09_eigenvalues.py`

### Task 10: Bisection and Fixed-Point Iteration

**Application:** Greenhouse temperature equilibrium.

This task estimates the equilibrium temperature of a greenhouse using two numerical methods:

- Bisection method.
- Fixed-point iteration.

The results are compared based on convergence and the number of iterations required. The effect of changing the greenhouse heat gain is also investigated.

**Main file:** `tasks/task_10_bisection_fixed_point.py`

### Task 11: Newton-Raphson and Secant Methods

**Application:** Solar-powered water pumping investment.

This task uses numerical methods to calculate the Internal Rate of Return (IRR) of a solar-powered water pumping project.

The following methods are implemented:

- Newton-Raphson method.
- Secant method.

The calculated IRR values are compared, and the effect of reducing the expected annual cash inflows is analysed.

**Main file:** `tasks/task_11_newton_secant.py`

### Task 12: Nonlinear Equation Solving

**Application:** Reservoir and embankment design.

This task solves nonlinear equations representing the intersection between a circular reservoir boundary and a parabolic embankment.

It identifies the intersection points and investigates how changing the reservoir radius affects their positions.

**Main file:** `tasks/task_12_nonlinear_equations.py`

## Repository Structure

```text
BIT2118/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── tasks/
│   ├── __init__.py
│   ├── task_09_eigenvalues.py
│   ├── task_10_bisection_fixed_point.py
│   ├── task_11_newton_secant.py
│   └── task_12_nonlinear_equations.py
│
├── tests/
│   └── test_tasks.py
│
└── outputs/
    ├── task_09_network_centrality.png
    ├── task_10_heat_balance.png
    ├── task_10_fixed_point_convergence.png
    ├── task_12_intersections.png
    └── execution_results.md
```

## Technologies Used

- Python 3
- NumPy
- SciPy
- Matplotlib
- Pytest

## Installation

Clone the group repository:

```bash
git clone <repository-url>
```

Navigate into the project directory:

```bash
cd BIT2118
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Programs

Run each task separately from the repository root:

```bash
python -m tasks.task_09_eigenvalues
```

```bash
python -m tasks.task_10_bisection_fixed_point
```

```bash
python -m tasks.task_11_newton_secant
```

```bash
python -m tasks.task_12_nonlinear_equations
```

## Running Tests

Run the automated tests using:

```bash
pytest -q
```

The tests check the numerical methods and verify that the calculated solutions satisfy the relevant equations.

## Results and Interpretation

The programs generate numerical results and graphical representations to help interpret the solutions.

- **Task 9:** Eigenvector scores indicate the relative importance of campus locations based on their network connections.
- **Task 10:** The equilibrium temperature is calculated using both bisection and fixed-point iteration, allowing their convergence behaviour to be compared.
- **Task 11:** The IRR represents the estimated annual return at which the project's net present value is zero.
- **Task 12:** The intersection coordinates identify where the reservoir boundary and embankment equations meet.

Generated graphs and execution results are stored in the `outputs/` directory.

## Assumptions and Limitations

The scenarios use illustrative input values to demonstrate the numerical methods. They are not based on measured campus network data, actual greenhouse measurements, verified investment forecasts, or an engineered reservoir survey.

The accuracy of the results depends on the input assumptions, initial estimates, convergence tolerances, and suitability of each numerical method.

## Contribution

This contribution implements BIT2118 Tasks 9–12 using Python. Each task applies a numerical method to a practical scenario, presents the calculated results, and investigates how changing selected parameters affects the outcome.

---

**Course:** BIT2118  
**Project:** Numerical Methods  
**Tasks:** 9–12

