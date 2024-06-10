"""Main file of the project"""
from cli import load_image, save_image, parse_arguments
from operations.advanced import edge_detection, roberts_cross
from operations.basic import sharpen_image, blur_image
from operations.color import bw_image, lighten_image, darken_image, inverse_image
from operations.transform import rotate_image, mirror_image

def main():
    """Main function"""
    try:
        input_path, output_path, operations = parse_arguments()
        image_array = load_image(input_path)

        operation_map = {
            '--rotate': rotate_image,
            '--mirror': mirror_image,
            '--inverse': inverse_image,
            '--bw': bw_image,
            '--lighten': lighten_image,
            '--darken': darken_image,
            '--sharpen': sharpen_image,
            '--blur': blur_image,
            '--ed': edge_detection,
            '--rc': roberts_cross
        }

        for operation in operations:
            if len(operation) == 1:
                image_array = operation_map[operation[0]](image_array)
            elif len(operation) == 2:
                image_array = operation_map[operation[0]](image_array, operation[1])
        save_image(image_array, output_path)
        print("Image saved successfully to", output_path)
    except ValueError as e:
        print("Value error:", e)
    except TypeError as e:
        print("Type error:", e)

if __name__ == '__main__':
    main()
