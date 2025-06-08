import random
import numpy as np

# Take in the limits
highest = int(input("Please input the upper number limit\n"))
lowest = int(input("Please input the lower number limit\n"))

# Setting guess limit based on O(log n)
full_arr = list(range(lowest, highest))
guess_limit = int(np.round(np.log(len(full_arr))) + 1)
user_guesses = 0

# Informing user of rules
print(f'Guess numbers between {highest} and {lowest} in the least amount of guesses. Guesses limit {guess_limit}\n')

target = random.randint(lowest, highest)

while user_guesses < guess_limit:
    user_guesses += 1
    guess = int(input("What is your guess?\n"))

    if (guess == target):
        print("Whoop Whoop, your guess was right\n")
        break;
    elif (user_guesses >= guess_limit and guess != target):
        print(f'Better luck next time - The number was {target}\n')
        break;
    elif (guess > target):
        print("Guess is too high\n")
    elif (guess < target):
        print("Guess is too low\n")
