
from src.file_reader import FileReader

if __name__ == "__main__":
    reader = FileReader()
    while True:
        # prompting user for a file name
        file_name = input("Please enter the file name or type 'quit' to exit: ")
        
        if file_name.lower() in ['quit', 'exit']: break

        #todo validate and read the file into reader.file_buffer here

        # init the nextChar call
        reader.nextChar()

        # main loop 
        while reader.currentChar() != "ETX":
            print(reader.position() + " " + reader.currentChar())
            reader.nextChar()
