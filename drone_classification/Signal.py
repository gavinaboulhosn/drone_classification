import ruptures as rpt
import matplotlib.pyplot as plt
from drone_classification.matio import Matio
import pywt


class Signal(object):
    """

    """
    def __init__(self, signal: Matio, freq=2.6e9):
        """
        constructor expects a Matio object to initialize all the signal parameters
        :param signal:
        """
        self.__signal = signal.extract_data()
        self.__carrier_frequency = freq
        self.signal_file = signal


    def get_signal(self):
        return self.__signal

    def get_frequency(self):
        return self.__carrier_frequency

    def change_point_detection(self, window_width = 2500, display=False, factor=780):
        signal_data = self.__signal[::factor]
        algo = rpt.Window(width=window_width, model="rbf").fit(signal_data)
        bkps = algo.predict(n_bkps=1)
        if display:
            rpt.display(self.__signal, [x*factor for x in bkps])
            plt.show()

        #self.__signal = self.__signal[bkps[0]*factor:]
        for i in range(len(bkps)):
            bkps[i] *= factor
        return bkps
    def cpd_signal(self, signal, window_width = 2500, display=False, factor=780):
        tmpsignal = signal[::factor]
        algo = rpt.Window(width=window_width, model="rbf").fit(tmpsignal)
        bkps = algo.predict(n_bkps=1)
        if display:
            rpt.display(signal, [x*factor for x in bkps])
            plt.show()

        #self.__signal = self.__signal[bkps[0]*factor:]
        for i in range(len(bkps)):
            bkps[i] *= factor
        return bkps

    def set_zeroes(self, index0=0, index1 = -1):
        self.__signal[index0:index1] = 0
    #
    # def downsample(self, factor=5):
    #     self.__signal = self.__signal[::factor]

    def set_new_signal(self, start_index, end_index):
        self.__signal = self.__signal[start_index:end_index]

    def export_to_mat(self, filename):
        self.signal_file.export(self.get_signal(), filename)

    def get_sample_freq(self):
        return 1/self.signal_file['Channel_1']['XInc'][0][0]

    def wavelet_decomposition(self, wavelet='haar'):
        max_level = pywt.dwt_max_level(len(self.__signal), pywt.Wavelet(wavelet).dec_len)
        coeffs = pywt.wavedec(self.__signal, 'haar', level=max_level)
        self.__signal = coeffs[-1]



    # # def quadrature_mirror_filter(self):
    #     self.__signal = pywt.qmf(self.__signal)
    #     return pywt.qmf(self.__signal)


# class Process(Signal):
#     def __init__(self, signal):
#         super(Process, self).__init__(signal)
#         self.wavelet_decomposition()
#         factor = math.floor(len(self.get_signal())/50000)
#         self.downsample(factor)
#         bkps = self.change_point_detection(3)
#         self.set_zeroes(0, bkps[0])
#         finalfactor = math.floor(len(self.get_signal())/5000)
#         self.downsample(finalfactor)
#
