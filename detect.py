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


    def HOGE(self,show:bool=False):
        ''''
            use HOGE and K-means to get waveguide line
        '''

        image_blurred = cv2.GaussianBlur(self.img_array,ksize=(9,9),sigmaX=-1,sigmaY=-1)
        edges = cv2.Canny(image_blurred,threshold1=50,threshold2=100)
        lines = cv2.HoughLines(edges,rho=1,theta=np.pi/180,threshold=110,min_theta=0,max_theta=np.pi)

        # to print scatter
        lines = list(zip(*list(map(lambda x:x[0].tolist(),lines)))) # get x_list,y_list format data

        if show:
            self.show_HOGE(lines)

        return lines
    
    def horizontal_waveguide(self):
        lines=self.HOGE()
        
        # get rotate angle
        angle=np.mean(np.array(lines[1]))
        
        horizonal_img=rotate_image(*self.height_width,self.img_array,180*(angle/np.pi)-90)

        return horizonal_img


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

    def detect_waveguide_row(self):
        horizon_img=self.horizontal_waveguide()

        # normalize
        horizon_img = horizon_img/np.max(horizon_img)
        
        strong_rows=[]
        last_row=0
        row_signal_buffer=np.zeros(horizon_img.shape[1])

        strong_rows.append(dict())
        for row in range(horizon_img.shape[0]):
            if np.mean(horizon_img[row])>SIGNAL_RATE:
                if last_row==0:
                    strong_rows[-1]["start"]=row

                elif last_row!=row-1:
                    strong_rows[-1]["end"]=last_row
                    strong_rows[-1]["mean_signal"]=row_signal_buffer
                    row_signal_buffer=np.zeros(horizon_img.shape[1])
                    strong_rows.append(dict())
                    strong_rows[-1]["start"]=row

                
                row_signal_buffer+=horizon_img[row]
                last_row=row

        strong_rows[-1]["end"]=last_row
        strong_rows[-1]["mean_signal"]=row_signal_buffer

        for strong_rows_dict in strong_rows:
            assert len(strong_rows_dict)==3, "no valid strong rows"
            length=strong_rows_dict["end"]-strong_rows_dict["start"]+1
            strong_rows_dict["mean_signal"]=strong_rows_dict["mean_signal"]/length
            # print(strong_rows_dict)

            # draw the referring line
            line_mean=(strong_rows_dict["start"]+strong_rows_dict["end"])//2
            cv2.line(horizon_img, (0,line_mean), (horizon_img.shape[1]-1,line_mean), 1, 2)
            
            # test_plot(strong_rows_dict["mean_signal"])

        # test_show(horizon_img)
        return strong_rows, horizon_img
