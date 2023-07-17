import cv2 as cv
import random
from PIL import Image

def binarizar(img, threshold):
    binarizada = img
    for i in range(width):
        for j in range(height):
            R, G, B = img.getpixel((i, j))
            if ( (R + G + B) / 3 <= threshold):
                # regions
                binarizada.putpixel((i, j), (0, 0, 0))
            else:
                # backgrond
                binarizada.putpixel((i, j), (255, 255, 255))
    return binarizada

image_file_name = "imagem.jpeg"
original_image = Image.open(image_file_name)
width, height = original_image.size
print('------- Dimensões da imagem:')
print("------> Altura: ", height)
print("------> Largura: ", width)


#Transforma a imagem original em uma imagem binária
binarizada_image = binarizar(original_image, 127)

# Salvar imagem binarizada
binarizada_image.save(f'binaria-{image_file_name}')

img = cv.imread('binaria-'+image_file_name)
cv.imshow('Imagem Binarizada', img)
cv.waitKey()
cv.destroyAllWindows()

# Copia matrix para rotulação
labeling = binarizada_image
case1 = 0
case2 = 0
case3 = 0
case4 = 0

for i in range(1, width):
    for j in range(1, height):
        s = binarizada_image.getpixel((i - 1, j))
        r = binarizada_image.getpixel((i, j - 1))
        p = binarizada_image.getpixel((i, j))

        # Se p for preto ele vai passa direto 
        if p != (255, 255, 255):

            # case 4
            # Os pixels vizinhos são pretos e têm rótulos diferentes.
            # O que significa que as regiões rotuladas se encontraram.
            # Nesse caso, os rótulos são combinados e a nova região é rotulada com o menor número de rótulo.
            if (s != (255, 255, 255) and r != (255, 255, 255)) and (labeling.getpixel((i - 1, j)) != labeling.getpixel((i, j - 1))):
                case4 += 1
                labeling.putpixel( (i, j), labeling.getpixel((i, j - 1)) )
                labeling.putpixel( (i-1, j), labeling.getpixel((i, j - 1)) )

            # case 3
            # Os pixels vizinhos são pretos e têm o mesmo rótulo,
            # O que significa que o pixel atual pertence à mesma região que seus vizinhos pretos.
            elif (s != (255, 255, 255) and r != (255, 255, 255)) and (labeling.getpixel((i - 1, j)) == labeling.getpixel((i, j - 1))):
                case3 += 1
                labeling.putpixel( (i, j), labeling.getpixel((i, j - 1)) )

            # case 2
            # Um dos pixels vizinhos é preto e o outro é branco,
            # O que significa que o pixel atual está na borda de uma região.
            # Nesse caso, o pixel atual recebe o rótulo do pixel vizinho preto.
            elif s != (255, 255, 255) or r != (255, 255, 255):
                case2 += 1
                if s != (255, 255, 255):
                    labeling.putpixel((i, j), labeling.getpixel((i - 1, j)))
                elif r != (255, 255, 255):
                    labeling.putpixel((i, j), labeling.getpixel((i, j - 1)))

            # case 1
            # Os pixels vizinhos são brancos e o pixel atual também é branco,
            # o que significa que o pixel atual não faz parte de nenhuma região rotulada anteriormente.
            # Nesse caso, um novo rótulo é atribuído ao pixel atual.
            elif s != (0, 0, 0) and r != (0, 0, 0):
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)

                labeling.putpixel((i, j), (r, g-50, b))
                case1 += 1

# Salvar imagem rotulada
labeling.save('rotulada-'+image_file_name)
print('case1:', case1)
print('case2:', case2)
print('case3:', case3)
print('case4:', case4)

# using opencv to open image
img = cv.imread('rotulada-'+image_file_name)
cv.imshow('Imagem Rotulada', img)
cv.waitKey() 
cv.destroyAllWindows()