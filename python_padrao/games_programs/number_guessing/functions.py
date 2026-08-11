import random


# limpar tela

def clear_terminal_ansi():
    # \033[H moves cursor to top home, \033[2J clears the screen
    print("\033[H\033[2J", end="")

# ecolher dificuldade

def escolha_dificuldade(dificuldade):
    random_num = random.randint(1,100)
    if dificuldade.lower() == "facil":
        tentativas = 10
        return tentativas, random_num
    else:
        if dificuldade.lower() == "dificil":
            tentativas = 5
            return tentativas, random_num
        else:
            if dificuldade.lower() == "customizado":
                tentativas = 0
                while tentativas <= 0:
                    tentativas = int(input("Insira a quantidade de tentativas desejada: "))
                    if tentativas <= 0: 
                        print("Insira um numero acima de 0! ")
                        continue
                    return tentativas, random_num
            else:
                if dificuldade.lower() == "sair":
                    return "sair", random_num

                

# gerador do numero

def rand_num():
    return 