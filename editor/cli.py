"""Logic for processing the input from CLI"""
import sys
import os
from PIL import Image
import numpy as np

def load_image(path):
    """Loads the image from path variable"""
    image = Image.open(path)
    return np.array(image)

def save_image(image_array, path):
    """Saves the image into the path variable"""
    image = Image.fromarray(image_array.astype(np.uint8))
    image.save(path)

def check_args(args):
    """Validates the arguments"""
    if len(args) < 3:
        raise ValueError("Invalid number of arguments")
    input_path = args[-2]
    output_path = args[-1]
    if not (input_path.endswith('.jpg') or input_path.endswith('.png')):
        raise TypeError("Invalid input image format (only .jpg or .png are supported)")
    if not (output_path.endswith('.jpg') or output_path.endswith('.png')):
        raise TypeError("Invalid input image format (only .jpg or .png are supported)")

    input_ext = os.path.splitext(input_path)[1]
    output_ext = os.path.splitext(output_path)[1]
    if input_ext != output_ext:
        raise TypeError("Input and output image formats do not match")

def parse_arguments():
    """Parses the CLI arguments"""
    args = sys.argv[1:]
    check_args(args)
    input_path = args[-2]
    output_path = args[-1]
    operations = []
    i = 0
    while i < len(args) - 2:
        if args[i] in ['--mirror', '--inverse', '--bw', '--sharpen', '--blur', '--ed', '--rc']:
            operations.append((args[i],))
        elif args[i] in ['--lighten', '--darken', '--rotate']:
            assert int(args[i + 1]) >= 0
            operations.append((args[i], int(args[i + 1])))
            i += 1
        else:
            raise TypeError("Invalid operation")
        i += 1
    return input_path, output_path, operations
