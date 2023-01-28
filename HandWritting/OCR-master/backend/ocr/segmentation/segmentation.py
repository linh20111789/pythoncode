import cv2
import numpy as np
import imutils
from numpy.core.numeric import True_
from PIL import Image
import matplotlib.pyplot as plt

# def img_precessing(img):
#     mask_black = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 199, 5)
#     ## save 
#     cv2.imwrite('./test/preprocessing.jpg', mask_black)
#     return mask_black

def segment(input_path, output_path):
    image = cv2.imread(input_path)

    #grayscale
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # blurred = cv2.GaussianBlur(gray, (5, 5), 2)

    #binary
    ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)

    #dilation
    kernel = np.ones((12,200), np.uint8)
    img_dilation = cv2.dilate(thresh, kernel, iterations=1)


    #find contours
    ctrs = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    ctrs = ctrs[1] if imutils.is_cv3() else ctrs[0]

    #sort contours
    sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
    # sorted_ctrs = [ctr for ctr in reversed(sorted_ctrs)]
    x, y, w, h = cv2.boundingRect(sorted_ctrs[0])
    max_width, max_height = image[y:y+h, x:x+w].shape[0], image[y:y+h, x:x+w].shape[1]
    valid_img = 0

    for i, ctr in enumerate(sorted_ctrs):
        # Get bounding box
        x, y, w, h = cv2.boundingRect(ctr)
        # Getting ROI
        roi = image[y:y+h, x:x+w]
        width, height = roi.shape[0], roi.shape[1]
        # print(i, width)
        # print(i, height)
        
        
        if(width>=max_width*0.1 and height>=max_height*0.7):
            # show ROI   
            cv2.imwrite('{0}/img_transformer{1}.jpg'.format(output_path, valid_img), roi)
            valid_img += 1
    return valid_img

