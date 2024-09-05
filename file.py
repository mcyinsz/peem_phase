import cv2
import os
import numpy as np
import glob
from helper import *
import re
import matplotlib.pyplot as plt
from detect import DetectMethod
import tqdm

class ImagePool():

    def __init__(self):
        pass
        self.imagepool:list[dict]=[]
        self.get_images()

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

    def detect_parameters(self,img_name:str)->dict:
        para_dict=dict()

        wavelength_pattern=re.compile(r".?laser(\d+)nm.?")
        wavelength_match=re.match(wavelength_pattern,img_name)
        wavelength=wavelength_match.group(1) if wavelength_match else 0
        para_dict["wavelength"]=wavelength

        x_pattern=re.compile(r".+x(-?\d?\.\d+).+")
        x_match=re.match(x_pattern,img_name)
        x = x_match.group(1) if x_match else 0
        para_dict["x"]=x

        y_pattern=re.compile(r".+y(-?\d?\.\d+).+")
        y_match=re.match(y_pattern,img_name)
        y = y_match.group(1) if y_match else 0
        para_dict["y"]=y

        fov_pattern=re.compile(r".+fov(\d+)um.?")
        fov_match=re.match(fov_pattern,img_name)
        fov = fov_match.group(1) if fov_match else 0
        para_dict["fov"]=fov

        return para_dict
    
    def single_img_process(self,img_dict:dict):
        try:
            img_array=img_dict["ndarray"]
        except:
            raise Exception("img_array not correctly generated")
        
        img_result_folder=makedir(RESULT_DIR,img_dict["name"])

        # rotate and detect
        img_detect = DetectMethod(img_array)
        img_dict["strong_rows"], ref_img = img_detect.detect_waveguide_row()
        plt.imshow(ref_img)
        plt.savefig(os.path.join(img_result_folder,"ref_img.png"),dpi=600)

        # capture phase
        for signal_dict in img_dict["strong_rows"]:
            signal_result_folder=makedir(img_result_folder,str(signal_dict["start"]))
            np.save(os.path.join(signal_result_folder,"origin_signal.npy"),signal_dict["mean_signal"])


    def full_img_process(self):
        for img_dict in tqdm.tqdm(self.imagepool):
            self.single_img_process(img_dict)
        # print(self.imagepool)


        


a=ImagePool()
a.full_img_process()