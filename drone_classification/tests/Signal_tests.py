from drone_classification.Signal import *
from definitions import DATA_FILES, TEMPLATE_FILES
import time




if __name__ == '__main__':
    templates = []
    start = time.time()
    for template in TEMPLATE_FILES:
        temp = Process(Matio(template, True))
        templates.append(temp)

    for file in DATA_FILES[1:]:
        s = Signal(Matio(file))
        s.wavelet_decomposition()
        breakpoints = s.change_point_detection(3, display=True)
        s.set_zeroes(0, breakpoints[0])
        factor = math.floor(len(s.get_signal())/5000)
        s.downsample(factor)
        for temp in templates:
            print(fastdtw(s.get_signal(), temp.get_signal()))



    print("time: {}".format(time.time()-start))