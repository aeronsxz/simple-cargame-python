import random

# Rules :  Rock beats Scissors | Scissors beats Paper  | Paper beats Rock

def rock_paper_scissor():
    player1 = input("Please choice between 'r' for rock, 'p' for paper, 's' for scissors\n: ").lower()
    computer = random.choice(['r', 'p', 's']).lower()

    if player1 == computer:
        return "It's a tie!"

    if is_win(player1, computer):
        return 'You won!'

    if is_lost(computer, player1):
        return 'You lost!'

    return 'Sorry wrong input.'


def is_win(player, opponent):
    # return true if player1 wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True


def is_lost(opponent, player):
    # return true if computer wins
    if (opponent == 'r' and player == 's') or (opponent == 's' and player == 'p') \
            or (opponent == 'p' and player == 'r'):
        return True


print(rock_paper_scissor())