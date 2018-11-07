from definitions import *


def get_data_path(filename=None, n=4):
    if not filename:
        return os.path.join(DATA_PATH, DATA_FILES[n-1])

    if filename not in DATA_FILES:
        print("File not found in data directory.")
        raise IOError
    else:
        return os.path.join(DATA_PATH, filename)

