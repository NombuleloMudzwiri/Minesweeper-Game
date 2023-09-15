#create a grid of hashes and dashes
#create a  for loop that will go through each element in mines grid and count the number of hashes found around dashes then return the len of hashes
#use enumerate function to keep count of the points and values 

grid = [["-", "-", "-", "#", "#"],
              
         ["-", "#", "-", "-", "-"],

         ["-", "-", "#", "-", "-"],

         ["-", "#", "#", "-", "-"],

         ["-", "-", "-", "-", "-"]]

#we need to check each individual elemnts in the grid
#check wherether its a dash or  hash
#check whether the position of dash exists
# if its a dash count the number of adjacent hashes to it
             
def genPuzzle(grid):
    puzzle = []
    for i in range(len(grid)):
        puzzle.append(grid[i][:])
        for j in range(len(grid[i])):
            if grid[i][j] == '#':             # if a position in the grid is equal to a mine (#) we count all adjacent spots
                continue
            neighbors = 0
            for d in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1),        #This is where we check all the outsets
                      (1, -1), (-1, 1)]:
                di, dj = i + d[0], j + d[1]
                try:         # Use try and except to account for any index error that might occure
                    if di >= 0 and dj >= 0 and grid[di][dj] == '#':
                        neighbors += 1
                except IndexError:
                    pass
            puzzle[i][j] = neighbors
    return puzzle

print(genPuzzle(grid))

# I was able to re start this project afresh and redo it with the help of a friend 
# Explaining how to better understand the approche to the game 
# I also used google and diffrernt Youtube tutorials @ FreeCodeCamp 