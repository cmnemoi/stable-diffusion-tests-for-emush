from glob import glob
import os
from xml.dom.minidom import Element

from PIL import Image

# resize all images in raw folder to 512x512 and save to resized folder
# for image in glob('raw/*'):
#     img = Image.open(image)
#     img = img.resize((512, 512))
#     img.save(os.path.join('resized', os.path.basename(image)))

# # created mirror images of all images in resized folder and save to mirrored folder
# for image in glob('resized_and_augmented/*.jpg'):
#     img = Image.open(image)
#     img = img.transpose(Image.FLIP_LEFT_RIGHT)
#     img.save(os.path.join('mirrored_' + os.path.basename(image)))

# # creat a .txt for mirroed images based on the .txt of the original images
# for image in glob('resized_and_augmented/*'):
#     with open(os.path.join('resized_and_augmented', os.path.basename(image).split('.')[0] + '.txt')) as f:
#         line = f.readline()
#         with open(os.path.join('resized_and_augmented', "mirrored_" + os.path.basename(image).split('.')[0] + '.txt'), 'w') as f:
#             f.write(line)

# # move all files in current folder to resized_and_augmented folder*
# for image in glob('*'):
#     os.rename(image, os.path.join('resized_and_augmented', image))

females = ["eleesha", "frieda", "janice", "hua", "finola", "nurse", "paola", "chun", "raluca"]


#get all txt files in resized_and_augmented folder and replace the text in them
for text in glob('resized_and_augmented/*.txt'):
        with open(text, "w") as f:
            if "finola" in text or "frieda" in text or "janice" in text or "hua" in text or "eleesha" in text or "nurse" in text or "paola" in text or "chun" in text or "raluca" in text:
                f.write("a cartoon of a woman")
            else:
                f.write("a cartoon of a man")