import matplotlib.pyplot as plt

import pywt
from scipy.spatial.distance import euclidean
from drone_classification.matio import Matio
from drone_classification.Signal import Signal
from definitions import TEMPLATE_FILES





class DTW:
    """

    """

    def __init__(self, test_signal: Signal, dist_measure=euclidean):
        self.__test_signal = test_signal
        self.__templates = TEMPLATE_FILES
        self.dist_measure = dist_measure


    def dtw(self):
        pass



def wavelet_decomposition(signal: Signal):
    sample_frequency = signal.get_sampling_frequency()
    carrier_frequency = signal.get_frequency()
    levels = 0
    while sample_frequency > carrier_frequency:
        levels += 1









"""
The purpose of this test is to find changepoints in waveforms captured by 
oscilloscope.  This file will load the .mat files provided in the data
directory of this folder.  The goal of using change-point detection is to
minimize the amount of data we will be processing using Dynamic Time Warping.
"""


if __name__ == '__main__':
    mat = Matio("UAV00005.mat")
    signal = Signal(mat)
    signal.change_point_detection()
    new_signal = signal.get_signal()
    plt.plot(new_signal)
    plt.show()


