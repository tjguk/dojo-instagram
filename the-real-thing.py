import os

from PIL import Image, ImageChops
import pilgram

image = Image.open("abbey.jpg")
image.setpixel = image.putpixel
def sepiaise(image):
    pilgram.kelvin(image).save("abbey.kelvin.jpg")

#os.startfile("abbey.kelvin.jpg")

def average_filter(image):
    # Some people call this grayscale, but this is better... for some reason
    for x in range(image.width):
        for y in range(image.height):
            current = image.getpixel((x,y))
            average = int(sum(current) / 3)
            image.setpixel((x,y), (average, average, average))
    image.save("abbey.average.jpg")

def above_average_filter(image):
    # makes it over exposed (bumps lightness on all colors up a bit)
    for x in range(image.width):
        for y in range(image.height):
            current = image.getpixel((x,y))
            above_average = []
            for px in current:
                above_average.append(px + 50)
            image.setpixel((x,y), tuple(above_average))
    image.save("abbey.above_average.jpg")

def invert_filter(image):
    ImageChops.invert(image).save("abbey.inverted.jpg")


invert_filter(image)
os.startfile("abbey.inverted.jpg")