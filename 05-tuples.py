#data structure that can store multiple values - similar to list
#use () instead of []
coordinates = (2, 5)

#tuples are immutable, cannot be changed or modified
#can't erase, add, remove elements to it etc
#tuples are zero base indexed
print(coordinates[0]) #2

#error if try to modify a tuple by assigning a value
# e.g. coordinates[0] = 10