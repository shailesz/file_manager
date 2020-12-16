# checks for type of file with the help of dictionary

def check_file_type(extension, my_dictionary):
    if extension in my_dictionary['VIDEO']:
        return 'Video'
    elif extension in my_dictionary['AUDIO']:
        return 'Audio'
    elif extension in my_dictionary['IMAGE']:
        return 'Image'
    elif extension in my_dictionary['PROGRAMS']:
        return 'Programs'
    else:
        pass
