import unittest
from app import app, db
from models import Book

class TestBooks(unittest.TestCase):
    def setUp(self):
        # Set up test environment
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.client = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Clean up after tests
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_book(self):
        response = self.client.post(
            "/add_book",
            json={
                "title": "Book A",
                "author": "Author A",
                "year": 2020,
                "copies": 3
            }
        )
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data["title"], "Book A")

    def test_get_books(self):
        with app.app_context():
            book = Book(title="Book B", author="Author B", year=2021, copies=5)
            db.session.add(book)
            db.session.commit()

        response = self.client.get("/books")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)

    def test_update_book(self):
        with app.app_context():
            book = Book(title="Old Title", author="Old Author", year=2019, copies=2)
            db.session.add(book)
            db.session.commit()

        response = self.client.put(
            "/books/1",
            json={"title": "New Title"}
        )
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["title"], "New Title")

    def test_delete_book(self):
        with app.app_context():
            book = Book(title="To Be Deleted", author="Author D", year=2022, copies=1)
            db.session.add(book)
            db.session.commit()

        response = self.client.delete("/delete_book/1")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("Book deleted successfully", data["message"])

    def test_get_book_by_id(self):
        with app.app_context():
            book = Book(title="Single Book", author="Author Single", year=2023, copies=1)
            db.session.add(book)
            db.session.commit()

        response = self.client.get("/books/1")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["title"], "Single Book")
        self.assertEqual(data["author"], "Author Single")
        self.assertEqual(data["year"], 2023)
        self.assertEqual(data["copies"], 1)    

   

if __name__ == "__main__":
    unittest.main()
