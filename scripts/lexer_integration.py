from src.lexer import Lexer
from src.syntax_analyzer import SyntaxAnalyzer
import os

def test_lexer_integration():
    # Pulling from file
    file_name = input("\nEnter the name of the file to test (including extension): ")
    if not os.path.isfile(file_name):
        print(f"The file {file_name} does not exist.")
        return

    with open(file_name, "r") as f:
        file_content = f.read()

    # using the classes
    lexer = Lexer("var1 := var2")
    syntax_analyzer = SyntaxAnalyzer(lexer)
    result = syntax_analyzer.program()

    # test_string = "program example :"
    # lexer = Lexer(test_string)
    # analyzer = SyntaxAnalyzer(lexer)

    # print(f"First token from Lexer: {lexer.current_token}") # First token from Lexer: None
    # print(f"First token in Syntax Analyzer: {analyzer.current_token}") # First token from Syntax Analyzer: None

    # # Test the match function
    # try:
    #     print(f"current token in analyzer: {analyzer.current_token}")
    #     result = analyzer.match("Program")
    #     print(f"Result of matching 'Program': {result}")
    # except AttributeError as e:
    #     print(f"Error during matching: {e}")

    # # Check the next token in Syntax Analyzer
    # print(f"Next token in Syntax Analyzer: {analyzer.current_token}")
    # print(f"The current state of lexer.current_token: {lexer.current_token}")


test_lexer_integration()
