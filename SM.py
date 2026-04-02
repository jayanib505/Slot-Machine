# Build your plan using pseudocode
# using comments , use your own words to describe HOW you might begin to build this.
# Check with AI about your plan,
# Then start writing code based on your comments


import random

# Make a 2D list with symbols for machine
symbols = ["🍒", "🎰", "$", "111", "333", "777"]
grid = []

def generate_grid():
    """
    Append rows
    """
    for i in range(3):
        current_row = []
        for j in range(3):
            symbol = random.choice(symbols)
            current_row.append(symbol)
        grid.append(current_row)
    return grid

        
def display_grid(grid):
    """
    Prints out grid
    """
    for row in grid:
        print(f" | {' | '.join(row)} | ")
        
def check_wins(grid):
    """
    Checking if symbols  in row match
    """
    if grid[1][0] == grid[1][1] and grid[1][2] == grid[1][0] and grid[1][1] == grid[1][2]:
        print("YOU HAVE WON ROW 1!")
    if grid[0][0] == grid[0][1] and grid[0][2] == grid[0][0] and grid[0][1] == grid[0][2]:
        print("YOU HAVE WON ROW 2!")      
    if grid[2][0] == grid[2][1] and grid[2][2] == grid[2][0] and grid[2][1] == grid[2][2]:
        print("YOU HAVE WON ROW 3!")

#def repeat():
  #  spin = input("Send y if you want to spin again?".lower())
 #   if spin == "y":
        
        

# main routine
if __name__ == "__main__":
    generate_grid()
    display_grid(grid)
    check_wins(grid)
