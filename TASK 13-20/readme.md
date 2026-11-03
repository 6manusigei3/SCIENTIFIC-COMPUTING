# BIT 2118 – SCIENTIFIC COMPUTING
# Tasks 13–20

---

# TASK 13: INTERPOLATION

## 1. Mathematical Concept

Interpolation is a numerical method used to estimate unknown values that lie between known data points. It is useful when data has been collected at certain intervals, but an estimate is needed for a point where no measurement was taken.

One common method is linear interpolation, which assumes that the relationship between two known points is approximately a straight line.

The formula for linear interpolation is:

\[
y=y_0+\frac{x-x_0}{x_1-x_0}(y_1-y_0)
\]

Where:
- \(x_0,y_0\) are the first known data point.
- \(x_1,y_1\) are the second known data point.
- \(x\) is the point where an estimate is required.
- \(y\) is the estimated value.

## 2. Mathematical Example

Suppose a weather station records a temperature of 20°C at 10:00 AM and 28°C at 2:00 PM. We want to estimate the temperature at 12:00 PM.

Given:

- \(x_0=10\)
- \(y_0=20\)
- \(x_1=14\)
- \(y_1=28\)
- \(x=12\)

Using the interpolation formula:

\[
y=20+\frac{12-10}{14-10}(28-20)
\]

\[
y=20+\frac{2}{4}\times8
\]

\[
y=24^\circ C
\]

The estimated temperature at 12:00 PM is 24°C.

## 3. Real-World Applications

- Estimating temperatures between recorded measurements.
- Predicting population values between census periods.
- Estimating missing scientific measurements.
- Estimating sales between recorded dates.
- Calculating approximate positions using known coordinates.

## 4. Real-World Problem and Solution Approach

**Problem:** A weather station records temperatures at specific times, but users may need temperature estimates for times when no readings were taken.

**Solution Approach:** The recorded temperatures are used as known data points. Linear interpolation is then applied to estimate the temperature at the required time. This assumes that the temperature changes approximately linearly between the two selected readings.

## 5. Python Implementation – `interpolation.py`

The Python program uses known x-values and their corresponding y-values to estimate an unknown value between them.

The code performs the following operations:

1. Imports the required numerical libraries.
2. Defines the known data points using arrays.
3. Specifies the point where an estimate is needed.
4. Applies the interpolation formula.
5. Displays the estimated value.
6. Plots the known data points and the estimated point.

**Inputs:** Known x-values, known y-values and the x-value to estimate.

**Operation:** Linear interpolation.

**Output:** The estimated y-value at the selected point.

### Parameter Change Experiment

Change the estimated time from 12:00 PM to 11:00 AM. Run the program again and compare the results. Explain how changing the input affects the estimated temperature.

### Modified Real-World Case

The program can be modified to estimate daily sales between recorded dates. Different dates and sales figures can be entered, and interpolation can be used to estimate sales on a date between two recorded observations.

---

# TASK 14: CURVE FITTING

## 1. Mathematical Concept

Curve fitting is a numerical method used to find a mathematical function that best represents the general relationship between a set of observed data points.

Unlike interpolation, curve fitting does not necessarily pass through every data point. Instead, it attempts to identify the overall trend in the data.

One common approach is the least-squares method, which minimizes the sum of squared differences between actual observations and predicted values.

A simple linear curve is represented by:

\[
y=mx+c
\]

Where:
- \(m\) represents the slope.
- \(c\) represents the y-intercept.
- \(x\) is the independent variable.
- \(y\) is the predicted dependent variable.

## 2. Mathematical Example

Suppose a business uses the following mathematical model to describe the relationship between advertising expenditure and sales:

\[
y=5x+10
\]

If advertising expenditure is represented by \(x=4\):

\[
y=5(4)+10
\]

\[
y=30
\]

The model predicts 30 units of sales in the chosen units.

This is an illustrative model. In an actual curve-fitting program, the coefficients are calculated from the supplied observations.

## 3. Real-World Applications

- Analysing advertising expenditure and sales.
- Studying population growth.
- Analysing experimental scientific data.
- Identifying business and economic trends.
- Modelling relationships between different variables.

## 4. Real-World Problem and Solution Approach

**Problem:** A business wants to understand the relationship between the amount of money spent on advertising and the number of products sold.

**Solution Approach:** Historical advertising expenditure and sales data are collected. A curve-fitting method is applied to identify a mathematical relationship between the two variables. The resulting equation can be used to understand trends and make predictions.

## 5. Python Implementation – `curve_fitting.py`

The Python program uses observed data points to calculate a mathematical curve that represents their general relationship.

The code performs the following operations:

1. Imports NumPy and Matplotlib.
2. Defines the observed x-values and y-values.
3. Uses a curve-fitting method such as `numpy.polyfit()`.
4. Calculates the coefficients of the fitted curve.
5. Uses the coefficients to generate predicted values.
6. Displays the fitted equation.
7. Plots the original observations and fitted curve.

**Inputs:** Observed x-values, observed y-values and the selected polynomial degree.

**Operation:** Least-squares curve fitting.

**Output:** Fitted mathematical coefficients, predicted values and a graph.

### Parameter Change Experiment

Change the polynomial degree from 1 to 2 and observe how the fitted curve changes. Compare the equations and explain the difference between a straight-line model and a quadratic model.

### Modified Real-World Case

Modify the program to analyse the relationship between study hours and examination scores. Enter a different dataset, calculate the fitted curve and explain the relationship shown by the results.

---

# TASK 15: NUMERICAL DIFFERENTIATION

## 1. Mathematical Concept

Numerical differentiation is a method used to approximate the derivative of a mathematical function using numerical values.

Differentiation measures the rate at which one quantity changes in relation to another. It is useful when an exact derivative is difficult to calculate or when only numerical data is available.

One common method is the forward difference formula:

\[
f'(x)\approx\frac{f(x+h)-f(x)}{h}
\]

Where:
- \(f'(x)\) is the estimated derivative.
- \(h\) is a small step size.
- \(x\) is the point where the derivative is estimated.

Another method is central difference:

\[
f'(x)\approx\frac{f(x+h)-f(x-h)}{2h}
\]

## 2. Mathematical Example

Consider the function:

\[
f(x)=x^2
\]

Estimate its derivative at \(x=3\) using a step size of \(h=0.1\).

Using the forward difference formula:

\[
f'(3)\approx\frac{f(3.1)-f(3)}{0.1}
\]

\[
=\frac{9.61-9}{0.1}
\]

\[
=6.1
\]

The numerical estimate is 6.1.

The exact derivative is:

\[
f'(x)=2x
\]

Therefore:

\[
f'(3)=6
\]

The numerical result is close to the exact result.

## 3. Real-World Applications

- Estimating the speed of a moving vehicle.
- Calculating the rate of temperature change.
- Analysing changes in population.
- Measuring changes in business costs and revenue.
- Processing scientific and engineering measurements.

## 4. Real-World Problem and Solution Approach

**Problem:** A vehicle's position is recorded at different times, and its speed needs to be estimated.

**Solution Approach:** The recorded positions and corresponding times are used to calculate the approximate rate of change of position. Numerical differentiation is applied to estimate the vehicle's speed over the selected time interval.

## 5. Python Implementation – `numerical_differentiation.py`

The Python program estimates the derivative of a mathematical function using finite differences.

The code performs the following operations:

1. Imports the required numerical libraries.
2. Defines the mathematical function.
3. Specifies the point where the derivative is required.
4. Defines a small step size.
5. Evaluates the function at the required points.
6. Applies the finite difference formula.
7. Displays the estimated derivative.
8. Optionally plots the function and its rate of change.

**Inputs:** Mathematical function, evaluation point and step size.

**Operation:** Numerical differentiation using finite differences.

**Output:** Estimated derivative at the selected point.

### Parameter Change Experiment

Change the step size from 0.1 to 0.01 and compare the results. Explain how the step size affects the accuracy of the numerical approximation.

### Modified Real-World Case

Modify the program to estimate the speed of a moving object using recorded position measurements at different times. Explain how the estimated derivative represents the object's speed.

---

# TASK 16: NUMERICAL INTEGRATION

## 1. Mathematical Concept

Numerical integration is a mathematical technique used to approximate the definite integral of a function over a specified interval.

Integration can be used to calculate the area under a curve or determine the total accumulated value of a changing quantity.

One common numerical integration method is the trapezoidal rule.

The formula is:

\[
\int_a^b f(x)\,dx\approx
\frac{h}{2}\left[f(x_0)+2\sum_{i=1}^{n-1}f(x_i)+f(x_n)\right]
\]

Where:
- \(a\) is the lower limit.
- \(b\) is the upper limit.
- \(h\) is the width of each interval.
- \(n\) is the number of subintervals.
- \(f(x)\) is the function being integrated.

## 2. Mathematical Example

Estimate the integral:

\[
\int_0^2 x^2\,dx
\]

The exact integration is:

\[
\left[\frac{x^3}{3}\right]_0^2
\]

\[
=\frac{8}{3}
\]

\[
\approx2.667
\]

A numerical integration method divides the interval from 0 to 2 into smaller sections and estimates the total area.

The numerical result can then be compared with the exact result to evaluate its accuracy.

## 3. Real-World Applications

- Calculating distance travelled using speed measurements.
- Estimating total energy consumption.
- Calculating accumulated rainfall.
- Estimating areas under scientific graphs.
- Calculating total quantities from changing rates.

## 4. Real-World Problem and Solution Approach

**Problem:** A vehicle travels at different speeds over a period of time, and the total distance travelled needs to be estimated.

**Solution Approach:** Speed measurements are collected at different times. Numerical integration is applied to estimate the area under the speed-time curve. The resulting area represents the approximate distance travelled.

## 5. Python Implementation – `numerical_integration.py`

The Python program calculates an approximate definite integral using a numerical integration method.

The code performs the following operations:

1. Imports NumPy and the required plotting libraries.
2. Defines the mathematical function.
3. Specifies the lower and upper integration limits.
4. Defines the number of subintervals.
5. Applies a numerical integration method such as the trapezoidal rule.
6. Displays the estimated integral.
7. Compares the result with the exact value where available.
8. Plots the function and the integration interval.

**Inputs:** Function, lower limit, upper limit and number of subintervals.

**Operation:** Numerical integration.

**Output:** Estimated definite integral and corresponding graph.

### Parameter Change Experiment

Increase the number of subintervals and compare the numerical results. Explain how increasing the number of intervals affects the approximation.

### Modified Real-World Case

Modify the program to estimate the distance travelled by a vehicle using different speed readings recorded over time. Explain how the integration result represents the total distance.

---

# TASK 17: ORDINARY DIFFERENTIAL EQUATIONS USING EULER'S METHOD

## 1. Mathematical Concept

An ordinary differential equation (ODE) is an equation that contains an unknown function and its derivatives.

Euler's method is a numerical technique used to approximate solutions to ordinary differential equations, especially when an exact mathematical solution is difficult to obtain.

The Euler update formula is:

\[
y_{n+1}=y_n+h f(x_n,y_n)
\]

Where:
- \(y_{n+1}\) is the next estimated value.
- \(y_n\) is the current value.
- \(h\) is the step size.
- \(f(x_n,y_n)\) represents the derivative at the current point.

The method repeatedly uses the current value and slope to estimate the next value.

## 2. Mathematical Example

Consider the differential equation:

\[
\frac{dy}{dx}=y
\]

With the initial condition:

\[
y(0)=1
\]

Using Euler's method with a step size of 0.1:

First step:

\[
y_1=1+0.1(1)
\]

\[
y_1=1.1
\]

Second step:

\[
y_2=1.1+0.1(1.1)
\]

\[
y_2=1.21
\]

The method continues to estimate the solution at subsequent points.

## 3. Real-World Applications

- Modelling population growth.
- Predicting temperature changes.
- Simulating physical motion.
- Modelling changing quantities over time.
- Studying simple biological and environmental systems.

## 4. Real-World Problem and Solution Approach

**Problem:** A population increases over time at a rate that depends on its current population.

**Solution Approach:** A differential equation is created to represent the population growth rate. The initial population is provided, and Euler's method is applied repeatedly to estimate the population at later times.

## 5. Python Implementation – `euler_method.py`

The Python program uses Euler's method to approximate the solution of an ordinary differential equation.

The code performs the following operations:

1. Imports NumPy and Matplotlib.
2. Defines the derivative function.
3. Specifies the initial x-value and y-value.
4. Defines the step size and final point.
5. Applies the Euler update formula repeatedly.
6. Stores the calculated values.
7. Displays the estimated solution.
8. Plots the approximate solution.

**Inputs:** Differential equation, initial conditions, step size and final point.

**Operation:** Repeated Euler numerical updates.

**Output:** Approximate solution values and a graph.

### Parameter Change Experiment

Change the step size from 0.1 to 0.05 and compare the resulting values. Explain how reducing the step size affects the numerical approximation.

### Modified Real-World Case

Modify the program to model population growth using the equation:

\[
\frac{dP}{dt}=kP
\]

Where \(P\) represents population and \(k\) represents the growth-rate constant.

Provide an initial population and growth rate, then use Euler's method to estimate the population over time.

---

# TASK 18: SOLVING ORDINARY DIFFERENTIAL EQUATIONS USING SCIPY

## 1. Mathematical Concept

SciPy is a Python scientific computing library that provides numerical tools for solving mathematical problems.

It includes functions for solving ordinary differential equations. One commonly used function is `solve_ivp()` from the `scipy.integrate` module.

An initial-value ODE can be represented as:

\[
\frac{dy}{dt}=f(t,y)
\]

With an initial condition:

\[
y(t_0)=y_0
\]

SciPy uses numerical methods to approximate the solution over a specified time interval.

## 2. Mathematical Example

Consider the differential equation:

\[
\frac{dy}{dt}=-2y
\]

With the initial condition:

\[
y(0)=5
\]

The exact mathematical solution is:

\[
y(t)=5e^{-2t}
\]

SciPy can be used to calculate approximate values of the function at selected times.

The numerical results can then be compared with the exact solution.

## 3. Real-World Applications

- Modelling temperature changes.
- Studying population growth and decline.
- Modelling chemical reactions.
- Simulating physical systems.
- Analysing biological and environmental processes.

## 4. Real-World Problem and Solution Approach

**Problem:** A hot object gradually loses heat when placed in an environment with a lower surrounding temperature. Its temperature changes over time.

**Solution Approach:** A differential equation is used to represent the rate of temperature change. The initial temperature and cooling-rate constant are defined, and SciPy's ODE solver is used to estimate the temperature at different times.

## 5. Python Implementation – `odes_scipy.py`

The Python program uses SciPy to solve an ordinary differential equation numerically.

The code performs the following operations:

1. Imports `solve_ivp` from `scipy.integrate`.
2. Imports NumPy and Matplotlib.
3. Defines the derivative function.
4. Specifies the initial condition.
5. Defines the time interval.
6. Calls `solve_ivp()` to solve the equation.
7. Retrieves the calculated time and solution values.
8. Displays the numerical results.
9. Plots the solution against time.

**Inputs:** Differential equation, initial conditions, time interval and solver settings.

**Operation:** Numerical solution of an ODE using SciPy.

**Output:** Approximate solution values and a graph.

### Parameter Change Experiment

Change the cooling-rate constant in the differential equation and run the program again. Compare the graphs and explain how the cooling rate affects the temperature over time.

### Modified Real-World Case

Modify the program to model the decrease in the concentration of a substance over time using a first-order decay equation. Define the initial concentration and decay-rate constant, then interpret the results.

---

# TASK 19: NUMERICAL OPTIMIZATION

## 1. Mathematical Concept

Numerical optimization is a mathematical technique used to find the maximum or minimum value of a function.

It is commonly used when a mathematical problem involves selecting the best possible value from a range of alternatives.

For minimization, the objective is to find:

\[
x^*=\operatorname*{arg\,min}_x f(x)
\]

Where:
- \(f(x)\) is the objective function.
- \(x^*\) is the value that produces the minimum result.

Numerical optimization methods search for the best solution using computational procedures.

## 2. Mathematical Example

Consider the function:

\[
f(x)=(x-3)^2+2
\]

The function reaches its minimum when:

\[
x=3
\]

Substituting:

\[
f(3)=(3-3)^2+2
\]

\[
f(3)=2
\]

Therefore, the minimum value is 2, occurring at \(x=3\).

## 3. Real-World Applications

- Minimizing business operating costs.
- Maximizing company profits.
- Finding efficient production levels.
- Optimizing resource allocation.
- Reducing travel distances and operating time.

## 4. Real-World Problem and Solution Approach

**Problem:** A business wants to determine the production quantity that minimizes its operating costs.

**Solution Approach:** A mathematical cost function is created using production quantity as the independent variable. A numerical optimization method is then applied to find the production quantity that gives the lowest cost within the allowed range.

## 5. Python Implementation – `numerical_optimization.py`

The Python program uses numerical optimization to find the minimum or maximum value of a mathematical function.

The code performs the following operations:

1. Imports the required optimization functions from SciPy.
2. Defines the objective function.
3. Specifies the search interval.
4. Applies an optimization method such as `minimize_scalar()`.
5. Retrieves the estimated optimal value.
6. Displays the optimal input and corresponding function value.
7. Plots the function and marks the estimated optimum.

**Inputs:** Objective function, search interval and optimization settings.

**Operation:** Numerical optimization.

**Output:** Estimated optimal value and the corresponding minimum or maximum result.

### Parameter Change Experiment

Change the search interval or modify a parameter in the objective function. Run the program again and compare the optimal results. Explain how the changes affect the optimization process.

### Modified Real-World Case

Modify the program to find the production quantity that minimizes a simplified business operating-cost function. Define the cost equation, set realistic search limits and interpret the optimal production quantity.

---

# TASK 20: RANDOM NUMBERS AND MONTE CARLO SIMULATION

## 1. Mathematical Concept

Monte Carlo simulation is a numerical technique that uses random numbers and repeated experiments to estimate mathematical results.

It is useful when a problem is difficult to solve using direct mathematical calculations.

The method involves generating random values, performing repeated trials and analysing the results to estimate a probability or numerical quantity.

An estimated probability can be calculated using:

\[
P(A)\approx\frac{\text{Number of successful trials}}{\text{Total number of trials}}
\]

As the number of trials increases, the estimate generally becomes more stable.

## 2. Mathematical Example

One common example of Monte Carlo simulation is estimating the value of \(\pi\).

Random points are generated inside a square containing a quarter-circle of radius 1.

The proportion of points falling inside the quarter-circle is approximately:

\[
\frac{\pi}{4}
\]

Therefore:

\[
\pi\approx4\times\frac{\text{Points inside the quarter-circle}}{\text{Total points}}
\]

By generating many random points, the estimated value becomes closer to the actual value of \(\pi\), although individual simulations may differ.

## 3. Real-World Applications

- Estimating probabilities.
- Financial risk analysis.
- Simulating uncertain events.
- Analysing queues and service systems.
- Estimating areas and volumes.
- Modelling possible outcomes in scientific research.

## 4. Real-World Problem and Solution Approach

**Problem:** A researcher wants to estimate the probability of an event where there are many possible outcomes.

**Solution Approach:** A simulation is created to represent the situation. Random numbers are generated to produce different outcomes, and the number of times the event occurs is counted. The estimated probability is calculated by dividing successful trials by the total number of trials.

## 5. Python Implementation – `monte_carlo.py`

The Python program uses random numbers and repeated trials to estimate the value of pi.

The code performs the following operations:

1. Imports the required random-number and plotting libraries.
2. Defines the number of random trials.
3. Generates random x- and y-coordinates inside a square.
4. Checks whether each point falls inside the quarter-circle using:

\[
x^2+y^2\leq1
\]

5. Counts the points that fall inside the quarter-circle.
6. Calculates the estimated value of pi.
7. Displays the estimated value.
8. Optionally plots the random points to visualize the simulation.

**Inputs:** Number of random trials and an optional random seed.

**Operation:** Random sampling, counting and probability estimation.

**Output:** Estimated value of pi and a visualization of the generated points.

### Parameter Change Experiment

Run the program with 1,000 random points and record the estimated value of pi. Increase the number of points to 100,000 and run it again.

Compare the two results and explain how increasing the number of random trials affects the accuracy and stability of the estimate.

### Modified Real-World Case

Modify the program to estimate the probability that customer demand exceeds available stock in a business.

Generate random demand values based on an assumed demand model. Count the number of trials where demand exceeds stock and divide by the total number of trials.

Explain the assumptions used, the input values, the estimated probability and what the result means for inventory planning.

---

# CONCLUSION

Tasks 13 to 20 demonstrate different numerical methods used in scientific computing. These methods help solve mathematical problems that may be difficult to handle using direct calculations.

Interpolation and curve fitting are useful for analysing and estimating data. Numerical differentiation and integration help calculate rates of change and accumulated quantities. Euler's method and SciPy provide techniques for solving ordinary differential equations. Numerical optimization helps identify the best possible solutions, while Monte Carlo simulation uses random sampling to estimate mathematical results.

Python makes it possible to implement these methods, test different input values, visualize results and apply numerical techniques to practical problems.
