
# BIT2118 – Execution Results (Tasks 9–12)

## Task 9: Eigenvalues and Eigenvectors

**Application:** Campus Network Analysis

- Dominant eigenvalue: 2.935432
- Library centrality: 0.1593
- Lab centrality: 0.2136
- Admin centrality: 0.2541
- Lecture centrality: 0.2136
- Hostel centrality: 0.1593

After adding a connection between the Library and Hostel:

- New dominant eigenvalue: 3.236068
- Library centrality: 0.1910
- Lab centrality: 0.1910
- Admin centrality: 0.2361
- Lecture centrality: 0.1910
- Hostel centrality: 0.1910

**Interpretation:** The Admin location has the highest relative network importance in the original network. Adding a connection between the Library and Hostel changes the distribution of network importance.

## Task 10: Bisection and Fixed-Point Methods

**Application:** Greenhouse Temperature Equilibrium

- Bisection temperature: 26.793727 °C
- Fixed-point temperature: 26.793727 °C
- Bisection iterations: 39
- Fixed-point iterations: 16
- Residual: approximately 0

When heat gain increases from 14 to 18:

- New equilibrium temperature: 27.897229 °C

**Interpretation:** Both methods obtain approximately the same equilibrium temperature. Fixed-point iteration requires fewer iterations for the selected example. Increasing heat gain raises the equilibrium temperature.

## Task 11: Newton-Raphson and Secant Methods

**Application:** Solar-Powered Water Pumping Investment

- Newton-Raphson IRR: 17.990376%
- Secant IRR: 17.990376%
- NPV at the calculated IRR: approximately 0

After reducing annual cash inflows by 10%:

- New IRR: 13.864104%
- Change in IRR: -4.126 percentage points

**Interpretation:** Both methods calculate approximately the same internal rate of return. Reducing the expected annual cash inflows reduces the project's estimated return.

## Task 12: Nonlinear Equation Solving

**Application:** Reservoir and Embankment Design

For a reservoir radius of 5 metres:

- First intersection: x = -4.533085, y = 2.109772 m
- Second intersection: x = 4.533085, y = 2.109772 m

After increasing the radius to 5.5 metres:

- First intersection: x = -4.820692, y = 2.647815 m
- Second intersection: x = 4.820692, y = 2.647815 m

**Interpretation:** The two intersection points are symmetric about the vertical axis. Increasing the reservoir radius changes the intersection coordinates.

## Conclusion

The four tasks demonstrate how numerical methods can be applied to practical problems involving network analysis, temperature estimation, investment evaluation, and nonlinear equation solving.

The results are based on illustrative input values and assumptions.
