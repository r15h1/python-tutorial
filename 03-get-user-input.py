name = input("Your name please:")
age = input("Your age:")
print("Hello " + name + "! You are " + age + " years old.")

#python by default assumes input values are strings
#getting numbers
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

#first way - use int, float
result = float(num1) + float(num2)
print(result)