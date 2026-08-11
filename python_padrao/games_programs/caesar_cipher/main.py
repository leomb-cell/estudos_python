import python_padrao.games_programs.caesar_cipher.art as art

# data

alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [ '0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
special_chars = [ '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~' ]

# functions

def clear_terminal_ansi():
    # \033[H moves cursor to top home, \033[2J clears the screen
    print("\033[H\033[2J", end="")

def encrypt(original_text, shift_amount):

    encrypted_string = ""

    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            if shifted_position >= len(alphabet):
                encrypted_string += alphabet[shifted_position - len(alphabet)]
            else:
                encrypted_string += alphabet[shifted_position]
        elif letter in numbers:
            shifted_position = numbers.index(letter) + shift_amount
            if shifted_position >= len(numbers):
                encrypted_string += numbers[shifted_position - len(numbers)]
            else:
                encrypted_string += numbers[shifted_position]
        elif letter in special_chars:
            shifted_position = special_chars.index(letter) + shift_amount
            if shifted_position >= len(special_chars):
                encrypted_string += special_chars[shifted_position - len(special_chars)]
            else:
                encrypted_string += special_chars[shifted_position]

    return encrypted_string


def decrypt(original_text, shift_amount):

    decripted_string = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        if shifted_position < 0:
            decripted_string += alphabet[shifted_position + len(alphabet)]
        else:
            decripted_string += alphabet[shifted_position]

    return decripted_string


def caesar(direction, original_text, shift_amount):

    # lowering direction from user

    direction = direction.lower()

    # function call

    if direction == "encode":
        result = encrypt(original_text, shift_amount)
    else:
        result = decrypt(original_text, shift_amount)

    return result


# Menu

while True:
    print(art.main_menu)

    direction = str(input("Type 'encode' to encrypt, type 'decode' to decrypt, or 'exit' to quit:\n")).lower()

    if direction == 'exit': 
        print("Exiting... thank you for using caesar cipher!")
        break # stopping execution
    else:
        # validating direction
        if direction not in ['encode', 'decode']:
            print("Please insert a valid option.")
            continue

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    clear_terminal_ansi()
    print(f"Encrypted text: {caesar(direction, text, shift)}")
    