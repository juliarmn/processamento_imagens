#Uma imagem é composta por 3 canais de cores:
#RGB(Red, Green and Blue)
import cv2
#0: nada da cor
#255: maximo da cor
#Uso de listas para representar as cores:
[255, 0, 0]#Forma a cor vermelha
[0, 255, 0]#forma a cor verde
[0, 0, 255]#Forma a cor azul
#A imagem será uma matriz em que para cada pixel, teremos um valor RGB
#É uma matriz tridimensional
#Método imread() -> cv2:
#Pega a imagem e transforma ela em uma matriz tridimensional RGB

#imagem.jpg -> mesmo diretório:
#Achar o diretorio atual da imagem, caso precise:
import os
cwd = os.getcwd()
cwd

imagem = cv2.imread("imagem.jpg")#BGR - open cv
print(imagem)

cv2.imshow("Imagem", imagem)#Mostra a imagem muito rapidamente
cv2.waitKey(0)#Permite a visualização da imagem até uma tecla ser apertada
cv2.destroyAllWindows()
#Mostrar de 3 em 3 o valor de cada pixel da imagem:
#Extração de cada pixel
for i in range(0, imagem.shape[0]):
  for j in range(0, imagem.shape[1]):
    print(imagem[i][j])

#Extração de cada canal de imagem:
for i in range(0, imagem.shape[0]):
  for j in range(0, imagem.shape[1]):
    for h in range(0, 3):
      print(imagem[i][j][h])

#shape[0], shape[1], shape[2]:
#Imagens preto e branco tem menos canais de cor, por exemplo
#shape[0]: altura em pixel da imagem
#shape[1]: largura da imagem em pixel
#shape[2]: canais de cores
print(imagem.shape[0])
print(imagem.shape[1])
print(imagem.shape[2])