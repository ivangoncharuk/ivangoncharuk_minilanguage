class Token:
    def __init__(self, kind, value=None, position=None):
        """
        Initializes a new instance of the Token class.

        :param kind: The kind of the token (e.g., ID, NUM, keyword, symbol, end-of-text)
        :param value: The value of the token (if applicable)
        :param position: The position of the token in the input (line number, character number)
        """
        self.kind = kind
        self.value = value
        self.position = position

    def __str__(self):
        """
        Returns a string representation of the token.
        """
        position_str = (
            f"({self.position[0]}:{self.position[1]})"
            if self.position
            else "(Unknown Position)"
        )
        value_str = f": {self.value}" if self.value is not None else ""
        return f"{position_str} {self.kind}{value_str}"

class Lexer:
    
    def __init__(self, input_text):
        self.input_text = input_text
        self.current_char = self.input_text[0] if self.input_text else None
        self.line_number = 1
        self.char_number = 1
        self.index = 0
        self.current_token = None
        self.keywords = {'program', 'if', 'then', 'end', 'do', 'while', 'print', 'else', 'int', 'bool'}

    def next_char(self):
        if self.current_char == "\n":
            self.line_number += 1
            self.char_number = 1
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
        two_char_operators = {":=", "!=", "=<", ">="}
        current_char = self.current_char
        next_char = self.peek_char()
        if current_char + next_char in two_char_operators:
            self.next_char()
            self.next_char()
            return Token(current_char + next_char, position=(self.line_number, self.char_number - 1))
        self.next_char()
        return Token(current_char, position=(self.line_number, self.char_number - 1))

    def skip_comment(self):
        while self.current_char and self.current_char != "\n":
            self.next_char()
        self.next_char()

    def read_string_literal(self):
        start_index = self.index
        self.next_char()  # skip the opening double quote
        while self.current_char and self.current_char != "\"":
            self.next_char()
        self.next_char()  # skip the closing double quote
        string_literal = self.input_text[start_index:self.index]
        return Token("STRING", value=string_literal, position=(self.line_number, self.char_number - len(string_literal)))


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
        if self.current_char == "\"":
            self.current_token = self.read_string_literal()
        elif self.current_char.isalpha() or self.current_char == "_":
            self.current_token = self.read_identifier_or_keyword()
        elif self.current_char.isdigit():
            self.current_token = self.read_number()
        else:
            self.current_token = self.read_symbol()
