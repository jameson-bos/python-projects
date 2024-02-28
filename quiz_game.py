player = input("Hello, what is your name?\n")

print("Welcome" + ', ' + player + '!')

playing = input("Are you ready to play?\n")

if playing.title() != "Yes":
    print("Okay, maybe soon?")
    quit()
else:
    print("Okay! Let's get started. :) ")

answer = input("What does CPU stand for?\n")
if answer.title() == 'Central Processing Unit':
    print("Correct!")
else:
    print('Incorrect!')

answer = input("What does PC stand for?\n")
if answer.title() == 'Personal Computer':
    print("Correct!")
else:
    print('Incorrect!')

answer = input("What does RAM stand for?\n")
if answer.title() == 'Random Access Memory':
    print("Correct!")
else:
    print('Incorrect!')

answer = input("What does PSU stand for?\n")
if answer.title() == 'Power Supply Unit':
    print("Correct!")
else:
    print('Incorrect!')

answer = input("What does GPU stand for?\n")
if answer.title() == 'Graphics Processing Unit':
    print("Correct!")
else:
    print('Incorrect!')

print("Done! Great work, " + player + ":)")