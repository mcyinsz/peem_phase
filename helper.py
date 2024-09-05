import sys
import os
import matplotlib.pyplot as plt
import numpy as np

ROOT_DIR=os.path.dirname(__file__)

SRC_DIR=os.path.join(ROOT_DIR,"fig")



def test_show(img:np.ndarray):
    plt.imshow(img)
    plt.show()

def test_scatter(point_list:list):
    plt.scatter(point_list[0],point_list[1])
    plt.show()


