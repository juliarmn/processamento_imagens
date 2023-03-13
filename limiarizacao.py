import cv2
#limiarização
#Técnicas para visualizar melhor a imagem
imagem = cv2.imread("imagem.jpg")
print(imagem)

#Transforma todos os pixels da imagem em preto:
for i in range(0, imagem.shape[0]):
    for j in range(0, imagem.shape[1]):
        imagem[i][j] = (0, 0, 0)

fonte = cv2.FONT_HERSHEY_PLAIN

cv2.putText(imagem, 'Jua', (15, 67), fonte, 2, (255, 255, 255), 2)
cv2.putText(imagem, 'l', (15, 67), fonte, 2, (1,1,1), 2)#Quase preto -> difícil visualizar

#Fazer a limiarização:
#op 1:
for i in range(0, imagem.shape[0]):
    for j in range(0, imagem.shape[1]):
        if imagem[i][j][0] != 0: #and imagem[i][j][1] != 0 -> não precisa pois nesse caso todas são iguais
            imagem[i][j] = (255, 255, 255)#Verifica o que está escondido na imagem

cv2.imshow("Imagem", imagem)
cv2.waitKey(0)

#------------------------------------------Códigos separados----------------------------:

#Ou ocultar todos menos o que quero ver:
#op 2:
imagem = cv2.imread("imagem.jpg")
for i in range(0, imagem.shape[0]):
    for j in range(0, imagem.shape[1]):
        imagem[i][j] = (0, 0, 0)

fonte = cv2.FONT_HERSHEY_PLAIN

cv2.putText(imagem, 'Jua', (15, 67), fonte, 2, (255, 255, 255), 2)
cv2.putText(imagem, 'l', (15, 67), fonte, 2, (1, 1, 1), 2)
for i in range(0, imagem.shape[0]):
    for j in range(0, imagem.shape[1]):
        if imagem[i][j][0] == 1:
            imagem[i][j] = (255, 255, 255)#Verifica o que está escondido na imagem
        else:
            imagem[i][j] = (0, 0, 0)
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)