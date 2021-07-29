def morse_number(numbers):
    result = ''
    morse = '-----'
    for i in numbers:
        if 0<= int(i) <=5:
            morse = '-----'
            morse = morse.replace('-' * int(i), '.' * int(i), 1)
        elif 6<= int(i) <= 9:
            morse = '.....'
            morse = morse.replace('.' * (int(i)-5) , '-' * (int(i)-5), 1)
        result += ' ' + morse
    return result.strip()

print(morse_number("513"))
print(morse_number("005"))