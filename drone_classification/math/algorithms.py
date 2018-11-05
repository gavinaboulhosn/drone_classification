import matplotlib.pyplot as plt
import ruptures as rpt
import pywt
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
from drone_classification.get_data_path import get_data_path
from drone_classification.matio import matio





class DTW:
    """

    """

    def __init__(self, signalA, signalB, dist_measure=euclidean):
        pass

    def dtw(self, signal):
        pass



def wavelet_decomposition(signal, levels):
    pass

def changepoint_detection(signal, bkps = 1, window_width = 100, display = False):
    algo = rpt.Window(width=window_width, model="rbf").fit(signal)
    breakpoints = algo.predict(n_bkps=bkps)
    if display:
        rpt.display(signal, breakpoints)
        plt.show()
    return breakpoints







"""
The purpose of this test is to find changepoints in waveforms captured by 
oscilloscope.  This file will load the .mat files provided in the data
directory of this folder.  The goal of using change-point detection is to
minimize the amount of data we will be processing using Dynamic Time Warping.
"""


if __name__ == '__main__':

    path = get_data_path(4)
    mat = matio(path)
    data = mat.extract_data()
    bkps = changepoint_detection(data[::5], display=True)
    new_signal = data[bkps[0]*5:]
    plt.plot(new_signal)
    plt.show()


