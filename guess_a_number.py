import random
import math


# config
low = 1
high = 10000
log = math.log(high - low + 1, 2)
limit = math.ceil(log)

# helper functions
def show_start_screen():
    print("<><><><><><><><><><><><><>")
    print("<><> Guess a Number! <><>")
    print("<><><><><><><><><><><><><>")

def show_credits():
    print("Goodbye!")
    print()
    print("This game was created by Noah.")
    
def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")

def pick_number():
    print()
    print("I'm thinking of a number from " + str(low) + " to " + str(high) +".")
    print()
    print("You get " + str(limit) + " tries to guess the correct number.")
    print()

    return random.randint(low, high)

def check_guess(guess, rand):
    if guess < rand:
        print("You guessed too low.")
        print()
    elif guess > rand:
        print("You guessed too high.")
        print()

def show_result(guess, rand):
    if guess == rand:
        print("You win!")
    else:
        print("You lost! The number was " + str(rand) + ".")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ").lower()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    guess = -1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
