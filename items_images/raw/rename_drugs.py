from glob import glob
import os

# get all .jpg files in the current directory
files = glob('*.jpg')

i = 0

for file in files:
    # replace _ with space
    new_name = file.replace('_', ' ')

    # save the file
    os.rename(file, new_name)
