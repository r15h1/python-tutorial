#open file 
# r - read mode
# w - write mode
# a - append mode (append to the end of the file)
# r+ - read and write

my_opened_file = open("myfile.txt", "a")
#add to a new line
my_opened_file.write("\nEndo of loremo ipsumo") 
my_opened_file.close()


#create a new file in write mode
my_new_file = open("my_new_file", "w")
#add contents to new file, if file exists it will overwrite its contents
my_new_file.write("my new content")
my_new_file.close()