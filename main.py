from os import path, listdir
from shutil import move
from check_file_type import check_file_type
from make_directory import make_directory

# dictionary for file types
VIDEO = ['m1v', 'mpeg', 'mov', 'qt', 'mpa', 'mpg', 'mpe', 'avi', 'movie', 'mp4']
AUDIO = ['ra', 'aif', 'aiff', 'aifc', 'wav', 'au', 'snd', 'mp3', 'mp2']
IMAGE = ['ras', 'xwd', 'bmp', 'jpe', 'jpg', 'jpeg', 'xpm', 'ief', 
                'pbm', 'tif', 'gif', 'ppm', 'xbm', 'tiff', 'rgb', 'pgm', 'png', 'pnm']
PROGRAMS = ['exe']

my_dictionary = {'VIDEO' : VIDEO, 'IMAGE' : IMAGE, 'PROGRAMS' : PROGRAMS, 'AUDIO' : AUDIO}

my_path = 'c:/Users/sailesh/Downloads'
my_files = listdir(my_path) # returns list of files/folders in my_path directory

# creating list of file extensions in my_path directory
extensions = [extension.split('.')[-1] for extension in my_files if len(extension.split('.')) > 1 and extension.split('.')[-1] is not None]

if len(extensions) > 0:
    make_directory(extensions, my_dictionary, my_path) # makes directory for respective file types

    for my_file in my_files: # moving files
        if len(my_file.split('.')) > 1: # check for if file has a extension
            my_file_extension = my_file.split('.')[-1]
            my_file_type = check_file_type(my_file_extension, my_dictionary)
            my_file_path = path.join(my_path,my_file_type)

            if not path.isfile(path.join(my_file_path, my_file)): # check if file already exists in directory to avoid duplication
                src = path.join(my_path, my_file)
                move(src, my_file_path)