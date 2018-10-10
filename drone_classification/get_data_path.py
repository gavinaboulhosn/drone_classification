import os
from definitions import ROOT_DIR


def get_data_path(n=1, ext=".mat"):
    assert(n>0 and n<=6)
    return os.path.join(ROOT_DIR, 'data', 'UAV0000{}'.format(str(n)+ext))

