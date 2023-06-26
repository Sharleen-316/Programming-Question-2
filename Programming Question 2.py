#This code creates a game where the user must correctly guess a randonly generated integer between 1 and 100. 
#Seperated into different functions, the code provided below creates a target goal for the user to try and guess, prompts the user to enter
# their inital guess and checks to see if it's a valid input (whether or not it's between 1 and 100). If it's not, then it prompts the user to guess again.
#If it is, then it checks to see if the user's guess is correct. It will then display a message telling the user whether their guess is 
# too high, too low or correct. If their guess is too high or too low, it will prompt the user to guess again. This process repeats 
# until the user guesses the target goal. This code works because it utilises conditional functions such as if/elif/else statements 
# to make the necessary comparisons in order to determine whether the user's guess is valid and correct. It also calls the function "setting_guess" 
# if the user's guess isn't valid or correct and prints out a message letting the user know this beforehand. In the case of whether it's correct or not, 
# the code also calls one of two functions that prints out the message that lets the user know that their guess is incorrect,
# one telling them it's too high and another telling them it's too low.

import random

def check_message_to_display(guess, target):
        """
        Compares user's guess to the target goal and checks to see what message it should 
        display depending on whether user's guess is too high, too low, or correct

        :param guess: user's guess
        :param target: target goal
        """
        if guess == target:
            #Prompts code displaying message telling the user that guess and target are equal
            display_correct_message()
        elif guess > target:
            #Prompts code displaying message telling the user that guess is too high
            display_highest_message()
        else:
            #Prompts code displaying telling the user that guess is too low
            display_lowest_message()

def display_highest_message():
        """
        Prints a message telling the user that their guess is too high and prompts them to guess again
        """
        print("Your guess is too high")
        #Prompts user to guess again
        setting_guess()

def display_lowest_message():
        """
        Prints a message telling the user that their guess is too low and prompts them to guess again
        """
        print("Your guess is too low")
        #Prompts user to guess again
        setting_guess()

def display_correct_message():
        """
        Prints a message telling the user that their guess is correct
        """
        print("Your guess is correct!")

def validate_input(guess):
        """
        Checks to see if the user's guess is valid based on the range 
        and prompts them to guess again if it isn't
        """
        #Checks to see if the guess is lower than 1 or higher than 100
        if guess < 1 or guess > 100:
            #If it is, tells the user their guess is invalid and prompts them to guess again
            print("Your input is outside of the allocated range. Please try again.")
            setting_guess()
        
def setting_guess():
        """
        Gets user to input their guess and starts/continues the guessing game
        """
        #Informs the user about the range the target is in
        print("The target is in between 1 and 100")
        #Asks the user for their guess
        guess = int(input("Enter your guess: "))
        #Makes sure the guess is in the range
        validate_input(guess)
        #Checks if the guess is correct or not
        check_message_to_display(guess, target)


#Setting target for user to try to get to
#target = random.randint(1,100)
target = 1
#Starting the guessing game
setting_guess()

#Examples:
# 1. Change the target number to 80 and enter these guesses:
#       a) 101 (Expected output: "Your input is outside of the allocated range, please 
#       try again." and then prompts you to try again)
#       b) 0 (Expected output: "Your input is outside of the allocated range, please 
#       try again." and then prompts you to try again)
#       c) 81 (Expected output: "Your guess is too high" and then prompts you to try again)
#       d) 79 (Expected output: "Your guess is too low" and then prompts you to try again)
#       e) 80 (Expected output: "Your guess is correct!" and then ends the game)
# ---------------------------------------------------
# 2. Change the target number to 100 and enter these guesses:
#       a) 101 (Expected output: "Your input is outside of the allocated range, please 
#       try again." and then prompts you to try again)
#       b) 0 (Expected output: "Your input is outside of the allocated range, please 
#       try again." and then prompts you to try again)
#       c) 99 (Expected output: "Your guess is too low" and then prompts you to try again)
#       d) 100 (Expected output: "Your guess is correct!" and then ends the game)
# ---------------------------------------------------
# 3. Change the target number to 1 and enter these guesses:
#       a) 101 (Expected output: "Your input is outside of the allocated range, please 
#       try again." and then prompts you to try again)
#       b) 0 (Expected output: "Your input is outside of the allocated range, please 
#       try again." and then prompts you to try again)
#       c) 2 (Expected output: "Your guess is too high" and then prompts you to try again)
#       d) 1 (Expected output: "Your guess is correct!" and then ends the game)