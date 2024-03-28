import soundfile as sf
from scipy import signal

# Parameters
input_file = "sister.wav"
output_file = "sisterlfilter.wav"
order = 4
cutoff_freq = 5500.0

# Read input file
input_signal, sampl_freq = sf.read(input_file)

# Calculate cutoff frequency
Wn = 2 * cutoff_freq / sampl_freq

# Design butterworth filter
b, a = signal.butter(order, Wn, "low")

# Filter the input signal
output_signal = signal.lfilter(b, a, input_signal)

# Write the output file
sf.write(output_file, output_signal, sampl_freq)

print(f"The output file '{output_file}' has been successfully written!")