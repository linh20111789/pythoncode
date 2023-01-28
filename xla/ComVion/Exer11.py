
# ImageFilter for using filter() function
from PIL import Image, ImageFilter
# Importing the module
import cv2
import numpy as np
 
 
 
# Opening the image
# (R prefixed to string in order to deal with '\' in paths)
image = Image.open(r"./data/gaussF.png")


image = image.filter(ImageFilter.BoxBlur(2))

# Displaying the image
image.show()


# Reading the image
image2 = cv2.imread('./data/gfg.png')
 
# Applying the filter
gaussian = cv2.GaussianBlur(image2, (3, 3), 0)
 
# Showing the image
cv2.imshow('Original', image2)
cv2.imshow('Gaussian blur', gaussian)
 
cv2.waitKey()
cv2.destroyAllWindows()