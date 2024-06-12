from editor.operations.basic import blur_image, sharpen_image
from editor.operations.advanced import edge_detection, roberts_cross
from editor.operations.color import bw_image, darken_image, lighten_image, inverse_image
from editor.operations.transform import mirror_image, rotate_image

class Operations:
    @staticmethod
    def sharpen_image(image):
        return sharpen_image(image)
    def blur_image(image):
        return blur_image(image)
    def edge_detection(image):
        return edge_detection(image)
    def roberts_cross(image):
        return roberts_cross(image)
    def bw_image(image):
        return bw_image(image)
    def darken_image(image, percentage):
        return darken_image(image, percentage)
    def lighten_image(image, percentage):
        return lighten_image(image, percentage)
    def inverse_image(image):
        return inverse_image(image)
    def mirror_image(image):
        return mirror_image(image)
    def rotate_image(image, angle):
        return rotate_image(image, angle) 