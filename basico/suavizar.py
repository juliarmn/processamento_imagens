import cv2
#Recortar a imagem:
#Perde parte da imagem
imagem = cv2.imread("imagem.jpg")
imagemRecortada = imagem[555:100, 100:500]#limita a imagem
cv2.imshow("Imagem Original", imagem)
cv2.imshow("Imagem Recortada", imagemRecortada)
cv2.waitKey(0)

#Redimensionando a imagem:
#Não perde a informação
#Sem arrumar a proporção, a imagem fica modificada:
imagem = cv2.imread("imagem.jpg")
largura_nova = 300
altura_nova = 500
imagem = cv2.resize(imagem, (largura_nova, altura_nova))
cv2.imshow("Imagem Original", imagem)
cv2.waitKey(0)
#Para não perder a proporção:
imagem = cv2.imread("imagem.jpg")
largura = imagem.shape[1]
altura = imagem.shape[0]
prop = float(altura/largura)#Definir a proporção da imagem
largura_nova = 90
altura_nova = int(largura_nova * prop)
imagem = cv2.resize(imagem, (largura_nova, altura_nova))
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)

#Rotacionando imagens:
imagem = cv2.imread("imagem.jpg")
rotacionada = imagem[:, ::-1]
#Usando ::-1 colocamos a lista de trás para frente->inverte os pixels das imagens
cv2.imshow("Imagem Rotacionada", rotacionada)#rotacionou no eixo x
cv2.waitKey(0)
#Rotacionar em y:
rotacionada = imagem[::-1, :]
#Rotacionar em ambos os eixos:
rotacionada = imagem[::-1, ::-1]