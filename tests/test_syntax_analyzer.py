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

    def test_match_function_with_incorrect_token(self):
        lexer = Lexer("begin")
        analyzer = SyntaxAnalyzer(lexer)
        with self.assertRaises(SystemExit):
            analyzer.match("program")


if __name__ == "__main__":
    unittest.main()
