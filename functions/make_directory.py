from os import path, mkdir

# makes directory

def make_directory(extensions, my_dictionary, my_path):
    for extension in extensions:  # creating directory
        if extension in my_dictionary['VIDEO']:
            # makes Video directory if directory does not exist
            if not path.isdir(path.join(my_path, 'Video')):
                mkdir(path.join(my_path, 'Video'))
        elif extension in my_dictionary['AUDIO']:
            # makes Audio directory if directory does not exist
            if not path.isdir(path.join(my_path, 'Audio')):
                mkdir(path.join(my_path, 'Audio'))
        elif extension in my_dictionary['IMAGE']:
            # makes Image directory if directory does not exist
            if not path.isdir(path.join(my_path, 'Image')):
                mkdir(path.join(my_path, 'Image'))
        elif extension in my_dictionary['PROGRAMS']:
            # makes Programs directory if directory does not exist
            if not path.isdir(path.join(my_path, 'Programs')):
                mkdir(path.join(my_path, 'Programs'))
        else:
            pass
