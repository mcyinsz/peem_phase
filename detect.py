import cv2
import numpy as np
import matplotlib.pyplot as plt

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
        plt.imshow(edges)
        plt.show()



test=DetectMethod()
test.test_init("/home/mcyinsz/python_projects/peem_phase/fig/laser435nm_x-0.934y0.507fov30um.png")
test.HOGE()