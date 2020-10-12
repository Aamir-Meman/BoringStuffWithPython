import random
import sys

print('ROCK,PAPER,SCISSORS')

# This variables keeps the track of the number of wins, losses and ties
wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print('Enter your move:(r)ock (p)aper (s)cissors or (q)uit')
        playerInput = input()
        if playerInput == 'q':
            sys.exit()
        if playerInput == 'r' or playerInput == 'p' or playerInput == 's':
            break
        print('Type one of r, p, s, or q.')
    # Display what the player chooses
    if playerInput == 'r':
        print('ROCK versus...')
    elif playerInput == 'p':
        print('PAPER versus...')
    elif playerInput == 's':
        print('SCISSOR versus...')
    # Display what the computer chooses
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')
    # Display and record the win/loss/tie
    if playerInput == computerMove:  # type: ignore
        print('It is a tie')
        ties = ties + 1
    elif playerInput == 'r' and computerMove == 's':  # type: ignore
        print('You win!')
        wins = wins + 1
    elif playerInput == 'p' and computerMove == 'r':  # type: ignore
        print('You win!')
        wins = wins + 1
    elif playerInput == 's' and computerMove == 'p':  # type: ignore
        print('You win!')
        wins = wins + 1
    elif playerInput == 'r' and computerMove == 'p':  # type: ignore
        print('You lose!')
        losses = losses + 1
    elif playerInput == 'p' and computerMove == 's':  # type: ignore
        print('You lose!')
        losses = losses + 1
    elif playerInput == 's' and computerMove == 'r':  # type: ignore
        print('You lose!')
        losses = losses + 1