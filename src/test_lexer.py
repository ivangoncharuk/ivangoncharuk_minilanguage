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

comprehensive_test_1 = """program comprehensive_test:
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

comprehensive_test_2 = """program comprehensive_test_2:
  // Variable Declarations
  int a, b, c;
  bool flag;
  
  // Assignment Statements
  a := 10;
  b := 20;
  c := 30;
  flag := true;
  
  // Conditional Statement with Relational Operators
  if a < b and b >= c then
    print "a is less than b and b is greater or equal to c";
  else
    print "Condition is false";
  end
  
  // Iterative Statement with Not Equal Operator
  while a != 0 do
    a := a - 1;
    if a <= 1 then
      print "a is less or equal to 1";
    end
    
    if not flag then
      print "Flag is false";
    else
      print "Flag is true";
    end
  end
  
  // Print Statement with Expression
  print "Final value of a: ", a, ", b: ", b, ", c: ", c;
  
  // Test String with Special Characters
  print "Special Characters: !@#$%^&*()";
  
  // Test Empty String
  print "";
  
  // Test String with Escaped Characters
  print "New line:\nTab:\t";
end.
"""

comprehensive_test_3 = """program comprehensive_test_3:
  // Variable Declarations
  int x, y, result;
  bool flag, condition;
  
  // Assignment and Arithmetic Operations
  x := 10;
  y := 20;
  result := x + y;
  
  // Conditional Statement with Relational Operators
  if x >= y or y > x then
    print "x is either greater than or equal to y, or y is greater than x";
  else
    print "Neither condition is true";
  end
  
  // Iterative Statement with Comparison and Boolean Operators
  while not flag and result != 0 do
    result := result - 1;
    if result <= 10 then
      flag := true;
    end
  end
  
  // Print Statement with Expressions and String Concatenation
  print "Final value of result: ", result, ", flag: ", flag;
  
  // Test String with Special Characters and Escaped Characters
  print "Special Characters: !@#$%^&*()\nNew line and Tab:\t";
  
  // Test Boolean Operations
  condition := true or false;
  print "Condition: ", condition;
  
  // Test Unary Operator
  print "Negative result: ", -result;
end.
"""

lexically_not_okay = """
  program lexically_not_Ok :
    intt a;
    int b;
    a :== 2;
    b := 5;
    while (ab) do not print else do
      int b;
      b := 2 *** a;
      print b^2;
      a := a $ 1
    end %;
    print b~
  end
"""

current_test = lexically_not_okay
lexer = Lexer(current_test)
print("\n" + current_test + "\n")
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
