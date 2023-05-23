#write Rock Paper Scissors Game in Python

# import random module
import random

# define a function to check if the user input is valid
def check_input(user_input):
    if user_input in ['r', 'p', 's']:
        return True
    else:
        return False

# define a function to check if the user wins
def is_win(user, computer):
    # return true if the user wins
    # r > s, s > p, p > r
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') \
        or (user == 'p' and computer == 'r'):
        return True
    else:
        return False

# define a function to play the game
def play():
    # define a list of valid inputs
    valid_input = ['r', 'p', 's']
    # define a dictionary of the game rules
    rules = {'r':'s', 's':'p', 'p':'r'}

    # get the user input
    user = input("Enter your choice (r, p, s): ")
    # check if the user input is valid
    while not check_input(user):
        print("Invalid input. Please try again.")
        user = input("Enter your choice (r, p, s): ")

    # get the computer input
    computer = random.choice(valid_input)

    # check if the user wins
    if is_win(user, computer):
        print("You won!")
    # check if the computer wins
    elif is_win(computer, user):
        print("You lost!")
    # otherwise, it's a tie
    else:
        print("It's a tie")

    # print the computer choice by ascii art
    print("Computer choice: " + computer + "\n")
    if computer == 'r':
        print("    _______")
        print("---'   ____)")
        print("      (_____)")
        print("      (_____)")
        print("      (____)")
        print("---.__(___)")
    elif computer == 'p':
        print("    _______")
        print("---'   ____)____")
        print("          ______)")
        print("          _______)")
        print("         _______)")
        print("---.__________)")
    elif computer == 's':
        print("    _______")
        print("---'   ____)____")
        print("          ______)")
        print("       __________)")
        print("      (____)")
        print("---.__(___)")

# call the play function
play()
