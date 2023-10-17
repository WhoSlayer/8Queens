grid = [[0] * 8 for _ in range(8)] # Plots an 8 by 8 grid, with 0s.

def isSafe(grid, x, y): # checks if the position with co ordinates, (x,y) is safe to place a queen

    if sum(grid[x]):
        return False
# checks for row
    if sum(grid[n][y] for n in range(8)):
        return False


# column checked
    constant = y - x # checks both diagonals
    if (sum(grid[n][constant - n] for n in range(8)
            if constant - n in range(8))):
        return False

    constant = x + y
    if (sum(grid[n][constant + n] for n in range(8)
            if constant + n in range(8))):
        return False

    return True


#for i in range(8): print(grid[i]) # prints grid
  

#Tests performed:

print(isSafe(grid,0,0)) # True
grid[0][0] = 1
print(isSafe(grid,0,0)) # False
print(isSafe(grid,0,5)) #False
print(isSafe(grid,5,0)) # False 
print(isSafe(grid,1,1)) # False
print(isSafe(grid,1,2)) # True
