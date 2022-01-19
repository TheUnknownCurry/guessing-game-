import random

number = random.randint(0,50)
chances = 0
print("enter a number between 0 and 50")


while chances < 5:

        guess = int(input("enter your guess"))
        if guess == number:
                print("congrats you won")
                break
        elif guess < number:
                print("your guess is too low",guess)
                break
        else:
                print("your guess is too high",guess)
        chances += 1
if not chances < 5:
        print("you lose")
 