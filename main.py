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


title_author_date = "Morse Converter by naut 2022"
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "1234567890"
punc = ".,?!&;:'/-()"

print(f"\n{title_author_date}\n")
print(f"Acceptable characters: {alpha}{num}{punc}\n")
user_string = input("Enter string to encrypt into Morse Code: ")
print(morse_encrypt(user_string))
