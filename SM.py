# Build your plan using pseudocode

# using comments , use your own words to describe HOW you might begin to build this.


# Check with AI about your plan,

# Then start writing code based on your comments


import random

# Make a 2D list with symbols for machine
symbols = ["🍒", "🎰", "$", "111", "333", "777"]
row = []

# Play again
play = True

while play == True:
    grid = []
    
#Pick a random item from symbols and append it
    for i in range(3):
        row = []
        for j in range(3):
            row.append(random.choice(symbols))

        grid.append(row)
 # Print out 3 symbols in a row
    for row in grid:
        print(row)

# Check rows middle, top then bottom
    if grid[1][0] == grid[1][1] and grid[1][2] == grid[1][0] and grid[1][1] == grid[1][2]:
        print("YOU HAVE WON ROW 1!")

    if grid[0][0] == grid[0][1] and grid[0][2] == grid[0][0] and grid[0][1] == grid[0][2]:
        print("YOU HAVE WON ROW 2!")
          
    if grid[2][0] == grid[2][1] and grid[2][2] == grid[2][0] and grid[2][1] == grid[2][2]:
        print("YOU HAVE WON ROW 3!")
     
   
# Ask user input if they want to spin again
    spin_again = input("Would you like to spin again? y or n ".lower())

    if spin_again == "y":
        play = True
        row.clear()

    else:
        play = False
        row.clear()
    
