import os, sys
import glob
import subprocess

sys.path.append(".")  # need this to run
from src.lexer import Lexer
from src.syntax_analyzer import SyntaxAnalyzer


def test_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            lexer = Lexer(content)
            analyzer = SyntaxAnalyzer(lexer)
            analyzer.program()
            print(f"File '{file_path}' parsed without errors.")
    except Exception as e:
        print(f"Error in file '{file_path}': {e}")


def get_files_from_directory(directory_path):
    return glob.glob(
        os.path.join(directory_path, "*.txt")
    )  # Change extension if needed


def list_files_and_get_choice(files):
    for i, file_path in enumerate(files, start=1):
        print(f"{i}. {os.path.basename(file_path)}")
    choice = int(input("Enter your choice (0 to go back): "))
    return choice


def clear_screen():
    if os.name == "nt":  # for Windows
        subprocess.call("cls", shell=True)
    else:  # for MacOS and Linux
        subprocess.call("clear", shell=True)


def main():
    while True:
        clear_screen()
        print("\n1. Test Correct Syntax")
        print("2. Test Incorrect Syntax")
        print("3. Enter a custom file path")
        print("0. Exit")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            files = get_files_from_directory("grammar-examples/correct-syntax")
            print("\nChoose a file with correct syntax:")
            file_choice = list_files_and_get_choice(files)
            if 0 < file_choice <= len(files):
                test_file(files[file_choice - 1])

        elif choice == 2:
            files = get_files_from_directory("grammar-examples/incorrect-syntax")
            print("\nChoose a file with incorrect syntax:")
            file_choice = list_files_and_get_choice(files)
            if 0 < file_choice <= len(files):
                test_file(files[file_choice - 1])

        elif choice == 3:
            custom_path = input("\nEnter the custom file path: ")
            test_file(custom_path)

        elif choice == 0:
            clear_screen()
            print("Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
