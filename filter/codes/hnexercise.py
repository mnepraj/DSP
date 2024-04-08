import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Sampling frequency
Fs = 44100  # Assume a sampling frequency of 10 kHz

# Read coefficients from the text file
with open('filter_coefficients.txt', 'r') as file:
    lines = file.readlines()
    b_index = lines.index("b coefficients:\n") + 1
    a_index = lines.index("a coefficients:\n") + 1
    b = np.loadtxt(lines[b_index: a_index-3], delimiter=',')
    a = np.loadtxt(lines[a_index: 2*a_index - 3 - b_index], delimiter=',')

# Use the coefficients as needed
print("b coefficients:", b)
print("a coefficients:", a)

# Compute the frequency response
w, h = signal.freqz(b, a, worN=2000, fs=Fs)

# Plot the frequency response
plt.figure()
plt.plot(w, np.abs(h))
plt.title('Frequency Response of Butterworth Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.axvline(x=6000, color='r', linestyle='--', label='Cutoff Frequency')
plt.legend()
plt.grid()
plt.savefig('../figs/hnexercise.png')
plt.show()
