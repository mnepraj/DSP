import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft, ifft
from scipy import signal

# Load the WAV file
sample_rate, data_stereo = wavfile.read('sound.wav')
print("WAV file loaded with sample rate:", sample_rate)

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

# Extract individual channels
channel1 = data_stereo[:, 0]  # Left channel
channel2 = data_stereo[:, 1]  # Right channel
print("Channels extracted")
print("Channel 1:", channel1)
print("Channel 2:", channel2)

# Create an impulse signal
impulse = np.zeros(len(channel1))
impulse[0] = 1

# Apply the filter to the impulse signal to get the filter's impulse response
filter_impulse_response = signal.lfilter(b, a, impulse)
print("Filter impulse response obtained:")
print(filter_impulse_response)

# Take the FFT of the filter's impulse response to get its frequency response
frequency_response = np.fft.fft(filter_impulse_response)
print("Frequency response obtained:")
print(frequency_response)

# Perform FFT for each channel
fft_result_channel1 = fft(channel1)
fft_result_channel2 = fft(channel2)
print("FFT performed for both channels")
print("FFT result for channel 1:", fft_result_channel1)
print("FFT result for channel 2:", fft_result_channel2)

# Calculate the frequency axis
freqs_channel1 = np.fft.fftfreq(len(fft_result_channel1)) * sample_rate
freqs_channel2 = np.fft.fftfreq(len(fft_result_channel2)) * sample_rate
print("Frequency axis calculated")
print("Frequency axis for channel 1:", freqs_channel1)
print("Frequency axis for channel 2:", freqs_channel2)

# Ensure both frequency responses have the same length
frequency_response = np.pad(frequency_response, (0, len(fft_result_channel1) - len(frequency_response)))

# Multiply the frequency responses
result_frequency_response_channel1 = fft_result_channel1 * frequency_response
result_frequency_response_channel2 = fft_result_channel2 * frequency_response
print("Frequency responses multiplied")
print("Result frequency response for channel 1:", result_frequency_response_channel1)
print("Result frequency response for channel 2:", result_frequency_response_channel2)

signal_channel1 = np.real(ifft(result_frequency_response_channel1))
signal_channel2 = np.real(ifft(result_frequency_response_channel2))
print("Inverse FFT performed")
# Calculate the time axis in seconds
time_axis = np.arange(len(signal_channel1)) / sample_rate

# Plot the time-domain signals and their FFTs
plt.figure(figsize=(16, 8))

plt.subplot(2, 2, 1)
plt.plot(time_axis, signal_channel1)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Channel 1 Signal')
plt.grid()

plt.subplot(2, 2, 2)
plt.plot(freqs_channel1, np.abs(result_frequency_response_channel1))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Channel 1 Multiplied Frequency Response')
plt.grid()

plt.subplot(2, 2, 3)
plt.plot(time_axis, signal_channel2)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Channel 2 Signal')
plt.grid()

plt.subplot(2, 2, 4)
plt.plot(freqs_channel2, np.abs(result_frequency_response_channel2))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Channel 2 Multiplied Frequency Response')
plt.grid()

plt.tight_layout()
plt.savefig('../figs/ynexercise.png')
