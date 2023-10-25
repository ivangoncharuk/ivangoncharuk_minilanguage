# Lexical Analyzer
This Python script serves as a lexical analyzer, taking a program written in a simplified programming language and breaking it down into tokens. Each token is associated with its type, value (if applicable), and position in the original text.

## Prerequisites
`Python 3.x`

## Functionalities
The Lexer class handles the tokenization of the input text.
`__init__(self, input_text)`: Initializes the Lexer object with the specified input text.
`next_token(self)`: Reads the next token from the input text. Updates the current_token attribute with the new token.
`kind(self)`: Returns the kind of the current token.
`value(self)`: Returns the value of the current token.
`position(self)`: Returns the position (line and character number) of the current token.

## How to Run
Navigate to the directory containing the `main.py` script in your terminal or command prompt.

Run the script using the following command:

> `python3 src/main.py`

Follow the on-screen prompts to choose an example to test, or input your own code.

## Testing Options
- **Predefined examples**: Choose from a list of predefined examples to see how the lexical analyzer tokenizes different constructs.
- **Custom example**: Input your own code directly into the terminal.
- **Test from file**: Input the name of a text file (including the extension) to test the lexical analyzer on the contents of that file.

## Example Output
For the input program...

```
program example:
int x;
x := 5;
print x;
end.
```

The output will look like this:

```
(1:1) program
(1:9) ID: example
(1:15) :
(2:1) int
(2:5) ID: x
(2:6) ;
(3:1) ID: x
(3:3) :=
(3:6) NUM: 5
(3:7) ;
(4:1) print
(4:7) ID: x
(4:8) ;
(5:1) end
(5:4) .
```


Author
Ivan Goncharuk
