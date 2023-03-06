from PIL import Image,ImageChops
img1 = Image.open('panda1.jpg')
img2 = Image.open('panda2.jpg')
diff = ImageChops.difference(img1,img2)
if diff.getbbox():
   diff.show()