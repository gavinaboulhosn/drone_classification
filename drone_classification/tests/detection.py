from drone_classification.Signal import *
from definitions import DATA_FILES, NUM_SIGNALS
import numpy as np
from math import log10
import pywt
import scipy
import matplotlib.pyplot as plt


def wd_signal(signal,  wavelet='haar'):
    max_level = pywt.dwt_max_level(len(signal), pywt.Wavelet(wavelet).dec_len)
    coeffs = pywt.wavedec(signal, 'haar', level=max_level)
    return coeffs[-1]


def bandpower(x, fmin, fmax, fs=20e9):
    f, Pxx = scipy.signal.periodogram(x, fs=fs)
    ind_min = np.where(f > fmin)[0][0] - 1
    ind_max = np.where(f > fmax)[0][-1] - 1
    return scipy.trapz(Pxx[ind_min: ind_max], f[ind_min: ind_max])




def min_max_of_f(x, fs=20e9):
    f, Pxx = scipy.signal.periodogram(x, fs=fs)
    pxx_max_index = np.argmax(Pxx)
    pxx_threshold = Pxx[pxx_max_index]*.1
    min_idx = np.where(Pxx[0:pxx_max_index] >= pxx_threshold)
    max_idx = np.where(Pxx[pxx_max_index+1:] >= pxx_threshold) + pxx_max_index
    return f[min_idx[0][0]], f[max_idx[0][-1]]

def _signal_to_noise_helper(a):
    s_min_idx, s_max_idx = min_max_of_f(a)
    signal_power = bandpower(a, s_min_idx, s_max_idx)
    return signal_power
    # b = wd_signal(a)
    # b /= np.max(np.abs(a), axis=0)
    # signal = b[len(b)//2 + 1:]
    # noise = b[:len(b)//2]
    # p_signal = (1/len(signal)) * np.sum(abs(signal)**2)
    # p_noise = (1/len(noise)) * np.sum(abs(noise)**2)
    # return 10 * log10(p_signal/p_noise), (p_signal, p_noise)

def signal_to_noise(signal):
    return _signal_to_noise_helper(signal)

def get_noise_level(signal, desired_snr, threshold = .02):
    sig = signal.get_signal()
    plt.plot(sig)
    plt.title("original")
    plt.show()
    signal_power = signal_to_noise(sig)
    desired_snr_linear = 10**(desired_snr/20)
    noise_power = (signal_power/desired_snr_linear)
    k = (1/desired_snr_linear)**.5
    noise = np.random.normal(scale=k*np.max(sig), size=len(sig))
    noise_sig = sig + noise
    plt.plot(noise_sig)
    plt.title("modified: {}dB".format(desired_snr))
    plt.show()
    # db = signal_to_noise(sig)
    # lower_bound = desired_db - desired_db*threshold
    # upper_bound = desired_db + desired_db*threshold
    # noise_level = 0
    # noise_i = sig.shape[0]
    # while db >= lower_bound:
    #     noise_level += 5
    #     noise = np.random.normal(0, noise_level, (noise_i, ))
    #     noise_sig = sig[:noise_i] + noise
    #     sig[:noise_i] = noise_sig
    #     db = signal_to_noise(sig)
    #     if lower_bound <= db <= upper_bound:
    #         return sig
    # return sig
    return noise_sig


def main():
    detection_range = range(2455000, 2555000)
    detections = 0
    with open("./results/noise.txt", mode='w') as file:
        for desired_db in range(35, -1, -5):
            i = 0
            for sig_name in sorted(DATA_FILES):
                temp_sig = Signal(Matio(sig_name))
                signal = get_noise_level(temp_sig, desired_db)
                SNR = signal_to_noise(signal)
                print("SNR: " + str(SNR))
                bkp = temp_sig.cpd_signal(signal)[0]
                del temp_sig
                if bkp in detection_range:
                    detections += 1
                    print("Detected: {}".format(sig_name))
                    file.write("Detected Signal: \t\t\t" + sig_name + " with SNR: " + str(SNR) + "\n")
                else:
                    print("Not Detected: {}".format(sig_name))
                    file.write("Failed to Detect Signal: \t" + sig_name + " with SNR: " + str(SNR) + "\n")
                i += 1
                print(i)
            acc = detections / (len(DATA_FILES)) * 100
            file.write("\n\n\tDetection accuracy: " + str(acc) + "% at SNR: {}\n\n".format(desired_db))
            print("Accuracy at {}dB: ".format(desired_db) + str(acc))
            detections = 0

if __name__ == '__main__':
    #main()
    sig = 'phantom_4PRO00001.mat'
    signal = Signal(Matio(sig))
    noisesig = get_noise_level(signal, 77)