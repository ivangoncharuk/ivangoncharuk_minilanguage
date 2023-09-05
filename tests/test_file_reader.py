import unittest

from src.file_reader import FileReader

input_file = "test_input_file.txt"

class TestFileReader(unittest.TestCase):
    def test_nextChar(self):
        fr = FileReader(input_file)
        fr.nextChar()
        # testing that currentChar is the first char of the file
        self.assertEqual(fr.currentChar(), 'H')

    def test_currentChar(self):

        fr = FileReader(input_file)
        fr.nextChar()
        self.assertEqual(fr.currentChar(), 'H')

    def test_position(self):
        fr = FileReader(input_file)
        fr.nextChar()
        # Test position
        self.assertEqual(fr.position(), "1:1")

    def test_file_not_found_exception(self):
        # Test file not found exception
        with self.assertRaises(FileNotFoundError):
            fr = FileReader("non_existent_file.txt")
