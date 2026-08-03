# imports

import functions
import art
import random

# player variables

player_points = 0
player_score = 0
player_hand = []

#dealer variables

dealer_points = 0
dealer_score = 0
dealer_hand = []

# general variables

rounds = 1

# menu

#while True:
functions.clear_terminal_ansi()
print(
f"""
{art.logo}

Bem vindo/a ao BlackJack do leomb!

As regras da casa são:

    - O baralho tem tamanho ilimitado.
    - Não tem coringa.
    - As cartas valete, rei e rainha valem 10 pontos.
    - O ás pode valer 11 ou 1 caso ele faça a mão estourar.
    - Todas as cartas tem probabilidades iguais de vir.
    - As cartas não são removidas do baralho ao serem puchadas.
    - O computador será o dealer.
"""
)
play_exit = str(input("Gostaria de jogar uma rodada? s/n    ")).lower()

match play_exit:
    case "s":
        # First draw
        player_hand = functions.random_card(2)
        dealer_hand = functions.random_card(1)

        while True:
            # Counting score

            player_score = functions.score_counting(player_hand)
            dealer_score = functions.score_counting(dealer_hand)

            # clearing terminal

            functions.clear_terminal_ansi()

            # showing initial cards
            results = f"""    
                            Rodada - {rounds}
________________________________________________________________________
                                    
    Cartas do player: {player_hand}    
    Score do Player: {player_score}    
    Pontos do Player: {player_points}
________________________________________________________________________
    
    Cartas do Dealer: {dealer_hand}    
    Score do Dealer: {dealer_score}
    Pontos do Dealer: {dealer_points}  
________________________________________________________________________

"""
            print(results)

            # validating points after showing hands for feedback reasons

            if player_score > 21:
                print("A sua mão estourou! Você perdeu a rodada!")
                dealer_points += 1
                rounds += 1
                
                continue_break = str(input("Gostaria de jogar mais uma rodada? s/n  ")).lower()
                if continue_break == "s": 
                    player_hand = functions.random_card(2)
                    dealer_hand = functions.random_card(1)
                    continue
                else: 
                    if continue_break == "n":
                        player_hand = functions.random_card(2)
                        dealer_hand = functions.random_card(1)
                        break
                    else:
                        print("Insira uma resposta valida! jogo continuado por padrão...")
                        continue
            else:
                if dealer_score > 21:
                    print("A mão do dealer estourou! Você ganhou a rodada!")
                    player_points += 1
                    rounds += 1

                    continue_break = str(input("Gostaria de jogar mais uma rodada? s/n  ")).lower()
                    if continue_break == "s": 
                        player_hand = functions.random_card(2)
                        dealer_hand = functions.random_card(1)
                        continue
                    else: 
                        if continue_break == "n":
                            player_hand = functions.random_card(2)
                            dealer_hand = functions.random_card(1)
                            continue
                        else:
                            print("Insira uma resposta valida! jogo continuado por padrão...")
                            continue

            # new card?
                
            pull = str(input("Puxar mais uma carta? s/n ")).lower()

            if pull == "s":    
                player_hand.append(functions.random_card(1)[0])
                continue
            else:
                while dealer_score <= 17 or len(dealer_hand) <= 5:
                    dealer_hand.append(functions.random_card(1)[0])


    case "n":
        print("Saindo do jogo...")
    case __:
        print("Insira uma resposta valida!")

