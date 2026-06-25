# 📂 File Management App (Python)

A simple command-line File Management System built with Python. This application allows users to create, read, edit, rename, search, delete, and manage files directly from the terminal.

## 🚀 Features

* ✅ Create new files
* ✅ View all files in the current directory
* ✅ Read file contents
* ✅ Edit and append data to files
* ✅ Search files
* ✅ Rename existing files
* ✅ Delete files
* ✅ Clear all content from a file
* ✅ Error handling for missing files and invalid operations

---

## 🛠️ Technologies Used

* Python 3
* OS Module (`os`)

---

## 📂 Project Structure

```text
File-Management-App/
│
├── file_management.py
└── README.md
```

---

## 📖 Functionalities

### 1. Create File

Creates a new file in the current directory.

### 2. View Files

Displays all files available in the current working directory.

### 3. Delete File

Deletes a specified file permanently.

### 4. Read File

Displays the contents of a selected file.

### 5. Edit File

Appends new text to an existing file.

### 6. Search File

Searches for a file and displays its contents if found.

### 7. Rename File

Renames an existing file.

### 8. Clear File

Removes all content from a file without deleting the file itself.

### 9. Exit

Closes the application.

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/tayyab-ali2/File-management-app.git
```

### Move into Project Directory

```bash
cd file-management-app
```

### Run the Application

```bash
python file_management.py
```

---

## 📋 Menu Preview

```text
------FILE MANAGEMENT APP------

1. Create File
2. View File
3. Delete File
4. Read File
5. Edit File
6. Search File
7. Rename File
8. Clear File
9. Exit
```

---

## 💻 Example Usage

### Create a File

```text
Enter file name to create: notes.txt

File notes.txt: Created Successfully!
```

### Edit a File

```text
Enter file name to edit: notes.txt
Enter data to add: Learning Python

Content added to notes.txt successfully!
```

### Read a File

```text
Enter file name to read: notes.txt

Content of 'notes.txt'

Learning Python
```

### Rename a File

```text
Enter a file name which you want to rename: notes.txt
Enter new file name: mynotes.txt

notes.txt has been renamed to mynotes.txt successfully!
```

---

## 🎯 Learning Objectives

This project demonstrates:

* Python Functions
* File Handling
* OS Module Usage
* Exception Handling
* User Input Processing
* CRUD Operations on Files
* Command Line Applications

---

## ⚠️ Error Handling

The application handles common errors such as:

* File already exists
* File not found
* Invalid operations
* Unexpected exceptions

---

## 👨‍💻 Author

Developed by Tayyab ali

---

## 📜 License

This project is open-source and available under the MIT License.
