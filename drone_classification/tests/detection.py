from drone_classification.Signal import *
from definitions import DATA_FILES, NUM_SIGNALS
import numpy as np
from math import log10
import pywt
import scipy
import matplotlib.pyplot as plt
import csv


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

def signal_to_noise(signal):
    return _signal_to_noise_helper(signal)

def get_noise_level(signal, desired_snr, threshold = .02):
    sig = signal.get_signal()
    desired_snr_linear = 10**(desired_snr/20)
    k = (1/desired_snr_linear)**.5
    noise = np.random.normal(scale=k*np.max(sig), size=len(sig))
    noise_sig = sig + noise
    return noise_sig


def main():
    detection_range = range(2400000, 2600000)
    detections = 0
    totaldetections = 0
    i = 0
    matrix = []
    controllers = ['DJIMatrice','DJI_Phantom_3','FLY_SKY_FS-T']
    # controllers = ['DJIMatrice', 'dc-162.4GHz','DJI_Phantom_3','DX5e-Spectrum','DX6e','FLY_SKY_FS-T','FutabaT8FG',\
    #   'Graupner_MC-32','HK-T6A_V6Controller','JR_x930324GHz','Spektrum_DX6i']
    with open("./results/noise.txt", mode='w') as file:
        for controller in controllers:
            clist = [cname for cname in DATA_FILES if controller in cname]
            row = []
            for desired_db in range(70, -1, -10):
                for sig_name in sorted(clist):
                    try:
                        temp_sig = Signal(Matio(sig_name))
                    except OSError:
                        continue
                    signal = get_noise_level(temp_sig, desired_db)
                    print("Getting Breakpoint")
                    bkp = temp_sig.cpd_signal(signal)[0]
                    del temp_sig
                    if bkp in detection_range:
                        detections += 1
                        totaldetections += 1
                        print("Detected: {}".format(sig_name))
                        file.write("Detected Signal: \t\t\t" + sig_name +"\n")
                    else:
                        print("Not Detected: {}".format(sig_name))
                        file.write("Failed to Detect Signal: \t" + sig_name +"\n")
                acc = detections / (len(clist)) * 100
                row.append(acc)
                detections = 0
                file.write("\n\n\tDetection accuracy: " + str(acc) + "% at SNR: {}\n\n".format(desired_db))
                print("Accuracy at {}dB: ".format(desired_db) + str(acc))
            matrix.append(row)
    with open('results.csv', 'w') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(matrix)

if __name__ == '__main__':
    main()
