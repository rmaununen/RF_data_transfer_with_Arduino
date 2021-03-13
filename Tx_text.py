def create_text():
    print('Allowed characters: a-z . , ! ? -')
    message = input('Write message: ')
    coded = ''
    for char in message:
        if char == 'a':
            coded += '00000'
        elif char == 'b':
            coded += '00001'
        elif char == 'c':
            coded += '00010'
        elif char == 'd':
            coded += '00011'
        elif char == 'e':
            coded += '00100'
        elif char == 'f':
            coded += '00101'
        elif char == 'g':
            coded += '00110'
        elif char == 'h':
            coded += '00111'
        elif char == 'i':
            coded += '01000'
        elif char == 'j':
            coded += '01001'
        elif char == 'k':
            coded += '01010'
        elif char == 'l':
            coded += '01011'
        elif char == 'm':
            coded += '01100'
        elif char == 'n':
            coded += '01101'
        elif char == 'o':
            coded += '01110'
        elif char == 'p':
            coded += '01111'
        elif char == 'q':
            coded += '10000'
        elif char == 'r':
            coded += '10001'
        elif char == 's':
            coded += '10010'
        elif char == 't':
            coded += '10011'
        elif char == 'u':
            coded += '10100'
        elif char == 'v':
            coded += '10101'
        elif char == 'w':
            coded += '10110'
        elif char == 'x':
            coded += '10111'
        elif char == 'y':
            coded += '11000'
        elif char == 'z':
            coded += '11001'
        elif char == ' ':
            coded += '11010'
        elif char == '.':
            coded += '11011'
        elif char == ',':
            coded += '11100'
        elif char == '!':
            coded += '11101'
        elif char == '?':
            coded += '11110'
        elif char == '-':
            coded += '11111'
        else:
            print('Error: invalid character input')
    print(coded)
    return coded + '2'