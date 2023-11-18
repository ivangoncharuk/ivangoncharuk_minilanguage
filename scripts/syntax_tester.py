import os, sys
import glob

sys.path.append(".")  # need this to run
18
from src.lexer import Lexer  # Update this import as per your project structure
from src.syntax_analyzer import SyntaxAnalyzer  # Update this import as per your project structure

def test_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        lexer = Lexer(content)
        analyzer = SyntaxAnalyzer(lexer)
        try:
            analyzer.program()
            print(f"File '{file_path}' parsed without errors.")
        except Exception as e:
            print(f"Error in file '{file_path}': {e}")

def get_files_from_directory(directory_path):
    return glob.glob(os.path.join(directory_path, "*.txt"))  # Change extension if needed

def main():
    directory_path = "grammar-examples/correct-syntax"
    files = get_files_from_directory(directory_path)

    print("Choose a file to test:")
    for i, file_path in enumerate(files, start=1):
        print(f"{i}. {os.path.basename(file_path)}")

    print(f"{len(files) + 1}. Enter a custom file path")
    print(f"{len(files) + 2}. Exit")

    choice = int(input("Enter your choice: "))
    if choice > 0 and choice <= len(files):
        test_file(files[choice - 1])
    elif choice == len(files) + 1:
        custom_path = input("Enter the custom file path: ")
        test_file(custom_path)
    elif choice != len(files) + 2:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
