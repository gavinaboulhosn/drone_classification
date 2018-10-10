from drone_classification.math.CPD import changepoint_detection
from drone_classification.get_data_path import get_data_path
from drone_classification.matio import matio
import matplotlib.pyplot as plt

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
    plt.plot(data[bkps[0]*5:])
    plt.show()
