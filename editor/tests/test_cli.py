"""Test file for CLI"""
import unittest
import sys
from ..cli import parse_arguments

class TestCLI(unittest.TestCase):
    """Test the command line interface."""
    def test_check_args_valid(self):
        """Test the valid command line arguments."""
        sys.argv = ["--ed", "--rc", "--darken", "50", "test.png", "test.png"]
        try:
            parse_arguments()
            assert True
        except TypeError:
            assert False

    def test_check_args_more_than_two_files(self):
        """Test the invalid number of files."""
        sys.argv = ["--ed", "test.png", "test.jpg", "test.png"]
        try:
            parse_arguments()
            assert False
        except TypeError:
            assert True

    def test_check_args_missing_file_arg(self):
        """Test the missing file argument."""
        sys.argv = ["--bw", "output.jpg"]
        try:
            parse_arguments()
            assert False
        except ValueError:
            assert True

    def test_check_args_no_param_for_filters_with_params(self):
        """Test the missing parameter for filters with parameters."""
        sys.argv = ["--lighten", "test.jpg", "test.jpg"]
        try:
            parse_arguments()
            assert False
        except ValueError:
            assert True

    def test_check_args_invalid_output(self):
        """Test the invalid output path."""
        sys.argv = ["--bw", "--lighten", "50", "input.jpg", "output.png"]
        try:
            parse_arguments()
            assert False
        except TypeError:
            assert True

if __name__ == "__main__":
    unittest.main()
