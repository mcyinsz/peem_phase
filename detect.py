import cv2
import numpy as np
import matplotlib.pyplot as plt
from helper import *

class DetectMethod():

    def __init__(self,img_array:np.ndarray=None):
        self.img_array=img_array

    def test_init(self,img_path:str):
        self.img_array = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)


    def HOGE(self):
        ''''
            use HOGE and K-means to get waveguide line
        '''

        image_blurred = cv2.GaussianBlur(self.img_array,ksize=(9,9),sigmaX=-1,sigmaY=-1)
        edges = cv2.Canny(image_blurred,threshold1=50,threshold2=100)
        test_show(edges)
        lines = cv2.HoughLines(edges,rho=1,theta=np.pi/180,threshold=86,min_theta=0,max_theta=2*np.pi)
        print(lines)



test=DetectMethod()
test.test_init("/home/mcyinsz/python_projects/peem_phase/fig/laser435nm_x-0.934y0.507fov30um.png")
test.HOGE()