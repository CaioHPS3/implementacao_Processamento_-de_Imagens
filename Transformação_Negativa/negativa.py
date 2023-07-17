import sys
import cv2 as cv
import numpy as np
from PIL import Image as Img

# Pegar a imagem passada
file_name = sys.argv[1]

# Abre a imagem para poder fazer a modificações 
img = Img.open(file_name)

# Pega as dimenções da imagem passada
width, height = img.size

# Converte a imagem para uma escala de cinza
img_cinza = img.convert('L')

# Converte a imagem para um formato de arres gerando uma matriz
img2mat = np.asarray(img_cinza)

# Salva imagem preto e branco
mat2img = Img.fromarray(img2mat)
mat2img.save('BW-'+file_name)

# Cria uma copia da imagem da imagem em formato de matriz
final = img2mat.copy()

for i in range(height):
    for j in range(width):
        # Fazendo a inverção pixel a pixel
        final[i,j] = int( 256 - 1 - img2mat[i,j] )


mat2img = Img.fromarray(final)
mat2img.save('negativo-'+file_name)