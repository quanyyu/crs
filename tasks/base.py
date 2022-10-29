import os
FILE_PATH = os.path.abspath(__file__)
PROEJCT_DIR = os.path.dirname(FILE_PATH)
SPACE_DIR = os.path.dirname(PROEJCT_DIR)

import sys 
sys.path.append(SPACE_DIR)