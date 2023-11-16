
# The Syntax

## Program Structure
- **Program:** `program Identifier : Body .`

## Body
- **Body:** `[ Declarations ] Statements .`

## Declarations
- **Declarations:** `Declaration { Declaration } .`
- **Declaration:** `( "bool" | "int" ) Identifier { "," Identifier } ;`

## Statements
- **Statements:** `Statement { ";" Statement } .`
- **Statement:** `AssignmentStatement | ConditionalStatement | IterativeStatement | PrintStatement .`

### Types of Statements
- **AssignmentStatement:** `Identifier := Expression .`
- **ConditionalStatement:** `if Expression then Body [ "else" Body ] end .`
- **IterativeStatement:** `while Expression do Body end .`
- **PrintStatement:** `print Expression .`

## Expressions
- **Expression:** `SimpleExpression [ RelationalOperator SimpleExpression ] .`
- **RelationalOperator:** `< | =< | = | != | >= | > .`
- **SimpleExpression:** `Term { AdditiveOperator Term } .`
- **AdditiveOperator:** `+ | - | or .`
- **Term:** `Factor { MultiplicativeOperator Factor } .`
- **MultiplicativeOperator:** `* | / | mod | and .`
- **Factor:** `[ UnaryOperator ] (Literal | Identifier | "(" Expression ")" ) .`
- **UnaryOperator:** `- | not .`

## Literals and Identifiers
- **Literal:** `BooleanLiteral | IntegerLiteral .`
- **BooleanLiteral:** `false | true .`
- **IntegerLiteral:** `Digit { Digit } .`
- **Identifier:** `Letter { Letter | Digit | "_" } .`
- **Digit:** `0-9`
- **Letter:** `a-z | A-Z`

# Comments

1. **Integer literals and identifiers are treated as terminal symbols.**
2. **White space is allowed anywhere, except within terminal symbols.**
3. **A comment begins with a double slash ("//") and terminates at the end of the line.**
4. **"Maximum munch" rule applies. For example, "if1" is an identifier, not an "if" followed by a "1".**
5. **The scope of a variable is from its declaration to the end of the nearest enclosing body. Standard rules for hiding (a.k.a. shadowing) apply.**

---

# Example Programs

## Factorial
This program calculates the factorial of a given number. It demonstrates the use of iterative statements (while), conditional statements (if), and basic arithmetic operations.
```
program factorial:
    int num, result;

    // Initialize variables
    num := 5;
    result := 1;

    // Calculate factorial
    while num > 1 do
        result := result * num;
        num := num - 1;
    end;

    // Print result
    print result
    .
```

## Check Prime Number
This program checks whether a given number is prime or not. It utilizes conditionals, iteratives, and relationals.
```
program checkPrime:
    int number, i, flag;

    // Initialize variables
    number := 17;
    flag := 0;
    i := 2;

    // Check for prime number
    while i <= number / 2 do
        if number mod i = 0 then
            flag := 1;
            break;
        end;
        i := i + 1;
    end;

    // Print result
    if flag = 0 then
        print true;  // Number is prime
    else
        print false; // Number is not prime
    end
    .
```

## Calculate Sum of Numbers
This program calculates the sum of all numbers up to a specified limit. It's a good example of using a while loop to accumulate.

```
program sumNumbers:
    int limit, sum, i;

    // Initialize variables
    limit := 10;
    sum := 0;
    i := 1;

    // Calculate sum
    while i <= limit do
        sum := sum + i;
        i := i + 1;
    end;

    // Print the sum
    print sum
    .
```

## Fibonnacci Sequence
This program generates the Fibonacci sequence up to a certain number. It shows the use of iterative statements and assignment operations to compute a series.

```
program fibonacci:
    int n, first, second, next, c;

    // Initialize variables
    n := 10;
    first := 0;
    second := 1;
    c := 0;

    // Print the first two terms
    print first;
    print second;

    // Generate the rest of the sequence
    while c < n - 2 do
        next := first + second;
        first := second;
        second := next;
        print next;
        c := c + 1;
    end
    .
```

---

# Examples of Incorrect Grammar

## Missing Semicolons
This example omits necessary semicolons, leading to syntax errors.
```
program missingSemicolons
    int a, b, sum

    a := 10
    b := 20
    sum := a + b

    print sum
```

### Errors

- Missing semicolon after program missingSemicolons.
- Missing semicolons at the end of variable declarations and assignment statements.
- Missing period at the end of the program.

## Invalid Loop
This example demonstrates incorrect usage of the while loop syntax.
```
program invalidLoop:
    int count

    count := 1

    while count <= 5
        print count
        count := count + 1
    done
```

### Errors

- Missing semicolons after variable declaration and assignment statements.
while loop syntax is incorrect; it should end with end instead of done.
- Missing do keyword in the while loop.
- Missing period at the end of the program.

## Invalid Conditional

This example has an improperly structured if statement.
```
program wrongIf:
    bool check
    check := true

    if check
    print "It's true"
    else
    print "It's false"
```

- Missing semicolons after variable declaration and assignment statements.
The if and else blocks are incorrectly structured; they should be enclosed in then ... end.
- Missing then keyword after the if condition.