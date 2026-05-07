# Build your plan using pseudocode
# using comments , use your own words to describe HOW you might begin to build this.
# Check with AI about your plan,
# Then start writing code based on your comments


import random
gfcgfvgb


def generate_grid():
    """
    Append rows
    """
    
    # Runs code 3 times to create 3 rows
    for i in range(3):

        # Empty row
        current_row = []
        for j in range(3):

            # Generates random symbols and appends 3 into empty row
            symbol = random.choice(symbols)
            current_row.append(symbol)
        grid.append(current_row)
    # Returns row to grid variable
    return grid

        
def display_grid(grid):
    """
    Prints out grid
    """

     # Printing grid format
    for row in grid:
        print(f" | {' | '.join(row)} | ")

        
def check_wins(grid):
    """
    Checking if symbols  in row match
    """

    # Checks middle row for matches
    if grid[1][0] == grid[1][1] and grid[1][2] == grid[1][0] and grid[1][1] == grid[1][2]:
        print("YOU HAVE WON ROW 1!")


    # Checks top row for matches
    if grid[0][0] == grid[0][1] and grid[0][2] == grid[0][0] and grid[0][1] == grid[0][2]:
        print("YOU HAVE WON ROW 2!")      

    # Checks bottom row for matches
    if grid[2][0] == grid[2][1] and grid[2][2] == grid[2][0] and grid[2][1] == grid[2][2]:
        print("YOU HAVE WON ROW 3!")
    

# Main routine
if __name__ == "__main__":

    # Symbol list 
    symbols = ["🍒", "🎰", "$", "111", "333", "777"]
    

    # Loop until user quits
    while True:
        grid = []
        spin = input("Do you want to spin the Slot Machine? (y/n)").lower()

        # Ends Program
        if spin == "n":
            print("Goodbye!")
            break
        
        # Get, display and check grid
        generate_grid()
        display_grid(grid)
        check_wins(grid)

    
            
