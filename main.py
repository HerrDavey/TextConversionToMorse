LETTERS = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = '1234567890'
MORSE_CODE = ('·− −··· −·−· −·· · ··−· −−· ···· ·· ·−−− −·− ·−·· −− −· −−− ·−−· −−·− ·−· ··· − ··− ···− ·−− −··− −·−− '
              '−−·· ·−−−− ··−−− ···−− ····− ····· −···· −−··· −−−·· −−−−· −−−−− ')


def morse_conversion():
    morse_lst = MORSE_CODE.split(" ")
    dictionary = {k: m for (k, m) in zip(LETTERS + NUMBERS, morse_lst)}

    user_input = input("What do you want to convert?\n> ")

    new_phrase = ''
    for char in user_input:
        if char == ' ':
            new_phrase += '/ '

        for letter, morse in dictionary.items():
            if char.lower() == letter:
                char = char.replace(char, morse)
                new_phrase += char + ' '

    print(f'There is your phrase in Morse Code: {new_phrase}')


morse_conversion()
