#%%
import matplotlib.pyplot as plt
from skimage import io
from skimage.feature import hog
from skimage import data, color, exposure
from PIL import Image
#%%
img = io.imread(r"f15.jpg")
im= Image.open(r"f15.jpg")
image = color.rgb2gray(im)

fd, hog_image = hog(image, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

ax1.axis('off')
ax1.imshow(image, cmap=plt.cm.gray)
ax1.set_title('Input image')
ax1.set_adjustable("box","datalim")

# Rescale histogram for better display
hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 0.02))

ax2.axis('off')
ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
ax2.set_title('Histogram of Oriented Gradients')
ax1.set_adjustable("box","datalim")
plt.show()
