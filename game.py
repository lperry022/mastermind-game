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

# -----------------------START OF PART 3: CHECK INCORRECT AND CORRECT GUESSES-----------------------#


def check_code(guess, real_code):
    # the purpose of this function is to take the colour in the user's guess and compare it to the real code
    colour_counts = {}
    correct_position = 0
    incorrect_position = 0
# we create an empty dictionary to store the counts of each colour in the real code
# we also create two variables to store the number of colours that are in the correct position and the number of colours that are in the incorrect position
    for colour in real_code:
        if colour not in colour_counts:
            colour_counts[colour] = 0
            colour_counts[colour] += 1
# this for loop counts the number of times each colour appears in the real code and stores it in a dictionary

    for guess, real_colour in zip(guess, real_code):
        # zip() function is used to combine two lists into a list of tuples
        # for example, if guess = ["Red", "Blue", "Green", "Yellow"] and real_code = ["Blue", "Red", "Green", "Yellow"]
        if guess == real_colour:
            correct_position += 1
            colour_counts[guess] -= 1
# this for loop compares the user's guess to the real code and counts the number of colours that are in the correct position
# this removes the colour from the dictionary so that it is not counted again in the next for loop
        for guess_colour, real_colour in zip(guess, real_code):
            if guess_colour in colour_counts and colour_counts[guess_colour] > 0:
                incorrect_position += 1
                colour_counts[guess_colour] -= 1
# this for loop compares the user's guess to the real code and counts the number of colours that are in the incorrect position
# this checks if the colour is in the dictionary and if the count is greater than 0
    return correct_position, incorrect_position
    # we return the number of colours that are in the correct position and the number of colours that are in the incorrect position

# -----------------------END OF PART 3: CHECK INCORRECT AND CORRECT GUESSES-----------------------#

# -----------------------START OF PART 4: RUN THE GAME-----------------------#


def game():
    code = generate_code()
    for attempt in range(1, TRIES + 1):
        print(f"Attempt {attempt} of {TRIES}")
# we print the attempt number and the total number of tries
        guess = guess_code()
# we call the guess_code function to get the user's guess
        correct_position, incorrect_position = check_code(guess, code)
# we call the check_code function to compare the user's guess to the real code
        print(
            f"Correct Position: {correct_position}, Incorrect Position: {incorrect_position}")
        if correct_position == CODE_LENGTH:
            print("Congratulations! You've guessed the code!")
            break
# if the user has guessed all 4 colours in the correct position, they win the game
# if the user has not guessed the code in the given number of tries, they lose the game
# -----------------------END OF PART 4: RUN THE GAME-----------------------#
