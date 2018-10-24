# Least to Greatest
pointsInaGame = [0, -10, 15, -2, 1, 12]
sortedGame = sorted(pointsInaGame)
print(sortedGame)

# Alphabetically
children = ["Sue", "Jerry", "Linda"]
print(sorted(children))
print(sorted(["Sue", "jerry", "linda"]))

# Key Parameters
print(sorted("My favorite child is Linda".split(), key=str.upper))
print(sorted(pointsInaGame, reverse=True))

leaderBoard = {231: "CKL", 123:"ABC", 432:"JKC"}
print(sorted(leaderBoard, reverse=True))
print(leaderBoard.get(432))

students = [ ('alice', 'B', 12), ('eliza', 'A', 16), ('tae', 'C', 15)]
 #sort by the first entry in each tuple i.e. sort by student name
print(sorted(students, key=lambda student:student[0]))

#sort by the second entry in each tuple i.e. sort by student grade
print(sorted(students, key=lambda student:student[1]))

#sort by the third entry in each tuple i.e. sort by student marks
print(sorted(students, key=lambda student:student[2]))