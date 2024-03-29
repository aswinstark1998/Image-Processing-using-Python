import numpy as np 
import math
import cv2
from matplotlib import pyplot as plt 

def convolve(X,F):  #X=Image, F=Filter
    X_height = X.shape[0]
    X_width = X.shape[1]

    F_height = F.shape[0]
    F_width = F.shape[1]

    H = (F_height-1)/2
    W = (F_width-1)/2

    out = np.zeros((X_height,X_width))

    for i in np.arange(H,X_height-H):
        for j in np.arange(W,X_width-W):
            sum = 0
            for k in np.arange(-H,H+1):
                for l in np.arange(-W,W+1):
                    a = X[i+k,j+l]
                    w = F[H+k,W+l]
                    sum+=(w*a)
            out.itemset((i,j),sum)
    return out

def main():
    img = cv2.imread("cameraman.jpg",0)
    height = img.shape[0]
    width = img.shape[1]

    Hx = np.array([[-1,0,1],
                   [-2,0,2],
                   [-1,0,1]]
                   )

    Hy = np.array([[-1,-2,-1],
                   [0,0,0],
                   [-1,-2,-1]]
                 )
    
    img_x = convolve(img,Hx)/8.0
    img_y = convolve(img,Hy)/8.0

    img_out = np.sqrt(np.power(img_x,2)+np.power(img_y,2))
    img_out = (img_out/np.max(img_out))*255

    plt.imshow(img_out,cmap='gray')
    plt.show()




if __name__=="__main__":
    main()