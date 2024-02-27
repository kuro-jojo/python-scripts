
''' This is a simple program to copy the contents of a file into the clipboard. '''
import sys
import pyperclip

def main():
    # Read input from stdin
    content = ""
    for line in sys.stdin:
        content += line
    
    pyperclip.copy(content)
    
if __name__ == "__main__":
    main()