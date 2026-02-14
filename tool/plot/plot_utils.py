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

def plot_math_function(expr, symbol, x_range=(-10, 10), y_lim=None, title=None):
    """
    Plots a SymPy expression using the textbook style.
    """
    func = sp.lambdify(symbol, expr, 'numpy')
    
    # High resolution for smooth curves
    x_val = np.linspace(x_range[0], x_range[1], 2000)
    y_val = func(x_val)

    # Filter vertical asymptotes (the visual fix we discussed)
    threshold = 100
    y_val[np.abs(y_val) > threshold] = np.nan

    # Create plot
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # --- HERE IS THE MAGIC ---
    # We call our own helper function inside this function!
    set_textbook_style(ax) 
    # -------------------------

    ax.plot(x_val, y_val, label=f'${sp.latex(expr)}$', linewidth=2)
    
    # Set limits
    ax.set_xlim(x_range)
    if y_lim:
        ax.set_ylim(y_lim)
    
    if title:
        ax.set_title(title)
        
    ax.legend()
    plt.show()