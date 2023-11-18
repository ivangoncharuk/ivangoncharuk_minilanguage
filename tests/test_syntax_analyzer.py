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

    def test_unary_operator_simple_expression(self):
        lexer = Lexer("not 10")
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

    def test_iterative_statement_parsing(self):
        lexer = Lexer("while x < 10 do x := x + 1; end;")
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.statements()
        except Exception as e:
            self.fail(f"Iterative statement parsing failed with exception: {e}")

    def test_nested_statements(self):
        lexer = Lexer(
            "if x != 0 then while y < x do y := y + 1; end; else print x; end;"
        )
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.statements()
        except Exception as e:
            self.fail(f"Nested statements parsing failed: {e}")

    def test_mixed_operator_expression(self):
        lexer = Lexer("x + y * z - w / v")
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.expression()
        except Exception as e:
            self.fail(f"Mixed operator expression parsing failed: {e}")

    def test_assignment_with_complex_expression(self):
        lexer = Lexer("a := b * (c + d) / e - f")
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.statements()
        except Exception as e:
            self.fail(f"Assignment with complex expression failed: {e}")

    def test_expression_with_parentheses(self):
        lexer = Lexer("(a + b) * (c - d)")
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.expression()
        except Exception as e:
            self.fail(f"Expression with parentheses parsing failed: {e}")

    def test_boolean_literal_handling(self):
        lexer = Lexer("true and false or not true")
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.expression()
        except Exception as e:
            self.fail(f"Boolean literal handling failed: {e}")

    def test_full_program_parsing(self):
        program_code = """
        program Example:
            int i, j;
            i := 0;
            j := 10;
            while i < j do
                print i;
                i := i + 1;
            end;
        ."""
        lexer = Lexer(program_code)
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.program()
        except Exception as e:
            self.fail(f"Full program parsing failed with exception: {e}")

    def test_complex_conditional_statement(self):
        lexer = Lexer(
            """
if x < y and y > z then 
    print x; 
else 
    if x > y and y = x then
        print x + y;
    end
end
.
"""
        )
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.statements()
        except Exception as e:
            self.fail(f"Complex conditional statement parsing failed: {e}")

    def test_program_print(self):
        lexer = Lexer("program Print: print(77).")
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.program()
        except Exception as e:
            self.fail(
                f"Complete syntax analysis with correct code failed with exception: {e}"
            )

    def test_program_modulo(self):
        # for some reason my lexer is seeing 'mod' inside the id 'modulo' and treating
        # it as a 'MUL_OP' operator...weird
        lexer = Lexer(
            """program mudulo:
  int a, b, c;
  bool eq;
  a := 8;
  b := 3;
  c := a mod b;
  eq := a / b + c = 4;
  print a;
  print b;
  print c;
  print a / b + c;
  print eq
.
"""
        )
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.program()
        except Exception as e:
            self.fail(
                f"Complete syntax analysis with correct code failed with exception: {e}"
            )

    def test_program_hiding(self):
        # for some reason my lexer is seeing 'mod' inside the id 'modulo' and treating
        # it as a 'MUL_OP' operator...weird
        lexer = Lexer(
            """program Hiding :
   int a;
   int b;
   a := 2;
   b := 5;
   while not (a != b) do
     int b;
     b := 2 * a;
     print b;
     a := a + 1
   end;
   print b
.
"""
        )
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.program()
        except Exception as e:
            self.fail(
                f"Complete syntax analysis with correct code failed with exception: {e}"
            )

    def test_program_euclid(self):
        # for some reason my lexer is seeing 'mod' inside the id 'modulo' and treating
        # it as a 'MUL_OP' operator...weird
        lexer = Lexer(
            """// Euclid's algorithm for the greatest common divisor.
program GCD:
   int a;  int b;
   a := 15;
   b := 20;
   print a;  print b;
   while a != b do
      if a < b then b := b - a
      else a := a - b
      end
   end;
   print a
.
"""
        )
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.program()
        except Exception as e:
            self.fail(
                f"Complete syntax analysis with correct code failed with exception: {e}"
            )

    def test_program_bad_scoping(self):
        # for some reason my lexer is seeing 'mod' inside the id 'modulo' and treating
        # it as a 'MUL_OP' operator...weird
        lexer = Lexer(
            """
program bad_scoping:
   int a;
   while a = 0 do
     int b;
     b := a
   end;
   if a = 0 then
      int c;
      c := b
   else
      a := c
   end
.
"""
        )
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.program()
        except Exception as e:
            self.fail(
                f"Complete syntax analysis with correct code failed with exception: {e}"
            )

    def test_program_bad_expression_7(self):
        # for some reason my lexer is seeing 'mod' inside the id 'modulo' and treating
        # it as a 'MUL_OP' operator...weird
        lexer = Lexer(
            """program bad_expression:
   int a;
   int b;
   if a < b then
     bool b;
     b := 2 * a
   end
.
"""
        )
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.program()
        except Exception as e:
            self.fail(
                f"Complete syntax analysis with correct code failed with exception: {e}"
            )

    def test_program_bad_expression_6(self):
        # for some reason my lexer is seeing 'mod' inside the id 'modulo' and treating
        # it as a 'MUL_OP' operator...weird
        lexer = Lexer(
            """program bad_expression:
   int a;
   int b;
   a := 2;
   b := 5;
   while not a = b do
     bool b;
     b := 2 * a
   end
.
"""
        )
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.program()
        except Exception as e:
            self.fail(
                f"Complete syntax analysis with correct code failed with exception: {e}"
            )

    def test_program_bad_expression_5(self):
        # for some reason my lexer is seeing 'mod' inside the id 'modulo' and treating
        # it as a 'MUL_OP' operator...weird
        lexer = Lexer(
            """program bad_expression:
   int a;
   bool b;
   while not a = b do
     int b;
     print b
   end
.
"""
        )
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.program()
        except Exception as e:
            self.fail(
                f"Complete syntax analysis with correct code failed with exception: {e}"
            )

    def test_program_bad_expression_4(self):
        # for some reason my lexer is seeing 'mod' inside the id 'modulo' and treating
        # it as a 'MUL_OP' operator...weird
        lexer = Lexer(
            """program bad_expression:
   int a;
   bool b;
   b := a + b
.
"""
        )
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.program()
        except Exception as e:
            self.fail(
                f"Complete syntax analysis with correct code failed with exception: {e}"
            )

    def test_program_bad_expression_3(self):
        # for some reason my lexer is seeing 'mod' inside the id 'modulo' and treating
        # it as a 'MUL_OP' operator...weird
        lexer = Lexer(
            """program bad_expression:
   int a;
   bool b;
   b := not a and b
.
"""
        )
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.program()
        except Exception as e:
            self.fail(
                f"Complete syntax analysis with correct code failed with exception: {e}"
            )

    def test_program_bad_expression_2(self):
        # for some reason my lexer is seeing 'mod' inside the id 'modulo' and treating
        # it as a 'MUL_OP' operator...weird
        lexer = Lexer(
            """program bad_expression:
   int a;
   bool b;
   bool c;
   a := b and c
.
"""
        )
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.program()
        except Exception as e:
            self.fail(
                f"Complete syntax analysis with correct code failed with exception: {e}"
            )

    def test_program_bad_expression_1(self):
        # for some reason my lexer is seeing 'mod' inside the id 'modulo' and treating
        # it as a 'MUL_OP' operator...weird
        lexer = Lexer(
            """program bad_expression:
   int a;
   bool b;
   b := a and b
.
"""
        )
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.program()
        except Exception as e:
            self.fail(
                f"Complete syntax analysis with correct code failed with exception: {e}"
            )

    def test_program_bad_declaration(self):
        # for some reason my lexer is seeing 'mod' inside the id 'modulo' and treating
        # it as a 'MUL_OP' operator...weird
        lexer = Lexer(
            """program bad_declaration:
   int a;
   int b;
   bool a;
   a := a
.
"""
        )
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.program()
        except Exception as e:
            self.fail(
                f"Complete syntax analysis with correct code failed with exception: {e}"
            )

    def test_program_while_ab_print_twenty(self):
        # for some reason my lexer is seeing 'mod' inside the id 'modulo' and treating
        # it as a 'MUL_OP' operator...weird
        lexer = Lexer(
            """// This program should print the number 20.
program Twenty:
  int a;
  int b;
  a := 2;
  b := 1;
  if not (a < 0) then
    int b;
    b := - 2;     //     (the inner b, the outer one is still 1)
    a := a * b    // a = -4
  else
    int c;
    c := a - b;
    a := a * (c - b)
  end;
  print a * (a - b)    // -4 * (-4 - 1)  =  -4 * (-5)  =  20
.
"""
        )
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.program()
        except Exception as e:
            self.fail(
                f"Complete syntax analysis with correct code failed with exception: {e}"
            )

    def test_program_cond_ab_print_twenty(self):
        # for some reason my lexer is seeing 'mod' inside the id 'modulo' and treating
        # it as a 'MUL_OP' operator...weird
        lexer = Lexer(
            """// This program should print the number 20.
program Twenty:
  int a;
  int b;
  a := 2;
  b := 1;
  if not (a < 0) then
    int b;
    b := - 2;     //     (the inner b, the outer one is still 1)
    a := a * b    // a = -4
  else
    int c;
    c := a - b;
    a := a * (c - b)
  end;
  print a * (a - b)    // -4 * (-4 - 1)  =  -4 * (-5)  =  20
.

"""
        )
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.program()
        except Exception as e:
            self.fail(
                f"Complete syntax analysis with correct code failed with exception: {e}"
            )


if __name__ == "__main__":
    unittest.main()
