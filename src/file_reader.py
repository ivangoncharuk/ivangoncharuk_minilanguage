
class FileReader:
    def __init__(self):
        self.current_char = None
        self.current_line = 1
        self.current_column = 0
        self.file_buffer = None
    
    def nextChar(self):
        pass

    def currentChar(self):
        return self.current_char

    def position(self):
        return f"{self.current_line}:{self.current_column}"

    
