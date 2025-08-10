def read_and_modify_file():
    # Step 1: Ask user for input filename
    filename = input("Enter the filename to read: ")

    try:
        # Step 2: Try opening and reading the file
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        # Step 3: Modify content (example: make all text uppercase)
        modified_content = content.upper()

        # Step 4: Create a new file and write modified content
        new_filename = "modified_" + filename
        with open(new_filename, "w", encoding="utf-8") as new_file:
            new_file.write(modified_content)

        print(f"✅ File processed successfully! Modified file saved as '{new_filename}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"❌ Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    read_and_modify_file()
