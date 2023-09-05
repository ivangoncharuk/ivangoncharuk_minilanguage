from file_reader import FileReader

def main():
    while True:
        filename = input("Enter the filename (or 'quit' to exit): ")
        
        if filename.lower() in ["quit", "exit"]:
            break

        try:
            fr = FileReader(filename)
        except FileNotFoundError:
            print("File not found. Please try again.")
            continue

        fr.nextChar()
        while fr.currentChar() != "ETX":
            print(fr.position() + " " + fr.currentChar())
            fr.nextChar()

if __name__ == "__main__":
    main()
