from lexer import Lexer, Token


class SyntaxAnalyzer:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None

    def match(self, expected_kind):
        if self.current_token.kind == expected_kind:
            self.current_token = self.lexer.next_token()
            return True
        else:
            return False

    def program(self):
        # TODO create the program function
        pass
