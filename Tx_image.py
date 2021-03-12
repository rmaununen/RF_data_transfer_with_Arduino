# load and display an image with Matplotlib
from matplotlib import image
from matplotlib import pyplot
import numpy as np
# load image as pixel array
def create_data():
    from matplotlib import image
    image = image.imread('test_image.jpg').copy()

    # display the array of pixels as an image
    pyplot.imshow(image)
    pyplot.show()

    #Reducing 24-bit colour to 9-bit colour:
    def color_reduce(image):
        delta = int(round(255/7))
        colours = []
        total = 0
        while total < 255:
            colours.append(total)
            total+=delta
        # here are the values that each of the colour components(r,g,b) can take:
        print('Color compression initialized...')
        print('Possible color values: ', colours)
        print('\nCOMPRESSING COLOR...')
        reduced = []
        a = 1
        total_lines = image.shape[0]
        for line in image:
            line_list = []
            for pixel in line:
                pixel_list = []
                for p in pixel:
                    c_chosen = 0
                    for c in colours:
                        if abs(c-p) < (delta/2):
                            c_chosen = c
                            break
                    pixel_list.append(c_chosen)
                line_list.append(pixel_list)
            reduced.append(line_list)
            perc = round(100*(a/total_lines), 1)
            if perc%10==0:
                print(round(perc),'%')
            a+=1
        print('DONE')
        return np.array(reduced)

    reduced_img = color_reduce(image)
    pyplot.imshow(reduced_img)
    pyplot.show()

    #Encoding each pixel with 9 bits
    def encode_in_binary(image):
        print('\nDATA ENCODING...')
        delta = int(round(255/7))
        colours = []
        total = 0
        while total < 255:
            colours.append(total)
            total+=delta
        encoded = []
        data_out = ''
        a = 1
        total_lines = image.shape[0]
        for line in image:
            line_list = []
            for pixel in line:
                pixel_str = ''
                for p in pixel:
                    if p == 0:
                        c = '000'
                    elif p == delta:
                        c = '001'
                    elif p == 2*delta:
                        c = '010'
                    elif p == 3*delta:
                        c = '011'
                    elif p == 4*delta:
                        c = '100'
                    elif p == 5*delta:
                        c = '101'
                    elif p == 6*delta:
                        c = '110'
                    elif p == 7*delta:
                        c = '111'
                    else:
                        c = 'WAR'
                    pixel_str += c
                data_out += c
                line_list.append(pixel_str)
            encoded.append(line_list)
            perc = round(100*(a/total_lines), 1)
            if perc%10==0:
                print(round(perc),'%')
            a+=1
        print('DONE')
        return np.array(encoded), data_out

    coded_img, data_out = encode_in_binary(reduced_img)
    print(coded_img)
    return data_out + '2'