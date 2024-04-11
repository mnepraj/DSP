import numpy as np

# Given parameters
s1 = -0.1907 - 1.0322j
s2 = -0.4604 - 0.4276j
s3 = -0.4604 + 0.4276j
s4 = -0.1907 + 1.0322j
epsilon = 0.3
Omega_Lp = 1

# Define denominator polynomial
den = np.poly([s1, s2, s3, s4])

# Define frequency range
w = np.arange(-2, 2.01, 0.01)

num = 0.4166

# Define parameters for transformation
B = 0.089
Omega0 = 0.352
Omegap1 = 0.3104

# Perform transformation to get s_L
s_L = (1j * Omegap1)**2 + Omega0**2
s_L /= B * (1j * Omegap1)

H = num / np.polyval(den, s_L)
print(1 / abs(H))
