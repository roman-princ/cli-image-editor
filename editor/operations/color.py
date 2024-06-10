"""Operations for color manipulation"""
import numpy as np

def inverse_image(image_array):
    """Invert the colors of an image"""
    return 255 - image_array

def bw_image(image_array):
    """Convert an image to black and white"""
    grayscale = np.dot(image_array[...,:3], [0.2989, 0.5870, 0.1140])
    return np.stack((grayscale,)*3, axis=-1).astype(np.uint8)

def lighten_image(image_array, percentage):
    """Lighten an image by a percentage value"""
    if percentage < 0 or percentage > 100:
        raise ValueError("Percentage must be in the range 0 - 100")
    factor = 1 + (percentage / 100.0)
    return np.clip(image_array * factor, 0, 255).astype(np.uint8)

def darken_image(image_array, percentage):
    """Darken an image by a percentage value"""
    if percentage < 0 or percentage > 100:
        raise ValueError("Percentage must be in the range 0 - 100")
    factor = 1 - (percentage / 100.0)
    return np.clip(image_array * factor, 0, 255).astype(np.uint8)
