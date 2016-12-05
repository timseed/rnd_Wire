import numpy as np

'''
The purpose of this is to calculate is a length of wire is suitable for random wire lengths.

It should therefore not be

   a) Not Half wave on any frequency
   b) Not a multiple of the half-wave length.
'''

b160 = np.arange(1800, 2000.)
b80 = np.arange(3500., 4000.)
b60 = np.arange(5330.5, 5405.)  # 40m */
b40 = np.arange(7000., 7300.)  # 40m */
b30 = np.arange(10100., 10150.)  # 30m */
b20 = np.arange(14000., 14350.)  # 20m */
b17 = np.arange(18068., 18168.)  # 17m */
b15 = np.arange(21000., 21450.)  # 15m */
b12 = np.arange(24890., 24990.)  # 12m */
b10 = np.arange(28000., 29700.)  # 10m */

Frequency = b60.tolist() + b40.tolist() + b30.tolist() + b20.tolist() + \
            b17.tolist() + \
            b15.tolist() + \
            b12.tolist() + \
            b10.tolist()
Frequency = [f / 1000 for f in Frequency]
# Frequency = [1.9, 3.6, 7.01, 7.02, 7.03, 7.04, 7.05, 14.01, 14.02, 14.03, 14.04, 14.05, 18.7, 21.01, 21.02, 21.03,
#             21.04, 21.05,24.8, 24.9, 28.05]


Bad = []
maxHarmonic = 32  # Number of harmonics to check out too
maxAntLength = 50  # Max Length in M that the random wire can be


def f_to_w(freq_in_mhz):
    w = 300 / freq_in_mhz
    return w


def harmonic(wavelength_in_m, harmonic_level):
    return wavelength_in_m * harmonic_level


def meter_to_feet(m):
    return m * 3.28084


for f in Frequency:

    print(str.format('Freq {} Wavelength {}', f, f_to_w(f)))
    w_in_m = f_to_w(f)
    half_wave = w_in_m / 2.0
    for multi in range(1, maxHarmonic + 1):
        Bad.append(harmonic(half_wave, multi))

# Sort the Bad Frequencies
Bad.sort()
for b in Bad:
    print(str.format("Avoid {}m  {}f", round(b, 2), round(meter_to_feet(b), 2)))

print("=========Possible good lengths =============")
pre = Bad[0]
for b in Bad:
    if b - pre > 0.5:
        if b < maxAntLength:
            print(str.format("Possible good length at {}M {}Ft", round(b, 2), round(meter_to_feet(b), 2)))
    pre = b
