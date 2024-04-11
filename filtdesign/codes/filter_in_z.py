import sympy as sp

# Define symbols
s, z = sp.symbols('s z')

# Given transfer function
Ha_BP_s = 0.4166*s**4/(15938.2257321666*s**8 + 1847.17342181004*s**7 + 8132.51911510094*s**6 + 699.707774268437*s**5 + 1526.36460282701*s**4 + 86.6965920629564*s**3 + 124.852069847996*s**2 + 3.51369169341385*s + 3.75648173256279)
# Perform substitution
substitution = ((1 - z**-1) / (1 + z**-1))
substituted_expression = Ha_BP_s.subs(s, substitution)

# Simplify the expression
simplified_expression = sp.simplify(substituted_expression)

# Print the result
print("Expression in z:")
print(simplified_expression)


