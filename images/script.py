from glob import glob
import os

from PIL import Image

# # resize all images in raw folder to 512x512 and save to resized folder
# for image in glob('raw/*'):
#     img = Image.open(image)
#     img = img.resize((512, 512))
#     img.save(os.path.join('resized', os.path.basename(image)))

#created mirror images of all images in resized folder and save to mirrored folder
# for image in glob('resized_and_augmented/*.jpg'):
#     img = Image.open(image)
#     img = img.transpose(Image.FLIP_LEFT_RIGHT)
#     img.save(os.path.join('mirrored_' + os.path.basename(image)))

# creat a .txt for mirroed images based on the .txt of the original images
# for image in glob('resized_and_augmented/*'):
#     with open(os.path.join('resized_and_augmented', os.path.basename(image).split('.')[0] + '.txt')) as f:
#         line = f.readline()
#         with open(os.path.join('resized_and_augmented', "mirrored_" + os.path.basename(image).split('.')[0] + '.txt'), 'w') as f:
#             f.write(line)

# move all files in current folder to resized_and_augmented folder*
for image in glob('*'):
    os.rename(image, os.path.join('resized_and_augmented', image))

