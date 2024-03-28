import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

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

impulse = np.zeros(1000)
impulse[0] = 1

# Apply the filter to the impulse signal to get the filter's impulse response
filter_impulse_response = signal.lfilter(b, a, impulse)

# Take the FFT of the filter's impulse response to get its frequency response
frequency_response = np.fft.fft(filter_impulse_response)

# Frequency axis
frequency_axis = np.fft.fftfreq(len(frequency_response))

# Plot only positive frequencies
positive_freq_response = frequency_response[:len(frequency_response)//2]
positive_freq_axis = frequency_axis[:len(frequency_response)//2]

# Plot the frequency response
plt.figure()
plt.plot(positive_freq_axis, np.abs(positive_freq_response))
plt.title('Frequency Response of Butterworth Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid()
plt.savefig('../figs/hnexercise.png')
