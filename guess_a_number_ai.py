import random

# config
low = 1
high = 1000


# helper functions
def show_start_screen():
    print("<><><><><><><><><><><><><>")
    print("<>  Guess a Number A.I  <>")
    print("<><><><><><><><><><><><><>")

def show_credits():
    print("Goodbye!")
    print()
    print("This game was created by Noah.")
    
def get_guess(current_low, current_high):
    """
    Return a truncated average of current low and high.
    """
    pass


def pick_number():
    """
    Ask the player to think of a number between low and high.
    Then  wait until the player presses enter.
    """
    print ("Think of a number between " + str(low) + " and " + str(high) + ".")
    input ("Press ENTER to continue")
    print  ((high + low) // 2)
           
def check_guess(guess):
    """
    Computer will ask if guess was too high, low, or correct.

    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """
    while True:
        print ("Was my guess too high, too low, or correct?")
        print ("(Type high, low, or correct)")
        feedback = input().lower

        if feedback == 'high':
            return 1
        elif feedback == 'low':
            return -1
        elif feedback == 'correct':
            return 0
        else:
            print ("You must type 'high', 'low', or 'correct'")

def show_result():
    """
    Says the result of the game. (The computer might always win.)
    """
    pass

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

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
            pass
        elif check == 1:
            # adjust current_high
            pass

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()



