#python does not support overloading a la Java, C++, C#
#use default parameters to pass defaults

def next(number, increment = None):
    if increment == None:
        return number + 1
    else:
        return number + increment

print(next(12))
print(next(12, 3))