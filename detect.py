import cv2
import numpy as np
import matplotlib.pyplot as plt

class DetectMethod():

    def __init__(self,img_array:np.ndarray):
        self.img_array=img_array

    def HOGE(self):
        ''''
            use HOGE and K-means to get waveguide line
        '''

        image_blurred = cv2.GaussianBlur(self.img_array,ksize=(9,9),sigmaX=-1,sigmaY=-1)
        edges = cv2.Canny(image_blurred,threshold1=50,threshold2=100)
        


