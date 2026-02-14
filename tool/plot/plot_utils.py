import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def set_textbook_style(ax):
    """
    Moves left/bottom spines to zero and hides top/right.
    Adds a subtle grid.
    """
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.grid(True, linestyle=':', alpha=0.6)

def math_plot(expr, symbol, x_range=(-10, 10), y_lim=None, title=None):
    """
    Plots a SymPy expression with automatic asymptote handling.
    
    Args:
        expr: The SymPy expression to plot.
        symbol: The SymPy symbol variable (usually x).
        x_range: Tuple (min, max) for the x-axis.
        y_lim: Tuple (min, max) for the y-axis (optional).
        title: String for the plot title (optional).
    """
    # Convert SymPy to NumPy
    func = sp.lambdify(symbol, expr, 'numpy')
    
    x_val = np.linspace(x_range[0], x_range[1], 2000)
    y_val = func(x_val)

    # Asymptote Handling
    threshold = 100  # Adjust based on expected scale
    y_val[np.abs(y_val) > threshold] = np.nan

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x_val, y_val, label=f'${sp.latex(expr)}$', linewidth=2)

    
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend(loc='best')
    
    # Set Limits
    ax.set_xlim(x_range)
    if y_lim:
        ax.set_ylim(y_lim)
    
    if title:
        ax.set_title(title)

    plt.show()
