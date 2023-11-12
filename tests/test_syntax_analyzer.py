import unittest
import sys
# had to append the path so the testing suite would work
sys.path.append('/Users/ivangoncharuk/Documents/GitHub/ivangoncharuk_minilanguage/src')

from lexer import Lexer
from syntax_analyzer import SyntaxAnalyzer


class TestSyntaxAnalyzer(unittest.TestCase):
    
    def test_match_function(self):
        lexer = Lexer("program example :")
        analyzer = SyntaxAnalyzer(lexer)
        self.assertTrue(analyzer.match("program"))

    def test_program_valid_syntax(self):
        # A syntactically correct program string according to your grammar
        valid_syntax = "program validId : end"

        lexer = Lexer(valid_syntax)
        syntax_analyzer = SyntaxAnalyzer(lexer)

        result = syntax_analyzer.program()
        assert result, "Syntax should be valid for the given program string"
    
    def test_missing_program_keyword(self):
        missing_program = "validId : end"
        lexer = Lexer(missing_program)
        syntax_analyzer = SyntaxAnalyzer(lexer)

        result = syntax_analyzer.program()
        assert not result, "Syntax should be invalid when 'program' keyword is missing"

    def test_missing_identifier(self):
        missing_identifier = "program : end"
        lexer = Lexer(missing_identifier)
        syntax_analyzer = SyntaxAnalyzer(lexer)

        result = syntax_analyzer.program()
        assert not result, "Syntax should be invalid when the identifier is missing after 'program'"

    def test_extra_tokens_before_program(self):
        extra_tokens = "extra validId program validId : end"
        lexer = Lexer(extra_tokens)
        syntax_analyzer = SyntaxAnalyzer(lexer)

        result = syntax_analyzer.program()
        assert not result, "Syntax should be invalid with extra tokens before 'program' keyword"

if __name__ == "__main__":
    unittest.main()
