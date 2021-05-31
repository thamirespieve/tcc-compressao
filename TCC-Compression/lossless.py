from PIL import Image
import os
import time


def compression_ratio(image):
    return os.stat(image[1]).st_size / os.stat(image[0]).st_size


def percentage_ratio(image):
    return (os.stat(image[0]).st_size - os.stat(image[1]).st_size) / os.stat(image[0]).st_size


def compression_factor(image):
    return os.stat(image[0]).st_size / os.stat(image[1]).st_size


def print_lossless_metrics(image):
    print('CR:', compression_ratio(image))
    print('PR:', 100 * percentage_ratio(image), '%')
    print('CF:', compression_factor(image))


bmp = Image.open('Images/C0001.bmp')

images = ['Images/C0001.bmp']

print('\nTamanho em KB da Imagem Original:', os.stat('Images/C0001.bmp').st_size / 1024)

start_time = time.time()
bmp.save('Images/Lossless/C0001.png')
t = time.time() - start_time

print('\nTempo de Compressão:', 1000 * t, 'milisegundos')

png = Image.open('Images/Lossless/C0001.png')

images.append('Images/Lossless/C0001.png')

print('\nTamanho em KB da Imagem Comprimida:', os.stat('Images/Lossless/C0001.png').st_size / 1024, '\n')

print_lossless_metrics(images)
