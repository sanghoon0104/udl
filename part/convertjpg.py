# import os
# import glob
# from PIL import Image

# files = glob.glob(os.getcwd())

# for f in files:
#     title, ext = os.path.splitext(f)
#     if ext in ['.jpg', '.png']:
#         img = Image.open(f)
#         img_resize = img.resize(1000,1000)
#         img_resize.save()

from PIL import Image
import os
image1 = Image.open('save.jpg')

# image1.show()

imag1_size = image1.size

print(imag1_size)

image1 = image1.resize((1000, 1000))

imag1_size = image1.size


image1.save("save.jpg" )
print(imag1_size)