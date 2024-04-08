import numpy as np
import soundfile as sf
from scipy import signal
from mneprajfilter import mneprajfilter  # Importing the mneprajfilter function

# Read .wav file
input_signal, fs = sf.read('sound.wav')

# Extract number of channels
num_channels = input_signal.shape[1] if len(input_signal.shape) > 1 else 1

# Sampling frequency of Input signal
sampl_freq = fs

# Order of the filter
order = 4

# Cutoff frequency 6kHz
cutoff_freq = 6000

# Digital frequency
Wn = 2 * cutoff_freq / sampl_freq

# Get butterworth filter coefficients
b, a = signal.butter(order, Wn, 'low')

# Write coefficients to a text file
with open('filter_coefficients.txt', 'w') as file:
    file.write("b coefficients:\n")
    np.savetxt(file, b, delimiter=',')  # Write b coefficients
    file.write("\n\na coefficients:\n")
    np.savetxt(file, a, delimiter=',')  # Write a coefficients

# Filter the input signal with butterworth filter
output_signal = mneprajfilter(a, b, input_signal, sampl_freq)

# Write the output signal into .wav file
sf.write('soundmnepraj.wav', output_signal, fs)
