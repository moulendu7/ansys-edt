import numpy as np

data = np.loadtxt("s11_data.csv", delimiter=",", skiprows=1)

freq = data[:, 0]
s11 = data[:, 1]

mask = s11 <= -10
band_freqs = freq[mask]

if len(band_freqs) > 0:
    f_low = band_freqs.min()
    f_high = band_freqs.max()
    bw = f_high - f_low

    print("Bandwidth:")
    print("Lower:", f_low, "GHz")
    print("Upper:", f_high, "GHz")
    print("BW:", bw, "GHz")
else:
    print("No bandwidth found")

idx = np.argmin(s11)
print("\nResonance Frequency:", freq[idx], "GHz")
print("Min S11:", s11[idx], "dB")