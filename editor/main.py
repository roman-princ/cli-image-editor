"""Main file of the project"""
from editor.cli import load_image, save_image, parse_arguments
from editor.operations.facade import Operations

def main():
    """Main function"""
    try:
        input_path, output_path, operations = parse_arguments()
        image_array = load_image(input_path)

        operation_map = {
            '--rotate': Operations.rotate_image,
            '--mirror': Operations.mirror_image,
            '--inverse': Operations.inverse_image,
            '--bw': Operations.bw_image,
            '--lighten': Operations.lighten_image,
            '--darken': Operations.darken_image,
            '--sharpen': Operations.sharpen_image,
            '--blur': Operations.blur_image,
            '--ed': Operations.edge_detection,
            '--rc': Operations.roberts_cross
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
