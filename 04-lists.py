#basic list
friends = ["Veeraj", "Deepak", "Bof", "San", "Deven"]
print(friends)
print(friends[2])

#negative indexes start from the back of the list
print(friends[-2]) #San

#range [start:up-to-not-including] - up-to-not-including is optional
#grab all elements including & after element with index n
print(friends[2:])
print(friends[2:4])

#list functions
lucky_numbers = [4, 8, 15, 23, 42, 49]

#append: add an element to the end list
friends.append("Papi")
print(friends)

#insert: add an element to a specific position in the list
friends.insert(2, "Mami") #insert the element papi at position 2
print(friends)

#remove a specific element
friends.remove("Mami")
print(friends)

#extend: add a list at the end of another list
lucky_numbers.extend(friends)
print(lucky_numbers) #lucky_numbers now has all friends elements inside

#pop: remove the last element
popped = lucky_numbers.pop()
print(lucky_numbers)
print(popped)

#check existence of an element - if element not in list, get exception
print(friends.index("Papi")) 

#count - how many times a value shows up in the list
friends.insert(0, "Veeraj")
print(friends.count("Veeraj"))

#reverse the order of the list
friends.reverse()
print(friends)

#sorting in alphabetical order
friends.sort()
print(friends)

#make a copy
friends_copy = friends.copy()
print(friends_copy)

#empty the list
lucky_numbers.clear()
print(lucky_numbers)