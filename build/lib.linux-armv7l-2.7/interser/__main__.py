from PIL import Image
import numpy as np
import random
def ranim():
    w, h = 512, 512
    data = np.zeros((h, w, 3), dtype=np.uint8)
    data[0:w, :h] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    mnm = Image.fromarray(np.uint8(data))
    mnm.show()
