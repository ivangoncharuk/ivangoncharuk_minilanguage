from lexer import Lexer, Token

test_input_1 = "var1 := 123; x := 456; y := 789"
lexer = Lexer(test_input_1)
token = lexer.next_token()
while token and token.kind != "end-of-text":
    print(token)
    token = lexer.next_token()

