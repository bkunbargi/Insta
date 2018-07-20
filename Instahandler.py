import os,random

def get_image_path():
    basic_path = '/Users/Kunbargi/Desktop/Used/0/'
    pic2use_folder = os.listdir(basic_path) #Get Contents of folder
    pics2go_folder = os.listdir('/Users/Kunbargi/Desktop/Used/')
    image_num = str(len(pics2go_folder))
    new_location = '/Users/Kunbargi/Desktop/Used/{}.jpg'.format(image_num)
    random.shuffle(pic2use_folder)
    pic = pic2use_folder[0]
    photo_path = basic_path+pic
    os.rename(photo_path,new_location)
    return new_location
