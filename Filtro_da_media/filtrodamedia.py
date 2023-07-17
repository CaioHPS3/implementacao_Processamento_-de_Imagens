import sys
import numpy as np
from PIL import Image as pl

# Recebe o arquivo da imagem original
file_name = sys.argv[1];

# Abri a imagem
img_color = pl.open(file_name)

# Converte imagem colorida para escala de cinza
img_gray = img_color.convert('L')

# Pega as dimensões da imagem
width, height = img_gray.size

# Pega a imagem em formato de matriz
imgprincipal = np.asarray(img_gray)

# Salva a imagem em escala de cinza
mat2img = pl.fromarray(imgprincipal)
mat2img.save('cinza-' + file_name)

# Matriz onde ficará o resultado do processo
final = imgprincipal.copy()

# Aplica o filtro da média com tratamento de borda usando padding com zeros
for i in range(1, height - 1):
    for j in range(1, width - 1):
        temp = 0
        temp += imgprincipal[i - 1, j - 1]
        temp += imgprincipal[i - 1, j]
        temp += imgprincipal[i - 1, j + 1]
        temp += imgprincipal[i, j - 1]
        temp += imgprincipal[i, j]
        temp += imgprincipal[i, j + 1]
        temp += imgprincipal[i + 1, j - 1]
        temp += imgprincipal[i + 1, j]
        temp += imgprincipal[i + 1, j + 1]
        final[i, j] = int(temp / 9)

# Preenche a primeira e última linha da imagem filtrada com zeros
final[0, :] = 0
final[height - 1, :] = 0

# Preenche a primeira e última coluna da imagem filtrada com zeros
final[:, 0] = 0
final[:, width - 1] = 0

mat2img = pl.fromarray(final)
mat2img.save('mean-filter-' + file_name)
