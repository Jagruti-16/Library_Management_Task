from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = 'books'

    
    book_id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    copies = db.Column(db.Integer, nullable=False)

    def __init__(self, title, author, year, copies):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies
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
    member_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

   
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_dict(self):
        return {
            'member_id': self.member_id,
            'name': self.name,
            'email': self.email
        }
