"""Advanced operations tests."""
import unittest
import numpy as np
from editor.operations.facade import Operations
from editor.cli import load_image

class TestAdvancedOperations(unittest.TestCase):
    """Test the advanced operations."""
    def setUp(self):
        """Set up the image for the tests."""
        self.image = load_image("tests/img/kendrick.png")

    def test_edge_detection(self):
        """Test the edge detection operation."""
        ed = np.array(Operations.edge_detection(self.image))
        excepted = load_image("tests/img/edge_detection.png")
        np.testing.assert_almost_equal(ed, excepted)

    def test_roberts_cross(self):
        """Test the roberts cross operation."""
        rc = np.array(Operations.roberts_cross(self.image))
        excepted = load_image("tests/img/rc.png")
        np.testing.assert_almost_equal(rc, excepted)
