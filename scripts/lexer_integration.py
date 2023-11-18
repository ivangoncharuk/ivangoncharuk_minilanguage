import os, sys

sys.path.append(".")  # need this to run
from src.lexer import Lexer
from src.syntax_analyzer import SyntaxAnalyzer


def test_lexer_integration():
    # # Pulling from file
    # # file_name = input("\nEnter the name of the file to test (including extension): ")
    # file_name = "grammar-examples/correct-syntax/ab_print_twenty.txt"
    # if not os.path.isfile(file_name):
    #     print(f"The file {file_name} does not exist.")
    #     return

    # with open(file_name, "r") as f:
    #     file_content = f.read()

    lexer = Lexer("-10")
    analyzer = SyntaxAnalyzer(lexer)
    analyzer.expression()

    # try:
    #     analyzer.statements()
    # except Exception as e:
    #     print(e)


test_lexer_integration()
