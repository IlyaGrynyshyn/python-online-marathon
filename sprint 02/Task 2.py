MORSE_NUMBERS_DICT = { '0':'-----', '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                }

def morse_number(numbers):
    result = ''
    for number in numbers:
        if number != ' ':
            result += MORSE_NUMBERS_DICT[number] + ' '
        else:
            result += ' '

    return result

print(morse_number('005'))
