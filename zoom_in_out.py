import cv2
import numpy as np
def zoom_in_out(image, zoom_factor):
    """
    Görüntüyü belirli bir zoom faktörüyle yakınlaştırır veya uzaklaştırır.
    
    Args:
        image (numpy.ndarray): Görüntü.
        zoom_factor (float): Yakınlaştırma faktörü. 1.0'dan küçük bir değer uzaklaştırma, 1.0'den büyük bir değer ise yakınlaştırma yapar.
    
    Returns:
        numpy.ndarray: Yakınlaştırılmış veya uzaklaştırılmış görüntü.
    """
    # Görüntünün boyutlarını al
    height, width = image.shape[:2]

    # Zoom işlemi için yeni boyutları hesapla
    new_height = int(height * zoom_factor)
    new_width = int(width * zoom_factor)

   # Yakınlaştırma veya uzaklaştırma işlemini uygula
    zoomed_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    return zoomed_image
