# def - python keyword to define function 
# def function_name(): - all indented  code after this line 
#   considered to be part of the function

#naming convention in python
#all lowercase
#if 2 or more words, use _

def say_hello(name):
    print("Hello " + name)

#return
def prompt_user():
    return input("What's your name? ")

#call function by simply using its name
user = prompt_user()
say_hello(user)