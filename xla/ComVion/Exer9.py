# Bluring/Smoothing example using a 1D Gaussian Kernel and the
# sepFilter2D function to apply the separable filters one at a time.
#
# Jay Summet 2015
#
#Python 2.7, OpenCV 2.4.x
#

import cv2
import numpy as np


#Linux window threading setup code.
cv2.startWindowThread()
cv2.namedWindow("Difference")
cv2.namedWindow("Gaussian Blur")
cv2.namedWindow("Gaussian sepFilter2D")

#Load source / input image as grayscale, also works on color images...
imgIn = cv2.imread("./data/lena.png", cv2.IMREAD_GRAYSCALE)



# 1D Gausian Kernel using sigma of 1.7
kernel = cv2.getGaussianKernel( 11, 1.7 )

print (kernel.shape)

gBlurImg = cv2.GaussianBlur(imgIn, (11,11), 1.7)
cv2.imshow("Gaussian Blur", gBlurImg)


#this is how the GaussianBlur function actually works:
twoD = cv2.sepFilter2D(imgIn, -1, kernel, kernel)
cv2.imshow("Gaussian sepFilter2D", twoD)

diff = twoD - gBlurImg

cv2.imshow("Difference", diff)
cv2.waitKey(0)
