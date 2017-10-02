#guess_a_number_ai
#Noah G

import random

#config
high = 1000
low = 1
    
# helper functions
def get_name():
    global name
    name = input("Please type your name: ")
    return name

def show_start_screen():
    print("<><><><><><><><><><><><><>")
    print("<>  Guess a Number A.I  <>")
    print("<><><><><><><><><><><><><>")

def show_credits():
    print("Goodbye " + str(name) + "!")
    print()
    print("This game was created by Noah on October 2nd, 2017.")
    
def get_guess(current_low, current_high):
    """
    Return a truncated average of current low and high.
    """
    guess = (current_low + current_high) // 2
    return guess


def pick_number():
    """
    Ask the player to think of a number between low and high.
    Then  wait until the player presses enter.
    """
    print ()
    print (str(name) + ", think of a number between " + str(low) + " and " + str(high) + ".")
    input ("Press ENTER to continue")
    print()
    print  ((high + low) // 2)
           
def check_guess(guess):
    """
    Computer will ask if guess was too high, low, or correct.

    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """
    while True:
        print()
        print (str(name) + ", is " + str(guess) + " higher, lower, or did I guess correctly?")
        feedback = input("(Type higher, lower, or correct)").lower()

        if feedback == 'higher' or feedback == 'h' :
            return 1
        elif feedback == 'lower' or feedback == 'l' :
            return -1
        elif feedback == 'correct' or feedback == 'c' or feedback == 'y' or feedback == 'yes':
            return 0
        else:
            print ("You must type 'higher', 'lower', or 'correct'")

def show_result(guess, rand):
    """
    Says the result of the game. (The computer might always win.)
    """
    print ("I won")

def play_again():
    while True:
        decision = input(str(name) + ", would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print(str(name) + ", I don't understand. Please enter 'y' or 'n'.")

def play():
    current_low = low
    current_high = high
    check = -1
    
    pick_number()
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess)

        if check == -1:
            # adjust current_low
            current_low = (guess + 1)
            
        elif check == 1:
            # adjust current_high
            current_high = (guess - 1)
            

    show_result#(guess, rand)

# Game starts running here
show_start_screen()

get_name()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()



