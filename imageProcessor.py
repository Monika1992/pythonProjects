__author__ = 'Monika'

from pylab import imshow, show, get_cmap
import math
from PIL import Image, ImageFilter


image = Image.new('RGB', (512,512), "white")
pixelsData = image.load()

new_image = Image.open('ortofoto_2.jpg')
new_image = new_image.filter(ImageFilter.MedianFilter(size=5))

new_image.show()

new_img_pixels = new_image.load()

for y in range(new_image.size[0]):
    for x in range(new_image.size[1]):
        r, g, b = new_image.getpixel((y,x))

        #print r, g, b

        pixel_avg_value = (r + g + b) / 3

        #print pixel_avg_value

        if abs(pixel_avg_value - r) < abs(pixel_avg_value - g) and abs(pixel_avg_value -r) < abs(pixel_avg_value - b):
            r = 255
            g = 0
            b = 0
        elif abs(pixel_avg_value - g) < abs(pixel_avg_value - r) and abs(pixel_avg_value -g) < abs(pixel_avg_value - b):
            r = 0
            g = 255
            b = 0
        elif abs(pixel_avg_value - b) < abs(pixel_avg_value - g) and abs(pixel_avg_value -b) < abs(pixel_avg_value - r):
            r = 0
            g = 0
            b = 255
        else:
            r = 100
            g = 100
            b = 100

        new_img_pixels[y, x] = (int(r), int(g), int(b))

new_image.show()






