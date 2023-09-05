# tests/test_file_reader.py

import unittest
from src.file_reader import FileReader

class TestFileReader(unittest.TestCase):
  
    def test_nextChar(self):
        reader = FileReader()
        reader.load_file('test_file1.txt')  # Assuming this file contains 'Hello'
        
        reader.nextChar()
        self.assertEqual(reader.currentChar(), 'H')
        
        reader.nextChar()
        self.assertEqual(reader.currentChar(), 'e')
        
        reader.nextChar()
        self.assertEqual(reader.currentChar(), 'l')
        
        #todo add tests to check for End-of-Text (ETX)
        
        
    def test_currentChar(self):
        reader = FileReader()
        reader.load_file('test_file1.txt')
        
        reader.nextChar()
        self.assertEqual(reader.currentChar(), 'H')
        
        reader.nextChar()
        self.assertEqual(reader.currentChar(), 'e')


    def test_position(self):
        reader = FileReader()
        reader.load_file('test_file1.txt')
        
        reader.nextChar()
        self.assertEqual(reader.position(), '1:1')
        
        reader.nextChar()
        self.assertEqual(reader.position(), '1:2')
        
