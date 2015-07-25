author = "jdzollw"

import os

def remove_files(directory, extension, number_to_keep=10):
    """ Function that removes all but a user-specified files of a certain     type from a directory
    """
    
    flist = []
    for f in os.listdir(directory):
        if f.endswith(extension):
            flist += [f]
    
    flist.sort() # in-place sort
    for f in flist[:-number_to_keep+1]:
        os.remove(f)
