# def isValidMove(grid, row, col, number):
    
#     # Checking if the move is valid
    
#     for x in range(9):
#         if grid[row][x] == number:
#             return False
        
#     for x in range(9):
#         if grid[x][col] == number:
#             return False
    
#     # Find top right corner of the 3 x 3 sub grid
#     corner_row = row - row%3
#     corner_col = col - col%3

#     for x in range(3):
#         for y in range(3):
#             if grid[corner_row + x][corner_col + y] == number:
#                 return False
            
#     return True

# def solve(grid, row, col):

#     # If we overshoot the columns and we're in the last row, it means there's nothing more to solve
#     if col == 9:
#         if row == 8:
#             return True
        
#         # Else, increment the row and start from the 0th col (beginning of the row)
#         row += 1
#         col = 0
    
#     # If the current cell has a value, proceed to the next column
#     if grid[row][col] > 0:
#         solve(grid, row, col + 1)

#     for num in range(1,10):

#         if isValidMove(grid, row, col, num):
#             # Assume that the current number is the right one for now
#             grid[row][col] = num

#             if solve(grid, row, col + 1):
#                 return True
            
#         # If the above conditions aren't met, leave the number as 0
#         grid[row][col] = 0

#     return False

# grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0], 
#         [6, 0, 0, 1, 9, 5, 0, 0, 0], 
#         [0, 9, 8, 0, 0, 0, 0, 6, 0], 
#         [8, 0, 0, 0, 6, 0, 0, 0, 3], 
#         [4, 0, 0, 8, 0, 3, 0, 0, 1], 
#         [7, 0, 0, 0, 2, 0, 0, 0, 6], 
#         [0, 6, 0, 0, 0, 0, 2, 8, 0], 
#         [0, 0, 0, 4, 1, 9, 0, 0, 5], 
#         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

# if solve(grid, 0, 0):
#     for i in range(9):
#         for j in range(9):
#             print(grid[i][j], end=" ")
#         print()
# else:
#     print("No Solution")

def solve(grid):
    empty = find_empty(grid)
    if not empty:
        return True
    row, col = empty

    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve(grid):
                return True
            grid[row][col] = 0
    return False

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

def is_valid(grid, row, col, num):
    # Check row
    if num in grid[row]:
        return False
    
    # Check column
    if num in (grid[i][col] for i in range(9)):
        return False
    
    # Check 3x3 box
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    if num in (grid[i][j] for i in range(box_row, box_row + 3) for j in range(box_col, box_col + 3)):
        return False
    
    return True

grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve(grid):
    for row in grid:
        print(*row)
else:
    print("No Solution")