"""Basic operations for image processing."""
import numpy as np
from scipy.signal import fftconvolve

def sharpen_image(image_array):
    """Sharpen an image using a sharpening kernel."""
    kernel = np.array([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])
    result = np.zeros_like(image_array, dtype=float)

    for z in range(image_array.shape[2]):
        result[..., z] = fftconvolve(image_array[..., z], kernel, mode='same')
    return np.clip(result, 0, 255).astype(np.uint8)

def blur_image(image_array):
    """Blur an image using a Gaussian 3x3 blur kernel."""
    kernel = np.array([[1, 2, 1],
                       [2, 4, 2],
                       [1, 2, 1]]) * (1/16)
    result = np.zeros_like(image_array, dtype=float)

    for z in range(image_array.shape[2]):
        result[..., z] = fftconvolve(image_array[..., z], kernel, mode='same')

    return np.clip(result, 0, 255).astype(np.uint8)
