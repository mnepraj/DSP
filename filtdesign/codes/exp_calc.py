from sympy import symbols, simplify

# Define symbolic variable s
s = symbols('s')

# Constants
omega0_val = 0.352
B_val = 0.089

# Define s_L in terms of s, omega0, and B
s_L = (s**2 + omega0_val**2) / (B_val * s)

# Given roots
s5 = -0.1907 - 1.0322j
s6 = -0.4604 - 0.4276j
s7 = -0.4604 + 0.4276j
s8 = -0.1907 + 1.0322j

# Define the given polynomial expression
polynomial_expr = 0.4166 / ((s_L - s5) * (s_L - s6) * (s_L - s7) * (s_L - s8))

# Simplify the expression
simplified_expr = simplify(polynomial_expr)

# Print the simplified expression
print("Simplified Polynomial in terms of s:")
print(simplified_expr)
