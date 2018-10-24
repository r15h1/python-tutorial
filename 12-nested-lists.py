#2D matrix
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

#access individual element
print(grid[1][1]) #5

#loop
for row in grid:
    for col in row:
        print(col)