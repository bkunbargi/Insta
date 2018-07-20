#image_access.py

import os,sys
from InstagramAPI import ImageUtils
from PIL import Image


def image_aspect_change(image_loc):
    width,height = ImageUtils.getImageSize(image_loc)
    print((width,height))
    if width > height:
        new_height = int(width/1.91)
        print(new_height)
        print('Width is greater') #set to 1.91:1
    else:
        new_height = int((5*width)/4)
        print(new_height)
        print('Height is greater') #set to 4:5

    my_pic = Image.open(image_loc)
    my_pic = my_pic.resize((width,new_height),Image.ANTIALIAS)
    my_pic.save(image_loc)
    print()
    print(ImageUtils.getImageSize(image_loc))
    print('Success')
