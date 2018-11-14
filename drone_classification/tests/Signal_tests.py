from drone_classification.Signal import *
from definitions import DATA_FILES




if __name__ == '__main__':
    for file in DATA_FILES[1:]:
        s = Signal(Matio(file))
        s.wavelet_decomposition()
        s.change_point_detection(display=True)
        plt.plot(s.get_signal())
        plt.title("{} Before QMF".format(file).replace('.mat', ''))
        plt.show()
        test = s.quadrature_mirror_filter()
        plt.plot(test)
        plt.title("{} After QMF".format(file).replace('.mat', ''))
        plt.show()
