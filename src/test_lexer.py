from lexer import Lexer, Token

test_input_1 = "var1 := 123; x := 456; y := 789"
test_input_2 = "if x < 10 then y := x + 1 end"
test_input_3 = "// This is a comment\nx := 5 // Another comment"

program_example_1 =  """program example1:
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

lexer = Lexer(program_example_3)
print("\n" + program_example_3 + "\n")
lexer.next_token()
print(lexer.position(), lexer.kind(), lexer.value() if lexer.value() is not None else "")
while lexer.kind() != 'end-of-text':
    lexer.next_token()
    print(lexer.position(), lexer.kind(), lexer.value() if lexer.value() is not None else "")
