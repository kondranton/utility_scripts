from PIL import Image
import glob, os

dir = 'pngs'
if not os.path.exists(dir):
    os.makedirs(dir)

counter = 0
for filename in glob.glob('*.gif'): #assuming gif
    im=Image.open(filename)
    im.save(dir + '/frame' + str(counter) + '@2x.png')
    counter = counter + 1
