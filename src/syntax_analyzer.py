from src.lexer import Lexer
from icecream import ic


class SyntaxAnalyzer:
    def __init__(self, lexer):
        self.lexer = lexer
        self.lexer.next_token()  # Load the first token
        self.current_token = self.lexer.current_token

    def consume(self):
        self.lexer.next_token()
        self.current_token = self.lexer.current_token

    def match(self, expected_token_kind):
        if self.current_token and self.current_token.kind == expected_token_kind:
            self.consume()
        else:
            self.error(expected_token_kind)

    def error(self, expected_symbol):
        position = self.current_token.position if self.current_token else "Unknown"
        print("\n--- NOT OK ---\n")
        raise SyntaxError(
            f"Error: Unexpected Token: '{self.current_token.kind}' at {position}. Expected: {expected_symbol}"
        )

    def program(self):
        self.match("program")
        self.identifier()
        self.match(":")
        self.body()
        self.match(".")
        print("\n--- OK ---\n")

    def body(self):
        if self.current_token.kind in {"bool", "int"}:
            self.declarations()
        self.statements()

    def declarations(self):
        self.declaration()
        while self.current_token.kind in {"bool", "int"}:
            self.declaration()

    def declaration(self):
        if self.current_token.kind in {"bool", "int"}:
            self.consume()
            self.match("ID")
            while self.current_token.kind == ",":
                self.consume()
                self.match("ID")
            self.match(";")
        else:
            self.error("'bool' or 'int'")

    def statements(self):
        while self.current_token and self.current_token.kind in {
            "ID",
            "if",
            "while",
            "print",
        }:
            self.statement()
            if self.current_token.kind in {";"}:
                self.consume()

    def statement(self):
        if self.current_token.kind == "ID":
            self.assignment()
        elif self.current_token.kind == "if":
            self.conditional()
        elif self.current_token.kind == "while":
            self.iterative()
        elif self.current_token.kind == "print":
            self.print_statement()
        else:
            self.error("ID, if, while, or print")

    def assignment(self):
        self.match("ID")
        self.match("ASSIGN_OP")
        self.expression()

    def conditional(self):
        self.match("if")
        self.expression()
        self.match("then")
        self.body()
        if self.current_token.kind == "else":
            self.consume()
            self.body()
        self.match("end")

    def iterative(self):
        self.match("while")
        self.expression()
        self.match("do")
        self.body()
        self.match("end")

    def print_statement(self):
        self.match("print")
        self.expression()

    def expression(self):
        self.simple_expression()
        while self.current_token.kind in {
            "RELATIONAL_OP",
            "and",
            "or",
            "not",
        }:
            self.match(self.current_token.kind)  # Consume the relational operator
            self.simple_expression()  # Parse the right-hand side of the expression

    def simple_expression(self):
        self.term()
        while self.current_token.kind == "ADD_OP":
            self.consume()
            self.term()

    def term(self):
        self.factor()
        while self.current_token.kind == "MUL_OP":
            self.consume()
            self.factor()

    def factor(self):
        if self.current_token.kind == "not" or self.current_token.value == "-":
            self.consume()
            self.factor()
        else:
            if self.current_token.kind in {"false", "true", "NUM"}:
                self.literal()
            elif self.current_token.kind == "ID":
                self.consume()
            elif self.current_token.kind == "(":
                self.consume()
                self.expression()
                self.match(")")
            else:
                self.error("Expected: 'true', 'false', 'NUM', 'ID', '('")

    def literal(self):
        if self.current_token.kind == "NUM":
            self.consume()
        else:
            self.boolean_literal()

    def boolean_literal(self):
        if self.current_token.kind in {"false", "true"}:
            self.consume()
        else:
            self.error("Expected: 'false' or 'true'")

    def identifier(self):
        if self.current_token.kind == "ID":
            self.consume()
        else:
            self.error("Expected: ID")
