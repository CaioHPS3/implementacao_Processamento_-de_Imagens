import cv2 as cv
from PIL import Image, ImageDraw
import numpy as np

def operacao_reflexao():
    print("\nOperação de reflexão/espelhamento!")
    nome_imagem = "carro.jpg"
    # Abre a imagem 
    imagem = Image.open(nome_imagem)
    
    # Aloca memória para a imagem e carrega os dados dos pixels                 
    imagem_pixels = imagem.load()     
                     
    # Cria uma nova imagem do tipo RGB com o tamanho da imagem que foi "aberta"
    # Uma nova pagina em "branco" com um modelo RGB definido 
    imagem_espelhada = Image.new("RGB", imagem.size)
    
    # Cria um objeto que pode ser usado para desenhar a imagem dada 
    # Permite que eu posso modificar aquela imagem "desenhar nela"
    # Vai ser a matriz que vai guardar o resultado da reflexão
    draw = ImageDraw.Draw(imagem_espelhada)        

    print(20*"---")
    print("Digite o número do espelhamento desejado: ")
    print(20*"---")
    print("1. Espelhamento horizontal")
    print("2. Espelhamento vertical")
    espelhamento_escolhido = int(input(''))

    if espelhamento_escolhido == 1:
        print("Espelhamento horizontal escolhido!")

        # Trabalha nas linhas da imagem
        for i in range(imagem_espelhada.width):
            for j in range(imagem_espelhada.height):
                # Pega o Ultimo pixel
                # Indo ate o pixel inicial em cada rotação
                xp = imagem.width - i - 1
                # Vai fazer o processo de "troca" colocando o ultimo (n-1, 0) pixel na posição inicial (0 ,0)
                # fazendo esse processo andando toda a linha.     
                draw.point((i, j), imagem_pixels[xp, j])

        imagem_espelhada.save(f"{nome_imagem}_imagem_espelhada_horizontal.png")
    # Trabalha nas colunas da imagem
    elif espelhamento_escolhido == 2:
        print("Espelhamento vertical escolhido!")

        for i in range(imagem_espelhada.width):
            for j in range(imagem_espelhada.height):
                jp = imagem.height - j- 1
                draw.point((i, j), imagem_pixels[i, jp])

        imagem_espelhada.save(f"{nome_imagem}_imagem_espelhada_vertical.png")                

    else:
        print("Número inválido. Tente novamente!")
        operacao_reflexao()

    print('imagem_espelhada.height: ', imagem_espelhada.height)
    print('imagem_espelhada.width: ', imagem_espelhada.width)

def menu():
    operacao_reflexao() 
menu()