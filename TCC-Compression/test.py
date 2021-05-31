from PIL import Image

image = Image.open('Images/C0001.bmp')
print(image.format, image.size)

image2 = Image.open('Images/C0001.webp')
print(image2.format, image2.size)

