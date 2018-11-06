import matplotlib.pyplot as plt
import ruptures as rpt
import pywt
from scipy.spatial.distance import euclidean
from drone_classification.matio import Matio
from drone_classification.Signal import Signal





class DTW:
    """

    """

    def __init__(self, test_signal: Signal, templates: [Signal], dist_measure=euclidean):
        self.__test_signal = test_signal
        self.__templates = templates
        self.__dist_measure = dist_measure


    def dtw(self):
        pass



def wavelet_decomposition(signal: Signal):
    sample_frequency = signal.get_sampling_frequency()
    carrier_frequency = signal.get_frequency()
    levels = 0
    while sample_frequency > carrier_frequency:
        levels += 1


def changepoint_detection(signal: Signal, bkps = 1, window_width = 100, display = False):
    signal_data = signal.get_signal()[::5]
    algo = rpt.Window(width=window_width, model="rbf").fit(signal_data)
    breakpoints = algo.predict(n_bkps=bkps)
    if display:
        rpt.display(signal_data, breakpoints)
        plt.show()
    return breakpoints







"""
The purpose of this test is to find changepoints in waveforms captured by 
oscilloscope.  This file will load the .mat files provided in the data
directory of this folder.  The goal of using change-point detection is to
minimize the amount of data we will be processing using Dynamic Time Warping.
"""


if __name__ == '__main__':
    mat = Matio()
    data = Signal(mat)
    bkps = changepoint_detection(data, display=True)
    new_signal = data[bkps[0]*5:]
    plt.plot(new_signal)
    plt.show()


