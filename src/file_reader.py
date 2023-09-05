
class FileReader:
    def __init__(self, filename):
        self.filename = filename
        self.currentLine = 1
        self.currentColumn = 0
        self.currentCharVal = None  # Initialize to None, will change when `nextChar` is called
        try:
            self.file = open(filename, "r")
        except FileNotFoundError:
            raise FileNotFoundError("The file does not exist.")

    def nextChar(self):
        """ Reads the next character in the input file. """
        next_char = self.file.read(1)
        if not next_char:
            self.currentCharVal = "ETX"  # End of Text
        else:
            if next_char == '\n':
                self.currentLine += 1
                self.currentColumn = 0
                self.currentCharVal = " "  # replace newlines with space as per the requirements
            else:
                self.currentColumn += 1
                self.currentCharVal = next_char

    def currentChar(self):
        """ Returns a string containing the character that was just read. """
        return self.currentCharVal

    def position(self):
        """ Returns a string containing the line and column integers separated by a colon character. """
        return f"{self.currentLine}:{self.currentColumn}"

