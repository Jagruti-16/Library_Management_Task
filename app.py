from flask import Flask, request, jsonify
from models import db, Book, Member

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


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
    page = request.args.get("page", default=1, type=int) 
    per_page = request.args.get("per_page", default=10, type=int)

   
    books_query = Book.query.paginate(page=page, per_page=per_page, error_out=False)
    
    
    books = [book.to_dict() for book in books_query.items]
    response = {
        "books": books,
        "pagination": {
            "total_items": books_query.total,
            "total_pages": books_query.pages,
            "current_page": books_query.page,
            "per_page": books_query.per_page,
        },
    }
    return jsonify(response), 200



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
    page = request.args.get("page", default=1, type=int) 
    per_page = request.args.get("per_page", default=10, type=int) 

    
    members_query = Member.query.paginate(page=page, per_page=per_page, error_out=False)

    members = [member.to_dict() for member in members_query.items]
    response = {
        "members": members,
        "pagination": {
            "total_items": members_query.total,
            "total_pages": members_query.pages,
            "current_page": members_query.page,
            "per_page": members_query.per_page,
        },
    }
    return jsonify(response), 200


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
