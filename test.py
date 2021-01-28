import numpy as np
from skimage import io, color
import matplotlib.pyplot as plt

def display(img):
    # Show image
    plt.figure(figsize = (5,5))
    plt.imshow(img)
    plt.axis('off')
    plt.show()

image1 = io.imread('hw0_release/image1.jpg')
h = int(image1.shape[1]/2)
print(h)
print(image1[:,0:h,:])
