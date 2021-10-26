import random

def main():
    rand_num = random.randint(0,100)
    user = input("Hey, what's your name?")
    print(user, ", I'm thinking of a number between 1 and 100\n Try to guess my number")
    user_num = int(input("You're guess?"))
    
    while user_num != rand_num:
        if user_num > rand_num:
            print('Too high, guess again.')
        elif user_num < rand_num:
            print('Too low, guess again.')
        user_num = int(input("You're guess?"))
    if user_num == rand_num:
        print('You guessed it!')
    
main()