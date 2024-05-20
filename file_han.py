try:
    # Attempt to open a file
    file = open("example.txt", "r")
    # Attempt to read the file
    content = file.read()
    # Attempt to print the content
    print(content)
    # Attempt to close the file
    file.close()
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("An error occurred while reading the file.")
except Exception as e:
    print("An unexpected error occurred:", str(e))
