import unittest
from src.lexer import Lexer
from src.syntax_analyzer import SyntaxAnalyzer


class TestSyntaxAnalyzer(unittest.TestCase):
    def test_initialization(self):
        lexer = Lexer("program test: ...")
        analyzer = SyntaxAnalyzer(lexer)
        self.assertIsNotNone(
            analyzer.current_token,
            "Current token should not be None after initialization",
        )

    def test_match_function_with_correct_token(self):
        lexer = Lexer("program")
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.match("program")
        except Exception as e:
            self.fail(f"Match function raised an exception with correct token: {e}")

    def test_program_structure_parsing(self):
        lexer = Lexer("program test: int x; print x.")
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.program()
        except Exception as e:
            self.fail(f"Program structure parsing failed with exception: {e}")

    def test_declarations_parsing(self):
        lexer = Lexer("int x, y, z;")
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.declarations()
        except Exception as e:
            self.fail(f"Declarations parsing failed with exception: {e}")

    def test_statements_parsing(self):
        lexer = Lexer("x := 10; if x > 5 then x := x - 1; end;")
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.statements()
        except Exception as e:
            self.fail(f"Statements parsing failed with exception: {e}")

    def test_statements_parsing2(self):
        lexer = Lexer("x := 10; if x > 5 then print x; else print 0; end;")
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.statements()
        except Exception as e:
            self.fail(f"Statements parsing failed with exception: {e}")

    def test_expression_parsing(self):
        lexer = Lexer("x + 10 * y")
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.expression()
        except Exception as e:
            self.fail(f"Expression parsing failed with exception: {e}")

    def test_program_print(self):
        lexer = Lexer("program Print: print(77).")
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.program()
        except Exception as e:
            self.fail(
                f"Complete syntax analysis with correct code failed with exception: {e}"
            )
            
    def test_unary_operator_simple_expression(self):
        lexer = Lexer("-10")
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.expression()
        except Exception as e:
            self.fail(f"Unary operator in simple expression failed: {e}")
            
    def test_unary_operator_with_identifier(self):
        lexer = Lexer("not x")
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.expression()
        except Exception as e:
            self.fail(f"Unary operator with identifier failed: {e}")
    
    def test_unary_operator_complex_expression(self):
        lexer = Lexer("not (x > 5)")
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.expression()
        except Exception as e:
            self.fail(f"Unary operator in complex expression failed: {e}")
            
    def test_nested_unary_operators(self):
        lexer = Lexer("not not true")
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.expression()
        except Exception as e:
            self.fail(f"Nested unary operators failed: {e}")
            
    def test_unary_operator_in_conditional(self):
        lexer = Lexer("if not x then y := 0; else y := 1; end;")
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.statements()
        except Exception as e:
            self.fail(f"Unary operator in conditional statement failed: {e}")

    def test_complex_expression_multiple_operators(self):
        lexer = Lexer("x * (y + 3) - 4 / not z")
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.expression()
        except Exception as e:
            self.fail(f"Complex expression with multiple operators failed: {e}")


if __name__ == "__main__":
    unittest.main()
