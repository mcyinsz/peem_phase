import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import copy
import cv2

ROOT_DIR=os.path.dirname(__file__)

SRC_DIR=os.path.join(ROOT_DIR,"fig")

SIGNAL_RATE=0.25



def test_show(img:np.ndarray):
    plt.imshow(img)
    plt.show()

def test_scatter(point_list:list):
    plt.scatter(point_list[0],point_list[1])
    plt.show()

def test_plot(signal:np.ndarray):
    plt.plot(signal)
    plt.show()


def rotate_image(height:int, width:int, img_array:np.ndarray, angle:float):
    image = copy.deepcopy(img_array)
    center = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image