from glob import glob
import os

from PIL import Image

# resize all images in raw folder to 512x512 and save to resized folder
for image in glob('raw/*'):
    img = Image.open(image)
    img = img.resize((512, 512))
    img.save(os.path.join('resized', os.path.basename(image)))