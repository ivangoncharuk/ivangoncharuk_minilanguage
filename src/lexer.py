class Token:
    def __init__(self, kind: str, value=None, position=None):
        self.kind = kind
        self.value = value
        self.position = position

    def __str__(self):
        position = f"({self.position[0]}:{self.position[1]})" if self.position else "(Unknown Position)"
        value = f": {self.value}" if self.value is not None else ""
        return f"{position} {self.kind}{value}"


class Lexer:
    def __init__(self, input_text: str):
        self.input_text = input_text
        self.current_char = self.input_text[0] if self.input_text else None
        self.line_number = 1
        self.char_number = 1
        self.index = 0
        self.current_token = None
        self.keywords = {'program', 'if', 'then', 'end', 'do', 'while',
                         'print', 'else', 'int', 'bool', "and", "or", "not"}

    def next_char(self):
        """Move to the next character in the input text."""
        if self.current_char:
            if self.current_char == "\n":
                self.line_number += 1
                self.char_number = 1
            else:
                self.char_number += 4 if self.current_char == "\t" else 1
            self.index += 1
            self.current_char = self.input_text[self.index] if self.index < len(self.input_text) else None

    def peek_char(self) -> str:
        """Look at the next character in the input text without moving the current position."""
        peek_index = self.index + 1
        return self.input_text[peek_index] if peek_index < len(self.input_text) else None

    def kind(self):
        return self.current_token.kind if self.current_token else None

    def value(self):
        return self.current_token.value if self.current_token else None

    def position(self):
        return self.current_token.position if self.current_token else None

    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.next_char()

    def read_identifier_or_keyword(self):
        """
        Read an identifier or keyword from the input text.
        Identifiers can include alphanumeric characters and underscores.
        """
        start_index = self.index
        while self.current_char and (self.current_char.isalnum() or self.current_char == "_"):
            self.next_char()

        identifier = self.input_text[start_index:self.index]
        position = (self.line_number, self.char_number - len(identifier))
        return Token("ID", value=identifier, position=position) if identifier not in self.keywords else Token(identifier, position=position)

    def read_number(self):
        """
        Read a number from the input text.
        """
        start_index = self.index
        while self.current_char and self.current_char.isdigit():
            self.next_char()

        number = self.input_text[start_index:self.index]
        position = (self.line_number, self.char_number - len(number))
        return Token("NUM", value=int(number), position=position)

    def read_symbol(self):
        """
        Read a single character symbol from the input text.
        Handles multi-character symbols like ':='.
        Raises a SyntaxError for illegal token '***'.
        """
        start_line, start_char = self.line_number, self.char_number

        if self.current_char == '*' and self.input_text[self.index+1:self.index+4] == '**':
            error_msg = f"Illegal token '***' at position ({start_line}, {start_char})"
            raise SyntaxError(error_msg)

        if self.current_char == ':' and self.peek_char() == '=':
            self.next_char()  # skip ':'
            self.next_char()  # skip '='
            return Token(':=', position=(start_line, start_char))

        symbol = self.current_char
        self.next_char()
        return Token(symbol, position=(start_line, start_char))

    
    def skip_comment(self):
        """
        Skip a single-line comment in the input text.
        """
        while self.current_char and self.current_char != "\n":
            self.next_char()
        self.next_char()  # Skip the newline character at the end of the comment

    def read_string_literal(self):
        """
        Read a string literal from the input text.
        String literals are enclosed in double quotes.
        """
        start_line, start_char = self.line_number, self.char_number
        start_index = self.index  # start at the opening quotation mark
        self.next_char()
        
        while self.current_char and self.current_char != '"':
            if self.current_char in ['\n', '\t']:
                self.char_number = 1 if self.current_char == '\n' else self.char_number + 4
                self.line_number += 1 if self.current_char == '\n' else self.line_number
            else:
                self.char_number += 1
            self.index += 1
            self.current_char = self.input_text[self.index] if self.index < len(self.input_text) else None
        
        self.next_char()  # skip the closing quotation mark
        value = self.input_text[start_index:self.index]
        return Token("STRING", value=value, position=(start_line, start_char))
    
    def skip_whitespace_and_comments(self):
        """
        Skip whitespaces and single-line comments in the input text.
        """
        while self.current_char and (self.current_char.isspace() or (self.current_char == '/' and self.peek_char() == '/')):
            if self.current_char == '/' and self.peek_char() == '/':
                self.skip_comment()
            else:
                self.next_char()

    def set_end_of_text_token(self):
        """
        Set the 'end-of-text' token if the end of the input text is reached.
        """
        if not self.current_char:
            position = (self.line_number, self.char_number)
            self.current_token = Token("end-of-text", position=position)
            return True
        return False

    def check_for_illegal_characters(self):
        """
        Check for any illegal characters in the input text and raise a SyntaxError if found.
        """
        illegal_characters = ["!", "@", "^"]
        if self.current_char in illegal_characters:
            error_msg = f"Unexpected symbol '{self.current_char}' at position ({self.line_number}, {self.char_number})"
            raise SyntaxError(error_msg)

    def generate_token_based_on_current_char(self):
        """
        Generate the next token based on the current character in the input text.
        """
        if self.current_char == "\"":
            self.current_token = self.read_string_literal()
        elif self.current_char.isalpha() or self.current_char == "_":
            self.current_token = self.read_identifier_or_keyword()
        elif self.current_char.isdigit():
            self.current_token = self.read_number()
        else:
            next_chars = self.input_text[self.index:self.index+3]
            if next_chars == '***':
                error_msg = f"Illegal token '***' at position ({self.line_number}, {self.char_number})"
                raise SyntaxError(error_msg)
            self.current_token = self.read_symbol()

    def next_token(self):
        """
        Get the next token from the input text.
        """
        self.skip_whitespace_and_comments()
        if self.set_end_of_text_token():
            return
        self.check_for_illegal_characters()
        self.generate_token_based_on_current_char()
