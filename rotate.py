import cv2
import numpy as np

def custom_rotate(image, angle):
    if image is None:
        raise ValueError("Gelen görüntü 'None' olamaz.")
    rows, cols, _ = image.shape

    # Döndürme matrisini oluştur
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)

    # Görüntüyü döndür
    rotated_image = cv2.warpAffine(image, M, (cols, rows))

    return rotated_image
