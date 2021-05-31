from PIL import Image
from skimage.metrics import mean_squared_error as mse
from skimage.metrics import peak_signal_noise_ratio as psnr
import glymur
import numpy as np


def snr(reference_image, test_image):
    summation = np.sum(reference_image.astype('float') ** 2)

    pixels = float(reference_image.shape[0] * reference_image.shape[1])

    return 10 * np.log10(summation / (pixels * mse(reference_image, test_image)))


def print_lossy_metrics(reference_image, test_image):
    print('MSE:', mse(reference_image, test_image))
    print('SNR:', snr(reference_image, test_image), 'dB')
    print('PSNR', psnr(reference_image, test_image), 'dB')


# .gif87a-89a (Será implementado.)  .jpeg (OK!)  .jp2 (OK!)  .webp (Será implementado.)

bmp = Image.open('Images/C0001.bmp')

reference = np.array(bmp)

bmp.save('Images/Lossy/C0001.jpeg', optmize=True, quality=25)
# De acordo com a documentação, o parâmetro 'quality' - em compressões JPEG - deve ser utilizado em uma escala de
# 0 (pior) a 95 (melhor), de modo que quanto mais próximo o valor de 'quality' estiver de 0, maior será a compressão
# e a perda de dados.

jpeg = Image.open('Images/Lossy/C0001.jpeg')

test = np.array(jpeg)

print('\nJPEG\n')
print_lossy_metrics(reference, test)

jp2 = glymur.Jp2k('Images/Lossy/C0001.jp2', data=reference, cratios=[50])
# O parâmetro 'cratios' (Compression Ratios) atua de modo semelhante ao parâmetro 'quality', entretanto, com a escala
# de compressão invertida, isto é, para 'cratios = [1]', será produzida praticamente uma compressão sem perdas e para
# 'cratios > 1', será produzida uma compressão correspondente ao valor atribuído a este parâmetro. Por exemplo,
# 'cratios = [20]', determina que a imagem de referência deverá ser comprimida 20 vezes.

# Observação: Na biblioteca Glymur não se encontra especificado um limite superior para 'cratios'.

test = np.array(jp2[:])

print('\nJPEG 2000\n')
print_lossy_metrics(reference, test)
