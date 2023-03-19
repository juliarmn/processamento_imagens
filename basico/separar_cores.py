import cv2
#Imprime de só uma cor (nos locais de sua influência), no caso, o vermelho:
imagem = cv2.imread("imagem.jpg")
for i in range(0, imagem.shape[0]):
    for j in range(0, imagem.shape[1]):
        imagem[i][j][0] = 0
        imagem[i][j][1] = 0
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)

#Pode fazer com todos, o B, G e R
imagem = cv2.imread("imagem.jpg")
(B, G, R) = cv2.split(imagem)#Separa a imagem em suas cores ->matriz tridimensional vira uma matriz única sem misturar suas cores
cv2.imshow("Imagens", B)
cv2.waitKey(0)
cv2.imshow("Imagens", G)
cv2.waitKey(0)
cv2.imshow("Imagens", R)
cv2.waitKey(0)
#Não sai imagem  colorida -> mais azul = branco, menos azul = preto