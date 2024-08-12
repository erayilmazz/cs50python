import random


while True:
    try:
        level = int(input("Level: "))
        if (level > 0):
            break
    except ValueError:
        continue

number = random.randint(1,level)

while True:
    try:
        guess = int(input("Guess: "))

    except ValueError:
        continue

    if (number == guess):
        print("Just Right!")
        break

    elif (guess > number):
        print("Too large!")

    else:
        print("Too small!")





