import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread("kawaii.jpg", 0)
lap = cv.Laplacian(image, cv.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))
sobelX = cv.Sobel(image, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(image, cv.CV_64F, 0, 1)
canny = cv.Canny(image, 100, 200)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
soberl_combined = cv.bitwise_or(sobelY, sobelX)

titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobel_Combined', 'canny']
images = [image, lap, sobelX, sobelY, soberl_combined, canny]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()