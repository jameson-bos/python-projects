import random

# Intro
print("\nWelcome to the number guessing game!")
print("The goal of the game is to guess the number the computer chose.")

name = input("\nFirstly, what's your name? \n")

level_choice = input(f"\nOkay, {name}, would you like to play easy, medium, hard, or free play mode? \n").lower()

if level_choice == "easy" or level_choice == "easy mode":
    print("\nGreat, let's start with the easy level. The computer's guess will be between 1 and 10") 
elif level_choice == "medium" or level_choice == "medium mode":
    print("\nGreat, let's start with the medium level. The computer's guess will be between 1 and 50.")
elif level_choice == "hard" or level_choice == "hard mode":
    print("\nGreat, let's start with the hard level. You will not know the range of the numbers available for the computer to choose.")
elif level_choice == "free play" or level_choice == "free play mode":
    print("\nOkay, in this mode you will select your own range. Let's get started!")
    top_of_range = input("What would you like the top of the range to be?\n")
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
    else:
        print("Please print a number next time.")
        quit()
    print(f"\nOkay, the computer will choose a number between 1 and {top_of_range}")
else:
    print("\nPlease type easy, medium, hard, or free play mode next time.")
    quit()
#iuhxzihidsniu
# Randomizing top of the range, instead of having a defined top of range not revealed to user
# Could also randomize the bottom of the range? User is probably under the assumption 1 is the low
hard_top_range = random.randint(50,10000)
guesses = 0

# Play Time!
if level_choice == "free play" or level_choice == "free play mode":
    computer_choice = random.randint(1, top_of_range)   
elif level_choice == "easy" or level_choice == "easy mode":
    computer_choice = random.randint(1, 10)
elif level_choice == "medium" or level_choice == "medium mode":
    computer_choice = random.randint(1, 50)
elif level_choice == "hard" or level_choice == "hard mode":
    computer_choice = random.randint(1, hard_top_range)

while level_choice == "free play" or level_choice == "free play mode":
    guesses += 1
    user_guess = input("\nWhat's your guess? \n")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please choose a number next time.")
        quit()
    if user_guess == computer_choice:
        print("\nYou got it!")
        break
    if user_guess > computer_choice:
        print("You are higher than the computer's choice, try again!")
        continue
    if user_guess < computer_choice:
        print("You are lower than the computer's choice, try again!")
        continue

while level_choice != "free play" and level_choice != "free play mode":
    guesses += 1
    user_guess = input("\nWhat's your guess? \n")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else: 
        print("Please choose a number next time.")
        quit()
    if user_guess == computer_choice:
        print("\nYou got it!")
        break
    if user_guess > computer_choice:
        print("You are higher than the computer's choice, try again!")
        continue
    if user_guess < computer_choice:
        print("You are lower than the computer's choice, try again!")
        continue
    
# End of Game    
if guesses == 1:
    print(f"\nYou won in {guesses} guess! Great job, {name}!")
else:
    print(f"\nYou won in {guesses} guesses! Great job, {name}!")