## Overview

This Python program demonstrates file handling operations and exception handling techniques. It includes two main functionalities:

1. *File Read & Write Challenge*: Reads a file, modifies its content (converts to uppercase), and writes the modified version to a new file.
2. *Error Handling Lab*: Prompts the user for a filename and handles various file-related errors gracefully.

## Features

- Comprehensive error handling for common file operations
- User-friendly menu interface
- Clear error messages to guide the user
- Safe file operations with context managers (with statements)
- Sample file modification (uppercase conversion)

## How to Run

1. Ensure you have Python 3 installed on your system
2. Clone this repository or download the Python file
3. Run the program with:
   
   python file_handling_assignment.py
   
4. Follow the on-screen menu options

## Menu Options

1. *File Read & Write Challenge*
   - Enter the name of an existing file to read
   - Enter a name for the output file
   - The program will create a modified version of the input file

2. *Error Handling Lab*
   - Enter filenames to test
   - The program will check if the file exists and can be read
   - Type 'quit' to return to the main menu

3. *Exit*
   - Quits the program

## Error Handling

The program handles these exceptions gracefully:
- FileNotFoundError: When the specified file doesn't exist
- PermissionError: When the program lacks permission to access the file
- UnicodeDecodeError: When trying to read a non-text file
- General exceptions as a fallback

## Example Usage

1. Create a test file called sample.txt with some text content
2. Run the program and select option 1
3. Enter sample.txt as the input file
4. Enter output.txt as the output file
5. Check the new output.txt file containing the uppercase version of your text

## Requirements

- Python 3.x
- No additional libraries required

## Author

[Your Name]



