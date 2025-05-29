# Student Database Management System

This project is a **desktop application** built using **Python (Tkinter GUI)** and **Microsoft Access Database**. It provides a simple interface to manage student records, including functionalities to insert, update, delete, search, and navigate through records.

---

## Features

* **Insert** new student records
* **Update** existing records
* **Delete** records based on CNIC
* **Search** records by CNIC
* **Navigate** through records (First, Next, Previous, Last)
* **Clear** form fields
* Real-time feedback messages

---

## Technologies Used

| Component     | Details                     |
| ------------- | --------------------------- |
| Language      | Python                      |
| GUI Framework | Tkinter                     |
| Database      | Microsoft Access (`.accdb`) |
| DB Library    | pyodbc                      |

---

## 📁 Project Structure

```plaintext
student_database_app.py     # Main application script
Database.accdb              # Microsoft Access Database file (ensure path is correct)
README.md                   # Project documentation
```

---

## How to Run

1. **Install Requirements:**

   Ensure you have `pyodbc` installed:

   ```bash
   pip install pyodbc
   ```

2. **Check ODBC Driver:**

   Make sure you have the *Microsoft Access Driver (*.mdb, *.accdb)* installed on your system.

3. **Update Database Path:**

   Edit this line in the script if your database is stored elsewhere:

   ```python
   DBQ=C:\Users\vahee\Desktop\Database.accdb
   ```

4. **Run the Application:**

   ```bash
   python student_database_app.py
   ```

---

## Table Schema (Table1)

Make sure your MS Access table (`Table1`) has the following fields:

| Field Name  | Data Type | Description         |
| ----------- | --------- | ------------------- |
| CNIC        | Text      | Primary Key         |
| StudentName | Text      | Student's full name |
| FatherName  | Text      | Father's name       |
| CITY        | Text      | City name           |
| MARKS       | Number    | Student's marks     |

---

## Known Issues / Notes

* Record navigation may throw errors if there are no more records to move next or previous. Consider adding boundary checks.
* The CNIC field must be **unique**, as it is used as the primary key.
* Ensure the MS Access driver is correctly installed on your system, especially for 64-bit Python.



