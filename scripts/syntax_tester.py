import os, sys
import glob
import subprocess

sys.path.append(".")  # need this to run
from src.lexer import Lexer
from src.syntax_analyzer import SyntaxAnalyzer

should_clear_screen = True  # Default setting for clearing screen content
should_print_content = True  # Default setting for printing file content


def test_file(file_path):
    global should_print_content
    try:
        with open(file_path, "r") as file:
            content = file.read()
            if should_print_content:
                print("\nFile Content:")
                print(content)
                print("\nParsing Output:")
            lexer = Lexer(content)
            analyzer = SyntaxAnalyzer(lexer)
            analyzer.program()
            print(f"File '{file_path}' parsed without errors.")
    except Exception as e:
        print(f"Error in file '{file_path}': {e}")


def get_files_from_directory(directory_path):
    return glob.glob(os.path.join(directory_path, "*.txt"))


def list_files_and_get_choice(files):
    for i, file_path in enumerate(files, start=1):
        print(f"{i}. {os.path.basename(file_path)}")
    choice = int(input("\nEnter your choice (0 to go back): "))
    return choice


def clear_screen():
    global should_clear_screen
    if should_clear_screen:
        if os.name == "nt":  # for Windows
            subprocess.call("cls", shell=True)
        else:  # for MacOS and Linux
            subprocess.call("clear", shell=True)


def toggle_setting(setting_name):
    global should_clear_screen, should_print_content
    if setting_name == "clear_screen":
        should_clear_screen = not should_clear_screen
        print(f"Screen clearing {'enabled' if should_clear_screen else 'disabled'}.")
    elif setting_name == "print_content":
        should_print_content = not should_print_content
        print(
            f"Printing file content {'enabled' if should_print_content else 'disabled'}."
        )


def pause():
    input("\nPress Enter to continue...")


def main():
    while True:
        print("\n1. Test Correct Syntax")
        print("2. Test Incorrect Syntax")
        print("3. Enter a custom file path")
        print(
            "4. Toggle Screen Clearing (currently {})".format(
                "On" if should_clear_screen else "Off"
            )
        )
        print(
            "5. Toggle Printing File Content (currently {})".format(
                "On" if should_print_content else "Off"
            )
        )
        print("0. Exit")

        choice = int(input("\nEnter your choice: "))
        if should_clear_screen:
            clear_screen()

        if choice == 1 or choice == 2:
            directory = (
                "grammar-examples/correct-syntax"
                if choice == 1
                else "grammar-examples/incorrect-syntax"
            )
            files = get_files_from_directory(directory)
            print()
            file_choice = list_files_and_get_choice(files)
            if 0 < file_choice <= len(files):
                test_file(files[file_choice - 1])

        elif choice == 3:
            custom_path = input("\nEnter the custom file path: ")
            test_file(custom_path)

        elif choice == 4:
            toggle_setting("clear_screen")

        elif choice == 5:
            toggle_setting("print_content")

        elif choice == 0:
            print("Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")

        pause()
        if should_clear_screen:
            clear_screen()


if __name__ == "__main__":
    main()
