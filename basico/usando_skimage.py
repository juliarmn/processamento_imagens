#Programa para ler imagens com skimage
from skimage import io
imagem = io.imread("imagem.jpg")
print(imagem)
#Assim, ele imprime os dados da imagem no terminal