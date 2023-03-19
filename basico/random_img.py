import numpy as np
from matplotlib import pyplot as plt
from skimage import img_as_float
from skimage import io

#Gera imagem aleatória
random_img = np.random.random([300, 300])
plt.imshow(random_img)
#Valores float
print(random_img)
#Valores mínimos e máximo
print(random_img.min(), random_img.max())
#Observe que os valores estão entre 0 e 1

imagem = io.imread("imagem.jpg")
plt.show(imagem)
imagem_float = img_as_float(imagem)
print(imagem_float.min(), imagem_float.max())
