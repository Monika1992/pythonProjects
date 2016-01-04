__author__ = 'Monika'

from PIL import Image, ImageFilter, ImageEnhance
import random

# returns image with reduced color count
def prepare_original_image(file_name):

    new_image = Image.open(file_name)

    ImageEnhance.Contrast(new_image)
    ImageEnhance.Sharpness(new_image)

    new_image = new_image.convert('P', palette=Image.ADAPTIVE, colors=16)
    return new_image.convert('RGB', palette=Image.ADAPTIVE)

def process_image(prepared_image):
    new_img_pixels = prepared_image.load()

    for y in range(prepared_image.size[0]):
        for x in range(prepared_image.size[1]):
            current_pixel = prepared_image.getpixel((y, x))
            new_img_pixels[y, x] = change_pixel_rgb(current_pixel)

    return prepared_image

def change_pixel_rgb((r, g, b)):
    pixel_avg_value = (r + g + b) / 3

    if abs(pixel_avg_value - r) < abs(pixel_avg_value - g) and abs(pixel_avg_value - r) < abs(pixel_avg_value - b):
        return create_pixel(255, 0, 0)
    elif abs(pixel_avg_value - g) < abs(pixel_avg_value - r) and abs(pixel_avg_value - g) < abs(pixel_avg_value - b):
        return create_pixel(0, 255, 0)
    elif abs(pixel_avg_value - b) < abs(pixel_avg_value - g) and abs(pixel_avg_value - b) < abs(pixel_avg_value - r):
        return create_pixel(0, 0, 255)
    else:
        return create_pixel(100, 100, 100)

# returns rgb tuple, where all values are cast to int type
def create_pixel(r, g, b):
    return (int(r), int(g), int(b))

def show_image(image):
    image.show()

def export_image(image):
    image.save("output_image" + str(random.randint(1,10000)) + ".jpg")

image = process_image(prepare_original_image("ortofoto_2.jpg"))
show_image(image)
export_image(image)

