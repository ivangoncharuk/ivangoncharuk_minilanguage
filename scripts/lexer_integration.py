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

    lexer = Lexer("""// This program should print the number 20.
program Twenty:
  int a;
  int b;
  a := 2;
  b := 1;
  while a >= 0 do
    int b;
    b := - 2;     // (the inner b, the outer one is still 1)
    a := a * b    // a = -4
  end;
  print a * (a - b)    // -4 * (-4 - 1)  =  -4 * (-5)  =  20
.
""")
    analyzer = SyntaxAnalyzer(lexer)
    analyzer.program()

    # try:
    #     analyzer.statements()
    # except Exception as e:
    #     print(e)


test_lexer_integration()
