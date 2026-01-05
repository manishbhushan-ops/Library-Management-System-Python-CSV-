# Library Management System (Python, CSV)

A simple command-line library management system built with Python that uses CSV files for data storage.

## Features

- **Add Books**: Add new book records to the library
- **Modify Books**: Update existing book information
- **Delete Books**: Remove books from the library
- **List Books**: Display all books in a formatted table

## Book Information Stored

Each book record contains:
- Book ID (integer)
- Book Name (string)
- Author Name (string)
- Price (float)
- Number of Copies (float)

## Requirements

- Python 3.x
- No external dependencies (uses built-in `csv` and `os` modules)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/manishbhushan-ops/Library-Management-System-Python-CSV-.git
cd Library-Management-System-Python-CSV-
```

## Usage

Run the library management system:
```bash
python library.py
```

### Menu Options

1. **Add a new Book Record**: Enter book details to add to the library
2. **Modify Existing Book Record**: Update information for an existing book
3. **Delete Existing Book Record**: Remove a book from the library
4. **List all Books**: View all books in the library
5. **Exit**: Close the application

### Example Usage

1. Start the program and select option 1 to add a book
2. Enter the requested information (book id, name, author, price, copies)
3. The book will be saved to `library.csv`
4. Use option 4 to view all books in the library

## Data Storage

All book data is stored in `library.csv` file in the same directory as the script. The file is created automatically when you add the first book.

## Notes

- The system uses `\r\n` as the line terminator for CSV files
- A temporary file (`temp.csv`) is created during modify and delete operations
- Book IDs should be unique to avoid confusion

## License

This project is open source and available for educational purposes.