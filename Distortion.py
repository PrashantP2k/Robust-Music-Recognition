import numpy as np
from IPython.display import Audio
import matplotlib.pyplot as plt

def normalize(x, y_min, y_max):
    x_min = np.min(x)
    x_max = np.max(x)
    return (((x - x_min) / (x_max - x_min)) * (y_max - y_min))

def tanh_distortion(x, gain):
    rms = np.sqrt(np.mean(x ** 2))
    y = normalize(np.tanh(gain * x), np.min(x), rms)
    y = (y - np.mean(y))
    return y

def clipping_distortion(x, gain):
    rms = np.sqrt(np.mean(x ** 2))
    y = np.clip((gain * x), np.min(x), rms)
    y = (y - np.mean(y))
    return y

def distortion(x, gain, mode = 'tanh'):
    if (mode == 'tanh'):
        return tanh_distortion(x, gain)
    elif (mode == 'clipping'):
        return clipping_distortion(x, gain)
    else:
        raise ValueError (mode, "is not a valid distortion mode")
        return

if __name__ == '__main__':

    # Generate input signal (sine wave)
    fs = 44100
    duration = 5
    f = 440
    t = np.linspace(0, duration, int(fs * duration))
    x = (10 * np.sin(2 * np.pi * f * t))
    
    Audio(x, rate = fs)
    
    # Define Tube Screamer parameters
    gain = 30
    tone = 500
    level = 0
    
    y = distortion(x, 1e-4, 'tanh')
    
    Audio(y, rate = fs)
    
    # Plot input and output signals
    plt.plot(t[:100], x[:100], label = 'Input')
    plt.plot(t[:100], y[:100], label = 'Output')
    plt.legend()
    plt.show()