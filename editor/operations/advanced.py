"""Advanced image processing operations."""
import numpy as np
from scipy.signal import fftconvolve

def edge_detection(image_array):
    """Detect edges in an image using the Sobel operator."""
    sobel_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])

    sobel_y = np.array([[-1, -2, -1],
                        [ 0,  0,  0],
                        [ 1,  2,  1]])
    result = np.zeros_like(image_array, dtype=float)
    for z in range(image_array.shape[2]):
        grad_x = fftconvolve(image_array[..., z], sobel_x, mode='same')
        grad_y = fftconvolve(image_array[..., z], sobel_y, mode='same')
        result[..., z] = np.hypot(grad_x, grad_y)
    return np.clip(result / np.max(result) * 255, 0, 255).astype(np.uint8)

def roberts_cross(image_array):
    """Detect edges in an image using the Roberts Cross operator."""
    roberts_cross_1_kernel = np.array([
                            [1, 0],
                            [0, -1],
                            ])

    roberts_cross_2_kernel = np.array([
                            [0, 1],
                            [-1, 0],
                            ])
    result = np.zeros_like(image_array, dtype=float)
    for z in range(image_array.shape[2]):
        convolved_1 = fftconvolve(image_array[..., z], roberts_cross_1_kernel, mode='same')
        convolved_2 = fftconvolve(image_array[..., z], roberts_cross_2_kernel, mode='same')
        result[..., z] = np.sqrt(convolved_1**2 + convolved_2**2)
    return np.clip(result / np.max(result) * 255, 0, 255).astype(np.uint8)
