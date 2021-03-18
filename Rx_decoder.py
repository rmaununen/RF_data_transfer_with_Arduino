import numpy as np
def text_decode(message):
    print('Allowed characters: a-z . , ! ? -')
    decoded = ''
    byte = []
    data_out = []
    a = 0
    for bit in message:
        if a < 5:
            byte.append(bit)
            a += 1
        elif a == 5:
            data_out.append(byte)
            byte = []
            a = 0

        for byte in data_out:
            byte_str = ''
            for bit in byte:
                byte_str += str(bit)

            if byte_str == '00000':
                decoded += 'a'
            elif byte_str == '00001':
                decoded += 'b'
            elif byte_str == '00010':
                decoded += 'c'
            elif byte_str == '00011':
                decoded += 'd'
            elif byte_str == '00100':
                decoded += 'e'
            elif byte_str == '00101':
                decoded += 'f'
            elif byte_str == '00110':
                decoded += 'g'
            elif byte_str == '00111':
                decoded += 'h'
            elif byte_str == '01000':
                decoded += 'i'
            elif byte_str == '01001':
                decoded += 'j'
            elif byte_str == '01010':
                decoded += 'k'
            elif byte_str == '01011':
                decoded += 'l'
            elif byte_str == '01100':
                decoded += 'm'
            elif byte_str == '01101':
                decoded += 'n'
            elif byte_str == '01110':
                decoded += 'o'
            elif byte_str == '01111':
                decoded += 'p'
            elif byte_str == '10000':
                decoded += 'q'
            elif byte_str == '10001':
                decoded += 'r'
            elif byte_str == '10010':
                decoded += 's'
            elif byte_str == '10011':
                decoded += 't'
            elif byte_str == '10100':
                decoded += 'u'
            elif byte_str == '10101':
                decoded += 'v'
            elif byte_str == '10110':
                decoded += 'w'
            elif byte_str == '10111':
                decoded += 'x'
            elif byte_str == '11000':
                decoded += 'y'
            elif byte_str == '11001':
                decoded += 'z'
            elif byte_str == '11010':
                decoded += ' '
            elif byte_str == '11011':
                decoded += '.'
            elif byte_str == '11100':
                decoded += ','
            elif byte_str == '11101':
                decoded += '!'
            elif byte_str == '11110':
                decoded += '?'
            elif byte_str == '11111':
                decoded += '-'
            else:
                decoded += '*'
    return decoded


def image_decode(data):
    #decode first bits for image size:
    width = 720

    a = 0
    b = 0
    byte = []
    line = []
    img = []
    for bit in data:
        if a < width:
            if b < 9:
                byte.append(bit)
                b += 1
            elif b == 9:
                line.append(byte)
                byte = []
                b = 0
        a += 1
        elif a == width:
            img.append(line)
            line = []
            a = 0

    return np.array(img)