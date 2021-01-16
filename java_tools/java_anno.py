import os
import sys
sys.path.append("./")
from util import *

root_path = "./"

if __name__ == "__main__":
    osfile.get_files(root_path, "", ".py")
    pass