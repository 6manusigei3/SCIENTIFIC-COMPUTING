# TASK 1: DATA SCIENCE ESSENTIALS WITH PYTHON

Task 1 involves completing the prerequisite course titled **Data Science Essentials with Python (Self-paced)**.

The purpose of this course is to introduce the basic Python programming and data science concepts needed for scientific computing. It provides foundational knowledge for working with numerical data, performing calculations and using Python libraries.

The knowledge gained from this course is applied in the following tasks, particularly when using NumPy, SciPy and Matplotlib.

**Completion status:** [Completed / In Progress]  
**Completion date:** [Enter your actual completion date]

---

# TASK 2: NUMPY ARRAYS AND NUMERICAL COMPUTATION

**Python file:** `code/Task_02_numpy_arrays.py`

This task demonstrates how NumPy arrays are used to store numerical data and perform calculations efficiently.

The program begins by importing NumPy using:

```python
import numpy as np
```

It then creates an array containing 24 hourly temperature readings in degrees Celsius. Each value represents a temperature recorded at a particular hour.

After creating the array, the program calculates the average temperature using `np.mean()`. This function adds all the temperature readings and divides the total by the number of readings.

The program also uses `np.min()` to find the lowest temperature and `np.max()` to find the highest temperature.

Next, it converts all the temperature readings from Celsius to Fahrenheit using:

\[
F = 1.8C + 32
\]

The calculation is performed directly on the entire NumPy array instead of converting each value individually.

When the program runs, it displays the average, minimum and maximum temperatures, together with the converted Fahrenheit readings.

**What happens when the input changes?**

When 2°C is added to every temperature reading, the average, minimum and maximum temperatures also increase by 2°C. This demonstrates how changing the input data affects the calculated results.

**Real-world application: Water temperature monitoring**

The same approach can be used to monitor water temperatures. A water-quality officer can collect daily temperature readings and use NumPy to calculate the average, minimum and maximum temperatures. These results help describe temperature changes in the water over time.

---

# TASK 3: MATHEMATICAL FUNCTIONS AND VECTORIZATION

**Python file:** `code/Task_03_vectorization.py`

This task demonstrates vectorization and how it improves the efficiency of numerical calculations.

The program imports NumPy and the `timeit` module. NumPy is used to process numerical data, while `timeit` measures how long calculations take to execute.

The program generates one million simulated network latency readings between 5 and 250 milliseconds. A fixed random seed is used so that the same data can be generated again when the program is run.

The program then performs the same mathematical operation using two different approaches.

The first approach uses a normal Python loop. It goes through each latency reading individually, converts the value from milliseconds to seconds by dividing it by 1,000, squares the result and stores it in a list.

The second approach uses NumPy vectorization. Instead of processing one value at a time, it divides the entire array by 1,000 and squares all the values using a single mathematical expression.

The `timeit` module measures the execution time of both approaches. The program then calculates the approximate speed-up by dividing the loop execution time by the vectorized execution time.

When the program runs, it displays some of the calculated values, the time taken by each approach and the approximate speed-up.

**What happens when the input changes?**

When the number of latency readings is reduced from one million to 100,000, the program processes fewer values. This reduces the amount of work required and generally reduces execution time.

**Real-world application: Rainfall data processing**

Vectorization can also be used in rainfall monitoring. A weather station may collect thousands of rainfall measurements and need to convert them from millimetres to metres. NumPy can perform this conversion on the entire dataset at once, making data processing faster and easier.

---

# TASK 4: FLOATING-POINT ARITHMETIC AND NUMERICAL ERRORS

**Python file:** `code/Task_04_numerical_errors.py`

This task explains how numerical errors can occur when computers perform mathematical calculations.

Computers store most decimal numbers using binary floating-point representation. Because computer memory has limited precision, some decimal numbers cannot be represented exactly. This can cause small differences between expected and calculated results.

The program first imports NumPy and then performs the calculation:

```python
calculated = 0.1 + 0.2
expected = 0.3
```

It compares the calculated value with the expected value using the equality operator. The comparison may return `False` because the computer stores the decimal numbers as approximations.

The program then uses `np.isclose()` to check whether the two values are sufficiently close to each other. This method uses a tolerance rather than requiring exact equality.

Next, the program calculates the square root of 2 using NumPy and compares it with the approximation 1.414.

It calculates the absolute error by finding the difference between the true value and the approximate value. It also calculates relative error by dividing the absolute error by the true value.

Finally, the program investigates numerical cancellation using three small values of \(x\). It compares two mathematically equivalent expressions. The direct expression subtracts two nearly equal numbers, which can result in a loss of numerical precision. The alternative expression avoids this subtraction and is more numerically stable.

When the program runs, it displays the floating-point comparison results, the absolute and relative errors, and the results of the numerical cancellation comparison.

**What happens when the tolerance changes?**

A smaller tolerance makes the comparison stricter. Values must be closer to one another to be considered equal. This demonstrates why choosing an appropriate tolerance is important when working with approximate numerical results.

**Real-world application: Financial balance verification**

A similar technique can be used when comparing calculated and recorded balances. A system can calculate the difference between two balances and check whether it is within an acceptable tolerance. For real financial calculations, decimal arithmetic should be used for monetary values to avoid inappropriate floating-point rounding.

---

# TASK 5: MATRIX ALGEBRA AND MATRIX OPERATIONS

**Python file:** `code/Task_05_matrix_algebra.py`

This task demonstrates how matrices are used to transform two-dimensional coordinates.

The program imports NumPy and creates an array containing the four corners of a square. Each point is represented by two values: an x-coordinate and a y-coordinate.

The program then defines a rotation angle of 45 degrees. Since NumPy's trigonometric functions use radians, the angle is first converted from degrees to radians using `np.deg2rad()`.

A rotation matrix is created using the sine and cosine of the angle. This matrix determines how the coordinates move when the square is rotated.

The program also creates a scaling matrix. The scaling matrix multiplies the x-coordinates by 2 and the y-coordinates by 1.5.

The two matrices are combined using matrix multiplication with the `@` operator. This produces one transformation matrix containing both operations.

The transformation matrix is then applied to the original square coordinates. The program prints the original points, the transformation matrix and the transformed points.

It also calculates the determinant of the transformation matrix using `np.linalg.det()`. The determinant indicates how the transformation affects the area of the square.

**What happens when the input changes?**

When the rotation angle changes from 45 degrees to 90 degrees, the square rotates to a different orientation. The transformed coordinates change because the rotation matrix uses different sine and cosine values.

**Real-world application: Map-coordinate transformation**

Matrix transformations are useful in mapping and computer graphics. For example, a mapping application can rotate and scale a set of local map coordinates to change their orientation and size. Real geographic coordinates require an appropriate map projection before applying planar transformations.

---

# TASK 6: SOLUTION OF SYSTEMS OF LINEAR EQUATIONS

**Python file:** `code/Task_06_linear_systems.py`

This task demonstrates how Python can solve simultaneous linear equations using NumPy.

The program imports NumPy and creates a coefficient matrix representing the CPU and memory requirements of two different server types.

The mathematical system is represented as:

\[
Ax=b
\]

In this equation, \(A\) is the coefficient matrix, \(x\) contains the unknown quantities and \(b\) contains the known resource totals.

The program creates the coefficient matrix:

```python
A = np.array([
    [4.0, 2.0],
    [8.0, 12.0]
])
```

It then creates the right-hand-side vector:

```python
b = np.array([20.0, 72.0])
```

These values represent the total CPU and memory requirements.

The program uses `np.linalg.solve(A, b)` to solve the equations. NumPy calculates the unknown quantities that satisfy both equations.

After calculating the solution, the program verifies the answer by multiplying the coefficient matrix by the solution and comparing the result with the original totals.

It calculates the residual using:

```python
residual = b - A @ solution
```

The residual shows the difference between the original resource totals and the totals obtained from the calculated solution.

When the program runs, it displays the calculated server quantities and the residual. A residual close to zero indicates that the solution satisfies the equations accurately.

**What happens when the input changes?**

When the CPU total changes from 20 to 24 while the memory total remains 72, the solution changes because the system now has different resource requirements.

**Real-world application: Fertilizer mixture calculations**

The same method can calculate the quantities of two fertilizer mixtures needed to meet two nutrient requirements. Each mixture contributes a known amount of nutrients, and the equations determine the quantities required to reach the target totals.

---

# TASK 7: GAUSSIAN ELIMINATION AND LU DECOMPOSITION

**Python file:** `code/Task_07_gaussian_lu.py`

This task demonstrates how LU decomposition can be used to solve systems of linear equations efficiently, especially when the same coefficient matrix is used with different input vectors.

The program imports NumPy and the LU decomposition functions from SciPy:

```python
import numpy as np
from scipy.linalg import lu_factor, lu_solve
```

It then creates a 3 × 3 coefficient matrix representing the relationships between three unknown quantities.

The program also creates three different measurement vectors. Each vector contains different known values for the same system of equations.

The first major operation is LU factorization:

```python
lu, piv = lu_factor(A)
```

This operation factorizes the coefficient matrix and stores the information needed to solve the equations. The factorization is performed only once.

The program then loops through the three measurement vectors. For each vector, it calls:

```python
x = lu_solve((lu, piv), b)
```

The `lu_solve()` function uses the previously calculated LU factors to find the unknown values.

After each solution, the program calculates the residual by comparing the original right-hand-side vector with the result obtained from multiplying the coefficient matrix by the solution.

The program prints each measurement set, its calculated solution and the residual norm.

Finally, it uses `np.linalg.solve()` to calculate a direct solution for the first measurement set. This allows the result from LU decomposition to be compared with a direct solution.

**What happens when the input changes?**

When one of the measurement values changes, the solution also changes. However, the coefficient matrix remains the same, so the program can reuse the existing LU factorization instead of factorizing the matrix again.

**Real-world application: Electrical network calculations**

LU decomposition can be used in electrical network analysis. A network may have the same resistance and conductance structure but different current inputs. The same matrix factorization can be reused to calculate the resulting voltage values under different conditions.

---

# TASK 8: ITERATIVE METHODS FOR LINEAR SYSTEMS

**Python file:** `code/Task_08_iterative_linear.py`

This task demonstrates two iterative methods for solving systems of linear equations: the Jacobi method and the Gauss-Seidel method.

Unlike direct methods, iterative methods begin with an initial estimate and repeatedly improve that estimate until the calculated values are sufficiently accurate.

The program imports NumPy for numerical calculations and Matplotlib for creating the convergence graph.

It creates a 5 × 5 coefficient matrix representing five unknown interior temperatures. It also creates a right-hand-side vector representing the influence of the boundary temperatures.

The left boundary temperature is 100°C, while the right boundary temperature is 20°C.

### Jacobi method

The program defines a function called `jacobi()`.

The function begins with an initial estimate in which all unknown temperatures are set to zero.

It then separates the diagonal elements of the matrix from the remaining elements.

During each iteration, it calculates new temperature estimates using the values from the previous iteration.

The program calculates the maximum difference between the new and previous estimates. If this difference becomes smaller than the selected tolerance, the iteration stops.

If the tolerance has not been reached, the new estimates are used in the next iteration.

This process continues until the solution converges or the maximum number of iterations is reached.

### Gauss-Seidel method

The program also defines a function called `gauss_seidel()`.

This method also begins with an initial estimate of zero and repeatedly updates the unknown temperatures.

The main difference is that Gauss-Seidel immediately uses newly calculated values when updating the remaining unknowns. The Jacobi method instead uses the values from the previous iteration for all updates.

Both methods continue until the maximum change between successive estimates is smaller than the selected tolerance.

### Comparing the solutions

The program runs both iterative methods and stores their calculated solutions and error histories.

It also calculates a direct solution using:

```python
x_exact = np.linalg.solve(A, b)
```

This direct solution is used as a reference for checking the accuracy of the iterative results.

The program then prints the Jacobi solution, the Gauss-Seidel solution and the direct solution.

### Convergence graph

The program uses Matplotlib to plot the errors recorded during the iterations.

It uses `plt.semilogy()` to display the errors on a logarithmic vertical scale. This makes it easier to observe how the errors decrease as the number of iterations increases.

The graph includes a title, axis labels, a legend and grid lines. It allows the convergence behaviour of the two methods to be compared.

**What happens when the input changes?**

When the right boundary temperature changes from 20°C to 40°C while the left boundary remains at 100°C, the interior temperature estimates also change. This happens because the boundary conditions determine the temperature distribution.

**Real-world application: Heat-transfer modelling**

Iterative methods can be used to estimate temperatures at different points inside a material or room. Engineers can use the calculated temperatures to understand how heat moves between areas with different boundary temperatures.

---

# SUMMARY OF TASKS 1–8

| Task | Main concept | What is demonstrated |
|---|---|---|
| Task 1 | Data Science Essentials with Python | Foundational Python and data-science knowledge |
| Task 2 | NumPy arrays | Storing numerical data and calculating statistics |
| Task 3 | Vectorization | Comparing loop-based and vectorized calculations |
| Task 4 | Numerical errors | Understanding floating-point precision and numerical stability |
| Task 5 | Matrix algebra | Rotating and scaling two-dimensional coordinates |
| Task 6 | Linear equations | Solving simultaneous equations using NumPy |
| Task 7 | LU decomposition | Reusing matrix factorization to solve multiple systems |
| Task 8 | Iterative methods | Comparing Jacobi and Gauss-Seidel solutions |

# REFERENCES

- Python Documentation: https://docs.python.org/3/
- NumPy Documentation: https://numpy.org/doc/
- SciPy Documentation: https://docs.scipy.org/doc/scipy/
- Matplotlib Documentation: https://matplotlib.org/stable/
