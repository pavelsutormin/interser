#main#
from PIL import Image
import numpy as np
import random
import pandas as pd
__version__ = "0.1.0"
__author__ = 'Pavel Sutormin'
__credits__ = None
def ranimc():
    w, h = 512, 512
    data = np.zeros((h, w, 3), dtype=np.uint8)
    data[0:w, :h] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    mnm = Image.fromarray(np.uint8(data))
    mnm.show()
def pyoh(o):
    v1 = pd.DataFrame(o)
    v1.to_filetype(o, '.csv')
pyoh(list([123, 432, 760, [32, 'main', 32]]))