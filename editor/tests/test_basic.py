"""Simple operations for image processing."""
import unittest
import numpy as np
from numpy.testing import assert_almost_equal
from editor.operations.facade import Operations
from editor.cli import load_image

class TestBasicOperations(unittest.TestCase):
    """Test the basic operations."""
    def setUp(self):
        """Set up the image for the tests."""
        self.image = load_image("tests/img/kendrick.png")

    def test_sharpen_image(self):
        """Test the sharpen image operation."""
        sharpened = np.array(Operations.sharpen_image(self.image))
        expected = load_image("tests/img/sharpen.png")
        assert_almost_equal(sharpened, expected)

    def test_blur_image(self):
        """Test the blur image operation."""
        blurred = np.asarray(Operations.blur_image(self.image))
        expected = load_image("tests/img/blured.png")
        assert_almost_equal(blurred, expected)

if __name__ == '__main__':
    unittest.main()
