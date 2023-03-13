#Histograma:
#Gráfico que mostra os canais de cores qao longo da imagem:
#Mostra a quantidade de vezes que uma cor aparece na imagem
#Tentar otimizar o código depois
import cv2
import matplotlib.pyplot as plt
#as plt: para se refirir à biblioteca para aplicar seus métodos

imagem = cv2.imread("imagem.jpg")

#Listas vazias para guardar canais de cor:
blue = []
red = []
green = []

for i in range(0, imagem.shape[0]):#Percorre as linhas
    for j in range(0, imagem.shape[1]):
        blue.append(imagem[i][j][0])
        red.append(imagem[i][j][0])
        green.append(imagem[i][j][0])

#Cria uma liosta para saber os valores sem repetir
blue_sem_repeticao = sorted(set(blue))#Organiza e tira repetição
red_sem_repeticao = sorted(set(red))
green_sem_repeticao = sorted(set(green))

tamanho_blue_1 = len(blue)
tamanho_red_1 = len(red)
tamanho_green_1 = len(green)

tamanho_blue_2 = len(blue_sem_repeticao)
tamanho_red_2 = len(red_sem_repeticao)
tamanho_green_2 = len(green_sem_repeticao)

resultado_blue = []
resultado_red = []
resultado_green = []

#2 laços para contagem da quantidade de cada num:
for i in range(0, tamanho_blue_2):
    soma = 0
    for j in range(0, tamanho_blue_1):
        if(blue_sem_repeticao[i] == blue[j]):
            soma += 1
    resultado_blue.append(soma)

print(resultado_blue)

for i in range(0, tamanho_red_2):
    soma = 0
    for j in range(0, tamanho_red_1):
        if(red_sem_repeticao[i] == red[j]):
            soma += 1
    resultado_red.append(soma)

print(resultado_red)

for i in range(0, tamanho_green_2):
    soma = 0
    for j in range(0, tamanho_green_1):
        if(green_sem_repeticao[i] == green[j]):
            soma += 1
    resultado_green.append(soma)

print(resultado_green)

#Plotar o gráfico:
plt.plot(resultado_blue, color='blue')
plt.plot(resultado_green, color='green')
plt.plot(resultado_red, color='red')
plt.show()