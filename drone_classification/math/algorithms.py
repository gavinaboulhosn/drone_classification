import matplotlib.pyplot as plt
import ruptures as rpt
from time import time
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
from drone_classification.get_data_path import get_data_path
from drone_classification.matio import matio

# algo = rpt.Dynp(model="rbf").fit(y1c)              # dynamic programing O(k*n^2)
# algo = rpt.Binseg(model="rbf").fit(y)              # binary segmentation O(nlogn)
# algo = rpt.Window(width = 100, model="rbf").fit(y)  # window-based O(n)

def changepoint_detection(signal, bkps = 1, window_width = 100, display = False):
    algo = rpt.Window(width=window_width, model="rbf").fit(signal)
    breakpoints = algo.predict(n_bkps=bkps)
    if display:
        rpt.display(signal, breakpoints)
        plt.show()
    return breakpoints


class DTW(fastdtw):
    """

    """

    def __init__(self, signalA, signalB, dist_measure=euclidean):
        pass


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
    start_time = time()
    bkps = changepoint_detection(data[::5], display=True)
    end_time = time()
    new_signal = data[bkps[0]*5:]
    plt.plot(new_signal)
    plt.show()
    print(end_time-start_time)


