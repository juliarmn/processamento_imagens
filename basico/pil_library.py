from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = Image.open("imagem.jpg")
print(type(img))

#Mostrar a imagem
#img.show()

#extensão da imagem:
print(img.format)

#Tipo: numpy array
img_1 = np.asarray(img)
print(type(img_1))

#####################################
#Usando o matplotlib
imagem = mpimg.imread("imagem.jpg")
print(type(imagem))
print(imagem.shape)
#plt.imshow(imagem)
#plt.colorbar()