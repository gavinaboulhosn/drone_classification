import ruptures as rpt
import matplotlib.pyplot as plt
from drone_classification.matio import Matio
import pywt
import numpy as np

class Signal(object):
    """

    """
    def __init__(self, signal: Matio, freq=2.6e9):
        """
        constructor expects a Matio object to initialize all the signal parameters
        :param signal:
        """
        self.__signal = signal.extract_data()
        self.__sampling_frequency = signal.get_sample_freq()
        self.__carrier_frequency = freq
        self._SNR = None


    def get_signal(self):
        return self.__signal

    def get_sampling_frequency(self):
        return self.__sampling_frequency

    def get_frequency(self):
        return self.__carrier_frequency

    def change_point_detection(self, breakpoints = 1, window_width = 100, display=False, factor=5):
        signal_data = self.__signal[::factor]
        algo = rpt.Window(width=window_width, model="rbf").fit(signal_data)
        bkps = algo.predict(n_bkps=breakpoints)
        if display:
            rpt.display(self.__signal, [x*factor for x in bkps])
            plt.show()
        noise = np.max(self.__signal[:bkps[0] * factor]) - np.min(self.__signal[:bkps[0] * factor])
        signal = np.max(self.__signal[bkps[0] * factor:]) - np.min(self.__signal[bkps[0] * factor:])
        self._SNR = signal / noise
        self.__signal = self.__signal[bkps[0]*factor:]
        for i in range(len(bkps)):
            bkps[i] *= factor
        return bkps


    def wavelet_decomposition(self, wavelet='haar'):
        max_level = pywt.dwt_max_level(len(self.__signal), pywt.Wavelet(wavelet).dec_len)
        coeffs = pywt.wavedec(self.__signal, 'haar', level=max_level)
        self.__signal = coeffs[-1]

    def quadrature_mirror_filter(self):
        return pywt.qmf(self.__signal)
