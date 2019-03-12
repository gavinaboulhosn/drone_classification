from drone_classification.Signal import *
from definitions import DATA_FILES, NUM_SIGNALS
import numpy as np
from fastdtw import fastdtw






if __name__ == '__main__':
    num_test_signals = len(DATA_FILES)//NUM_SIGNALS - 1

    test_signals_matrix = np.ndarray(shape=(NUM_SIGNALS, num_test_signals), dtype=list)

    drone_controllers = ['FRSKY0000', 'phantom_4PRO0000', 'T14SG0000']

    for template_index in range(NUM_SIGNALS):
        for test_index in range(num_test_signals):
            sig_name = drone_controllers[template_index] + str(test_index+1) + '.mat'
            temp_sig = Signal(Matio(sig_name))
            temp_sig.set_new_signal(int(2.49e6), int(2.51e6))
            temp_sig.wavelet_decomposition()
            signal = temp_sig.get_signal()


            test_signals_matrix[template_index][test_index] = (signal)



    DTW_Cell = np.ndarray(shape=(3,), dtype=object)
    template_signal_index = 0
    cell = []
    l2 = lambda x,y: (x-y)**2

    for idx_dtw in range(NUM_SIGNALS):
        template_pk = test_signals_matrix[idx_dtw][template_signal_index]
        DTW_matrix = np.ndarray(shape=(NUM_SIGNALS, num_test_signals), dtype=list)
        for row_idx in range(NUM_SIGNALS):
            for col_idx in range(num_test_signals):
                test_signal = test_signals_matrix[row_idx][col_idx]

                temp_dtw = fastdtw(template_pk, test_signal, dist=l2)[0]
                DTW_matrix[row_idx][col_idx] = temp_dtw
                #print(col_idx)
        print("*******************************************************************************************************************************************************")
        print('\n'.join(['\t '.join(['{:8}'.format(item) for item in row])
                         for row in DTW_matrix]))
        DTW_Cell[idx_dtw] = DTW_matrix



    # for template in TEMPLATE_FILES:
    #     temp = Process(Matio(template, True))
    #     templates.append(temp)
    # min = float('inf')
    # for file in DATA_FILES[1:]:
    #     s = Signal(Matio(file))
    #     # s.wavelet_decomposition()
    #     breakpoints = s.change_point_detection(3)
    #     s.set_zeroes(0, breakpoints[0])
    #     factor = math.floor(len(s.get_signal())/5000)
    #     s.downsample(factor)
    #     for temp in templates:
    #         distance, path = fastdtw(s.get_signal(), temp.get_signal())
    #         print(distance)
    #         plt.plot(path)
    #         plt.show()



