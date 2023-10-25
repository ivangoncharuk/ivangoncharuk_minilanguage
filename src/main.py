import os
import lexer

class TestLexer:
    def __init__(self):
        self.lexer = lexer.Lexer("")
        self.examples = {
            1: ("Basic Arithmetic", "program example_1: int a, b; a := 5; b := 10; print a + b; end."),
            2: ("Conditional Statements", "program example_2: int x; x := 5; if x > 0 then print 'Positive'; else print 'Non-Positive'; end end."),
            3: ("While Loop", "program example_3: int i; i := 0; while i < 5 do print i; i := i + 1; end end."),
            4: ("Lexically Not OK", "program lexically_not_Ok: intt a; int b; a :== 2; b := 5; while (a!b) do not print else do int b@; b := 2 *** a; print b^2; a := a $ 1 end %; print b~ end."),
            5: ("Custom Example", ""),
            6: ("Test From File", "")
        }

    def run(self):
        while True:
            print("\nChoose an example to test the lexical analyzer:")
            for number, (name, _) in self.examples.items():
                print(f"{number}. {name}")
            print("0. Exit")

            choice = input("Enter the number of your choice: ")
            if not choice.isdigit():
                print("Please enter a valid number.")
                continue

            choice = int(choice)
            if choice == 0:
                print("Exiting.")
                break
            elif choice == 6:
                self.test_from_file()
            elif choice in self.examples:
                self.test_example(choice)
            else:
                print("Invalid choice. Please choose a valid example.")

    def test_from_file(self):
        file_name = input("\nEnter the name of the file to test (including extension): ")
        if not os.path.isfile(file_name):
            print(f"The file {file_name} does not exist.")
            return

        with open(file_name, 'r') as f:
            file_content = f.read()

        self.test_code(file_content)

    def test_example(self, example_number):
        if example_number == 5:
            example_code = input("\nEnter your custom example code:\n")
            self.test_code(example_code)
        else:
            example_name, example_code = self.examples[example_number]
            print(f"\nExample: {example_name}\nCode:\n{example_code}\n")
            self.test_code(example_code)

    def test_code(self, code):
        self.lexer.__init__(code)
        print("Tokens:")
        while True:
            self.lexer.next_token()
            if self.lexer.kind() == "end-of-text":
                break
            print(self.lexer.current_token)

if __name__ == "__main__":
    tester = TestLexer()
    tester.run()
