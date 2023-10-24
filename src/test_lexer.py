from lexer import Lexer, Token

test_input_1 = "var1 := 123; x := 456; y := 789"
test_input_2 = "if x < 10 then y := x + 1 end"
test_input_3 = "// This is a comment\nx := 5 // Another comment"

program_example_1 = """program example1:
  x := 10;
  y := 20;
  print x + y."""

program_example_2 = """program example2:
  if x < 10 then
    y := x + 1;
  end."""

program_example_3 = """program example3:
  while x >= 0 do
    print x;
    x := x - 1;
  end."""

program_example_4 = """program control_flow:
  int x;
  if x > 0 then
    while x != 0 do
      x := x - 1
    end
  else
    x := 10
  end.
"""

program_example_4_comments = """program control_flow:
  int x; // initialize x
  if x > 0 then // if statement
    while x != 0 do // while statement
      x := x - 1 //assigning x to the expression
    end //ending the while loop
  else
    x := 10
  end.
"""

program_tricky = """program bad_expression:
   int a;
   int b;
   if4 a < b then5
     2int b;
     b := 2 * a
   5else
     bool b;
     b := 2 * a
   fii
end"""

non_sense = "Program lexically-ok-2"

comprehensive_test = """program comprehensive_test:
  int x, y, z;
  bool flag;
  x := 10;
  y := 20;
  z := 30;
  flag := true;
  if x < y then
    print x + y * z;
  else
    print y - z;
  end
  while x != 0 do
    x := x - 1;
    if x <= 1 then
      print "x is less than 1"
    if flag then
      print "x is not zero";
    else
      print "x is zero";
    end
  end
  print "Final value of x: ", x;
end.
"""

lexer = Lexer(comprehensive_test)
print("\n" + comprehensive_test + "\n")
lexer.next_token()
print(
    lexer.position(), lexer.kind(), lexer.value() if lexer.value() is not None else ""
)
while lexer.kind() != "end-of-text":
    lexer.next_token()
    print(
        lexer.position(),
        lexer.kind(),
        lexer.value() if lexer.value() is not None else "",
    )
