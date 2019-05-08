from definitions import *


def get_data_path(filename=None):
    return os.path.join(DATA_PATH, filename)

def get_template_path(filename):
    return os.path.join(TEMPLATE_PATH, filename)
