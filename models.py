from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = 'books'

    # Define columns
    book_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Auto-incrementing primary key
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    copies = db.Column(db.Integer, nullable=False)

    # Constructor method is optional, SQLAlchemy will automatically use the default constructor
    def __init__(self, title, author, year, copies):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    # Method to convert object to dictionary (useful for returning API responses)
    def to_dict(self):
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'copies': self.copies
        }

class Member(db.Model):
    __tablename__ = 'members'

    # Define columns
    member_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Auto-incrementing primary key
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    # Constructor method
    def __init__(self, name, email):
        self.name = name
        self.email = email

    # Method to convert object to dictionary (useful for returning API responses)
    def to_dict(self):
        return {
            'member_id': self.member_id,
            'name': self.name,
            'email': self.email
        }
