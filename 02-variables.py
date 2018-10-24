import ptvsd
address=('0.0.0.0', 5678)
ptvsd.enable_attach(address)
#print("waiting to attach...")
#ptvsd.wait_for_attach()

country_name = "Mauritius"
character_age = "45"
is_island = True

print("Once upon a time, in a country named " + country_name + ", ")
print("there was a tall man who was " + character_age + " years old.")
print("He loved fried chicken,")
print("but did not like fish")
country_name="Canada"
print(country_name + " is a beautiful country")
print("\n")

#27.30 - working with strings
#use backslash to espace e.g \n
#concatenation operator: +
phrase="programagic is magic"
print(phrase)

#lowercase, uppercase
print(phrase.lower())
print(phrase.upper())

#check if uppercase or lowercase
print(phrase.isupper())
print(phrase.islower())

#string length
print(len(phrase))

#grab specific character, treat string as a zero based array of characters
print(phrase[3])

#find location of a specific character
print(phrase.index("g"))
print(phrase.index("magic"))
#print(phrase.index("z")) #error

#replace
print(phrase.replace("ic", "x"))

#numbers - bodmas
print(3 + 4 * 5)

#modulo %
print(10 % 3)

#convert number to string
print(str(3*15) + " = 3 x 15")

#math functions
print(abs(-23))
print(pow(3,2)) #3-squared
#similarly max, min, round

#for additional math functions
#import math module
#from math import *