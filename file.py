def file_read_write_challenge():
    """File Read & Write Challenge: Reads a file and writes a modified version to a new file."""
    try:
       
        input_file = input("Enter the name of the file to read: ")
        output_file = input("Enter the name of the output file: ")
        
       
        with open(input_file, 'r') as file:
            content = file.read()
        
       
        modified_content = content.upper()
        
       
        with open(output_file, 'w') as file:
            file.write(modified_content)
            
        print(f"File successfully modified and saved as {output_file}")
    
    except FileNotFoundError:
        print("Error: The input file was not found.")
    except PermissionError:
        print("Error: You don't have permission to access this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def error_handling_lab():
    """Error Handling Lab: Asks user for a filename and handles errors if it doesn't exist."""
    while True:
        filename = input("Enter a filename to check (or 'quit' to exit): ")
        
        if filename.lower() == 'quit':
            break
            
        try:
            
            with open(filename, 'r') as file:
                content = file.read()
            print(f"File '{filename}' exists and can be read successfully!")
            print(f"Preview of content:\n{content[:200]}...")  # Show first 200 chars
            
        except FileNotFoundError:
            print(f"Error: The file '{filename}' does not exist.")
        except PermissionError:
            print(f"Error: You don't have permission to read '{filename}'.")
        except UnicodeDecodeError:
            print(f"Error: Cannot decode the contents of '{filename}' as text.")
        except Exception as e:
            print(f"An unexpected error occurred with '{filename}': {str(e)}")

def main():
    print("File Handling and Exception Handling Assignment")
    print("1. File Read & Write Challenge")
    print("2. Error Handling Lab")
    print("3. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            file_read_write_challenge()
        elif choice == '2':
            error_handling_lab()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "_main_":
    main()