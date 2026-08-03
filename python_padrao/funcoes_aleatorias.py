# numeros primos

def is_prime(num):
    if num < 2:
        return False 
    else:
        for i in range(2,num):
            if num%i == 0:
                return False
    return True

print(is_prime(7523345879345938742594784643))


# limpar tela

def clear_terminal_ansi():
    # \033[H moves cursor to top home, \033[2J clears the screen
    print("\033[H\033[2J", end="")