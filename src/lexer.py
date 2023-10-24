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

    def next_char(self):
        self.index += 1
        if self.index < len(self.input_text):
            self.current_char = self.input_text[self.index]
            self.char_number += 1
            if self.current_char == "\n":
                self.line_number += 1
                self.char_number = 0
        else:
            self.current_char = None

    def next_token(self):
        while self.current_char and self.current_char.isspace():
            self.next_char()

        if not self.current_char:
            return Token("end-of-text", position=(self.line_number, self.char_number))

        # Placeholder token for testing
        return Token(
            "placeholder-token",
            "placeholder-value",
            (self.line_number, self.char_number),
        )

    def kind(self):
        pass

    def value(self):
        pass

    def position(self):
        pass


token = Token(kind="ID", value="variableName", position=(1, 5))
print(token)
