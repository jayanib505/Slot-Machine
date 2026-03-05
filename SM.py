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

# Check if symbols match
    if row[0] == row[1] and row[1] == row[2]:
        print("You won!")


# Ask user input if they want to spin again
    spin_again = input("Would you like to spin again? y or n ".lower())

    if spin_again == "y":
        play = True
        row.clear()

    else:
        play = False
        row.clear()
    
