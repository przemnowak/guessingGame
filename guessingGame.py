import random

number = random.randint(1, 100)
tries = 0
win = False

uName = input("Hello, what's your name? ")

if uName == "":
    print("You don't have a name?\nOk, I will call you Zygfryd then!")
    uName = "Zygfryd"

print("Hello " + uName)
question = input("Would you like to play a game? [Y/N] ")


if question.lower() == "n":
    print("oh.. okay\nno worries!")
else:
    print("I am thinking of a number between 1 and 100")
    while not win:
        guess = int(input("Have a guess: "))
        tries += 1
        if guess == number:
            win = True
        elif guess < number:
            print("Guess higher!")
        elif guess > number:
            print("Guess lower!")
    if win:
        print("Correct! \n"
              "You did it in " + str(tries) + " tries!")
