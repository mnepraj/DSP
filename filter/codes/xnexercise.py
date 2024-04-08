import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Load the WAV file
sample_rate, data_stereo = wavfile.read('sound.wav')

# Extract individual channels
channel1 = data_stereo[:, 0]  # Left channel
channel2 = data_stereo[:, 1]  # Right channel

# Calculate the time axis in seconds
time_axis = np.arange(len(channel1)) / sample_rate

# Plot both channels
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(time_axis, channel1)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Left Channel')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(time_axis, channel2)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Right Channel')
plt.grid()

plt.tight_layout()
plt.savefig('../figs/xnexercise.png')
