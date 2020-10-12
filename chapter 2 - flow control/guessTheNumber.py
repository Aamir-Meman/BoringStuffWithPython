# This is a guess number game
import random

# guess the number in between 1 and 20
secretNumber = random.randint(1,20)
print('I am thinking number between 1 and 20')

# Guess the number by 6 times
for guessTaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess > secretNumber:
        print(' Your guess is too high')
    elif guess < secretNumber:
        print(' Your guess is too low')
    else:
        break  # Your guess is correct
if guess == secretNumber:  # type: ignore
    print('You guess was correct after ' + str(guessTaken) + ' times.')  # type: ignore
else:
    print('Nope. The number I was thinking of ' + str(secretNumber))
