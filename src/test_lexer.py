from lexer import Lexer, Token

test_input_1 = "var1 := 123; x := 456; y := 789"
test_input_2 = "if x < 10 then y := x + 1 end"
test_input_3 = "// This is a comment\nx := 5 // Another comment"


lexer = Lexer(test_input_2)
lexer.next_token()
print(lexer.position(), lexer.kind(), lexer.value() if lexer.value() is not None else "")
while lexer.kind() != 'end-of-text':
    lexer.next_token()
    print(lexer.position(), lexer.kind(), lexer.value() if lexer.value() is not None else "")
