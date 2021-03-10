# load and display an image with Matplotlib
from matplotlib import image
from matplotlib import pyplot
import numpy as np
# load image as pixel array
image = image.imread('test_image.jpg')
# summarize shape of the pixel array
image2 = np.array(image)
# display the array of pixels as an image
pyplot.imshow(image)
pyplot.show()

print(image2)