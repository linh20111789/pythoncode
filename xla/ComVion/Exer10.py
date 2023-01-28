# ImageFilter for using filter() function
from PIL import Image, ImageFilter

# Opening the image
# (R prefixed to string in order to deal with '\' in paths)
image = Image.open(r"./data/gaussF.png")
image.show()
# Blurring image by sending the ImageFilter.
# GaussianBlur predefined kernel argument
image2 = image.filter(ImageFilter.GaussianBlur)

# Displaying the image
image2.show()


