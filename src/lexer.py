class Token:
    def __init__(self, kind: str, value=None, position=None):
        self.kind = kind
        self.value = value
        self.position = position

    def __str__(self, max_value_length=0):
        # Format the position of the token. If the position is unknown, display "Unknown Position".
        position = (
            f"({self.position[0]: >3} :{self.position[1]: >3} )"  # Align the line and column numbers to the right
            if self.position
            else "(Unknown Position)"
        )

        # Format the value of the token, ensuring it's right-padded with spaces for alignment.
        # If the value is None (for tokens without a specific value), display an empty string.
        value = (
            f" {self.value}".ljust(max_value_length + 1)  # Right-pad the value
            if self.value is not None
            else ""
        )

        # Format the kind of the token.
        # If the token kind is one of the special characters or 'end-of-text', set kind to an empty string.
        # This ensures that kinds like ":" and "end-of-text" are not displayed twice.
        kind = (
            f" {self.kind}"  # Add a space before the kind for separation
            if self.kind and self.kind not in {":", ",", ";", ".", "end-of-text"}
            else ""
        )

        # If the kind is 'end-of-text', explicitly set kind to " end-of-text" to ensure it gets displayed.
        if self.kind == "end-of-text":
            kind = " end-of-text"

        # Combine the formatted position, value, and kind into a single string and return it.
        return f"{position}{value}{kind}"


class Lexer:
    def __init__(self, input_text: str):
        self.input_text = input_text
        self.current_char = self.input_text[0] if self.input_text else None
        self.line_number = 1
        self.char_number = 1
        self.index = 0
        self.current_token = None
        self.relational_operators = {"<", "=<", "=", "!=", ">=", ">"}
        self.valid_multi_char_tokens = {"=<", "!=", ">=", ":="}
        self.additive_operators = {"+", "-", "or"}
        self.multiplicative_operators = {"*", "/", "mod", "and"}
        self.unary_operators = {"-", "not"}
        self.assignment_operators = {":="}
        self.operators = (
            self.additive_operators.union(self.multiplicative_operators)
            .union(self.unary_operators)
            .union(self.relational_operators)
        )

        self.other_symbols = {",", ":", ";", ".", "(", ")", "'", '"'}
        self.keywords = {
            "program",
            "if",
            "then",
            "end",
            "do",
            "while",
            "print",
            "else",
            "int",
            "bool",
            "and",
            "or",
            "not",
        }

    def next_char(self):
        """Move to the next character in the input text."""
        if self.current_char:
            if self.current_char == "\n":
                self.line_number += 1
                self.char_number = 1
            else:
                self.char_number += 4 if self.current_char == "\t" else 1
            self.index += 1
            self.current_char = (
                self.input_text[self.index]
                if self.index < len(self.input_text)
                else None
            )

    def peek_char(self) -> str:
        """Look at the next character in the input text without moving the current position."""
        peek_index = self.index + 1
        return (
            self.input_text[peek_index] if peek_index < len(self.input_text) else None
        )

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
        while self.current_char and (
            self.current_char.isalnum() or self.current_char == "_"
        ):
            self.next_char()

        identifier = self.input_text[start_index : self.index]
        position = (self.line_number, self.char_number - len(identifier))
        return (
            Token("ID", value=identifier, position=position)
            if identifier not in self.keywords
            else Token(identifier, position=position)
        )

    def read_number(self):
        """
        Read a number from the input text.
        """
        start_index = self.index
        while self.current_char and self.current_char.isdigit():
            self.next_char()

        number = self.input_text[start_index : self.index]
        position = (self.line_number, self.char_number - len(number))
        return Token("NUM", value=int(number), position=position)

    def read_symbol(self):
        """
        Read a single character symbol from the input text.
        Handles multi-character symbols like ':='.
        Raises a SyntaxError for illegal token '***'.
        """
        start_line, start_char = self.line_number, self.char_number
        symbol = self.current_char
        self.next_char()

        # Check for multi-character operators
        potential_multi_char_token = symbol + (self.current_char or "")
        if potential_multi_char_token in self.valid_multi_char_tokens:
            symbol = potential_multi_char_token
            self.next_char()

        # Determine the token type based on the operator
        if symbol in self.relational_operators:
            kind = "RELATIONAL_OP"
        elif symbol in self.additive_operators:
            kind = "ADD_OP"
        elif symbol in self.unary_operators:
            kind = "UNARY_OP"
        elif symbol in self.assignment_operators:
            kind = "ASSIGN_OP"
        elif symbol in self.other_symbols:
            kind = symbol  # Set kind to the symbol itself
        elif symbol in self.multiplicative_operators:
            kind = "MUL_OP"
        else:
            kind = "UNKNOWN"

            # Check if the next character is also a symbol and not a whitespace
            if (
                self.current_char
                and not self.current_char.isspace()
                and not self.current_char.isalnum()
            ):
                error_msg = f"Undefined token '{symbol}' at position ({start_line}, {start_char})"
                raise SyntaxError(error_msg)

        return Token(kind, value=symbol, position=(start_line, start_char))

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
        String literals are enclosed in single or double quotes.
        """
        start_line, start_char = self.line_number, self.char_number
        start_index = self.index  # start at the opening quotation mark
        quote_type = (
            self.current_char
        )  # Save the type of quote used to start the string
        self.next_char()

        while self.current_char and self.current_char != quote_type:
            if self.current_char in ["\n", "\t"]:
                self.char_number = (
                    1 if self.current_char == "\n" else self.char_number + 4
                )
                self.line_number += 1 if self.current_char == "\n" else self.line_number
            else:
                self.char_number += 1
            self.index += 1
            self.current_char = (
                self.input_text[self.index]
                if self.index < len(self.input_text)
                else None
            )

        if not self.current_char:
            raise SyntaxError(
                f"Unclosed string literal at position ({start_line}, {start_char})"
            )

        self.next_char()  # skip the closing quotation mark
        value = self.input_text[
            start_index + 1 : self.index - 1
        ]  # Exclude the quotes from the value
        return Token("STRING", value=value, position=(start_line, start_char))

    def skip_whitespace_and_comments(self):
        """
        Skip whitespaces and single-line comments in the input text.
        """
        while self.current_char and (
            self.current_char.isspace()
            or (self.current_char == "/" and self.peek_char() == "/")
        ):
            if self.current_char == "/" and self.peek_char() == "/":
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

    def check_for_invalid_token_combinations(self):
        """
        Check for invalid combinations of characters and raise a SyntaxError if found.
        """
        if self.current_char in self.operators or self.current_char in self.other_symbols:
            next_char = self.peek_char()
            if next_char and (next_char in self.operators or next_char in self.other_symbols):
                combined_token = self.current_char + next_char
                if combined_token not in self.valid_multi_char_tokens:
                    error_msg = f"Invalid token '{combined_token}' at position ({self.line_number}, {self.char_number})"
                    raise SyntaxError(error_msg)

    def generate_token_based_on_current_char(self):
        """
        Generate the next token based on the current character in the input text.
        """
        self.check_for_invalid_token_combinations()
        
        if self.current_char in {'"', "'"}:
            self.current_token = self.read_string_literal()
        elif self.current_char.isalpha() or self.current_char == "_":
            # Check if the current token is "mod"
            if self.input_text[self.index : self.index + 3] == "mod":
                self.current_token = Token(
                    "MUL_OP", value="mod", position=(self.line_number, self.char_number)
                )
                self.index += 3
                self.char_number += 3
                self.current_char = (
                    self.input_text[self.index]
                    if self.index < len(self.input_text)
                    else None
                )
            else:
                self.current_token = self.read_identifier_or_keyword()
        elif self.current_char.isdigit():
            self.current_token = self.read_number()
        elif self.current_char in self.relational_operators.union(
            self.additive_operators,
            self.unary_operators,
            self.assignment_operators,
            self.other_symbols,
        ):
            self.current_token = self.read_symbol()
        elif self.current_char in self.multiplicative_operators:
            if self.current_char == "*" or self.current_char == "/":
                self.current_token = Token(
                    "MUL_OP",
                    value=self.current_char,
                    position=(self.line_number, self.char_number),
                )
                self.next_char()
            else:
                error_msg = f"Unexpected character '{self.current_char}' at position ({self.line_number}, {self.char_number})"
                raise SyntaxError(error_msg)

    def next_token(self):
        """
        Get the next token from the input text.
        """
        self.skip_whitespace_and_comments()
        if self.set_end_of_text_token():
            return

        if self.current_char == "!":
            if self.peek_char() == "=":
                self.current_token = Token(
                    "RELATIONAL_OP",
                    value="!=",
                    position=(self.line_number, self.char_number),
                )
                self.next_char()
                self.next_char()
                return

        self.check_for_illegal_characters()
        self.generate_token_based_on_current_char()
