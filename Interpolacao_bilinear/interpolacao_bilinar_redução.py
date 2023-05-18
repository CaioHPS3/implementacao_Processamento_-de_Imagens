from PIL import Image
import numpy as np
import sys

# Vai pegar a imagem que eu passa pelo terminal
arquivo = sys.argv[1]

# Usando uma das funções que foram importada da biblioteca PIL vai abrir a abrir a imagem
imagem_original  = Image.open(arquivo)

# Utizando o metado convert transformamos a imagem original em tons de cinza 
imagem_cinza = imagem_original.convert('L')

# Pegando as porpoções da imagem 
largura, altura = imagem_cinza.size

#Transformando a imagem em uma tabela com a função .asarray
img_tabela = np.asarray(imagem_cinza)

# Criando uma tabela com medade do tamanho da imagem original 
reducao = np.resize(imagem_cinza, (int(altura/2), int(largura/2)))

# Percore toda a tabela
for l in range (0 , altura - 1, 2):
    for c in range(0, largura -1, 2):
        soma = 0
        soma += img_tabela[l, c]
        soma += img_tabela[l, c+1] # vizinho do lado direito
        soma += img_tabela[l+1, c] # vizinho de baixo
        soma += img_tabela[l+1, c+1] # vizinho da diagonal
        reducao[int(l/2), int(c/2)] = (soma / 4)

# Tranformando a tabela reducao em uma imagem 
nova_img = Image.fromarray(reducao)
# Salvando nova imagem reduzida
nova_img.save('redução:'+str(reducao.shape[0])+'x'+str(reducao.shape[1])+':'+arquivo)

