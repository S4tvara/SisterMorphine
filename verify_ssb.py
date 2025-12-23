import numpy as np
from scipy.signal import hilbert
import matplotlib.pyplot as plt

# Parameters
fs = 100_000
fc = 10_000
fm = 500
duration = 0.01
Amplitude = 1.0
ka = 0.5
time_array = np.arange(0, duration, 1/fs)

# Signals
message = np.sin(2 * np.pi * fm * time_array)
carrier = Amplitude * np.sin(2 * np.pi * fc * time_array)
s_dsb_sc = ka * message * carrier

# Hilbert
message_hat = np.imag(hilbert(message))
carrier_quad = Amplitude * np.cos(2 * np.pi * fc * time_array)

# SSB LSB
s_ssb_lower = s_dsb_sc - (ka * message_hat * carrier_quad)

# Check first few values
print("t=0:")
print(f"message: {message[0]}")
print(f"message_hat: {message_hat[0]}")
print(f"carrier: {carrier[0]}")
print(f"carrier_quad: {carrier_quad[0]}")
print(f"s_dsb_sc: {s_dsb_sc[0]}")
print(f"s_ssb_lower: {s_ssb_lower[0]}")

print("\nPeak values:")
print(f"Max SSB: {np.max(s_ssb_lower)}")
print(f"Min SSB: {np.min(s_ssb_lower)}")
print(f"Expected Amp: {ka * Amplitude}")

# Check frequency content
freqs = np.fft.rfft(s_ssb_lower)
freq_axis = np.fft.rfftfreq(len(time_array), 1/fs)
peak_freq = freq_axis[np.argmax(np.abs(freqs))]
print(f"\nDominant Frequency: {peak_freq} Hz")
print(f"Expected LSB Frequency: {fc - fm} Hz")
