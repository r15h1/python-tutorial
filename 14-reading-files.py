#open file 
# r - read mode
# w - write mode
# a - append mode (append to the end of the file)
# r+ - read and write

my_opened_file = open("myfile.txt", "r")

#is file readable
print(my_opened_file.readable())

#get all the data from the file using read()
print(my_opened_file.read())

#reads a single line and moves the cursor to the beginning of the next line
print(my_opened_file.readline())

#reads all the lines and puts it inside an array
print(my_opened_file.readlines())

#loop through each line
for line in my_opened_file.readlines():
    print(line)


# Read one line at a time
print("My one line: " + my_opened_file.readline())

#reset pointer to beginning of file
my_opened_file.seek(0)

# Iterate through each line of a file
for line in my_opened_file:
    newHighScorer = line.replace("BBB", "PDJ")
    print(newHighScorer)

#close the opened file
my_opened_file.close()