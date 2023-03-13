import cv2
import numpy as np

#numpy cria vetores
dark_red = np.array([60, 0, 90], dtype="uint8")#dtype = tipo de dado
light_red = np.array([60, 100, 255], dtype="uint8")

camera = cv2.VideoCapture(0)#referencia a webcam

#Não sabemos quando a câmera para de gravar:
while True:
    (existe, frame) = camera.read()
    if not existe:
        break

    objeto = cv2.inRange(frame, dark_red, light_red)#mantém apenas as cores escolhidas(FICA BRANCO) e deixa as outras pretas
    #identificar os contornos:
    (contornos, _) = cv2.findContours(objeto.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #o _ é para pular a posição
    #RETR_TREE: hierarquia entre os elementos
    #CHAIN_APPROX_SIMPLE: apenas pega os contornos principais (otimizar)

    tamanho = len(contornos)

    if tamanho > 0:#Se tem um contorno
        #Organiza as informações em ordem decresente:
        contorno = sorted(contornos, key = cv2.contourArea, reverse = True)[0]
        retangulo = np.int32(cv2.boxPoints(cv2.minAreaRect(contorno)))
        #Desenhar todos os contornos:
        cv2.drawContours(frame, [retangulo], -1, (255, 0, 0))


    cv2.imshow("Imagem", frame)
    cv2.imshow("Objeto", objeto)
    if cv2.waitKey(1) & 0xFF == ord("e"):#Quando apertar a tecla "e" (exit), consigo sair
        break
#Desliga a câmera e destrói as janelas abertas
camera.release()
cv2.destroyAllWindows()