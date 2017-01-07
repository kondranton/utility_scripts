import os, sys
from PIL import Image

phone = [20, 29, 40, 58, 60, 76, 80, 87, 152, 120, 165, 167, 180]
watch = [48, 55, 84, 172, 196]

sizes = phone + watch
file = "image"


for size in sizes:
    im = Image.open(file + ".png")
    par = size, size
    im.thumbnail(par, Image.ANTIALIAS)
    im.save(file + str(size) + ".png")
