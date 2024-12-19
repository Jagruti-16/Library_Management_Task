from flask import Flask, request, jsonify
from models import db, Book, Member

app = Flask(__name__)

# Configure the database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database
db.init_app(app)


with app.app_context():
    db.create_all()


# ----------------- Book Routes -----------------

@app.route("/add_book", methods=["POST"])
def create_book():
    data = request.json
    book = Book(title=data["title"], author=data["author"], year=data["year"], copies=data["copies"])
    db.session.add(book)
    db.session.commit()
    return jsonify(book.to_dict()), 201

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify(book.to_dict()), 200

@app.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books]), 200


@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.json
    book = Book.query.get(book_id)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    book.title = data.get("title", book.title)
    book.author = data.get("author", book.author)
    book.year = data.get("year", book.year)
    book.copies = data.get("copies", book.copies)
    db.session.commit()
    return jsonify(book.to_dict()), 200


@app.route("/delete_book/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted successfully"}), 200


# ----------------- Member Routes -----------------

@app.route("/add_member", methods=["POST"])
def create_member():
    data = request.json
    if Member.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "Email already exists"}), 400
    member = Member(name=data["name"], email=data["email"])
    db.session.add(member)
    db.session.commit()
    return jsonify(member.to_dict()), 201


@app.route("/members", methods=["GET"])
def get_members():
    members = Member.query.all()
    return jsonify([member.to_dict() for member in members]), 200


@app.route("/members/<int:member_id>", methods=["GET"])
def get_member(member_id):
    member = Member.query.get(member_id)
    if member is None:
        return jsonify({"error": "Member not found"}), 404
    return jsonify(member.to_dict()), 200


@app.route("/update_member/<int:member_id>", methods=["PUT"])
def update_member(member_id):
    data = request.json
    member = Member.query.get(member_id)
    if member is None:
        return jsonify({"error": "Member not found"}), 404
    member.name = data.get("name", member.name)
    if "email" in data and data["email"] != member.email:
        if Member.query.filter_by(email=data["email"]).first():
            return jsonify({"error": "Email already exists"}), 400
        member.email = data["email"]
    db.session.commit()
    return jsonify(member.to_dict()), 200


@app.route("/delete_member/<int:member_id>", methods=["DELETE"])
def delete_member(member_id):
    member = Member.query.get(member_id)
    if member is None:
        return jsonify({"error": "Member not found"}), 404
    db.session.delete(member)
    db.session.commit()
    return jsonify({"message": "Member deleted successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)