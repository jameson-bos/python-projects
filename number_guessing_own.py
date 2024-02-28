import random

print("\nWelcome to the number guessing game!")
print("The goal of the game is to guess the number the computer chose. You will define the range of numbers.")

name = input("\nFirstly, what's your name? \n")

top_of_range = input("\nGreat, let's get started. What would you like your top of range to be? \n")

if top_of_range.isdigit(): 
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please choose a number higher than zero next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

computer_guess = random.randint(1, top_of_range)
guesses = 0
print(computer_guess)


while True:
    guesses += 1
    user_guess = input("\nWhat's your guess? \n")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please choose a number next time.")
        break

    if user_guess == computer_guess:
        print("\nYou got it!")
        break

    if user_guess > computer_guess:
        print("You are higher than the computer's choice, try again!")
        continue
    if user_guess < computer_guess:
        print("You are lower than the computer's choice, try again!")
        continue


if guesses == 1:
    print(f"\nYou won in {guesses} guess! Great job, {name}!")
else:
    print(f"\nYou won in {guesses} guesses! Great job, {name}!")



    


