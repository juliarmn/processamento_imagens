import cv2

imagem = cv2.imread("imagem.jpg")#BGR - open cv
print(imagem)
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)

#Alterando valores de pixels:
imagem[0][0] = (255, 255, 255) #tupla
#todos 255: cor branca
#Modifica só 1 pixel

#Mudar mais de um pixel
imagem[0:10, 0:10] = (255, 255, 255)
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)

#Alterar dinamicamente os pixels com estruturas de repetição:
branco = (255, 255, 255)
preto = (0, 0, 0)
for i in range(0, imagem.shape[0]):
  for j in range(0, imagem.shape[1]):
    imagem[i][j] = branco
#Todos os pixels brancos:
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)

#Pulando de 10 em 10 pixels:
#No caso, como modificamos a imagem anteriormente, ficam pontos pretos na imagem branca
#Se não tivéssemos trocado a imagem por branco, seria na imagem original
for i in range(0, imagem.shape[0], 10):
  for j in range(0, imagem.shape[1], 10):
    imagem[i][j] = preto
#Todos os pixels brancos:
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)

#Só mexendo na altura:
for i in range(0, imagem.shape[0], 10):
  for j in range(0, imagem.shape[1]):
    imagem[i][j] = preto
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)

#Só mexendo na largura:
for i in range(0, imagem.shape[0]):
  for j in range(0, imagem.shape[1], 10):
    imagem[i][j] = preto
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)

#Observe que formaram quadradinhos

imagem = cv2.imread("imagem.jpg")#BGR - open cv
print(imagem)

#Outra forma:
for i in range(0, imagem.shape[0], 10):
  for j in range(0, imagem.shape[1], 10):
    #Aumenta o tamanho dos quadradinhos formados:
    imagem[i:i+5, j:j+5] = branco
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)

#A partir de condições:
imagem = cv2.imread("imagem.jpg")#BGR - open cv
print(imagem)
for i in range(0, imagem.shape[0], 10):
  for j in range(0, imagem.shape[1], 10):
    #Lembre que open cv é BGR
    #Aonde for azul puro fica branco->pontos brancos na imagem
    if(imagem[i][j][0] == 255):
      imagem[i][j] = branco
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)

#Escrevendo texto em cima da imagem:
#Usa um método do open cv
imagem = cv2.imread("imagem.jpg")#BGR - open cv
fonte = cv2.FONT_HERSHEY_PLAIN#Fonte da palavra
cv2.putText(imagem, "Jua", (50, 50), fonte, 2, (255,255,255), 2)#imagem, texto, pixel onde inicia, fonte, expessura, cor, tamanho
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)

#Desenho da escrita bem pixelado, para arrumar:
cv2.putText(imagem, "Jua", (50, 50), fonte, 2, (255,255,255), 2, cv2.LINE_AA)