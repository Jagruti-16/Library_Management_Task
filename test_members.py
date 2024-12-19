import unittest
from app import app, db
from models import Member

class TestMembers(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.client = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_member(self):
        response = self.client.post(
            "/add_member",
            json={
                "name": "John Doe",
                "email": "johndoe@example.com"
            }
        )
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data["name"], "John Doe")
        self.assertEqual(data["email"], "johndoe@example.com")

    def test_get_members(self):
        with app.app_context():
            member = Member(name="Jane Doe", email="janedoe@example.com")
            db.session.add(member)
            db.session.commit()

        response = self.client.get("/members")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], "Jane Doe")

    def test_update_member(self):
        with app.app_context():
            member = Member(name="Old Name", email="oldemail@example.com")
            db.session.add(member)
            db.session.commit()

        response = self.client.put(
            "/update_member/1",
            json={"name": "New Name"}
        )
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["name"], "New Name")

    def test_delete_member(self):
        with app.app_context():
            member = Member(name="To Be Deleted", email="delete@example.com")
            db.session.add(member)
            db.session.commit()

        response = self.client.delete("/delete_member/1")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("Member deleted successfully", data["message"])

    def test_get_member_by_id(self):
        with app.app_context():
            member = Member(name="Single Member", email="singlemember@example.com")
            db.session.add(member)
            db.session.commit()

        response = self.client.get("/members/1")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["name"], "Single Member")
        self.assertEqual(data["email"], "singlemember@example.com")    

if __name__ == "__main__":
    unittest.main()
