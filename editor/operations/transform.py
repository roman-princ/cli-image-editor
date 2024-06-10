"""Operations to transform images"""
import numpy as np

def rotate_image(image_array, degrees):
    """Rotate an image by 90, 180, or 270 degrees"""
    if degrees == 90:
        return np.rot90(image_array, k=3)
    if degrees == 180:
        image_array = np.rot90(image_array, k=3)
        return np.rot90(image_array, k=3)
    if degrees == 270:
        image_array = np.rot90(image_array, k=3)
        image_array = np.rot90(image_array, k=3)
        return np.rot90(image_array, k=3)
    raise ValueError("Degrees must be 90, 180, or 270")

def mirror_image(image_array):
    """Mirror an image horizontally"""
    return np.fliplr(image_array)
