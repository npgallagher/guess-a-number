#
#
#guess_a_number_ai
#Noah G
#
#
import random
import math

ask = True

def ask():
    while True:
        print ("Hello!")
        print ("Would you like to guess the number or should I?")
        print ("Type 'me' or 'you'")
        answer = input().lower()

        if answer == 'me':
            # config
            global low
            low = 1
            global high
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
                        quit()
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
        elif answer == 'you':
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
                        print (str(name) + ", ou must type 'higher', 'lower', or 'correct'")

            def show_result():   #guess, rand
                """
                Says the result of the game. (The computer might always win.)
                """
                print (str(name) + ", I won in " + str(tries) + " guesses.")

            def play_again():
                while True:
                    decision = input(str(name) + ", would you like to play again? (y/n) ")

                    if decision == 'y' or decision == 'yes':
                        return True
                    elif decision == 'n' or decision == 'no':
                        quit()
                        return False
                    else:
                        print(str(name) + ", I don't understand. Please enter 'y' or 'n'.")

            def play():
                print (str(name) + ", please type the highest possible number")
                global high
                high = input()
                high = int(high)
                print (str(name) + ", please type the lowest possible number")
                global low
                low = input()
                low = int(low)
                current_low = low
                current_high = high
                check = -1
                global tries
                tries = 0
                
                pick_number()
                
                while check != 0:
                    guess = get_guess(current_low, current_high)
                    check = check_guess(guess)

                    if check == -1:
                        # adjust current_low
                        current_low = (guess + 1)
                        tries += 1
                        
                    elif check == 1:
                        # adjust current_high
                        current_high = (guess - 1)
                        tries += 1
                        

                show_result()   #(guess, rand)

            # Game starts running here
            show_start_screen()

            get_name()

            playing = True

            while playing:
                play()
                playing = play_again()

            show_credits()
        else:
            print ("You must type 'me' or 'you'")
            
change_game = True
def change_game():
    while True:
        print ("Would you like to change games?")
        print ("Type 'yes' or 'no'")
        response = input().lower()

        if response == 'yes':
            return True

        elif response == 'no':
            quit()
        else:
            print ("You must type 'yes' or 'no'")
        
ask()
change_game()
