import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread("imagem.jpg")
print(img.min(), img.max())
print(img)
blue = [255, 0, 0]
cv2.rectangle(img, (300, 600), (600, 300), blue, -1)
cv2.imshow("Imagem", img)
cv2.waitKey(0)