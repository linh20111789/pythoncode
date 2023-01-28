# Importing Image module from PIL package
from PIL import Image
  
# creating a image1 object and converting it to mode 'L'
im1 = Image.open(r"./data/apple.jpg").convert('L')
  
# creating a image2 object and converting it to mode 'L'
im2 = Image.open(r"./data/imagr_or.PNG").convert('L')
  
# creating a mask image object and converting it to mode 'L'
mask = Image.open(r"./data/lena.png").convert('L')
  
# compositing all the three images
im3 = Image.composite(im1, im2, mask)
  
# to show specified image 
im3.show()
