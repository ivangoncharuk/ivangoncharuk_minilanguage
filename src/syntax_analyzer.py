from lexer import Lexer, Token


class SyntaxAnalyzer:
    def __init__(self, lexer):
        self.lexer = lexer
        self.lexer.next_token()  # Load the first token
        self.current_token = self.lexer.current_token

    def match(self, expected_kind):
        if self.current_token and self.current_token.kind == expected_kind:
            self.lexer.next_token()  # Move to the next token
            self.current_token = self.lexer.current_token  # Update the current token
            return True
        return False

    def program(self):
        if not self.match("program"):
            return False
        if not self.match("ID"):
            return False
        if not self.match(":"):
            return False
        if not self.body():
            return False
        if not self.match("end"):
            return False
        return True

    def body(self):
        if self.current_token.kind in {"bool", "int"}:
            if not self.declarations():
                return False
        if not self.statements():
            return False
        return True

    
    def declarations(self):
        while self.current_token.kind in {"bool", "int"}:
            if not self.single_declaration():
                return False
        return True

    def single_declaration(self):
        if not self.match(self.current_token.kind):  # Match "bool" or "int"
            return False
        if not self.match("ID"):
            return False
        while self.current_token.kind == ",":
            self.match(",")
            if not self.match("ID"):
                return False
        if not self.match(";"):
            return False
        return True

    def statements(self):
        while self.current_token.kind is not None and self.current_token.kind != "end":
            if not self.statement():
                return False
            if self.current_token.kind != "end":
                if not self.match(";"):
                    return False
        return True

    def statement(self):
        if self.current_token.kind == "if":
            return self.conditional_statement()
        elif self.current_token.kind == "while":
            return self.iterative_statement()
        elif self.current_token.kind == "print":
            return self.print_statement()
        else:
            return self.assignment_statement()

    def conditional_statement(self):
        return True

    def iterative_statement(self):
        return True

    def print_statement(self):
        return True

    def assignment_statement(self):
        if not self.match("ID"):
            return False
        if not self.match(":="):
            return False
        if not self.expression():
            return False
        return True

    def expression(self):
        return True

    def is_declaration_start(self):
        # TODO Implement logic to determine if the current token starts a declaration
        return False

    def single_declaration(self):
        # TODO Implement logic for parsing a single declaration
        return True
