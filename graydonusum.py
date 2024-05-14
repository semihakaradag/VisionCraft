import numpy as np

def custom_gray_conversion(image):
    # Görüntünün boyutlarını al
    height, width, _ = image.shape

    # Gri tonlamalı görüntü için bir boş matris oluştur
    gray_image = np.zeros((height, width), dtype=np.uint8)

    # Her pikselin gri tonlamalı değerini hesapla ve gri tonlamalı görüntü matrisine ata
    for i in range(height):
        for j in range(width):
            # Görüntünün her pikselinin renk kanallarını al
            b, g, r = image[i, j]

            # Gri tonlamalı değeri hesapla ve gri tonlamalı görüntüye ata
            gray_value = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
            gray_image[i, j] = gray_value

    return gray_image




