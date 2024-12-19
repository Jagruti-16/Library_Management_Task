Library Management System
A Flask-based Library Management System to manage books and members with features like adding, retrieving, updating, and deleting books and members.

Features
Add, update, delete, and retrieve books.
Add, update, delete, and retrieve members.

How to Run the Project
Prerequisites
Python 3.x
Flask
SQLAlchemy
Installation
Clone the repository:

git clone https://github.com/your-username/library-management.git
Navigate to the project folder:

cd library-management
Create a virtual environment:

python -m venv venv
Activate the virtual environment:

On Windows:

venv\Scripts\activate
On macOS/Linux:


source venv/bin/activate
Install dependencies:

pip install -r requirements.txt
Set the Flask environment variables and run the app:

set FLASK_APP=app.py  # For Windows
set FLASK_ENV=development  # For Windows
flask run
Or on macOS/Linux:

export FLASK_APP=app.py
export FLASK_ENV=development
flask run
Access the Application
Open your browser and visit:
http://127.0.0.1:5000
Design Choices
Flask was chosen for its simplicity and flexibility in building APIs.
SQLite was used as the database for simplicity, ideal for small-scale projects.
SQLAlchemy ORM is used for database interaction.
