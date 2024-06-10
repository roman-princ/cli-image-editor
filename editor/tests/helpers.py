"""Helpers for image manipulation."""
import numpy as np
from PIL import Image

def read_image(image_path):
    """Read an image from a file path and return it as a numpy array."""
    return np.asarray(Image.open(image_path), dtype=float)
