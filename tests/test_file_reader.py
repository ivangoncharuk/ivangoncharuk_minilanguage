import unittest

from src.file_reader import FileReader

class TestFileReader(unittest.TestCase):

    def test_nextChar(self):
        fr = FileReader("some_input_file.txt")
        fr.nextChar()
        # testing that currentChar is the first char of the file
        self.assertEqual(fr.currentChar(), "Expected first character")

    def test_currentChar(self):

        fr = FileReader("some_input_file.txt")
        fr.nextChar()
        self.assertEqual(fr.currentChar(), "Expected first character")

    def test_position(self):
        fr = FileReader("some_input_file.txt")
        fr.nextChar()
        # Test position
        self.assertEqual(fr.position(), "1:1")

    def test_file_not_found_exception(self):
        # Test file not found exception
        with self.assertRaises(FileNotFoundError):
            fr = FileReader("non_existent_file.txt")
