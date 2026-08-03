import random
import art

# declaração de variaveis

options = [art.pedra, art.papel, art.tesoura]

pontos_computador = 0
pontos_usuario = 0

print(art.title)
print("Bem vindo ao pedra papel e tesoura!")
rodadas = int(input("Quantas rodadas gostaria de jogar?"))



for i in range(rodadas):
    # computer choice

    computer_choice_index = random.randint(0,2)

    computer_choice_art = options[computer_choice_index]

    # user choice

    while True:
        user_choice_index = int(input("Qual voce escolhe? \n0 - pedra\n1 - papel\n2 - tesoura\n\n"))
        # verificando se a escolha e compativel
        if user_choice_index in [0,1,2]:
            break
        else:
            print("Escolha uma opção entre 0, 1, 2!")
            continue

    user_choice_art = options[user_choice_index]

    print("Computador escolheu...")
    print(computer_choice_art)
    print(art.x)
    print("Usuario escolheu...")
    print(user_choice_art)

    #     escolhas iguais

    if computer_choice_index == user_choice_index:
        print("Usuario e computador escolheram a mesma opção...")
        print(art.empate)

    #     pedra x papel

    elif computer_choice_index == 0 and user_choice_index == 1:
        print("Papel vence pedra, usuário ganha!")
        print(art.ganhou)

        # add pontos

        pontos_usuario += 1

    #     pedra x tesoura

    elif computer_choice_index == 0 and user_choice_index == 2:
        print("Tesoura perde para pedra, computador ganha!")
        print(art.perdeu)

        # add pontos

        pontos_computador += 1

    #     papel x pedra

    elif computer_choice_index == 1 and user_choice_index == 0:
        print("Pedra perde para papel, computador ganha!")
        print(art.perdeu)

        # add pontos

        pontos_computador += 1

    #     papel x tesoura

    elif computer_choice_index == 1 and user_choice_index == 2:
        print("tesoura vence papel, usuário ganha!")
        print(art.ganhou)

        # add pontos

        pontos_usuario += 1

    #    tesoura x pedra

    elif computer_choice_index == 2 and user_choice_index == 0:
        print("Pedra vence Tesoura, usuario ganha!")
        print(art.ganhou)

        # add pontos

        pontos_usuario += 1

    #     papel x pedra

    elif computer_choice_index == 2 and user_choice_index == 1:
        print("Pedra perde para papel, computador ganha!")
        print(art.perdeu)

        # add pontos

        pontos_computador += 1

# resultado final da partida

print(art.separador)

print(art.resultado)

if pontos_computador > pontos_usuario:
    print(art.vitoria_computador)
    print(f"Computador venceu com: {pontos_computador} pontos")
elif pontos_usuario > pontos_computador:
    print(art.vitoria_usuario)
    print(f"Usuario venceu com: {pontos_usuario} pontos")
elif pontos_usuario == pontos_computador:
    print(art.empate)
    print(f"Jogo terminou empatado")

print("Obrigado por jogar pedra-papel-tesoura!")