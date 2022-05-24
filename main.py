import argparse
import pyperclip    # pip install pyperclip


def morse_encrypt(string):
    morse_dict = {
        'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
        'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
        'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',
        'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
        'Y':'-.--', 'Z':'--..',
        '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....',
        '6':'-....', '7':'--...', '8':'---..',
        '9':'----.', '0':'-----',
        '.':'.-.-.-', ',':'--..--', '?':'..--..', '!':'-.-.--', '&':'.-...',
        ';':'-.-.-.', ':':'---...', "'":".----.", '/':'-..-.', '-':'-....-',
        '(':'-.--.', ')':'-.--.-', ' ':' '
    }

    cipher = ""

    for letter in string.upper():
        cipher += morse_dict[letter] + " "
    
    return cipher


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Morse Coder',
        description='A simple python command line script to encrypt your message into Morse Code.'
    )
    parser.add_argument("--version", "-v", action='version', version='%(prog)s v1.0.0')
    parser.add_argument("--message", "-m", help="Your message to convert.", default=None, type=str)
    args = parser.parse_args()

    title_author_date = "Morse Coder by naut 2022"
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "1234567890"
    punc = ".,?!&;:'/-()"

    print(f"\n{title_author_date}\n")
    print(f"Acceptable characters: {alpha}{num}{punc}\n")

    user_string = args.message
    if user_string is None:
        user_string = input("Enter your string to encrypt into Morse Code: ")

    encrypted_message = morse_encrypt(user_string)
    pyperclip.copy(encrypted_message)
    print(encrypted_message)