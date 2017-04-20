fromm PIL import Image
import glob, os

dir = 'new_sizes'
ext = 'jpg'
width = 180
height = 240


if not os.path.exists(dir):
    os.makedirs(dir)

for filename in glob.glob('*.jpg'):
    im=Image.open(filename)
    im.thumbnail((with, height)))
    im.save(dir + '/filename')
