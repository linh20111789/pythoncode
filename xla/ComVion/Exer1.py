# Viết một ứng dụng đơn giản để thay đổi cân bằng màu của hình ảnh 
# bằng cách nhân từng giá trị màu với một hằng số do người dùng chỉ định khác nhau.
#  Nếu bạn muốn trở nên lạ mắt, bạn có thể làm cho ứng dụng này trở nên tương tác, bằng các thanh trượt.

from PIL import Image, ImageEnhance 
import cv2

User_Const = input("User-speciﬁed constant value: ")
im = Image.open("./data/lena.png")
enhancer = ImageEnhance.Color(im)

# factor – A floating point value controlling the enhancement. 
# Factor 1.0 always returns a copy of the original image, 
# lower factors mean less color (brightness, contrast, etc), and higher values more. 

enhanced_im = enhancer.enhance(float(User_Const))
enhanced_im.save("./data/enhanced.sample2.png")
im2 = Image.open("./data/enhanced.sample2.png")
im.show("original")
im2.show("enhanced")