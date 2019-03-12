import h5py
import numpy as np
from drone_classification.get_data_path import get_data_path, get_template_path


class Matio:
    """
    This class deals with handling I/O of .mat files and contains helper functions
    to easily obtain the different structures contained in the files.

    """
    def __init__(self,file=None, template=False):
        if template:
            self.path = get_template_path(filename=file)
        else:
            self.path = get_data_path(filename=file)
            self.file = h5py.File(self.path)


    def extract_data(self):
        """
        This function is specific to opening Channel_1 struct's Data field
        :return: numpy array of points recorded by oscilloscope
        """
        channel_1 = self.file["Channel_1"]
        return np.array(channel_1['Data'])[0]

    def extract_keys(self):
        """
        This function will return all keys stored inside .mat file.
        :return: list of keys
        """
        return list(self.file.keys())

    def channel_1_keys(self):
        """
        this helper function will obtain the keys in the channel_1 struct
        :return: list of channel 1 keys
        """
        return list(self.file['Channel_1'].keys())

    def export(self, filename):
        pass

