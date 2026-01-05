# Library Management System - Usage Examples

## Running the Program

```bash
python library.py
```

## Sample Workflow

### Example 1: Adding Books

**Input:**
```
Enter your choice: 1
Enter book id: 101
Enter book name: Python Programming
Enter author name: John Doe
Enter price: 29.99
Enter number of copies: 10
```

**Output:**
```
Book Record Saved
Press any key to continue..
```

### Example 2: Listing All Books

**Input:**
```
Enter your choice: 4
```

**Output:**
```
List of All Books
<<<<<<<<<<<<=========>>>>>>>>>>>>>>
bookid			bookname			bauthor				price				copies					
101			Python Programming		John Doe			29.99				10.0
102			Data Science			Jane Smith			35.50				5.0
103			Web Development			Bob Johnson			27.99				8.0
-------------------------------
```

### Example 3: Modifying a Book

**Input:**
```
Enter your choice: 2
Enter bookid whose record you want to modify: 101
Do you want to modify this Book Record(y/n): y
Enter new book id: 101
Enter new book name: Advanced Python Programming
Enter new author name: John Doe
Enter new price: 34.99
Enter new number of copies: 15
```

**Output:**
```
Book Record Modified
Press any key to continue..
```

### Example 4: Deleting a Book

**Input:**
```
Enter your choice: 3
Enter bookid whose record you want to delete: 103
Do you want to delete this Book Record(y/n): y
```

**Output:**
```
Book Record Deleted....
Press any key to continue..
```

### Example 5: Exiting the Program

**Input:**
```
Enter your choice: 5
```

**Output:**
```
Software Terminated.......
```

## Notes

- Book IDs are entered as integers
- Prices and copies can be decimal values
- All data is saved in `library.csv` file
- The program uses a simple menu-driven interface
- Always confirm before modifying or deleting records
