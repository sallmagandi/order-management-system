# Order Management System

A robust Python terminal application designed for order management, powered by a persistent SQLite database.

## 🚀 About the Project
This is my **very first independent programming project**, created during my first week of learning Python and backend development from complete scratch. 

Originally built using temporary in-memory structures, I completely refactored the application to integrate a persistent relational database. I designed the automated **Unique Order ID** tracker using SQL primary keys, built modular functions for database operations, and implemented secure data storage that survives application restarts.

*Note: This is a pet project built entirely for educational purposes to master Python fundamentals and the basics of Database Management Systems (DBMS).*

## 🛠️ Features
- **Auto-Initialization**: Automatically checks for the database file and creates the required tables with correct schemas upon startup.
- **Add Orders**: Saves item choices securely into a persistent database using structured SQL queries with auto-incremented IDs.
- **View Orders**: Validates if the database queue is empty and cleanly displays active records via formatted loops.
- **Deliver Orders**: Dynamically targets a specific record by its unique ID, removes it upon completion, and updates the database file.
- **Clear Orders**: Instantly wipes the entire database table to reset the kitchen queue for the next shift using automated transaction commits.
- **Close Shift**: Safely terminates the execution loop and gracefully closes the database connection to prevent memory leaks.

## 💻 Tech Stack
- **Language**: Python 3.x
- **Database**: SQLite3 (Embedded Relational DBMS)
- **Concepts used**: Database Connections (`.connect`), SQL Queries (`INSERT`, `SELECT`, `DELETE`), Transaction Commits (`.commit`), cursors, Functions (`def`), Loops (`while`, `for`), Lists, Error-catching.

---
*Created by [sallmagandi](https://github.com) as a milestone in my 2-year journey to becoming a professional software engineer.*
