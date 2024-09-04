import cv2
import os
import numpy as np
import glob
from helper import *
import re
import matplotlib.pyplot as plt

class ImagePool():

    def __init__(self):
        pass
        self.imagepool:list[dict]=[]

    def get_images_path(self)->list[str]:
        png_files = glob.glob(os.path.join(SRC_DIR, '*.png'))
        return png_files

    def get_image_name(self,img_path:str)->str:
        return os.path.splitext(os.path.basename(img_path))[0]

    def get_images(self):
        for img_path in self.get_images_path():
            img_name=self.get_image_name(img_path)
            img_ndarray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            

            img_dict=dict()
            img_dict["name"]=img_name
            img_dict["ndarray"]=img_ndarray
            for key,value in self.detect_parameters(img_name).items():
                img_dict[key]=value

            self.imagepool.append(img_dict)

    def test_show(self,img_ndarray:np.ndarray):
        plt.imshow(img_ndarray)
        plt.show()

    def detect_parameters(self,img_name:str)->dict:
        para_dict=dict()

        wavelength_pattern=re.compile(".?laser(\d+)nm.?")
        wavelength_match=re.match(wavelength_pattern,img_name)
        wavelength=wavelength_match.group(1) if wavelength_match else 0
        para_dict["wavelength"]=wavelength

        x_pattern=re.compile(".+x(-?\d?\.\d+).+")
        x_match=re.match(x_pattern,img_name)
        x = x_match.group(1) if x_match else 0
        para_dict["x"]=x

        y_pattern=re.compile(".+y(-?\d?\.\d+).+")
        y_match=re.match(y_pattern,img_name)
        y = y_match.group(1) if y_match else 0
        para_dict["y"]=y

        fov_pattern=re.compile(".+fov(\d+)um.?")
        fov_match=re.match(fov_pattern,img_name)
        fov = fov_match.group(1) if fov_match else 0
        para_dict["fov"]=fov

        return para_dict

# a=ImagePool()
# a.get_images()
# print(a.imagepool[0]["ndarray"].mean())