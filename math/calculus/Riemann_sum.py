import numpy as np

def riemann_sum(f, a, b, n, method='midpoint'):
    dx = (b - a) / n
    x = np.linspace(a, b, n + 1)
    
    if method == 'left':
        x_points = x[:-1]
    elif method == 'right':
        x_points = x[1:]
    else: # midpoint
        x_points = (x[:-1] + x[1:]) / 2
        
    return np.sum(f(x_points) * dx)

print(riemann_sum(lambda x: x**2, 0, 1, 1000))