import numpy as np

def custom_gray_conversion(image):
    # Görüntünün boyutlarını al
    height, width = image.shape

    # Siyah beyaz görüntü için bir boş matris oluştur
    bw_image = np.zeros((height, width), dtype=np.uint8)

    # Her pikselin gri tonlamalı değerini hesapla ve siyah beyaz görüntü matrisine ata
    for i in range(height):
        for j in range(width):
            # Gri tonlamalı değeri al
            gray_value = image[i, j]

            # Eşik değeri belirle (örneğin, 128)
            threshold = 128

            # Gri tonlamalı değere göre pikseli siyah veya beyaz yap
            if gray_value >= threshold:
                bw_image[i, j] = 255  # Beyaz
            else:
                bw_image[i, j] = 0    # Siyah

    return bw_image