import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')


player1 = input('Please input your name: ')
print(f"Hello {player1}, Welcome to the Guessing Game.")
game = input("Please choose between you guess the computer number (P) or the computer guess your number. (C): ").lower()

if game == 'p':
    num = int(input("Please enter a highest number: "))
    print(f"The computer will have it's number between 1 and {num}. Good luck on guessing!")
    guess(num)

elif game == 'c':
    num = int(input("Please enter a highest number: "))
    print(f"Please choose your number between 1 and {num}. The computer will guess your number")
    computer_guess(num)

else:
    print('Invalid Input')