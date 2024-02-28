import random

name = input("Hello! What's your name?  ")

print(f"\nOkay,", name, "Start by defining the top of your range. \nThe computer will pick a random number within this range. :)")
top_of_range = input("Please type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number higher than 0 next time.")
        quit()
else:
    print("Please type in a number next time.")
    quit()

random_number = random.randint(1, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess:  ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    else:
        if user_guess > random_number:
            print("You were above the number!")
        else:
            print("You were below the number!")

if guesses < 2:
    print(f"Congrats,", name, "you won after", guesses, "guess! Great work!")
else:
    print(f" Congrats,", name, "you won after", guesses, "guesses! Great work!")