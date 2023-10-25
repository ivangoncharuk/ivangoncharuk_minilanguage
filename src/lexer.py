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
    
    def __init__(self, input_text):
        self.input_text = input_text
        self.current_char = self.input_text[0] if self.input_text else None
        self.line_number = 1
        self.char_number = 1
        self.index = 0
        self.current_token = None
        self.keywords = {'program', 'if', 'then',
                         'end', 'do', 'while',
                         'print', 'else', 'int',
                         'bool', "and", "or", "not"}

    def next_char(self):
        if self.current_char == "\n":
            self.line_number += 1
            self.char_number = 0
        elif self.current_char == "\t":
            self.char_number += 4  # Assuming a tab is 4 spaces
        else:
            self.char_number += 1

        self.index += 1
        if self.index < len(self.input_text):
            self.current_char = self.input_text[self.index]
        else:
            self.current_char = None

    def peek_char(self):
        peek_index = self.index + 1
        if peek_index < len(self.input_text):
            return self.input_text[peek_index]
        return None

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
        start_index = self.index
        while self.current_char and (self.current_char.isalnum() or self.current_char == "_"):
            self.next_char()
        identifier = self.input_text[start_index:self.index]
        if identifier in self.keywords:
            return Token(identifier, position=(self.line_number, self.char_number - len(identifier)))
        return Token("ID", value=identifier, position=(self.line_number, self.char_number - len(identifier)))

    def read_number(self):
        start_index = self.index
        while self.current_char and self.current_char.isdigit():
            self.next_char()
        number = self.input_text[start_index:self.index]
        return Token("NUM", value=int(number), position=(self.line_number, self.char_number - len(number)))

    def read_symbol(self):
        start_line = self.line_number
        start_char = self.char_number

        current_char = self.current_char
        next_chars = self.input_text[self.index+1:self.index+4]

        if current_char == '*' and next_chars == '**':
            error_msg = f"Illegal token '***' at position ({start_line}, {start_char})"
            raise SyntaxError(error_msg)

        self.next_char()
        return Token(current_char, position=(start_line, start_char))

    def skip_comment(self):
        while self.current_char and self.current_char != "\n":
            self.next_char()
        self.next_char()

    def next_token(self):
        while self.current_char and (self.current_char.isspace() or (self.current_char == '/' and self.peek_char() == '/')):
            if self.current_char == '/' and self.peek_char() == '/':
                self.skip_comment()
            else:
                self.next_char()
                
        self.skip_whitespace()

        if not self.current_char:
            self.current_token = Token("end-of-text", position=(self.line_number, self.char_number))
            return
        
        illegal_characters = ["!", "@", "^"]
        
        if self.current_char in illegal_characters:
            error_msg = f"Unexpected symbol '{self.current_char}' at position ({self.line_number}, {self.char_number})"
            raise SyntaxError(error_msg)
            
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

    def read_string_literal(self):
        start_line = self.line_number
        start_char = self.char_number
        start_index = self.index  # start at the opening quotation mark
        self.next_char()
        while self.current_char not in ['"', None]:
            if self.current_char == '\n':
                self.line_number += 1
                self.char_number = 0
            elif self.current_char == '\t':
                self.char_number += 4
            else:
                self.char_number += 1
            self.index += 1
            self.current_char = self.input_text[self.index] if self.index < len(self.input_text) else None
        self.next_char()  # skip the closing quotation mark
        return Token("STRING", value=self.input_text[start_index:self.index], position=(start_line, start_char))
