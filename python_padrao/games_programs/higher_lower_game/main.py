import python_padrao.games_programs.higher_lower_game.functions as functions
import python_padrao.games_programs.higher_lower_game.art as art

score = 0

while True:

    celeb_A, follower_A = functions.random_celeb()
    celeb_B, follower_B = functions.random_celeb()

    print(art.title)

    print(f"""
    Compare A: {celeb_A}

    {art.vs}

    Against B: {celeb_B}
    """)

    # user answear

    while True:    
        try:
            response = str(input("Who has more followers? Type 'A' or 'B':  ")).upper()
            break
        except ValueError:
            print("Insert a valid option.    ")
            continue

    match response:
        case 'A':
            if follower_A > follower_B:
                score += 1
                print(f"Thats right! - current score {score}")
            else:
                print("Game over!")
                break
        case 'B':
            if follower_B > follower_A:
                score += 1
                print(f"Thats right! - current score {score}")
            else:
                print("Game over!")
                break
        

