import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import copy
import cv2
import shutil

ROOT_DIR=os.path.dirname(__file__)

SRC_DIR=os.path.join(ROOT_DIR,"fig")

RESULT_DIR=os.path.join(ROOT_DIR,"result")

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

def makedir(parent_folder:str,new_folder_name:str):
    new_folder_path = os.path.join(parent_folder, new_folder_name)

    if os.path.exists(new_folder_path):
        shutil.rmtree(new_folder_path)

    try:
        os.makedirs(new_folder_path, exist_ok=True)
        print(f'successfully create new folder: {new_folder_path}')
    except Exception as e:
        print(f'error creating new folder: {e}')

    return new_folder_path