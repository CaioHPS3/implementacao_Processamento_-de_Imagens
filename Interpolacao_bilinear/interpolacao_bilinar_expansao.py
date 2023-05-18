from PIL import Image
import numpy as np
import sys

# Vai pegar a imagem que eu passa pelo terminal
arquivo = sys.argv[1]

# Usando uma das funções que foram importada da biblioteca PIL vai abrir a abrir a imagem
imagem_original = Image.open(arquivo)

# Utizando o metado convert transformamos a imagem original em tons de cinza 
imagem_cinza = imagem_original.convert('L')

# Pegando as porpoções da imagem 
largura, altura = imagem_cinza.size

#Transformando a imagem em uma tabela com a função .asarray
img_tabela = np.asarray(imagem_cinza)

# Criando uma tabela com o doblo do tamanho da imagem original 
expansao = np.resize(imagem_cinza, (altura*2, largura*2))

# copia os pixels da foto original para a matriz extendida, sem colocar pixel nos elementos (i, j+1), (i+1), (i+1, j+1)
for l in range(0, altura-1):
    for c in range(0, largura-1):
        expansao[l*2, c*2] = img_tabela[l,c]


# para cada pixel (i, j), aplicada a regra de interpolação bilinear nos elementos
# (i, j+1), (i+1, j), (i+1, j+1), (i+1, j+2), (i+2, j+1)
for l in range(0, altura*2-1, 2):
    for c in range(0, largura*2-1, 2):
        x = 0
        x += expansao[l, c]
        x += expansao[l, c+1]
        expansao[l,c+1] = (x/2)     # a

        x = 0
        x += expansao[l, c]
        x += expansao[l+1, c]
        expansao[l+1,c] = (x/2)     # b

        x = 0
        x += expansao[l, c]
        x += expansao[l, c+1]
        x += expansao[l+1, c]
        x += expansao[+1, c+1]
        expansao[l+1,c+1] = (x/4)   # c

        x = 0
        x += expansao[l, c+1]
        x += expansao[l+1, c+1]
        if c+2 <= largura*2-1:
            expansao[l+1,c+2] = (x/2)   # d

        x = 0
        x += expansao[l+1, c]
        x += expansao[l+1, c+1]
        if l+2 <= altura*2-1:
            expansao[l+2,c+1] = (x/2)     # e

# Tranformando a tabela expansao em uma imagem 
nova_img = Image.fromarray(expansao)

# Salvando nova imagem expandida
nova_img.save('Expansão:'+str(expansao.shape[0])+'x'+str(expansao.shape[1])+':'+arquivo)