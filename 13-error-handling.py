#basic
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("You did not enter a number")

#multilevel excepts
try:
    10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Can not divide by zero")
except ValueError:
    print("Invalid input")

#catch exception as a variable
try:
    10/0
except ZeroDivisionError as ex:
    print(ex.args)