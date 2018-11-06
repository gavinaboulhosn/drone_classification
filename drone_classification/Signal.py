from drone_classification.matio import Matio

class Signal(object):
    """

    """
    def __init__(self, signal: Matio, freq=2.6e9):
        """
        constructor expects a Matio object to initialize all the signal parameters
        :param signal:
        """
        self.__signal = signal.extract_data()
        self.__sampling_frequency = signal.get_sample_freq()
        self.__carrier_frequency = freq

    def get_signal(self):
        return self.__signal

    def get_sampling_frequency(self):
        return self.__sampling_frequency

    def get_frequency(self):
        return self.__carrier_frequency

