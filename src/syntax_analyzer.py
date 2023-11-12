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
        if not self.declarations():
            return False
        if not self.statements():
            return False
        return True
    
    def declarations(self):
        while self.is_declaration_start():
            if not self.single_declaration():
                return False
        return True

    def is_declaration_start(self):
        # Implement logic to determine if the current token starts a declaration
        return False

    def single_declaration(self):
        # Implement logic for parsing a single declaration
        return True

    def statements(self):
        # Placeholder for statements method
        # Implement the logic to validate statements
        return True
