"""This module contains tests for the transform operations in the operations module."""
import unittest
import numpy as np
from ..operations.transform import rotate_image, mirror_image
from ..cli import load_image

class TestTransformOperations(unittest.TestCase):
    """Test the transform operations."""
    def setUp(self):
        """Set up the image for the tests."""
        self.image = load_image("tests/img/kendrick.png")

    def test_rotate_image(self):
        """Test the rotate image operation."""
        rotated90 = np.array(rotate_image(self.image, 90))
        expected90 = load_image("tests/img/rot90.png")
        np.testing.assert_array_equal(rotated90, expected90)

        rotated180 = np.array(rotate_image(self.image, 180))
        expected180 = load_image("tests/img/rot180.png")
        np.testing.assert_array_equal(rotated180, expected180)

        rotated270 = np.array(rotate_image(self.image, 270))
        expected270 = load_image("tests/img/rot270.png")
        np.testing.assert_array_equal(rotated270, expected270)

    def test_mirror_image(self):
        """Test the mirror image operation."""
        mirrored = np.array(mirror_image(self.image))
        expected = load_image("tests/img/mirror.png")
        np.testing.assert_array_equal(mirrored, expected)

if __name__ == '__main__':
    unittest.main()
