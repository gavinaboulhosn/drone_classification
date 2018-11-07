import matplotlib.pyplot as plt
import time
from scipy.spatial.distance import euclidean
from drone_classification.matio import Matio
from drone_classification.Signal import Signal
from definitions import TEMPLATE_FILES



class DTW:
    """

    """

    def __init__(self, test_signal: Signal, measure=euclidean):
        self.__test_signal = test_signal
        self.__templates = TEMPLATE_FILES
        self.dist_measure = measure


    def dtw(self):
        pass



"""
The purpose of this test is to find changepoints in waveforms captured by 
oscilloscope.  This file will load the .mat files provided in the data
directory of this folder.  The goal of using change-point detection is to
minimize the amount of data we will be processing using Dynamic Time Warping.
"""


if __name__ == '__main__':
    mat = Matio("UAV00005.mat")
    signalBefore = Signal(mat)
    print("Signal before ")
    ta = time.time()
    signalBefore.change_point_detection(display=True)
    print("First: ", time.time()-ta, " Seconds")
    new_signal = signalBefore.get_signal()

    plt.figure(1)
    plt.plot(new_signal)
    plt.title("Signal without wavelet decomp")
    # plt.show()
    signalAfter = Signal(mat)
    print("Signal After")

    signalAfter.wavelet_decomposition()
    tb = time.time()
    signalAfter.change_point_detection(display=True)
    print("Second: ", time.time()-tb, " Seconds")
    new_signalAfter = signalAfter.get_signal()
    plt.figure(2)
    plt.plot(new_signalAfter)
    plt.title("Signal with wavelet decomp")
    plt.show()




