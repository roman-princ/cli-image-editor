"""Tests for color manipulation."""
import unittest
import numpy as np
from editor.operations.facade import Operations
from ..cli import load_image

class TestColorOperations(unittest.TestCase):
    """Test the color operations."""
    def setUp(self):
        """Set up the image for the tests."""
        self.image = load_image("tests/img/kendrick.png")


    def test_inverse_image(self):
        """Test the inverse image operation."""
        inversed = np.array(Operations.inverse_image(self.image))
        expected = load_image("tests/img/inverse.png")
        np.testing.assert_almost_equal(inversed, expected)

    def test_bw_image(self):
        """Test the black and white image operation."""
        bw = np.array(Operations.bw_image(self.image))
        excepted = load_image("tests/img/bw.png")
        np.testing.assert_almost_equal(bw, excepted)

    def test_lighten_image(self):
        """Test the lighten image operation."""
        try:
            Operations.lighten_image(self.image, 101)
        except ValueError:
            pass

        try:
            Operations.lighten_image(self.image, -1)
        except ValueError:
            pass
        lightened = np.array(Operations.lighten_image(self.image, 50))
        expected = load_image("tests/img/lighten50.png")
        np.testing.assert_almost_equal(lightened, expected)

    def test_darken_image(self):
        """Test the darken image operation."""
        try:
            Operations.darken_image(self.image, 101)
        except ValueError:
            pass

        try:
            Operations.darken_image(self.image, -1)
        except ValueError:
            pass

        darkened = np.array(Operations.darken_image(self.image, 50))
        expected = load_image("tests/img/darken50.png")
        np.testing.assert_almost_equal(darkened, expected)

if __name__ == '__main__':
    unittest.main()
