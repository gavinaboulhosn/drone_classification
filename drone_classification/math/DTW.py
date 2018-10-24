from fastdtw import fastdtw
from drone_classification.matio import matio
from drone_classification.math.CPD import changepoint_detection
from drone_classification.get_data_path import get_data_path
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt

path = get_data_path(2)
mat = matio(path)

data = mat.extract_data()
bkps = changepoint_detection(data[::5])

signal = data[bkps[0]*5:]



distance, path = fastdtw(signal, data, dist=euclidean)
plt.plot(path)
plt.show()
