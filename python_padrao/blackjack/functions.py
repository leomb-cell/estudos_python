import random


# data for functions

CARTAS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def clear_terminal_ansi():
    # \033[H moves cursor to top home, \033[2J clears the screen
    print("\033[H\033[2J", end="")

def random_card(number):
    """
    This function returns one or more integer values from CARTAS global array based on the ammount specified by the params
    """
    global CARTAS
    random_cards = []
    for i in range(0,number):
        random_cards.append(random.choice(CARTAS))
    return random_cards

def score_counting(hand):
    """
    A simple function to count the points based on the hads either from the dealer or the player just because i can
    """
    score = 0
    for i in range(len(hand)):
        score += hand[i]
    return score