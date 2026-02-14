import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define functions
x = sp.symbols('x')
expr = x**3 - 2*x - 5
expr_diff = sp.diff(expr, x)
f = sp.lambdify(x, expr)
df = sp.lambdify(x, expr_diff)
print(f"f: {expr}")
print(f"df: {expr_diff}")

# Setting up first x value
x_vals = range(-10, 11)
x1 = min(x_vals, key=lambda i: abs(f(i)))
x_num = np.linspace(-10, 10, 1000)

max_iter = 20
count = 1
while count < max_iter:
    print(f"Attempt {count} ----------")
    print(f"x{count} = {x1}, f(x{count}) = {f(x1)}, f'(x{count}) = {df(x1)}")

    # Slope check
    slope = df(x1)
    if abs(slope) < 1e-9:
        print("Slope is too flat!")
        break

    # Calculate tangent line on x1
    tangent = df(x1)*(x - x1) + f(x1)
    print(f"tangent line: {tangent}")
    print(f"x{count} = {float(x1)}")
    tan_line_f = sp.lambdify(x, tangent)

    # Plot original function with tangent line
    fig, ax = plt.subplots(figsize=(8,5))
    ax.plot(x_num, f(x_num), color='b', label='f(x)')
    ax.plot(x_num, tan_line_f(x_num), color='r', label='tangent')
    ax.legend()
    ax.grid(True)
    ax.set_title(f"Newton-Raphson Method Attempt {count}")
    plt.axhline(0, color='black', linewidth=1)
    plt.show()

    # Update x1 value
    x_intercept = x1 - f(x1) / df(x1)
    epsilon = 1e-4
    if abs(x1 - x_intercept) > epsilon:
        x1 = x_intercept
        count += 1
    else: break

