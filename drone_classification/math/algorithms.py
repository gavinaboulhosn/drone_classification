import matplotlib.pyplot as plt
import time
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
from drone_classification.matio import Matio
from drone_classification.Signal import Signal
from definitions import TEMPLATE_FILES



class DTW:
    """

    """

    def __init__(self, test_signal, measure=euclidean):
        self.__test_signal = test_signal
        self.__templates = TEMPLATE_FILES
        self.dist_measure = measure
        self.signal = self.__test_signal.get_signal()


    def dtw(self):
        for test in self.__templates:
            template = Signal(Matio(test, template=True))
            print("here")
            template_signal = template.get_signal()
            print("got signal")
            print(fastdtw(self.signal, template_signal, dist=self.dist_measure))




"""
The purpose of this test is to find changepoints in waveforms captured by 
oscilloscope.  This file will load the .mat files provided in the data
directory of this folder.  The goal of using change-point detection is to
minimize the amount of data we will be processing using Dynamic Time Warping.
"""


if __name__ == '__main__':
    mat = Matio("UAV00005.mat")
    signal = Signal(mat)
    signal.wavelet_decomposition()
    signal.change_point_detection()
    dtw = DTW(signal)
    dtw.dtw()