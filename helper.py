import sys
import os
import matplotlib.pyplot as plt

ROOT_DIR=os.path.dirname(__file__)

SRC_DIR=os.path.join(ROOT_DIR,"fig")



def test_show(img):
    plt.imshow(img)
    plt.show()
