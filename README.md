# Syntax Analyzer

## Overview
This Python script is a syntax analyzer that tests various programs for correct or incorrect syntax based on a defined grammar. The script allows you to test files with predefined correct or incorrect syntax, or to specify a custom file for syntax analysis.

- Supports full error handling!

## Requirements
- Python 3.11.6

## Running the Script

1. **Clone or Download the Repository**
   
   Ensure you have the project repository on your local machine. If not, clone or download it from its source.

2. **Navigate to the Project Directory**
   
   Open a terminal or command prompt and navigate to the root directory of the project.

   ```sh
   cd path/to/project
   ```

3. **Running the Syntax Analyzer**

   From the root directory of the project, execute the syntax analyzer script using Python. Depending on your system's configuration, you may use either `python` or `python3` as the command.

   ```sh
   python scripts/syntax_analyzer.py
   ```
   
   or

   ```sh
   python3 scripts/syntax_analyzer.py
   ```

   This will start the script and present you with a menu of options to test various syntax files.

## Script Options

- **Test Correct Syntax**: Test files with syntax that is expected to be correct.
- **Test Incorrect Syntax**: Test files with syntax that is expected to be incorrect.
- **Enter a Custom File Path**: Test a specific file by entering its file path.
- **Toggle Screen Clearing**: Enable or disable the clearing of the screen after each action.
- **Toggle Printing File Content**: Enable or disable the printing of a file's content before parsing it.
- **Exit**: Exit the script.

Follow the on-screen prompts to navigate through the options. Selecting an option for testing syntax will require you to choose a file from a provided list or enter a custom file path.

## Error Handling
  The analyzer supports full error handling. Here is what it might look like:

```
% python3 scripts/syntax_tester.py

1. Test Correct Syntax
2. Test Incorrect Syntax
3. Enter a custom file path
4. Toggle Screen Clearing (currently On)
5. Toggle Printing File Content (currently On)
0. Exit

Enter your choice: 2

1. ab1.txt
...
4. euclid-error.txt
...
10. print.txt

Enter your choice (0 to go back): 4

File Content: ... (will print file content if enabled.)

Parsing Output:

--- NOT OK ---

Syntax Error at Line 11, Column 14:
Unexpected token: 'RELATIONAL_OP'. Expected: Expected: 'true', 'false', 'NUM', 'ID', '('
9:    b := 20;
10:    print a;  print b;
11:    while a !== b do
                  ^
12:       if a < b then b := b - a
13:       else a := a - b
Error in file 'grammar-examples/incorrect-syntax/euclid-error.txt': Parsing failed due to syntax error.

Press Enter to continue...
```





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
Navigate to the directory containing the `lexer_tester.py` script in your terminal or command prompt.

Run the script using the following command:

> `python3 scripts/lexer_tester.py`

Follow the on-screen prompts to choose an example to test, or input your own code.

## Testing Options
- **Predefined examples**: Choose from a list of predefined examples to see how the lexical analyzer tokenizes different constructs.
- **Custom example**: Input your own code directly into the terminal.
- **Test from file**: Input the name of a text file (including the extension) to test the lexical analyzer on the contents of that file.

## Example Output
For the input program: `test_program.txt`

```
program comprehensive_test_3:
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
```

The output will look like this (using option 6)

```
% python3 src/main.py

Choose an example to test the lexical analyzer:
1. Basic Arithmetic
2. Conditional Statements
3. While Loop
4. Lexically Not OK
5. Custom Example
6. Test From File
0. Exit
Enter the number of your choice: 6

Enter the name of the file to test (including extension): test_program.txt
Tokens:
(  1 :  1 ) program
(  1 :  9 ) comprehensive_test_3                                           ID
(  1 : 29 ) :                                                             
(  3 :  3 ) int
(  3 :  7 ) x                                                              ID
(  3 :  8 ) ,                                                             
(  3 : 10 ) y                                                              ID
(  3 : 11 ) ,                                                             
(  3 : 13 ) result                                                         ID
(  3 : 19 ) ;                                                             
(  4 :  3 ) bool
(  4 :  8 ) flag                                                           ID
(  4 : 12 ) ,                                                             
(  4 : 14 ) condition                                                      ID
(  4 : 23 ) ;                                                             
(  7 :  3 ) x                                                              ID
(  7 :  5 ) :=                                                             ASSIGN_OP
(  7 :  8 ) 10                                                             NUM
(  7 : 10 ) ;                                                             
(  8 :  3 ) y                                                              ID
(  8 :  5 ) :=                                                             ASSIGN_OP
(  8 :  8 ) 20                                                             NUM
(  8 : 10 ) ;                                                             
(  9 :  3 ) result                                                         ID
(  9 : 10 ) :=                                                             ASSIGN_OP
(  9 : 13 ) x                                                              ID
(  9 : 15 ) +                                                              ADD_OP
(  9 : 17 ) y                                                              ID
(  9 : 18 ) ;                                                             
( 12 :  3 ) if
( 12 :  6 ) x                                                              ID
( 12 :  8 ) >=                                                             RELATIONAL_OP
( 12 : 11 ) y                                                              ID
( 12 : 13 ) or
( 12 : 16 ) y                                                              ID
( 12 : 18 ) >                                                              RELATIONAL_OP
( 12 : 20 ) x                                                              ID
( 12 : 22 ) then
( 13 :  5 ) print
( 13 : 11 ) x is either greater than or equal to y, or y is greater than x STRING
( 13 : 75 ) ;                                                             
( 14 :  3 ) else
( 15 :  5 ) print
( 15 : 11 ) Neither condition is true                                      STRING
( 15 : 38 ) ;                                                             
( 16 :  3 ) end
( 19 :  3 ) while
( 19 :  9 ) not
( 19 : 13 ) flag                                                           ID
( 19 : 18 ) and
( 19 : 22 ) result                                                         ID
( 19 : 29 ) !=                                                             RELATIONAL_OP
( 19 : 32 ) 0                                                              NUM
( 19 : 34 ) do
( 20 :  5 ) result                                                         ID
( 20 : 12 ) :=                                                             ASSIGN_OP
( 20 : 15 ) result                                                         ID
( 20 : 22 ) -                                                              ADD_OP
( 20 : 24 ) 1                                                              NUM
( 20 : 25 ) ;                                                             
( 21 :  5 ) if
( 21 :  8 ) result                                                         ID
( 21 : 15 ) <                                                              RELATIONAL_OP
( 21 : 16 ) =                                                              RELATIONAL_OP
( 21 : 18 ) 10                                                             NUM
( 21 : 21 ) then
( 22 :  7 ) flag                                                           ID
( 22 : 12 ) :=                                                             ASSIGN_OP
( 22 : 15 ) true                                                           ID
( 22 : 19 ) ;                                                             
( 23 :  5 ) end
( 24 :  3 ) end
( 27 :  3 ) print
( 27 :  9 ) Final value of result:                                         STRING
( 27 : 34 ) ,                                                             
( 27 : 36 ) result                                                         ID
( 27 : 42 ) ,                                                             
( 27 : 44 ) , flag:                                                        STRING
( 27 : 54 ) ,                                                             
( 27 : 56 ) flag                                                           ID
( 27 : 60 ) ;                                                             
( 30 :  3 ) print
( 30 :  9 ) Special Characters: !@#$%^&*()\nNew line and Tab:\t            STRING
( 30 : 62 ) ;                                                             
( 33 :  3 ) condition                                                      ID
( 33 : 13 ) :=                                                             ASSIGN_OP
( 33 : 16 ) true                                                           ID
( 33 : 21 ) or
( 33 : 24 ) false                                                          ID
( 33 : 29 ) ;                                                             
( 34 :  3 ) print
( 34 :  9 ) Condition:                                                     STRING
( 34 : 22 ) ,                                                             
( 34 : 24 ) condition                                                      ID
( 34 : 33 ) ;                                                             
( 37 :  3 ) print
( 37 :  9 ) Negative result:                                               STRING
( 37 : 28 ) ,                                                             
( 37 : 30 ) -                                                              ADD_OP
( 37 : 31 ) result                                                         ID
( 37 : 37 ) ;                                                             
( 38 :  1 ) end
( 38 :  4 ) .                                                             
( 38 :  5 ) end-of-text

Choose an example to test the lexical analyzer:
1. Basic Arithmetic
2. Conditional Statements
3. While Loop
4. Lexically Not OK
5. Custom Example
6. Test From File
0. Exit
Enter the number of your choice: 0
Exiting.
```

## Example Use (Custom Example)

```
% python3 src/main.py

Choose an example to test the lexical analyzer:
1. Basic Arithmetic
2. Conditional Statements
3. While Loop
4. Lexically Not OK
5. Custom Example
6. Test From File
0. Exit
Enter the number of your choice: 5

Enter your custom example code:
print "Final value of result: ", result, ", flag: ", flag;
Tokens:
(  1 :  1 ) print
(  1 :  7 ) Final value of result:  STRING
(  1 : 32 ) ,                      
(  1 : 34 ) result                  ID
(  1 : 40 ) ,                      
(  1 : 42 ) , flag:                 STRING
(  1 : 52 ) ,                      
(  1 : 54 ) flag                    ID
(  1 : 58 ) ;                      
(  1 : 59 ) end-of-text

Choose an example to test the lexical analyzer:
1. Basic Arithmetic
2. Conditional Statements
3. While Loop
4. Lexically Not OK
5. Custom Example
6. Test From File
0. Exit
Enter the number of your choice: 0
Exiting.
```

## Example Syntax Error Raised
```
% python3 src/main.py
Choose an example to test the lexical analyzer:
1. Basic Arithmetic
2. Conditional Statements
3. While Loop
4. Lexically Not OK
5. Custom Example
6. Test From File
0. Exit
Enter the number of your choice: 5

Enter your custom example code:
print "Final value of result: "; ^,!,***;

> Traceback...

SyntaxError: Unexpected symbol '^' at position (1, 34)
```

Removing the symbol '^' will result in another SyntaxError due to the '!' ('^' is replaced by the token ';')

```
> Menu Items...
Enter the number of your choice: 5

Enter your custom example code:
print "Final value of result: "; ,!,***;       
> Traceback...
SyntaxError: Unexpected symbol '!' at position (1, 35)
```

