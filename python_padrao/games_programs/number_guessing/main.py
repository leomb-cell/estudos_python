import random
import python_padrao.games_programs.number_guessing.art as art
import python_padrao.games_programs.number_guessing.functions as functions

while True:

# titulo principal do menu

    print(f"""

    {art.title}

    Bem vindo ao jogo de adivinhar numeros!

    Tem duas dificuldades:
    - Facil: 10 tentativas
    - Dificil: 5 tentativas
    - Customizado: escolha o numero de tentativas
    - 'sair' pra fechar o jogo

""")

    # escolha da dificuldade, e gerar numero

    while True:
        option = str(input("Insira a dificuldade desejada: ")).lower()
        if option in ["facil", "dificil", "customizado"]:
            tentativas, random_num = functions.escolha_dificuldade(option)
            break
        else:
            if option == "sair":
                print("Saindo...")
                break
            else:
                print("Escolha uma opção valida! ")
                continue

    # exit?

    if option == 'sair':
        break

    # starting game

    print(random_num)

    while True:
        # verificando vidas

        if tentativas <= 0:
            print("Fim de jogo, acabaram as tentativas...")
            break

        print(f"Voce tem {tentativas} restantes para adivinhar o numero.")

        guess = int(input("Palpite: "))
        print(guess)

        if guess == random_num:
            print(f"Parabens! adivinhou o numero com {tentativas} tentativas faltando!")
            break
        else:
            if guess > random_num:
                print("Muito alto! tente novamente")
                tentativas -= 1
                continue
            else:
                if guess < random_num:
                    print("Muito baixo! tente novamente")
                    tentativas -= 1
                    continue



        

