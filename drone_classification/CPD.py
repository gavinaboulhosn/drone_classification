import numpy as np
import matplotlib.pyplot as plt
import ruptures as rpt
import scipy.io
import h5py
import os


# algo = rpt.Dynp(model="rbf").fit(y1c)              # dynamic programing O(k*n^2)
# algo = rpt.Binseg(model="rbf").fit(y)              # binary segmentation O(nlogn)
# algo = rpt.Window(width = 100, model="rbf").fit(y)  # window-based O(n)

def changepoint_detection(signal, window_width = 150, display = False):
    algo = rpt.Window(width=window_width, model="rbf").fit(signal)
    breakpoints = algo.predict(n_bkps=2)
    print(breakpoints)
    start, end = breakpoints[0], breakpoints[1]
    if display:
        rpt.display(signal, breakpoints)
        plt.show()
    return signal[start:end]

if __name__ == '__main__':
    curr_path = os.path.dirname(__file__)
    path = os.path.relpath('../data/UAV00001.mat', curr_path)
    mat = h5py.File(path)
    # dset = mat.create_dataset("UAV001",shape=(50000,1), dtype=float)
    # print(mat["Channel_1"]["Data"])
    res = []
    for x in mat["Channel_1"]["Data"]:
        print(x)