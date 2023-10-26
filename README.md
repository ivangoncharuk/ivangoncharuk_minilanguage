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

The output will look like this:
> Note: use option 6 to test from file.
```
% python3 src/main.py                                                           ✹

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
(  1 :  1  ) program      
(  1 :  9  ) ID            comprehensive_test_3
(  1 : 29  )               :
(  3 :  3  ) int          
(  3 :  7  ) ID            x
(  3 :  8  )               ,
(  3 : 10  ) ID            y
(  3 : 11  )               ,
(  3 : 13  ) ID            result
(  3 : 19  )               ;
(  4 :  3  ) bool         
(  4 :  8  ) ID            flag
(  4 : 12  )               ,
(  4 : 14  ) ID            condition
(  4 : 23  )               ;
(  7 :  3  ) ID            x
(  7 :  5  ) ASSIGN_OP     :=
(  7 :  8  ) NUM           10
(  7 : 10  )               ;
(  8 :  3  ) ID            y
(  8 :  5  ) ASSIGN_OP     :=
(  8 :  8  ) NUM           20
(  8 : 10  )               ;
(  9 :  3  ) ID            result
(  9 : 10  ) ASSIGN_OP     :=
(  9 : 13  ) ID            x
(  9 : 15  ) ADD_OP        +
(  9 : 17  ) ID            y
(  9 : 18  )               ;
( 12 :  3  ) if           
( 12 :  6  ) ID            x
( 12 :  8  ) RELATIONAL_OP >=
( 12 : 11  ) ID            y
( 12 : 13  ) or           
( 12 : 16  ) ID            y
( 12 : 18  ) RELATIONAL_OP >
( 12 : 20  ) ID            x
( 12 : 22  ) then         
( 13 :  5  ) print        
( 13 : 11  ) STRING        x is either greater than or equal to y, or y is greater than x
( 13 : 75  )               ;
( 14 :  3  ) else         
( 15 :  5  ) print        
( 15 : 11  ) STRING        Neither condition is true
( 15 : 38  )               ;
( 16 :  3  ) end          
( 19 :  3  ) while        
( 19 :  9  ) not          
( 19 : 13  ) ID            flag
( 19 : 18  ) and          
( 19 : 22  ) ID            result
( 19 : 29  ) RELATIONAL_OP !=
( 19 : 32  ) NUM           0
( 19 : 34  ) do           
( 20 :  5  ) ID            result
( 20 : 12  ) ASSIGN_OP     :=
( 20 : 15  ) ID            result
( 20 : 22  ) ADD_OP        -
( 20 : 24  ) NUM           1
( 20 : 25  )               ;
( 21 :  5  ) if           
( 21 :  8  ) ID            result
( 21 : 15  ) RELATIONAL_OP <
( 21 : 16  ) RELATIONAL_OP =
( 21 : 18  ) NUM           10
( 21 : 21  ) then         
( 22 :  7  ) ID            flag
( 22 : 12  ) ASSIGN_OP     :=
( 22 : 15  ) ID            true
( 22 : 19  )               ;
( 23 :  5  ) end          
( 24 :  3  ) end          
( 27 :  3  ) print        
( 27 :  9  ) STRING        Final value of result: 
( 27 : 34  )               ,
( 27 : 36  ) ID            result
( 27 : 42  )               ,
( 27 : 44  ) STRING        , flag: 
( 27 : 54  )               ,
( 27 : 56  ) ID            flag
( 27 : 60  )               ;
( 30 :  3  ) print        
( 30 :  9  ) STRING        Special Characters: !@#$%^&*()\nNew line and Tab:\t
( 30 : 62  )               ;
( 33 :  3  ) ID            condition
( 33 : 13  ) ASSIGN_OP     :=
( 33 : 16  ) ID            true
( 33 : 21  ) or           
( 33 : 24  ) ID            false
( 33 : 29  )               ;
( 34 :  3  ) print        
( 34 :  9  ) STRING        Condition: 
( 34 : 22  )               ,
( 34 : 24  ) ID            condition
( 34 : 33  )               ;
( 37 :  3  ) print        
( 37 :  9  ) STRING        Negative result: 
( 37 : 28  )               ,
( 37 : 30  ) ADD_OP        -
( 37 : 31  ) ID            result
( 37 : 37  )               ;
( 38 :  1  ) end          
( 38 :  4  )               .
( 38 :  5  ) end-of-text  

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
(  1 :  1  ) print      
(  1 :  7  ) STRING      Final value of result: 
(  1 : 32  )             ,
(  1 : 34  ) ID          result
(  1 : 40  )             ,
(  1 : 42  ) STRING      , flag: 
(  1 : 52  )             ,
(  1 : 54  ) ID          flag
(  1 : 58  )             ;
(  1 : 59  ) end-of-text

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
print "Final value of result: "; ^        

> Traceback...

SyntaxError: Unexpected symbol '^' at position (1, 34)
```

Author
Ivan Goncharuk
