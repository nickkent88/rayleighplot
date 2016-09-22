import math

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

from numpy import exp, inf, linspace, log, log10
from scipy.special import jv as first_bessel
# import seaborn as sns

# BOLTZMANNS_CONSTANT_k = -228.6;                           # dBW/Hz/K
BOLTZMANNS_CONSTANT_k = 1.38065e-23                          # J/K
NOISE_TEMP_T = 350                                           # K (250K Receiver 
                                                             #   + 150K Antenna)
NOISE_EQUIV_BANDWIDTH_B = 1.2672                             # MHz
NOISE_EQUIV_BANDWIDTH_B = NOISE_EQUIV_BANDWIDTH_B * 1000000  # Hz
TOTAL_THERMAL_NOISE_POWER_kTB = (BOLTZMANNS_CONSTANT_k *
                                 NOISE_TEMP_T *
                                 NOISE_EQUIV_BANDWIDTH_B)

X_LABEL = 'percent exceeding ordinate'
X_TICKS = [0.0001, 0.01, 0.1, 1, 5, 10, 20, 30,
           40, 50, 60, 70, 80, 90, 95, 98, 99]
X_TICKS_LABEL = [str(number) for number in X_TICKS]
X_TICKS_ACTUAL = [number / 100 for number in X_TICKS]


def probability_false_alarm(envelope, thermal_noise_power):
    # Bob said to put the 50 in there
    return exp(-(envelope**2) /
                (2 * 50 * thermal_noise_power))


def threshold_from_probability_false_alarm(
        probability_false_alarm, thermal_noise_power):
    return math.sqrt(-2 * 50 * thermal_noise_power *
                     log(probability_false_alarm))


# snr = amplitude**2/(2*thermal_noise_power)
# amplitude = sqrt(snr*2*thermal_noise_power)
def envelope_pdf(envelope, amplitude, thermal_noise_power):
    return ((envelope / thermal_noise_power) *
            exp(-(envelope**2 + amplitude**2) / (2 * thermal_noise_power)) *
            first_bessel(0, (envelope * amplitude) / thermal_noise_power))


def probability_detection(
        voltage_threshold, envelope, amplitude, thermal_noise_power):
    pdf_of_envelope = envelope_pdf(envelope, amplitude, thermal_noise_power)
    return sp.integrate.quad(pdf_of_envelope, voltage_threshold, inf)


def rayleigh_x(probability, probability_at_origin):
    return (10.0 * log10(-log(probability_at_origin)) -
            10.0 * log10(-log(probability)))


def rayleigh_y(amplitude):
    return 10.0 * log10(amplitude**2)


def rayleigh_x_ticks(x_ticks):
    x_at_origin = x_ticks[0]
    return rayleigh_x(x_ticks, x_at_origin)


def amplitude_probability_density(samples):
    amplitude = np.sort(samples)
    N = len(samples)
    probability = 1 - np.arange(0, N) / N
    # print(probability)
    return probability, amplitude


def plot_apd(amplitude, probability, title='APD'):
    ptick = X_TICKS_ACTUAL
    porigin = ptick[0]

    # if min(amplitude) == 0:
    #   index = np.find(min(amplitude))
    #   amplitude[index] = None

    # probability[-1] = None

    x = rayleigh_x(probability, porigin)
    y = rayleigh_y(amplitude)
    plt.plot(x, y)
    plt.grid()

    plt.xlabel('percent exceeding ordinate')
    plt.ylabel('dBV')
    xtick = rayleigh_x(ptick, porigin)
    plt.xlim(0, 1)
    plt.xticks(xtick, X_TICKS_LABEL)
    plt.title(title)
    plt.show()


if __name__ == '__main__':
    voltages = linspace(0, .00002, 300000)[1:]
    probability = probability_false_alarm(voltages, TOTAL_THERMAL_NOISE_POWER_kTB)
    amplitude = voltages
    plt.plot(probability, amplitude)
    plt.ylim(0, .00003)
    plt.grid()
    # plt.ylim(0,5000)
    plt.show()

    print(probability[0:5], amplitude[0:5])
    print(probability[-5:-1], amplitude[-5:-1])

    plot_apd(amplitude, probability, 'Probability of False Alarm')

    # BOB'S GAUSSIAN NOISE GRAPH
    n = 10**6
    v = np.random.randn(n) + np.random.randn(n) * 1j
    probability, amplitude = amplitude_probability_density(abs(v))
    # plot_apd(amplitude, probability,
    # 'Simulated complex Gaussian noise, variance 2V^2, N=10^6.')
    # plt.show()

    # BOB'S OTHER GRAPH
    n = 10**4
    v = np.arange(0, n - 1)
    # probability, amplitude = amplitude_probability_density(abs(v))
    # plot_apd(amplitude, probability)
    # snr = 8
    # amplitude = np.sqrt(snr * 2 * TOTAL_THERMAL_NOISE_POWER_kTB)
    # print(
    #     probability_detection(5000, 100, amplitude, TOTAL_THERMAL_NOISE_POWER_kTB))

    # kTB = BOLTZMANNS_CONSTANT_k * NOISE_TEMP_T * NOISE_EQUIV_BANDWIDTH_B
