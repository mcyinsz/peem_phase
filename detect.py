import cv2
import numpy as np
import matplotlib.pyplot as plt
from helper import *
import copy

class DetectMethod():

    def __init__(self,img_array:np.ndarray=None):
        self.img_array=img_array

    def test_init(self,img_path:str):
        self.img_array = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    @property
    def height_width(self):
        height,width =self.img_array.shape[0],self.img_array.shape[1]
        print(height,width)
        return height,width


    def HOGE(self):
        ''''
            use HOGE and K-means to get waveguide line
        '''

        image_blurred = cv2.GaussianBlur(self.img_array,ksize=(9,9),sigmaX=-1,sigmaY=-1)
        edges = cv2.Canny(image_blurred,threshold1=50,threshold2=100)
        test_show(edges)
        lines = cv2.HoughLines(edges,rho=1,theta=np.pi/180,threshold=86,min_theta=0,max_theta=np.pi)

        # to print scatter
        lines = list(zip(*list(map(lambda x:x[0].tolist(),lines)))) # get x_list,y_list format data
        test_scatter(lines)
        return lines
    
    def rotate_image(self, angle):
        image = copy.deepcopy(self.img_array)

        (height, width) = self.height_width
        
        center = (width // 2, height // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

        rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
        
        return rotated_image


    def show_HOGE(self,lines:list[list]):
        new_img = self.img_array.copy()
        if lines is not None:
            for line in zip(*lines):
                rho, theta = line
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = rho * a
                y0 = rho * b
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * a)
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * a)
                cv2.line(new_img, (x1,y1), (x2,y2), (0,0,255), 2)
        plt.imshow(new_img)
        plt.axis('off')
        plt.show()



# test=DetectMethod()
# test.test_init("/home/mcyinsz/python_projects/peem_phase/fig/laser435nm_x-0.934y0.507fov30um.png")
# # test.show_HOGE(test.HOGE())
# angle=np.mean(np.array(test.HOGE()[1]))
# test_show(test.rotate_image(180*(angle/np.pi)-90))