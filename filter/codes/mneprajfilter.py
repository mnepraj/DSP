import numpy as np

def unit_step(t):
    """
    Define unit step function
    """
    return np.where(t >= 0, 1, 0)

def mneprajfilter(a, b, input_signal, sampl_freq):
    """
    Apply butterworth filter to input signal using forward-backward filtering
    """
    num_channels = input_signal.shape[1] if len(input_signal.shape) > 1 else 1
    N = len(input_signal)
    t = np.arange(N) / sampl_freq
    output_signal = np.zeros_like(input_signal)
    for channel in range(num_channels):
        # Convolve b with unit step
        forward_filtered = np.convolve(b, unit_step(t) * input_signal[:, channel], mode='full')[:N]
        # Convolve a with unit step
        backward_filtered = np.convolve(a, unit_step(t) * forward_filtered, mode='full')[:N]
        # Assign filtered signal to appropriate channel
        output_signal[:, channel] = backward_filtered
    # Return the output signal
    return output_signal
