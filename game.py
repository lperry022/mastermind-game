# -----------------------START OF PART 1: GENERATE A RANDOM CODE-----------------------#
import random

COLOURS = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]
# variable is written in all captials as it is a constant, so it is a variable that will not change
# in the real game there are 6 colours, so we will offer our players 6 colours to choose from
TRIES = 10
# the amount of tries a player has to guess the correct sequence, again since this is a constant is is written in captials and it will not change
CODE_LENGTH = 4
# the length of the code that the player has to guess, in this case it is 4


def generate_code():
    # this is a function that we will use to generate a random code for the player to guess
    # a function is a reusable block of code that performs a specific task
    code = []
    # to generate the code that the user will guess we need to generate a list of 4 random colours
    for _ in range(CODE_LENGTH):
        # we use a for loop to repeat the process of adding a random colour to the code 4 times
        # we want to make this function select a random colour from the COLOURS list and add it to the code list
        colour = random.choice(COLOURS)
        code.append(colour)
        # append means to add something to the end of a list
    return code
    # we return the code list so that we can use it later in the game


code = generate_code()
# we call the generate_code function and store the result in the code variable = generate a list of 4 random colours


# -----------------------END OF PART 1: GENERATE A RANDOM CODE-----------------------#

# -----------------------START OF PART 2: ALLOW THE USER TO GUESS THE CODE-----------------------#
def guess_code():
    # we need to allow the user to enter input for their guess into the console
    while True:
        guess = input("Guess: ").upper().split(" ")
    # upper() function is used to convert the input to uppercase letters. This makes the formatting look nicer
    # if a user puts in g, the upper() function will convert it to G
    # split(" ") function is used to split the input into a list of strings based on spaces
    # if a user inputs "Red Blue Green Yellow", the split(" ") function will convert it to ["Red", "Blue", "Green", "Yellow"] - allows the computer to read the user input
        if len(guess) != CODE_LENGTH:
            print(f"Please enter {CODE_LENGTH} colours.")
            continue
    # error handling - if the user does not enter 4 colours, the program will print an error message
    # this all is put into a while loop so that the user can keep trying until they enter a valid input
    # continue statement is used to skip the rest of the code in the loop and go back to the start of the loop
        for colour in guess:
            if colour in COLOURS:
                print(f"Invalid colour: {colour}. Please try again.")
                break
        else:
            break
    return guess
    # we return the guess list so that we can use it later in the game


# -----------------------END OF PART 2: ALLOW THE USER TO GUESS THE CODE-----------------------#
