import random

# Roll dice
roll = random.randint(1,6)
guess = int(input('Guess the dice roll:\n'))

if guess == roll:
    print('Correct!')
else:
    print('Wrong!')