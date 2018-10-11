import random

num = random.randint(1,10)

my_guess = int(input("Guess a number 1 through 10: "))

while my_guess != num:
    if my_guess > num:
        print("too high")
    else:
        print("too low")

    my_guess = int(input("Guess a number 1 through 10: "))

print("You got it!")
