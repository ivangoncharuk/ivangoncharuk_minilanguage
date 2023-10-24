# Text File Reader

This Python script allows you to read from a text file character by character, displaying each character along with its position in the format `line_number:character_number character`.

## Prerequisites
- Python 3.x

## Functionalities
`__init__(self, filename)`: Initializes the FileReader object, opening the specified file and setting initial values for the current line, current column, and current character.

`nextChar(self)`: Reads the next character from the file, updating the current line, current column, and current character values accordingly. If the end of the file is reached, it sets the current character value to "ETX" (End of Text).

`currentChar(self)`: Returns the current character as a string.

`position(self)`: Returns a string containing the current line and column numbers, separated by a colon.

## How to Run
1. Place your text file in an accessible directory.
2. Navigate to the directory containing the `main.py` script in your terminal or command prompt.
3. Run the script using the following command:
`python3 src/main.py`

4. Follow the on-screen prompts to enter the path to your text file. The file must be inside the parent directory of the project itself, and not inside the /src/ directory.
Type '`quit`' or '`exit`' to stop the program.

## Example Output
For a text file containing "Hello there!", the output will look like this:

```
1:1 H
1:2 e
1:3 l
1:4 l
1:5 o
1:6  
1:7 t
1:8 h
1:9 e
1:10 r
1:11 e
1:12 !
```

## Author
Ivan Goncharuk
