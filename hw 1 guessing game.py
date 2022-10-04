#Priscilla Abigail 2602109883 Guessing Game HW

import random
random_num = random.randint(0,100)

your_guess = 0
your_guess = int(input(print("guess a number between 1-100:")))

while your_guess != random_num:

    if your_guess > random_num:
        print("too high")
        your_guess = int(input(print("guess a number between 1-100:")))

    elif your_guess < random_num:
        print("too low")
        your_guess = int(input(print("guess a number between 1-100:")))

else:
    print("correct!")





