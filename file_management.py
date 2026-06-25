import os

# making a function to create file.
def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"File {filename}: Created Successfully!")

    except FileExistsError:
        print(f"File {filename}: already exists!")

    except Exception as e:
        print('An error occurred!', e)

# making a function to view all file.
def view_all_files():
    files = os.listdir()
    if not files:
        print('NO files found!')
    else:
        print('Files in directory!')
        for file in files:
            print(file)
        
# making a function to delete file.
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully!")

    except FileNotFoundError:
        print("File not found!")

    except Exception as e:
        print('An error occurred!', e)

# making a function to read file.
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"Content of '{filename}' \n{content}")

    except FileNotFoundError:
        print(f"{filename}: Doesn't exist!")

    except Exception as e:
        print('An error occurred!', e)

# making a function to edit file.
def edit_file(filename):
    if not os.path.exists(filename):
        print(f"{filename}: Doesn't exist!")
        return

    try:
        with open(filename, 'a') as f:
            content = input('Enter data to add: ')
            f.write(content + '\n')
            print(f"Content added to {filename} successfully!")

    except Exception as e:
        print('An error occurred:', e)

# making a function to search a file.
def searching_file(filename):
    if not os.path.exists(filename):
        print(f"{filename}: Doesn't exist!")
        return
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"{filename} found \n{content}" )
    except Exception as e:
        print('An error occurred!', e)

#making a function to rename a file.
def rename_file(filename, newname):
    if not os.path.exists(filename):
        print(f"{filename}: doesn't exist!")
        return
    try:
        os.rename(filename, newname)
        print(f"{filename} has been renamed to {newname} successfully! ")

    except FileExistsError:
        print(f"The file '{newname}' already exists.")

    except Exception as e:
        print("An error occurred!", e)

#creating a function to remove all content in the file.
def clear_file(filename):
    if not os.path.exists(filename):
        print(f"{filename}: doesn't exist.")
        return
    try:
        with open(filename, 'w') as f:
            pass
        print(f"{filename} has been cleaned successfully!.")
    
    except Exception as e:
        print("An error occurred!", e)

# making a main function to get user choice.
def main():
    while True:
        #creating a main menu for user requirnments.
        print('------FILE MANAGEMENT APP------')
        print("1. Create File")
        print("2. View File")
        print("3. Delete File")
        print("4. Read File")
        print("5. Edit File")
        print("6. Search File")
        print("7. Rename File")
        print("8. Clear File")
        print("9. Exit")
        
        #for new creating file.
        choice = input('Enter your choice(1-9): ')
        if choice == '1':
            filename = input('Enter file name to create: ')
            create_file(filename)
        
        #to view all files.
        elif choice == '2':
            view_all_files()
        
        #to delete a single file.
        elif choice == '3':
            filename = input('Enter file name to delete: ')
            delete_file(filename)
        
        #to read a file.
        elif choice == '4':
            filename = input('Enter file name to read: ')
            read_file(filename)

        #to edit a file.
        elif choice == '5':
            filename = input('Enter file name to edit: ')
            edit_file(filename)

        #to search a file by name.
        elif choice == '6':
            filename = input('Enter file name to search: ')
            searching_file(filename)
        
        #to rename a exist file.
        elif choice == '7':
            old_file_name = input("Enter a file name which you want to rename: ")
            rename = input("Enter new file name: ")
            rename_file(old_file_name,rename)

        #for clearing all content in the file.
        elif choice == '8':
            filename = input("Enter file name to clear all content: ")
            clear_file(filename)
        
        #to close the program.
        elif choice == '9':
            print('Closing the app.....')
            break 

        #for invalid input from user.
        else:
            print('Invalid choice!')

if __name__ == '__main__':
    main()