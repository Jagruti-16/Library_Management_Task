Library Management System
This is a Flask-based API for managing books and members in a library system. The API provides endpoints for CRUD operations on books and members, with support for pagination.

How to Run the Project

Clone the Repository:

git clone https://github.com/Jagruti-16/Library_Management_Task.git 
cd Library_Management_Task

Set up a Virtual Environment:

python -m venv venv 
use venv\Scripts\activate

Install Dependencies:

pip install -r requirements.txt

python app.py
Test the Application
Run unit tests to ensure everything works correctly:

python -m unittest discover


Design Choices Made
Framework: Used Flask for its simplicity and flexibility in building RESTful APIs.
Database: SQLite is chosen for simplicity during development. SQLAlchemy ORM is used for interacting with the database.
Pagination: Added pagination to the GET endpoints for books and members to handle large datasets efficiently.
Query parameters page and per_page allow clients to control pagination.
Pagination metadata is included in the response for better clarity.
Error Handling: Ensured proper error messages are returned for missing or invalid resources.
Unit Testing: Comprehensive tests using unittest to validate API functionality.
Assumptions and Limitations
Assumptions
Each book's title and author combination is unique in the library.
Members are identified uniquely by their email addresses.
Pagination defaults:
If page or per_page is not provided, defaults are applied (page=1, per_page=10).
JSON format is used for all request payloads and responses.
Limitations
Database: SQLite is not ideal for production environments. Replace with a more robust database (e.g., PostgreSQL) for deployment.
Authentication: No authentication or authorization is implemented, making it insecure for public use.
Pagination Defaults: The API does not validate extremely large per_page values, which could affect performance.