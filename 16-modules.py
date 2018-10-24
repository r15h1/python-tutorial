#use modules to import existing functionality
def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

#print(get_file_ext("myfile.txt"))
#   this function get_file_ext can be used in a different 
#   file without having to rewrite it over there
#   to use it in a different file use import statement
#       import 16-modules
#
#   to get list of all built in python modules go to https://docs.python.org/3/py-modindex.html

#----------------------------------------------------
# external modules - written by other people and not part of built-in modules
# use pip - package manager to import external modules