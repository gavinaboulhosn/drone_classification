from drone_classification.Signal import *
from definitions import DATA_FILES, NUM_SIGNALS
import numpy as np

if __name__ == '__main__':
    num_test_signals = len(DATA_FILES)//NUM_SIGNALS - 1
    signals_matrix = np.ndarray(shape=(num_test_signals, ), dtype=list)
    drone_controllers = ['FRSKY0000', 'phantom_4PRO0000', 'T14SG0000']
    detection_range = range(2455000, 2555000)
    detections = 0


    with open("detection_results.txt", mode='w') as file:
        for factor in [500, 750, 1000]:
            file.write("CPD Decimation Factor: " + str(factor) + "\n\n")
            for sig_name in DATA_FILES:
                temp_sig = Signal(Matio(sig_name))
                bkp = temp_sig.change_point_detection(factor=factor)[0]
                if bkp in detection_range:
                    detections += 1
                    file.write("\tDetected Signal: " + sig_name+ "\n")
                else:
                    file.write("\tFailed to Detect Signal: " + sig_name + "\n")

            accuracy = detections/(len(DATA_FILES)) * 100
            file.write("\n\n\tDetection accuracy: " + str(accuracy)+ "%")
            print(accuracy)
            detections = 0