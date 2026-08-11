import random
import python_padrao.games_programs.hangman.words as words
import python_padrao.games_programs.hangman.art as art
import time

#functions

def clear_terminal_ansi():
    # \033[H moves cursor to top home, \033[2J clears the screen
    print("\033[H\033[2J", end="")

def random_word(word_list):
    word = random.choice(word_list)
    return word

def animated_victory():
    duration = 5
    start_time = time.time()
    while time.time() < start_time + duration:
        for position in art.victory_flip:
            print(art.victory)
            print(position)
            time.sleep(0.13)
            clear_terminal_ansi()

def animated_gameover():
    duration = 5
    start_time = time.time()
    while time.time() < start_time + duration:
        for position in art.hanged:
            print(art.game_over)
            print(position)
            time.sleep(0.1)
            clear_terminal_ansi()

# variables 

lives = 8
points = 0
guesses = []
wrong_guesses = []
placeholder = ""
chosen_word = ""
word_placeholder = "_" * len(chosen_word)

# menu

while True:

    # clear screen

    clear_terminal_ansi()

    print(
f"""
    {art.title}

    Welcome to the python hangman game! 

    Please choose the difficulty you want to play at or 0 to exit!:

        1 - Easy game: 3 to 6 letters, common words, repeated vowels
        2 - Medium game: 6 to 9 letters, some uncommon words, slightly trickier spellings
        3 - Hard game: 8 or more letters, rare letters, unusual letter combinations
        0 - Exit Game

"""
    )

    difficulty = int(input("Insert choice: "))

    match difficulty:
        case 1:
            word_list = words.easy_words
        case 2:
            word_list = words.medium_words
        case 3:
            word_list = words.hard_words
        case 0:
            print("Bye Bye!")
            break
        case __:
            print("Please insert a valid option.")
            continue

    chosen_word = random_word(word_list)

    print(chosen_word)

    while True:
        placeholder = ""

        for letter in chosen_word:
            if letter in guesses:
                placeholder += letter
            else:
                placeholder += "_"

        # wrong guesses stringfication

        wrong_guesses_str = "-".join(wrong_guesses)

        # confirming if the word is finished or not

        if placeholder == chosen_word:
            animated_victory()
            guesses = []
            wrong_guesses = []
            break
        elif lives == 0:
            animated_gameover()
            guesses = []
            wrong_guesses = []
            break   

        # ascii art for the hangman + placeholder

        print(
        f"""
        {art.hangman[lives-1]}
                {placeholder}

        Wrong guesses: {wrong_guesses_str}
        """)

        guess = str(input("Make a guess (or 0 to exit): ")).lower()

        clear_terminal_ansi()

        if len(guess) < 1:
            print("Insert a valid letter!")
            continue
        elif guess == "0": 
            print("Bye bye...")
            break

        guess = guess[0]
            
        # saving all guesses into an array 

        if guess in guesses:
            print("Warning, this letter has been guessed before!")
            continue
        elif guess in chosen_word:
            guesses.append(guess)
            print("Right!")        
            points += 1
        else:
            wrong_guesses.append(guess)
            lives -= 1
            print(F"Wrong... {lives} attempts left")
