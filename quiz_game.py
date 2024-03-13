print('Welcome to my quiz!') # Prints welcome message

playing = input("Do you want to play? ") # lets user input string

if playing != "yes":  # if user input is not yes, quit program
    quit()

print("Okay! Let's play :)")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print('Correct!')
else:
    print("Incorrect!")

answer = input("What does GPU stnad for? ")
if answer == "graphics processing unit":
    print('Correct!')
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print('Correct!')
else:
    print("Incorrect!")

answer = input("What does PSU stand for?")
if answer == "power supply unit":
    print('Correct!')
else:
    print("Incorrect!")
