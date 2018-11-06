import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))   # gets path to the root directory (drone_classification)

DATA_PATH = os.path.join(ROOT_DIR, "data")              # gets path to the data directory (drone_classification/data)

DATA_FILES = sorted([file for file in os.listdir(DATA_PATH) if ".mat" in file])     # list of all files in data directory

TEMPLATE_PATH = os.path.join(DATA_PATH, "templates")

TEMPLATE_FILES = [file.lower() for file in os.listdir(TEMPLATE_PATH) if ".mat" in file]